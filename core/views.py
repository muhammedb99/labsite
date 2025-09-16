from django.shortcuts import render, redirect
from .forms import AgeGenderForm, LabInputsForm
from .reference import compare_value, HEBREW_LABELS, advice_for, is_severe ,RANGES
from django.http import HttpResponse
from pathlib import Path

def home(request):
    return render(request, 'home.html')

def start_view(request):
    if request.method == "POST":
        form = AgeGenderForm(request.POST)
        if form.is_valid():
            request.session["age"] = form.cleaned_data["age"]
            request.session["gender"] = form.cleaned_data["gender"]
            return redirect("inputs")  
    else:
        form = AgeGenderForm()
    return render(request, "start.html", {"form": form})

def inputs_view(request):
    if not request.session.get("age") or not request.session.get("gender"):
        return redirect("start")

    gender = request.session.get("gender")
    gender_label = "זכר" if gender == "male" else "נקבה" if gender == "female" else "—"

    if request.method == "POST":
        form = LabInputsForm(request.POST)
        if form.is_valid():
            data = {}
            for k, v in form.cleaned_data.items():
                if v not in (None, ""):
                    try:
                        data[k] = float(v)  
                    except (TypeError, ValueError):
                        data[k] = v        
            request.session["lab_inputs"] = data
            request.session.modified = True
            return redirect("results")
    else:
        form = LabInputsForm()

    return render(request, "inputs.html", {
        "form": form,
        "age": request.session.get("age"),
        "gender": gender,
        "gender_label": gender_label,
    })



def results_view(request):
    age = request.session.get("age")
    gender = request.session.get("gender")
    data = request.session.get("lab_inputs")

    if not age or not gender or not data:
        return redirect("start")

    rows = []
    abnormal_count = 0
    for key, raw in data.items():
        try:
            val = float(raw)
        except Exception:
            continue
        status, lo, hi = compare_value(key, val, gender)
        if status in ("low", "high"):
            abnormal_count += 1
        rows.append({
            "key": key,
            "label": HEBREW_LABELS.get(key, key),
            "value": val,
            "status": status,
            "range": (lo, hi) if lo is not None else None,
            "advice": advice_for(key, status) if status != "normal" else "",
        })

    severe_flag = is_severe({k: float(v) for k, v in data.items() if v not in (None, "")})

    context = {
        "age": age,
        "gender": gender,
        "rows": rows,
        "abnormal_count": abnormal_count,
        "severe_flag": severe_flag,
    }
    return render(request, "results.html", context)


def results_pdf_view(request):
    try:
        from weasyprint import HTML, CSS
    except Exception as e:
        return HttpResponse(
            "WeasyPrint isn't fully installed on this machine yet. "
            "See the installation notes.", status=503
        )
    age = request.session.get("age")
    gender = request.session.get("gender")
    data = request.session.get("lab_inputs")
    if not age or not gender or not data:
        return redirect("start")

    # נשתמש באותו עיבוד של rows כמו ב-results_view
    from .reference import compare_value, HEBREW_LABELS, advice_for, is_severe
    rows, abnormal_count = [], 0
    for key, raw in data.items():
        try:
            val = float(raw)
        except Exception:
            continue
        status, lo, hi = compare_value(key, val, gender)
        if status in ("low", "high"):
            abnormal_count += 1
        rows.append({
            "key": key,
            "label": HEBREW_LABELS.get(key, key),
            "value": val,
            "status": status,
            "range": (lo, hi) if lo is not None else None,
            "advice": advice_for(key, status) if status != "normal" else "",
        })
    severe_flag = is_severe({k: float(v) for k, v in data.items() if v not in (None, "")})

    html = render_to_string("results_print.html", {
        "age": age, "gender": gender, "rows": rows,
        "abnormal_count": abnormal_count, "severe_flag": severe_flag,
    })

    pdf = HTML(string=html, base_url=request.build_absolute_uri("/")).write_pdf(
        stylesheets=[CSS(filename=str(Path("static")/"site.css"))]
    )
    resp = HttpResponse(pdf, content_type="application/pdf")
    resp["Content-Disposition"] = 'attachment; filename="results.pdf"'
    return resp


def reference_ranges_view(request):

    g = (request.GET.get("g") or request.session.get("gender") or "any").lower()
    if g not in ("male", "female", "any"):
        g = "any"

    gender_label = {"male": "זכר", "female": "נקבה", "any": "כללי"}[g]

    rows = []
    for key, label in HEBREW_LABELS.items():
        spec = RANGES.get(key, {})
        rng = spec.get(g) or spec.get("any")
        rows.append({
            "key": key,
            "label": label,
            "range": rng,   
        })

    ctx = {
        "gender": g,
        "gender_label": gender_label,
        "rows": rows,
    }
    return render(request, "reference_ranges.html", ctx)