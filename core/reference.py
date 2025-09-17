from typing import Tuple, Optional, Dict, Any


RANGES: Dict[str, Dict[str, Tuple[float, float] | None]] = {
    # --- Hematology (Diff, CBC extensions) ---
    "NEUTROPHILS_PCT": {"any": (42, 72)},                 # %  :contentReference[oaicite:0]{index=0}
    "LYMPHOCYTES_PCT": {"any": (25, 43)},                 # %  :contentReference[oaicite:1]{index=1}
    "LYMPHOCYTES_ABS": {"any": (1.3, 4.7)},               # K/µL :contentReference[oaicite:2]{index=2}
    "MONOCYTES_PCT":   {"any": (2, 9)},                   # %  (כללית מציינת טווחים טיפוסיים בדפי CBC; נשתמש בסטנדרט)
    "MONOCYTES_ABS":   {"any": (0.1, 1.0)},               # K/µL
    "EOSINOPHILS_PCT": {"any": (0, 4)},                   # %
    "EOSINOPHILS_ABS": {"any": (0.0, 0.4)},               # K/µL
    "BASOPHILS_PCT":   {"any": (0, 1)},                   # %  :contentReference[oaicite:3]{index=3}
    "BASOPHILS_ABS":   {"any": (0.0, 0.2)},               # K/µL :contentReference[oaicite:4]{index=4}
    "MPV":             {"any": (7.0, 11.0)},              # fL :contentReference[oaicite:5]{index=5}
    # LUC: בכללי אין טווח רשמי באתר כללית; ערכי ייחוס משתנים לפי האנלייזר. ניתן להציג ללא טווח/עם טווח אינפורמטיבי.
    "LUC_ABS":         {"any": (0.0, 0.4)},               # K/µL (מקור מחקרי, לא כללית) :contentReference[oaicite:6]{index=6}
    "LUC_PCT":         {"any": (150000, 450000)},                     # %  (אין טווח רשמי בכללית)

    # --- Biochemistry ---
    "GLUCOSE_FASTING": {"any": (70, 100)},                # mg/dL :contentReference[oaicite:7]{index=7}
    "UREA":            {"any": (17, 43)},                 # mg/dL (אוריאה) – כללית מציינת כך בדפי הסבר
    "CREATININE":      {"male": (0.67, 1.17), "female": (0.51, 0.95)},  # mg/dL (דפי RBC/כללי) :contentReference[oaicite:8]{index=8}
    "TRIGLYCERIDES":   {"any": (0, 150)},                     # יעדים/המלצות, לא טווח קשיח :contentReference[oaicite:9]{index=9}
    "AST":             {"male": (0, 35), "female": (0, 31)},  # U/L  :contentReference[oaicite:10]{index=10}
    "ALT":             {"male": (0, 45), "female": (0, 34)},  # U/L  :contentReference[oaicite:11]{index=11}
    "ALK_PHOSPHATASE": {"any": (30, 120)},                # U/L  :contentReference[oaicite:12]{index=12}
    "LDH":             {"any": (230, 480)},               # U/L  (כללית) :contentReference[oaicite:13]{index=13}
    # Sample quality flags – לא טווחים קליניים אלא איכות דגימה
    "HEMOLYTIC_FLAG":  {"male": (41, 53), "female": (36, 46)},                     # :contentReference[oaicite:14]{index=14}
    "LIPEMIC_FLAG":    {"any": (60,160)},                     # :contentReference[oaicite:15]{index=15}
    "ICTERIC_FLAG":    {"any": (1.71,20.5)},                     # :contentReference[oaicite:16]{index=16}
    "URIC_ACID":       {"male": (3.5, 7.2), "female": (2.6, 6)},                     # לא מצאנו טווח רשמי יחיד בעמוד כללית – אפשר להשלים בהמשך
    "SODIUM":          {"any": (135, 145)},               # mEq/L (דפי כימיה כלליים)
    "POTASSIUM":       {"any": (3.5, 5.1)},               # mEq/L
    "CALCIUM":         {"any": (8.5, 10.5)},              # mg/dL
    "PROTEIN_TOTAL":   {"any": (6,8.3)},                     # Total protein – לעיתים 6.0–8.3 g/dL (לא נמצא דף רשמי מובהק)
    "ALBUMIN":         {"any": (3.5, 5.2)},               # g/dL :contentReference[oaicite:17]{index=17}
    "CHOLESTEROL_TOTAL": {"any": (0,200)},                   # מומלץ <200 mg/dL (יעד) :contentReference[oaicite:18]{index=18}
    "CHOLESTEROL_HDL":   {"male": (40, 300), "female": (50, 300)},                   
    "CHOLESTEROL_LDL_CALC": {"any": (0,100)},                # יעד לפי סיכון – לא טווח קשיח :contentReference[oaicite:20]{index=20}
    "NON_HDL_CHOLESTEROL":  {"any": (0,120)},                # יעד לפי סיכון – לא טווח קשיח :contentReference[oaicite:21]{index=21}
    "BILIRUBIN_TOTAL": {"any": (0.3, 1.2)},               # mg/dL
    "BILIRUBIN_DIRECT":{"any": (0.0, 0.3)},               # mg/dL

    # --- Hormones / Endocrine ---
    "LH":              {"any": (3,10)},                     # תלוי גיל/מין/פאזה; אין טווח יחיד אחיד בעמודי כללית
    "FSH":             {"any": (2,12)},                     # כנ"ל
    "PROLACTIN":       {"male": (3, 15), "female": (4, 23)},                     # תלוי מגדר/היריון/שעה
    "PROGESTERONE":    {"any": (3.5,33.5)},                    
    "TESTOSTERONE_TOTAL": {"male": (240, 950), "female": None},                  # תלוי מגדר/גיל
    "TSH":             {"any": (0.55, 4.78)},             # mIU/L :contentReference[oaicite:22]{index=22}
    "T4_FREE":         {"any": (11.22, 22.70)},           # pmol/L :contentReference[oaicite:23]{index=23}
    "T3_FREE":         {"any": (3.5, 6.5)},               # pmol/L :contentReference[oaicite:24]{index=24}

    # --- Proteins / Iron & Vitamins ---
    "VITAMIN_B12":     {"any": (170, 712)},               # pmol/L (כללית)  :contentReference[oaicite:25]{index=25}
    "IRON":            {"male": (60, 160), "female": (40, 145)},  # µg/dL :contentReference[oaicite:26]{index=26}
    "FERRITIN":        {"any": (10, 291)},                # ng/mL :contentReference[oaicite:27]{index=27}
}

# תוויות תצוגה באנגלית (כמו בדפי כללית)
EN_LABELS: Dict[str, str] = {
    # Hematology
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

    # Biochemistry
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

# לקיבוץ לפי הקטגוריות שביקשת (לתבניות ולניווט בטופס)
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
        # sample flags (איכות דגימה)
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

# כללים ל"התרעה חמורה" – אפשר להרחיב לפי צורך קליני
SEVERE_RULES = [
    ("SODIUM", lambda v: v < 130 or v > 150),
    ("POTASSIUM", lambda v: v < 3.0 or v > 5.5),
    ("GLUCOSE_FASTING", lambda v: v >= 126),  # בהתאם להקשר קליני ו/או כפל בדיקות  :contentReference[oaicite:28]{index=28}
    ("CRP", lambda v: v > 3.0),               # אם יתווסף CRP בפורם
]

def _range_for(test_key: str, gender: str) -> Optional[Tuple[float, float]]:
    spec = RANGES.get(test_key)
    if not spec:
        return None
    if gender in spec and spec[gender] is not None:
        return spec[gender]  # type: ignore
    return spec.get("any")  # type: ignore

def compare_value(test_key: str, value: float, gender: str):
    """
    מחזיר (status, low, high): 'low'/'normal'/'high' + גבולות אם קיימים.
    אם אין טווח קשיח (None), נחזיר 'normal' (הערכת יעד/סיכון תיעשה בטקסט).
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

# ---------------------------------------------------
# המלצות עדינות אך פרקטיות – לא תחליף לרופא
# ---------------------------------------------------
ADVICE: dict[str, str] = {
    # --- אלקטרוליטים ---
    "SODIUM_low":  "הקטן שתיית מים בלי אלקטרוליטים; העדף משקה איזוטוני/מרק מלוח קל, במיוחד לאחר הזעה/שלשול. הימנע משתנים בלי הנחיה. [NHS/WHO][1][2]",
    "SODIUM_high": "צמצם מלח נסתר (חטיפים/נקניקים/רטבים); בדוק תוויות (>1.5g Salt/100g = גבוה). שתה לפי צמא אם אין הגבלת נוזלים. [NHS/WHO][2][1]",

    "POTASSIUM_low":  "הוסף מקורות אשלגן יומיומיים: בננה, תפוח־אדמה עם קליפה, קטניות, תרד/אבוקדו. אם נוטל משתנים — בדוק התאמות. [NHS][3]",
    "POTASSIUM_high": "הימנע ממחליפי מלח מבוססי K⁺ ותוספי K⁺; העדף אורז/פסטה/לחם לבן; השרֵה וּבַשֵּׁל ירקות ואז סנֵן להפחתת K⁺. [NHS][3]",

    "CALCIUM_low":   "הגדל סידן מהמזון (חלב/יוגורט/גבינות, סרדינים עם עצם, ברוקולי/קייל, משקאות מועשרים) וודא ויטמין D. אל תחרוג במינוני תוספים. [NIH-ODS][4][14]",
    "CALCIUM_high":  "עצור זמנית תוספי סידן/ויטמין D והקפד על הידרציה עד בירור; תרופות מסוימות (תיאזידים) עלולות להעלות סידן — ודא התאמות. [NHS/NIH-ODS][4]",

    # --- כליה / אוריאה / קריאטינין / חומצה אורית ---
    "UREA_high":        "הידרציה טובה והפחתת עודף חלבון/התייבשות; חזור לדיגום בצום תקין. [NKF][7][15]",
    "CREATININE_high":  "הידרציה; הימנע זמנית מ-NSAIDs ומקריאטין; אל תעשה אימון עצים יום-יומיים לפני בדיקה. בדוק תרופות קבועות. [NKF][7][15]",
    "URIC_ACID_high":   "צמצם בירה/אלכוהול ומשקאות עתירי פרוקטוז; הפחת אברים/בשר אדום/פירות־ים; ירידה במשקל ושתייה מספקת. [NHS][—]",  # ראה הערה: דיאטת פורינים נמוכה (NHS/עמותות גאוט)
    "URIC_ACID_low":    "לרוב משנית לתרופות/תוספים; בדוק מינון אם אתה בטיפול להורדת חומצה אורית. (כללי)",

    # --- גלוקוז ---
    "GLUCOSE_FASTING_high": "פזר פחמימות על פני היום; החלף לקמחים מלאים וסיבים מסיסים (שיבולת־שועל/קטניות); 150 ד׳/שבוע פעילות אירובית + יומיים כוח. [CDC][0][8]",

    # --- שומנים בדם ---
    "TRIGLYCERIDES_high":       "הפסק אלכוהול ל-4 שבועות, חתוך סוכרים פשוטים/משקאות ממותקים, הוסף אומגה-3 ממזון, ועסוק בפעילות אירובית. [NHS/NLA][2][10]",
    "CHOLESTEROL_TOTAL_high":   "אכול תבנית ים־תיכונית: הרבה ירקות/קטניות/דגנים מלאים; החלף לחומצות שומן חד-בלתי רוויות (שמן זית/אגוזים). [AHA][1][9]",
    "CHOLESTEROL_LDL_CALC_high":"הפחת שומן רווי/טרנס (בשרים מעובדים/מאפים); הוסף סיבים מסיסים (בטא-גלוקן משיבולת־שועל, קטניות); שקול סטרולים/סטנולים תזונתיים. [AHA][1][9]",
    "NON_HDL_CHOLESTEROL_high": "כמו LDL: דגש על סיבים מסיסים, שמנים בלתי־רווים ופעילות; עקוב אחרי משקל ומדוד בצום תקין. [AHA][1][9]",
    "CHOLESTEROL_HDL_low":      "הגדל פעילות אירובית/כוח; הפסק עישון; העדף שומנים בלתי רוויים (זית/אבוקדו/אגוזים). [AHA/CDC][1][0]",

    # --- כבד / אנזימים ---
    "ALT_high": "עצור אלכוהול; אם BMI↑ — ירידת 7–10% משקל משפרת NAFLD; בדוק תרופות/צמחי מרפא (כולל NSAIDs). בצע דיגום בצום/מנוחה. [ניירות AASLD + NHS][—][—]",
    "AST_high": "דומה ל-ALT; הימנע מאימון שרירי עצים 24–48ש׳ לפני בדיקה, כי עלול להעלות AST. [NHS/מעבדות][—][16]",
    "ALK_PHOSPHATASE_high": "בדוק ויטמין D ובריאות עצם/שיניים; אם יש גרד/צהבת — הימנע אלכוהול עד בירור כולסטטי. (פרקטי/קליני)",
    "LDH_high": "תאם דיגום במנוחה והימנע המוליזה (גומי לחץ ממושך/ניעור מבחנה). חזור על בדיקה אם יש חשד לדגימה המוליטית. [Lab/Quest][16]",
    "BILIRUBIN_TOTAL_high": "אם תסמונת ג׳ילברט: הימנע מצום/התייבשות; אכול ושתה סדיר — זה מקטין תנודת בילירובין. [NHS Gilbert][17]",
    "BILIRUBIN_DIRECT_high": "שמור על הידרציה והימנע אלכוהול עד בירור דרכי מרה/כבד. (פרקטי)",

    # --- חלבונים ---
    "PROTEIN_TOTAL_low": "העלה חלבון איכותי (1–1.2 גר׳/ק״ג ליום אם אין מגבלת כליה): קטניות, עוף/דגים, מוצרי חלב דלי שומן או טופו. [BDA/NHS][—]",
    "ALBUMIN_low":       "הוסף חלבון מלא (ביצים/דגים/חלב) ובדוק אובדני חלבון (שלשול כרוני/בצקות). שקול דיאטתון קליני. [BDA/NHS][—]",

    # --- בלוטת התריס (כולל הפרעות בדיקות) ---
    "TSH_high":  "הפסק בִּיאָטִין 48–72ש׳ לפני דיגום; אם נוטל לבו־תירוקסין — קח על קיבה ריקה והפרד מברזל/סידן ב-4ש׳. [FDA][3][11]",
    "TSH_low":   "אותו כלל בִּיאָטִין; אם יש פלפיטציות/רעידות — צמצם קפאין עד בירור. [FDA][3][11]",
    "T4_FREE_low":"הימנע מבִּיאָטִין/תוספים לפני בדיקה; בצע דיגום בבוקר בעקביות. [FDA][3][11]",
    "T4_FREE_high":"כמו לעיל; אם סימני יתר-תריסיות — הגבל קפאין/אנרגיה זמנית. [FDA][3][11]",
    "T3_FREE_low":"אותן הנחיות הכנה; שמור תזונה מסודרת וחלבון מספיק. [FDA][3][11]",
    "T3_FREE_high":"הפסק זמנית בִּיאָטִין/יוד לפני דיגום; חזור על בדיקה תקינה. [FDA][3][11]",

    # --- הורמונים נוספים ---
    "PROLACTIN_high":        "בצע בדיקה בבוקר לאחר מנוחה; הימנע מלחץ, מאמץ, וגירוי פטמות לפני דיגום; אשר תרופות מעלות פרולקטין. (פרקטי)",
    "TESTOSTERONE_TOTAL_low":"שפר שינה (7–9ש׳), בצע אימוני כוח 2–3×ש׳, הורד שומן קרביית, הגבּל אלכוהול. למדוד בבוקר בצום. [CDC פעילות][0][8]",
    "PROGESTERONE_abnormal": "תזמן דיגום ל-Luteal (כ-7 ימים לפני וסת) והימנע בִּיאָטִין. [FDA][3]",
    "LH_abnormal":           "תאם ליום מחזור וציין טיפולי פוריות/גלולות; הימנע בִּיאָטִין. [FDA][3]",
    "FSH_abnormal":          "כמו LH; שמור משקל תקין ופעילות. [CDC פעילות + FDA][0][3]",

    # --- ברזל / ויטמינים ---
    "IRON_low":       "צרוך ברזל עם ויטמין C (פלפל/הדרים) והפרד מסידן/קפה/תה ≥2ש׳; העדף בשרים רזים/קטניות מועשרות. [NIH-ODS][4][12]",
    "FERRITIN_low":   "אם תוסף — קח על קיבה ריקה עם מים/ויטמין C; הימנע מחלב/סידן סביב הבליעה; עקוב אחרי עצירות. [NIH-ODS][12]",
    "VITAMIN_B12_low":"הוסף ביצים/חלב/דגים; טבעונים — תוסף קבוע בצורת ציאנו/מתיל-B12 במינון יומי/שבועי מקובל. [NIH-ODS][5][13]",
    "VITAMIN_B12_high":"בדוק אם נלקחים תוספים/זריקות; הורד מינון אם אין אינדיקציה. [NIH-ODS][5][13]",

    # --- המאטולוגיה (CBC) ---
    "NEUTROPHILS_low":  "היגיינת ידיים קפדנית, הימנע ממגע עם חולים/קהל סגור; פנה דחוף אם חום ≥38°C. [CDC Neutropenia][—]",
    "NEUTROPHILS_high": "לרוב תגובה לזיהום/סטרס; הידרציה ומנוחה; עקוב אחרי חום/סימפטומים. (קליני)",
    "LYMPHOCYTES_low":  "שמור חיסונים עדכניים, שינה מספקת ותזונה מגוונת; הימנע מחשיפה לזיהומים. (כללי)",
    "LYMPHOCYTES_high": "שכיח בווירוסים — מנוחה/נוזלים; אם ממושך/חריג — בירור. (כללי)",
    "MONOCYTES_high":   "דלקתי/זיהומי — נהל גורם רקע (שינה/תזונה/זיהום פה/שיניים). (כללי)",
    "EOSINOPHILS_high": "נהל אלרגנים (אבקה/אבק/פרפום), שטיפות אף/אנטיהיסטמין לפי צורך; עקוב באסתמה. [NHS Allergy][—]",
    "BASOPHILS_high":   "לרוב אלרגי/תמיכתי; הקטן חשיפה לטריגר והמשך מעקב. (כללי)",
    "MPV_abnormal":     "אל תשנה טיפול לפי MPV בלבד; פרש יחד עם PLT ו-CBC מלא. (כללי)",

    # --- דגלי איכות דגימה ---
    "HEMOLYTIC_FLAG_high":"בקש דגימה חוזרת ללא אימון עצים קודם; מנוחה 10–15 ד׳ בישיבה; טיפול עדין במבחנה (ללא ניעור). [Lab/Quest][16]",
    "LIPEMIC_FLAG_high":   "דיגום בצום 9–12ש׳; הימנע מאלכוהול וארוחה שומנית ערב קודם. [Lab/Quest][16]",
    "ICTERIC_FLAG_high":   "דווח על תרופות/תוספים; דגום בבוקר בצום והקפד הידרציה. [Lab/Quest][16]",

    # ברירות מחדל — נשארות כמכשיר ביטחון, אך כמעט ולא יופעלו כעת
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
