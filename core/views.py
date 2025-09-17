from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from pathlib import Path

from .forms import AgeGenderForm, LabInputsForm
from .reference import (
    compare_value, EN_LABELS, advice_for, is_severe,
    RANGES, CATEGORIES, range_bounds
)

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

    if age is None or not gender or not data:
        return redirect("start")

    try:
        age_val = float(age)
    except Exception:
        age_val = None

    rows = []
    abnormal_count = 0
    for key, raw in data.items():
        try:
            val = float(raw)
        except Exception:
            continue
        # pass age to age-aware ranges
        status, lo, hi = compare_value(key, val, gender, age_years=age_val)
        if status in ("low", "high"):
            abnormal_count += 1
        rows.append({
            "key": key,
            "label": EN_LABELS.get(key, key),
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
    if age is None or not gender or not data:
        return redirect("start")

    try:
        age_val = float(age)
    except Exception:
        age_val = None

    rows, abnormal_count = [], 0
    for key, raw in data.items():
        try:
            val = float(raw)
        except Exception:
            continue
        # pass age to age-aware ranges
        status, lo, hi = compare_value(key, val, gender, age_years=age_val)
        if status in ("low", "high"):
            abnormal_count += 1
        rows.append({
            "key": key,
            "label": EN_LABELS.get(key, key),  # fixed (was LABELS)
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
    # gender (as before)
    gender = (request.GET.get("g") or request.session.get("gender") or "any").lower()
    if gender not in ("male", "female", "any"):
        gender = "any"

    # session age
    session_age = request.session.get("age")
    try:
        session_age_val = float(session_age) if session_age is not None else None
    except Exception:
        session_age_val = None

    ab = (request.GET.get("ab") or "").lower()  
    if ab == "p":
        age_val = 10.0     
        bucket_label = "ילדים/נוער"
        active_ab = "p"
    elif ab == "a":
        age_val = 30.0     
        bucket_label = "מבוגרים"
        active_ab = "a"
    else:
        age_val = session_age_val
        bucket_label = "ילדים/נוער" if (age_val is not None and age_val < 18) else "מבוגרים"
        active_ab = "p" if (age_val is not None and age_val < 18) else "a"

    gender_label = {"male": "זכר", "female": "נקבה", "any": "כללי"}[gender]

    rows = []
    for key, label in EN_LABELS.items():
        rng = range_bounds(key, gender, age_val)
        if rng is None:
            spec = RANGES.get(key, {})
            rng = spec.get(gender) or spec.get("any")
        rows.append({"key": key, "label": label, "range": rng})

    ctx = {
        "gender": gender,
        "gender_label": gender_label,
        "bucket_label": bucket_label,   
        "active_ab": active_ab,         
        "rows": rows,
        "age": session_age,            
    }
    return render(request, "reference_ranges.html", ctx)

