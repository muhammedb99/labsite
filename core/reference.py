from typing import Tuple, Optional, Dict, Any

def range_bounds(test_key: str, gender: str, age_years: Optional[float]) -> Optional[Tuple[float, float]]:
    """
    Returns (lo, hi) using the same logic as compare_value, without needing a value.
    """
    return _range_for(test_key, gender, age_years)

def age_bucket(age_years: Optional[float]) -> str:
    """
    Returns 'pediatric' if age < 18 (and age provided), else 'adult'.
    Safe default is 'adult' when age is None to preserve old behavior.
    """
    try:
        return "pediatric" if (age_years is not None and float(age_years) < 18) else "adult"
    except Exception:
        return "adult"

RANGES: Dict[str, Dict[str, Tuple[float, float] | None]] = {
    "NEUTROPHILS_PCT": {"any": (42, 72)},
    "LYMPHOCYTES_PCT": {"any": (25, 43)},
    "LYMPHOCYTES_ABS": {"any": (1.3, 4.7)},
    "MONOCYTES_PCT":   {"any": (2, 9)},
    "MONOCYTES_ABS":   {"any": (0.1, 1.0)},
    "EOSINOPHILS_PCT": {"any": (0, 4)},
    "EOSINOPHILS_ABS": {"any": (0.0, 0.4)},
    "BASOPHILS_PCT":   {"any": (0, 1)},
    "BASOPHILS_ABS":   {"any": (0.0, 0.2)},
    "MPV":             {"any": (7.0, 11.0)},
    "LUC_ABS":         {"any": (0.0, 0.4)},
    "LUC_PCT":         {"any": (150000, 450000)},

    "GLUCOSE_FASTING": {"any": (70, 100)},
    "UREA":            {"any": (17, 43)},
    "CREATININE":      {"male": (0.67, 1.17), "female": (0.51, 0.95)},  
    "TRIGLYCERIDES": {
        "pediatric": (0, 90),   
        "any": (0, 150)        
    },
    "AST":             {"male": (0, 35), "female": (0, 31)},
    "ALT":             {"male": (0, 45), "female": (0, 34)},
    "ALK_PHOSPHATASE": {
        "pediatric": (90, 340),  
        "any": (30, 120)         
    },
    "LDH":             {"any": (230, 480)},
    "HEMOLYTIC_FLAG":  {"male": (41, 53), "female": (36, 46)},
    "LIPEMIC_FLAG":    {"any": (60,160)},
    "ICTERIC_FLAG":    {"any": (1.71,20.5)},
    "URIC_ACID":       {"male": (3.5, 7.2), "female": (2.6, 6)},

    "SODIUM":          {"any": (135, 145)},
    "POTASSIUM":       {"any": (3.5, 5.1)},
    "CALCIUM":         {"any": (8.5, 10.5)},

    "PROTEIN_TOTAL":   {"any": (6, 8.3)},
    "ALBUMIN":         {"any": (3.5, 5.2)},

    "CHOLESTEROL_TOTAL": {
        "pediatric": (0, 170),   
        "any": (0, 200)          
    },
    "CHOLESTEROL_HDL": {
        "pediatric": (45, 300),  
        "male": (40, 300),
        "female": (50, 300),
    },
    "CHOLESTEROL_LDL_CALC": {
        "pediatric": (0, 110),   
        "any": (0, 100)        
    },
    "NON_HDL_CHOLESTEROL": {
        "pediatric": (0, 120),  
        "any": (0, 120)
    },

    "BILIRUBIN_TOTAL": {"any": (0.3, 1.2)},
    "BILIRUBIN_DIRECT":{"any": (0.0, 0.3)},

    "LH":              {"any": (3, 10)},    
    "FSH":             {"any": (2, 12)},
    "PROLACTIN":       {"male": (3, 15), "female": (4, 23)},
    "PROGESTERONE":    {"any": (3.5, 33.5)},
    "TESTOSTERONE_TOTAL": {"male": (240, 950), "female": None},
    "TSH":             {"any": (0.55, 4.78)},   
    "T4_FREE":         {"any": (11.22, 22.70)},
    "T3_FREE":         {"any": (3.5, 6.5)},

    "VITAMIN_B12":     {"any": (170, 712)},
    "IRON":            {"male": (60, 160), "female": (40, 145)},
    "FERRITIN":        {"any": (10, 291)},
}

EN_LABELS: Dict[str, str] = {
    "NEUTROPHILS_PCT": "Neutrophils (%)",
    "LYMPHOCYTES_PCT": "Lymphocytes (%)",
    "LYMPHOCYTES_ABS": "Lymphocytes (K/µL)",
    "MONOCYTES_PCT": "Monocytes (%)",
    "MONOCYTES_ABS": "Monocytes (K/µL)",
    "EOSINOPHILS_PCT": "Eosinophils (%)",
    "EOSINOPHILS_ABS": "Eosinophils (K/µL)",
    "BASOPHILS_PCT": "Basophils (%)",
    "BASOPHILS_ABS": "Basophils (K/µL)",
    "MPV": "MPV (fL)",
    "LUC_ABS": "LUC (K/µL)",
    "LUC_PCT": "LUC (%)",

    "GLUCOSE_FASTING": "Glucose (fasting) mg/dL",
    "UREA": "Urea (mg/dL)",
    "CREATININE": "Creatinine (mg/dL)",
    "TRIGLYCERIDES": "Triglycerides (mg/dL)",
    "AST": "AST (GOT) U/L",
    "ALT": "ALT (GPT) U/L",
    "ALK_PHOSPHATASE": "Alkaline Phosphatase (U/L)",
    "LDH": "LDH (U/L)",
    "HEMOLYTIC_FLAG": "Hemolytic (sample flag)",
    "LIPEMIC_FLAG":   "Lipemic (sample flag)",
    "ICTERIC_FLAG":   "Icteric (sample flag)",
    "URIC_ACID": "Uric Acid (mg/dL)",
    "SODIUM": "Sodium (Na⁺) mEq/L",
    "POTASSIUM": "Potassium (K⁺) mEq/L",
    "CALCIUM": "Calcium (mg/dL)",
    "PROTEIN_TOTAL": "Total Protein (g/dL)",
    "ALBUMIN": "Albumin (g/dL)",
    "CHOLESTEROL_TOTAL": "Total Cholesterol (mg/dL)",
    "CHOLESTEROL_HDL":   "HDL Cholesterol (mg/dL)",
    "CHOLESTEROL_LDL_CALC": "LDL Cholesterol (calc) mg/dL",
    "NON_HDL_CHOLESTEROL":  "Non-HDL Cholesterol (mg/dL)",
    "BILIRUBIN_TOTAL": "Bilirubin, Total (mg/dL)",
    "BILIRUBIN_DIRECT": "Bilirubin, Direct (mg/dL)",

    # Hormones / Endocrine
    "LH": "LH",
    "FSH": "FSH",
    "PROLACTIN": "Prolactin",
    "PROGESTERONE": "Progesterone",
    "TESTOSTERONE_TOTAL": "Testosterone, Total",
    "TSH": "TSH (mIU/L)",
    "T4_FREE": "Free T4 (pmol/L)",
    "T3_FREE": "Free T3 (pmol/L)",

    # Proteins / Iron & Vitamins
    "VITAMIN_B12": "Vitamin B12 (pmol/L)",
    "IRON": "Iron (µg/dL)",
    "FERRITIN": "Ferritin (ng/mL)",
}

CATEGORIES = {
    "hematology": [
        "NEUTROPHILS_PCT", "LYMPHOCYTES_PCT", "LYMPHOCYTES_ABS",
        "MONOCYTES_PCT", "MONOCYTES_ABS",
        "EOSINOPHILS_PCT", "EOSINOPHILS_ABS",
        "BASOPHILS_PCT", "BASOPHILS_ABS",
        "MPV", "LUC_PCT", "LUC_ABS",
    ],
    "biochemistry": [
        "GLUCOSE_FASTING", "UREA", "CREATININE", "TRIGLYCERIDES",
        "AST", "ALT", "ALK_PHOSPHATASE", "LDH",
        "URIC_ACID", "SODIUM", "POTASSIUM", "CALCIUM",
        "PROTEIN_TOTAL", "ALBUMIN",
        "CHOLESTEROL_TOTAL", "CHOLESTEROL_HDL", "CHOLESTEROL_LDL_CALC", "NON_HDL_CHOLESTEROL",
        "BILIRUBIN_TOTAL", "BILIRUBIN_DIRECT",
        "HEMOLYTIC_FLAG", "LIPEMIC_FLAG", "ICTERIC_FLAG",
    ],
    "hormone_endo": [
        "LH", "FSH", "PROLACTIN", "PROGESTERONE", "TESTOSTERONE_TOTAL",
        "TSH", "T4_FREE", "T3_FREE",
    ],
    "proteins": [
        "VITAMIN_B12", "IRON", "FERRITIN",
    ],
}

SEVERE_RULES = [
    ("SODIUM", lambda v: v < 130 or v > 150),
    ("POTASSIUM", lambda v: v < 3.0 or v > 5.5),
    ("GLUCOSE_FASTING", lambda v: v >= 126),
    ("CRP", lambda v: v > 3.0),
]

def _range_for(test_key: str, gender: str, age_years: Optional[float]) -> Optional[Tuple[float, float]]:
    spec = RANGES.get(test_key)
    if not spec:
        return None
    bucket = age_bucket(age_years)  
    combined = f"{bucket}_{gender}"
    if combined in spec and spec[combined] is not None:
        return spec[combined]  
    if bucket in spec and spec[bucket] is not None:
        return spec[bucket]  
    if gender in spec and spec[gender] is not None:
        return spec[gender]  
    return spec.get("any") 

def compare_value(test_key: str, value: float, gender: str, age_years: Optional[float] = None):
    rng = _range_for(test_key, gender, age_years)
    if not rng:
        return "normal", None, None
    lo, hi = rng
    if value < lo:
        return "low", lo, hi
    if value > hi:
        return "high", lo, hi
    return "normal", lo, hi


ADVICE: dict[str, str] = {
    "SODIUM_low":  "הקטן שתיית מים בלי אלקטרוליטים; העדף משקה איזוטוני/מרק מלוח קל, במיוחד לאחר הזעה/שלשול. הימנע משתנים בלי הנחיה. [NHS/WHO][1][2]",
    "SODIUM_high": "צמצם מלח נסתר (חטיפים/נקניקים/רטבים); בדוק תוויות (>1.5g Salt/100g = גבוה). שתה לפי צמא אם אין הגבלת נוזלים. [NHS/WHO][2][1]",
    "POTASSIUM_low":  "הוסף מקורות אשלגן יומיומיים: בננה, תפוח־אדמה עם קליפה, קטניות, תרד/אבוקדו. אם נוטל משתנים — בדוק התאמות. [NHS][3]",
    "POTASSIUM_high": "הימנע ממחליפי מלח מבוססי K⁺ ותוספי K⁺; העדף אורז/פסטה/לחם לבן; השרֵה וּבַשֵּׁל ירקות ואז סנֵן להפחתת K⁺. [NHS][3]",
    "CALCIUM_low":   "הגדל סידן מהמזון (חלב/יוגורט/גבינות, סרדינים עם עצם, ברוקולי/קייל, משקאות מועשרים) וודא ויטמין D. אל תחרוג במינוני תוספים. [NIH-ODS][4][14]",
    "CALCIUM_high":  "עצור זמנית תוספי סידן/ויטמין D והקפד על הידרציה עד בירור; תרופות מסוימות (תיאזידים) עלולות להעלות סידן — ודא התאמות. [NHS/NIH-ODS][4]",
    "UREA_high":        "הידרציה טובה והפחתת עודף חלבון/התייבשות; חזור לדיגום בצום תקין. [NKF][7][15]",
    "CREATININE_high":  "הידרציה; הימנע זמנית מ-NSAIDs ומקריאטין; אל תעשה אימון עצים יום-יומיים לפני בדיקה. בדוק תרופות קבועות. [NKF][7][15]",
    "URIC_ACID_high":   "צמצם בירה/אלכוהול ומשקאות עתירי פרוקטוז; הפחת אברים/בשר אדום/פירות־ים; ירידה במשקל ושתייה מספקת. [NHS][—]",  # ראה הערה: דיאטת פורינים נמוכה (NHS/עמותות גאוט)
    "URIC_ACID_low":    "לרוב משנית לתרופות/תוספים; בדוק מינון אם אתה בטיפול להורדת חומצה אורית. (כללי)",
    "GLUCOSE_FASTING_high": "פזר פחמימות על פני היום; החלף לקמחים מלאים וסיבים מסיסים (שיבולת־שועל/קטניות); 150 ד׳/שבוע פעילות אירובית + יומיים כוח. [CDC][0][8]",
    "TRIGLYCERIDES_high":       "הפסק אלכוהול ל-4 שבועות, חתוך סוכרים פשוטים/משקאות ממותקים, הוסף אומגה-3 ממזון, ועסוק בפעילות אירובית. [NHS/NLA][2][10]",
    "CHOLESTEROL_TOTAL_high":   "אכול תבנית ים־תיכונית: הרבה ירקות/קטניות/דגנים מלאים; החלף לחומצות שומן חד-בלתי רוויות (שמן זית/אגוזים). [AHA][1][9]",
    "CHOLESTEROL_LDL_CALC_high":"הפחת שומן רווי/טרנס (בשרים מעובדים/מאפים); הוסף סיבים מסיסים (בטא-גלוקן משיבולת־שועל, קטניות); שקול סטרולים/סטנולים תזונתיים. [AHA][1][9]",
    "NON_HDL_CHOLESTEROL_high": "כמו LDL: דגש על סיבים מסיסים, שמנים בלתי־רווים ופעילות; עקוב אחרי משקל ומדוד בצום תקין. [AHA][1][9]",
    "CHOLESTEROL_HDL_low":      "הגדל פעילות אירובית/כוח; הפסק עישון; העדף שומנים בלתי רוויים (זית/אבוקדו/אגוזים). [AHA/CDC][1][0]",
    "ALT_high": "עצור אלכוהול; אם BMI↑ — ירידת 7–10% משקל משפרת NAFLD; בדוק תרופות/צמחי מרפא (כולל NSAIDs). בצע דיגום בצום/מנוחה. [ניירות AASLD + NHS][—][—]",
    "AST_high": "דומה ל-ALT; הימנע מאימון שרירי עצים 24–48ש׳ לפני בדיקה, כי עלול להעלות AST. [NHS/מעבדות][—][16]",
    "ALK_PHOSPHATASE_high": "בדוק ויטמין D ובריאות עצם/שיניים; אם יש גרד/צהבת — הימנע אלכוהול עד בירור כולסטטי. (פרקטי/קליני)",
    "LDH_high": "תאם דיגום במנוחה והימנע המוליזה (גומי לחץ ממושך/ניעור מבחנה). חזור על בדיקה אם יש חשד לדגימה המוליטית. [Lab/Quest][16]",
    "BILIRUBIN_TOTAL_high": "אם תסמונת ג׳ילברט: הימנע מצום/התייבשות; אכול ושתה סדיר — זה מקטין תנודת בילירובין. [NHS Gilbert][17]",
    "BILIRUBIN_DIRECT_high": "שמור על הידרציה והימנע אלכוהול עד בירור דרכי מרה/כבד. (פרקטי)",
    "PROTEIN_TOTAL_low": "העלה חלבון איכותי (1–1.2 גר׳/ק״ג ליום אם אין מגבלת כליה): קטניות, עוף/דגים, מוצרי חלב דלי שומן או טופו. [BDA/NHS][—]",
    "ALBUMIN_low":       "הוסף חלבון מלא (ביצים/דגים/חלב) ובדוק אובדני חלבון (שלשול כרוני/בצקות). שקול דיאטתון קליני. [BDA/NHS][—]",
    "TSH_high":  "הפסק בִּיאָטִין 48–72ש׳ לפני דיגום; אם נוטל לבו־תירוקסין — קח על קיבה ריקה והפרד מברזל/סידן ב-4ש׳. [FDA][3][11]",
    "TSH_low":   "אותו כלל בִּיאָטִין; אם יש פלפיטציות/רעידות — צמצם קפאין עד בירור. [FDA][3][11]",
    "T4_FREE_low":"הימנע מבִּיאָטִין/תוספים לפני בדיקה; בצע דיגום בבוקר בעקביות. [FDA][3][11]",
    "T4_FREE_high":"כמו לעיל; אם סימני יתר-תריסיות — הגבל קפאין/אנרגיה זמנית. [FDA][3][11]",
    "T3_FREE_low":"אותן הנחיות הכנה; שמור תזונה מסודרת וחלבון מספיק. [FDA][3][11]",
    "T3_FREE_high":"הפסק זמנית בִּיאָטִין/יוד לפני דיגום; חזור על בדיקה תקינה. [FDA][3][11]",
    "PROLACTIN_high":        "בצע בדיקה בבוקר לאחר מנוחה; הימנע מלחץ, מאמץ, וגירוי פטמות לפני דיגום; אשר תרופות מעלות פרולקטין. (פרקטי)",
    "TESTOSTERONE_TOTAL_low":"שפר שינה (7–9ש׳), בצע אימוני כוח 2–3×ש׳, הורד שומן קרביית, הגבּל אלכוהול. למדוד בבוקר בצום. [CDC פעילות][0][8]",
    "PROGESTERONE_abnormal": "תזמן דיגום ל-Luteal (כ-7 ימים לפני וסת) והימנע בִּיאָטִין. [FDA][3]",
    "LH_abnormal":           "תאם ליום מחזור וציין טיפולי פוריות/גלולות; הימנע בִּיאָטִין. [FDA][3]",
    "FSH_abnormal":          "כמו LH; שמור משקל תקין ופעילות. [CDC פעילות + FDA][0][3]",
    "IRON_low":       "צרוך ברזל עם ויטמין C (פלפל/הדרים) והפרד מסידן/קפה/תה ≥2ש׳; העדף בשרים רזים/קטניות מועשרות. [NIH-ODS][4][12]",
    "FERRITIN_low":   "אם תוסף — קח על קיבה ריקה עם מים/ויטמין C; הימנע מחלב/סידן סביב הבליעה; עקוב אחרי עצירות. [NIH-ODS][12]",
    "VITAMIN_B12_low":"הוסף ביצים/חלב/דגים; טבעונים — תוסף קבוע בצורת ציאנו/מתיל-B12 במינון יומי/שבועי מקובל. [NIH-ODS][5][13]",
    "VITAMIN_B12_high":"בדוק אם נלקחים תוספים/זריקות; הורד מינון אם אין אינדיקציה. [NIH-ODS][5][13]",
    "NEUTROPHILS_low":  "היגיינת ידיים קפדנית, הימנע ממגע עם חולים/קהל סגור; פנה דחוף אם חום ≥38°C. [CDC Neutropenia][—]",
    "NEUTROPHILS_high": "לרוב תגובה לזיהום/סטרס; הידרציה ומנוחה; עקוב אחרי חום/סימפטומים. (קליני)",
    "LYMPHOCYTES_low":  "שמור חיסונים עדכניים, שינה מספקת ותזונה מגוונת; הימנע מחשיפה לזיהומים. (כללי)",
    "LYMPHOCYTES_high": "שכיח בווירוסים — מנוחה/נוזלים; אם ממושך/חריג — בירור. (כללי)",
    "MONOCYTES_high":   "דלקתי/זיהומי — נהל גורם רקע (שינה/תזונה/זיהום פה/שיניים). (כללי)",
    "EOSINOPHILS_high": "נהל אלרגנים (אבקה/אבק/פרפום), שטיפות אף/אנטיהיסטמין לפי צורך; עקוב באסתמה. [NHS Allergy][—]",
    "BASOPHILS_high":   "לרוב אלרגי/תמיכתי; הקטן חשיפה לטריגר והמשך מעקב. (כללי)",
    "MPV_abnormal":     "אל תשנה טיפול לפי MPV בלבד; פרש יחד עם PLT ו-CBC מלא. (כללי)",
    "HEMOLYTIC_FLAG_high":"בקש דגימה חוזרת ללא אימון עצים קודם; מנוחה 10–15 ד׳ בישיבה; טיפול עדין במבחנה (ללא ניעור). [Lab/Quest][16]",
    "LIPEMIC_FLAG_high":   "דיגום בצום 9–12ש׳; הימנע מאלכוהול וארוחה שומנית ערב קודם. [Lab/Quest][16]",
    "ICTERIC_FLAG_high":   "דווח על תרופות/תוספים; דגום בבוקר בצום והקפד הידרציה. [Lab/Quest][16]",
    "default_low":  "עצה כללית: להגדיל מקורות תזונתיים ייעודיים ולבדוק נטילת תוספים/תרופות רלוונטיות.",
    "default_high": "עצה כללית: להפחית מקורות ייעודיים ולהפסיק תוספים עד בירור; לשקול חזרה על בדיקה בתנאי דיגום תקינים.",
}


def advice_for(test_key: str, status: str) -> str:
    key_specific = f"{test_key}_{status}"
    if key_specific in ADVICE:
        return ADVICE[key_specific]
    return ADVICE["default_low"] if status == "low" else ADVICE["default_high"]

def is_severe(all_values: Dict[str, Any]) -> bool:
    for k, rule in SEVERE_RULES:
        v = all_values.get(k)
        if v is not None:
            try:
                if rule(float(v)):
                    return True
            except Exception:
                pass
    return False
