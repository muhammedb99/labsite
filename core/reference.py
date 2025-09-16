from typing import Tuple, Optional

RANGES = {
    "alt": {"male": (0, 45), "female": (0, 34)},  # U/L
    "ast": {"male": (0, 35), "female": (0, 31)},  # U/L
    "alp": {"any": (30, 120)},                    # U/L
    "ggt": {"male": (0, 55), "female": (0, 38)},  # U/L
    "bilirubin_total": {"any": (0.3, 1.2)},       # mg/dL
    "bilirubin_direct": {"any": (0.0, 0.3)},      # mg/dL
    "albumin": {"any": (3.5, 5.2)},               # g/dL
    "sodium": {"any": (135, 145)},                # mEq/L
    "potassium": {"any": (3.5, 5.1)},             # mEq/L
    "chloride": {"any": (98, 106)},               # mEq/L
    "calcium": {"any": (8.5, 10.5)},              # mg/dL
    "phosphate": {"any": (2.5, 4.5)},             # mg/dL 
    "urea": {"any": (17, 43)},                    # mg/dL 
    "creatinine": {"male": (0.67, 1.17), "female": (0.51, 0.95)},  # mg/dL
    "esr": {"any": (0, 20)},                      # mm/h 
    "crp": {"any": (0.0, 0.5)},                   # mg/dL
    "glucose_fasting": {"any": (70, 100)},        # mg/dL
    "wbc": {"any": (4500, 11000)},                # K/µL
    "rbc": {"male": (4.5, 5.9), "female": (4.1, 5.1)},  # M/µL
    "hb": {"male": (13.5, 17.5), "female": (11.5, 16.1)},  # g/dL
    "hct": {"male": (41, 53), "female": (36, 46)},  # %
    "mcv": {"any": (80, 100)},                    # fL
    "mch": {"any": (26, 34)},                     # pg
    "mchc": {"any": (31, 37)},                    # g/dL
    "rdw": {"any": (11.5, 14.5)},                 # %
    "plt": {"any": (150000, 450000)},             # K/µL
    "neutrophils_pct": {"any": (42, 72)},         # %
    "lymphocytes_pct": {"any": (25, 43)},         # %
    "lymphocytes_abs": {"any": (1.3, 4.7)},       # K/µL
    "monocytes_pct": {"any": (2, 9)},             # %
    "monocytes_abs": {"any": (0.1, 1.0)},         # K/µL
    "eosinophils_pct": {"any": (0, 4)},           # %
    "eosinophils_abs": {"any": (0.0, 0.4)},       # K/µL
    "basophils_pct": {"any": (0, 1)},             # %
    "basophils_abs": {"any": (0.0, 0.2)},         # K/µL
    "tsh": {"any": (0.55, 4.78)},                 # mIU/L
    "ferritin": {"any": (10, 291)},               # ng/mL
    "b12": {"any": (170, 712)},                   # pmol/L
}

HEBREW_LABELS = {
    "alt": "ALT (GPT)",
    "ast": "AST (GOT)",
    "alp": "ALP",
    "ggt": "GGT",
    "bilirubin_total": "בילירובין כללי",
    "bilirubin_direct": "בילירובין ישיר",
    "albumin": "אלבומין",
    "sodium": "נתרן (Na⁺)",
    "potassium": "אשלגן (K⁺)",
    "chloride": "כלוריד (Cl⁻)",
    "calcium": "סידן",
    "phosphate": "זרחן (פוספט)",
    "urea": "אוריאה",
    "creatinine": "קריאטינין",
    "esr": "ESR (שקיעת דם)",
    "crp": "CRP",
    "glucose_fasting": "גלוקוז בצום",
    "wbc": "WBC",
    "rbc": "RBC",
    "hb": "Hb (המוגלובין)",
    "hct": "HCT (המטוקריט)",
    "mcv": "MCV",
    "mch": "MCH",
    "mchc": "MCHC",
    "rdw": "RDW",
    "plt": "PLT (טסיות)",
    "neutrophils_pct": "Neutrophils (%)",
    "lymphocytes_pct": "Lymphocytes (%)",
    "lymphocytes_abs": "Lymphocytes (K/µL)",
    "monocytes_pct": "Monocytes (%)",
    "monocytes_abs": "Monocytes (K/µL)",
    "eosinophils_pct": "Eosinophils (%)",
    "eosinophils_abs": "Eosinophils (K/µL)",
    "basophils_pct": "Basophils (%)",
    "basophils_abs": "Basophils (K/µL)",
    "tsh": "TSH",
    "ferritin": "פריטין",
    "b12": "B12",
}

ADVICE = {
    "sodium_low": "איזון שתייה ומלחים בהתאם להנחיות רופא; הימנע מעודף מים ללא אלקטרוליטים.",
    "sodium_high": "שתייה מספקת; בדיקה להפרעות נוזלים/מלחים; להיוועץ ברופא אם גבוה מאוד.",
    "potassium_low": "בד\"כ תזונה/החלפת אובדנים; בדוק תרופות משתנות.",
    "potassium_high": "הימנע מתוספי אשלגן; יש לפנות לרופא אם הערך גבוה משמעותית.",
    "alt_high": "הימנע מאלכוהול/תרופות מזיקות לכבד; שקול בדיקת המשך לפי רופא.",
    "ggt_high": "הפחתת אלכוהול ובירור תרופתי עם הרופא.",
    "glucose_fasting_high": "איזון תזונתי/פעילות גופנית; מעקב רופא לסוכר.",
    "ferritin_low": "תזונה עשירת ברזל/תוספים לפי הנחיית רופא.",
    "b12_low": "שקול תוסף B12 לפי רופא/דיאטנית.",
    "default_low": "התייעצות עם רופא/דיאטנית והמשך מעקב.",
    "default_high": "התייעצות עם רופא והמשך בירור.",
}

SEVERE_RULES = [
    ("sodium", lambda v: v < 130 or v > 150),
    ("potassium", lambda v: v < 3.0 or v > 5.5),
    ("glucose_fasting", lambda v: v >= 126),  
    ("crp", lambda v: v > 3.0),
]

def _range_for(test_key: str, gender: str) -> Optional[Tuple[float, float]]:
    spec = RANGES.get(test_key)
    if not spec:
        return None
    if gender in spec:
        return spec[gender]
    return spec.get("any")

def compare_value(test_key: str, value: float, gender: str):
    """
    מחזיר (status, low, high) כאשר status: 'low'/'normal'/'high'
    """
    rng = _range_for(test_key, gender)
    if not rng:
        return "normal", None, None
    lo, hi = rng
    if value < lo:
        return "low", lo, hi
    if value > hi:
        return "high", lo, hi
    return "normal", lo, hi

def advice_for(test_key: str, status: str):
    key = None
    if test_key == "sodium":
        key = "sodium_low" if status == "low" else "sodium_high"
    elif test_key == "potassium":
        key = "potassium_low" if status == "low" else "potassium_high"
    elif test_key == "alt" and status == "high":
        key = "alt_high"
    elif test_key == "ggt" and status == "high":
        key = "ggt_high"
    elif test_key == "glucose_fasting" and status == "high":
        key = "glucose_fasting_high"
    elif test_key == "ferritin" and status == "low":
        key = "ferritin_low"
    elif test_key == "b12" and status == "low":
        key = "b12_low"

    if key and key in ADVICE:
        return ADVICE[key]
    return ADVICE["default_low"] if status == "low" else ADVICE["default_high"]

def is_severe(all_values: dict) -> bool:
    for k, rule in SEVERE_RULES:
        v = all_values.get(k)
        if v is not None:
            try:
                if rule(float(v)):
                    return True
            except Exception:
                pass
    return False
