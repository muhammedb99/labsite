from django import forms

class AgeGenderForm(forms.Form):
    GENDER_CHOICES = [
        ("male", "זכר"),
        ("female", "נקבה"),
    ]

    age = forms.IntegerField(
        label="גיל",
        min_value=18,
        widget=forms.NumberInput(attrs={
            "class": "input-text",     
            "min": "18",
            "inputmode": "numeric",
            "placeholder": "מעל 18",
            "id": "id_age",
        })
    )
    gender = forms.ChoiceField(
        label="מגדר",
        choices=GENDER_CHOICES,
        widget=forms.RadioSelect(attrs={
            "class": "gender-radio"    
        })
    )

class LabInputsForm(forms.Form):
    alt = forms.DecimalField(label="ALT (GPT)", required=False, max_digits=6, decimal_places=2)
    ast = forms.DecimalField(label="AST (GOT)", required=False, max_digits=6, decimal_places=2)
    alp = forms.DecimalField(label="ALP", required=False, max_digits=6, decimal_places=2)
    ggt = forms.DecimalField(label="GGT", required=False, max_digits=6, decimal_places=2)
    bilirubin_total = forms.DecimalField(label="בילירובין כללי", required=False, max_digits=6, decimal_places=3)
    bilirubin_direct = forms.DecimalField(label="בילירובין ישיר", required=False, max_digits=6, decimal_places=3)
    albumin = forms.DecimalField(label="אלבומין", required=False, max_digits=6, decimal_places=2)

    sodium = forms.DecimalField(label="נתרן (Na⁺)", required=False, max_digits=6, decimal_places=2)
    potassium = forms.DecimalField(label="אשלגן (K⁺)", required=False, max_digits=6, decimal_places=2)
    chloride = forms.DecimalField(label="כלוריד (Cl⁻)", required=False, max_digits=6, decimal_places=2)
    calcium = forms.DecimalField(label="סידן", required=False, max_digits=6, decimal_places=2)
    phosphate = forms.DecimalField(label="זרחן (פוספט)", required=False, max_digits=6, decimal_places=2)

    urea = forms.DecimalField(label="אוריאה (BUN/אוריאה)", required=False, max_digits=6, decimal_places=2)
    creatinine = forms.DecimalField(label="קריאטינין", required=False, max_digits=6, decimal_places=3)

    esr = forms.DecimalField(label="ESR (שקיעת דם)", required=False, max_digits=6, decimal_places=2)
    crp = forms.DecimalField(label="CRP", required=False, max_digits=6, decimal_places=3)
    glucose_fasting = forms.DecimalField(label="גלוקוז בצום", required=False, max_digits=6, decimal_places=1)

    wbc = forms.DecimalField(label="WBC (אל״ד)", required=False, max_digits=6, decimal_places=1)
    rbc = forms.DecimalField(label="RBC (כדוריות אדומות)", required=False, max_digits=6, decimal_places=2)
    hb = forms.DecimalField(label="Hb (המוגלובין)", required=False, max_digits=6, decimal_places=2)
    hct = forms.DecimalField(label="HCT (המטוקריט, %)", required=False, max_digits=6, decimal_places=2)
    mcv = forms.DecimalField(label="MCV (fL)", required=False, max_digits=6, decimal_places=1)
    mch = forms.DecimalField(label="MCH (pg)", required=False, max_digits=6, decimal_places=1)
    mchc = forms.DecimalField(label="MCHC (g/dL)", required=False, max_digits=6, decimal_places=2)
    rdw = forms.DecimalField(label="RDW (%)", required=False, max_digits=6, decimal_places=2)
    plt = forms.DecimalField(label="PLT (טסיות)", required=False, max_digits=7, decimal_places=0)

    neutrophils_pct = forms.DecimalField(label="Neutrophils (%)", required=False, max_digits=5, decimal_places=1)
    lymphocytes_pct = forms.DecimalField(label="Lymphocytes (%)", required=False, max_digits=5, decimal_places=1)
    lymphocytes_abs = forms.DecimalField(label="Lymphocytes (K/µL)", required=False, max_digits=5, decimal_places=1)
    monocytes_pct = forms.DecimalField(label="Monocytes (%)", required=False, max_digits=5, decimal_places=1)
    monocytes_abs = forms.DecimalField(label="Monocytes (K/µL)", required=False, max_digits=5, decimal_places=1)
    eosinophils_pct = forms.DecimalField(label="Eosinophils (%)", required=False, max_digits=5, decimal_places=1)
    eosinophils_abs = forms.DecimalField(label="Eosinophils (K/µL)", required=False, max_digits=5, decimal_places=1)
    basophils_pct = forms.DecimalField(label="Basophils (%)", required=False, max_digits=5, decimal_places=1)
    basophils_abs = forms.DecimalField(label="Basophils (K/µL)", required=False, max_digits=5, decimal_places=1)

    tsh = forms.DecimalField(label="TSH (mIU/L)", required=False, max_digits=6, decimal_places=3)
    ferritin = forms.DecimalField(label="פריטין (ng/mL)", required=False, max_digits=7, decimal_places=1)
    b12 = forms.DecimalField(label="B12 (pmol/L)", required=False, max_digits=7, decimal_places=1)

    def clean(self):
        cleaned = super().clean()
        any_filled = any(v not in (None, "") for v in cleaned.values())
        if not any_filled:
            raise forms.ValidationError("יש להזין לפחות רכיב אחד כדי להמשיך.")
        return cleaned
