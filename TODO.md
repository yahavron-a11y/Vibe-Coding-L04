# לוח המשימות המשותף (*Shared TODO Board*) ומעקב השלמה (`TODO.md`)

**פרויקט:** CivicShield AI — מגן התודעה הלאומי (`GOV-IL-RFP-2026-CSAI`)  
**ממשל הלוח:** `master` (תזמור ומעקב בין `architect`, `theory`, `simulator`, `redteam`)

---

## 1. משימות ארכיטקטורה, LaTeX ו-TikZ (`architect`)
- [x] **ARC-01:** הקמת מחלקת `civicshield.cls` עבור LuaLaTeX (פלטת צבעים, גופני `Heebo`/`JetBrains Mono`, כותרות עמוד, באנרי פרקים, קופסאות `tcolorbox`, ומעטפת `tikzhebrew`).
- [x] **ARC-02:** עיצוב שער הדוח המוסדי (`cover.tex`) עם רשת רקע, סמל מגן-רשת ב-TikZ, כרטיסיית תקציר ופס תחתון.
- [x] **ARC-03:** כתיבת פרק 1 (תקציר מנהלים, CONOPS, מטריצת RFP) + תרשים TikZ איור 1.1 (`fig_conops`).
- [x] **ARC-04:** הפקת תרשים TikZ איור 2.1 (`fig_public_sphere`) לשילוב בפרק 2.
- [x] **ARC-05:** כתיבת פרק 3 (בעלי עניין, FR-01..FR-15, NFR-01..NFR-08, תרחישי ייחוס UC-01..UC-04).
- [x] **ARC-06:** כתיבת פרק 4 (ארכיטקטורת 5 השכבות, טופולוגיית Hub/Inbox/TODO/ReAct, מפרט `Listing 4.1`, תקציב השהיה `238 ms`) + תרשימי TikZ איור 4.1 ואיור 4.2.
- [x] **ARC-07:** הפקת תרשימי TikZ איור 6.1 (עץ החלטות חוקתי), איור 7.1 (Gantt ל-24 חודשים), ואיור 8.1 (זרימת הפקת הדוח ומעגל תיקוני Red Team).
- [x] **ARC-08:** אימות הידור נקי ב-LuaLaTeX ללא אזהרות `Overfull \hbox` או שגיאות BiDi/RTL.

---

## 2. משימות תיאוריה, משפט חוקתי וביבליוגרפיה (`theory`)
- [x] **THY-01:** כתיבת פרק 2 (`chapters/ch2_theory.tex`) — 7 תיאוריות הליבה בתקשורת פוליטית ומדעי המדינה + טבלה 2.1 (מיפוי לרכיבי AI).
- [x] **THY-02:** כתיבת פרק 6 (`chapters/ch6_law.tex`) — דמוקרטיה מתגוננת, עץ 4 השערים (`OPA/Rego`), חתימה משולשת (`3-of-3 Ed25519`), $\epsilon$-DP וטבלה 6.1 (EU AI Act / DSA / NIST).
- [x] **THY-03:** שילוב ואימות רשימה ביבליוגרפית מלאה (26 מקורות אקדמיים והנדסיים ממוספרים) ותאימות ציטוטים בכל הפרקים.

---

## 3. משימות סימולציה, מודלים כמותיים ו-ROI (`simulator`)
- [x] **SIM-01 (SIRI Engine):** מימוש פותר RK4 (`dt=0.1`, `T=30d`, `beta=0.68`, `gamma=0.14`, `nu=0.22/day`) וסריקת רגישות; אימות `R0=4.86`, `pc=79.4%`, `Peak I(t)<=7.6%`, `R(30)<20%`.
- [x] **SIM-02 (Hegselmann-Krause Engine):** מימוש משטר מקוטב (`eps=0.22`, `delta_rep=0.03`) מול גישור פלורליסטי (`eps_eff=0.402`, עוגן `0.28*x_i(0)`) עבור `N=200, T=60`.
- [x] **SIM-03 (Bayesian Fusion Engine):** מימוש איחוד לוג-אודס ב-4 מודאליות (`P(F)=0.05`) וכיול כך ש-`AUC > 0.96` ו-`Precision >= 0.90` (תיקון פער `0.942` מאיור 5.3A).
- [x] **SIM-04 (M/M/c Queueing & Auto-Scaler):** מימוש מודל Erlang-C (`mu=480 EPS/Pool`, `T_pipe=38 ms`) עבור `c in {16, 24, 34}` ופרופיל 24 שעות; אימות `E[T_sys] <= 250 ms` ב-`12,000 EPS`.
- [x] **SIM-05 (Spillover & 5Y ROI Models):** מימוש מודל זליגה 72 שעות ומסגור אנטמן + מחשבון CAPEX/OPEX/ROI ל-5 שנים (`TCO=68.7M`, `Value=145.0M`, `Break-Even=2.2y`) ופרקים 5 ו-7.
- [x] **SIM-06 (Scripts & Figures):** הפקת 6 הגרפים המדעיים ב-`scripts/generate_figures.py` ועטיפת המודלים ככלי Python דטרמיניסטיים עם בדיקות `pytest`.

---

## 4. משימות ביקורת חוקתית ואימות LuaLaTeX BiDi (`redteam`)
- [x] **QA-BUILD:** הידור רב-שלבי נקי של `main.tex` ב-`lualatex` (`0` שגיאות, `0` הפניות לא מוגדרות `??`, תאימות TOC/LOF/LOT ו-26 מקורות).
- [x] **QA-BIDI (`RT-03`):** בדיקת איטום RTL בתיבות `tcolorbox` וב-`tikzhebrew`, בידוד LTR למונחים באנגלית/JSON (`Listing 4.1`), כיווניות משוואות (Eq. 5.1–6.1) וסדר עמודות RTL בטבלאות.
- [x] **QA-FIGS (`RT-04`):** הרצת `scripts/verify_report.py`, אימות 6 הגרפים ללא חיתוך טקסט, והצלבת מספרים מלאה בין טקסט, טבלאות ואיורים (כולל סגירת פער `AUC > 0.96`).
- [x] **QA-SIGN:** כתיבת פרק 8 (`chapters/ch8_method.tex`), ביקורת עמוד-אחר-עמוד של ה-PDF הסופי, וחתימת Red Team (`0` ממצאים קריטיים פתוחים ב-`RT-01`..`RT-04`).

---

## 5. איחוד והרכבה סופית (`master`)
- [x] **MAS-01:** יצירת `PRD.md`, `PLAN.md`, `TODO.md` ועדכון `README.md` לפי מדריך הפרויקט.
- [x] **MAS-02:** הרכבת `main.tex` והפקת `CivicShield_AI_Preliminary_Report.pdf` המאושר לאחר חתימת `redteam`.
