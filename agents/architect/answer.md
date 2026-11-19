# Architecture, LaTeX Class, TikZ Diagrams & Documentation Spec (Matching `CivicShield_AI_Preliminary_Report.pdf`)

This document provides the complete architectural and typographic specification derived from inspecting `CivicShield_AI_Preliminary_Report.pdf`, ready for immediate integration into our repository's LaTeX build, TikZ figures, `PLAN.md`, `PRD.md`, `TODO.md`, and `README.md`.

---

## 1. LaTeX Class & Visual Design Specification (`civicshield.cls`)

### 1.1 Engine, Encoding & BiDi/RTL Architecture
- **Compiler:** `LuaLaTeX` (required for native OpenType Hebrew/English font shaping and reliable BiDi).
- **Language & BiDi:**
  - `\usepackage[bidi=basic, layout=tabular]{babel}`
  - `\babelprovide[main, import]{hebrew}`
  - `\babelprovide[import]{english}`
- **Typography (`fontspec`):**
  - Primary Hebrew/Latin Sans-Serif: `Heebo` (or `Assistant` / `Arial` fallback) for crisp institutional readability.
  - Monospace (JSON envelopes, code, IDs): `JetBrains Mono` (or `Consolas` fallback) with `Scale=0.88`.
- **Page Geometry (`geometry`):**
  - `a4paper`, `top=2.4cm`, `bottom=2.4cm`, `left=2.1cm`, `right=2.1cm`, `headheight=16pt`.
- **Headers & Footers (`fancyhdr`):**
  - **Header (content pages):** Right: `\textbf{CivicShield AI} — מגן התודעה הלאומי (מטלה 2: דוח מכין)` | Left: current chapter name (`\leftmark`). Thin `0.8pt` teal rule (`csTeal`) underneath.
  - **Footer (content pages):** Left: `עמוד \thepage` | Right (odd/even): `אוניברסיטת חיפה | יישומי AI ו-Vibe Coding (ד"ר יורם סגל)` / `CivicShield AI — מסמך חזוי והצעה למכרז לאומי`. Thin `0.5pt` slate rule above.

### 1.2 Official Color Palette (`xcolor`)
```latex
\definecolor{csNavy}{HTML}{0B1F3A}       % Primary institutional dark navy (cover, chapter banners, code headers)
\definecolor{csTeal}{HTML}{0F766E}       % Secondary accent teal (subsections, use cases, healthy/bridging nodes)
\definecolor{csAmber}{HTML}{D97706}      % Gold/amber accent (cover subtitle, tender callouts, dividers)
\definecolor{csCrimson}{HTML}{B91C1C}    % Alert red (constitutional redlines, FIMI/adversarial nodes)
\definecolor{csSlate}{HTML}{334155}      % Body/caption secondary slate
\definecolor{csNavyBg}{HTML}{F0F4F8}     % Soft navy tint for info boxes & roadmap
\definecolor{csTealBg}{HTML}{F0FDFA}     % Soft teal tint for operational use cases
\definecolor{csAmberBg}{HTML}{FFFBEB}    % Soft amber tint for tender & executive boxes
\definecolor{csRedBg}{HTML}{FEF2F2}      % Soft crimson tint for constitutional warnings
\definecolor{csBorder}{HTML}{CBD5E1}     % Table & neutral frame borders
```

### 1.3 Cover Page Layout
1. **Top Hero Band (40% page height, full-bleed `csNavy`):**
   - Subtle dark-blue geometric grid overlay drawn in TikZ (`step=1cm`, `opacity=0.12`).
   - Top centered English header in `csAmber`: `UNIVERSITY OF HAIFA  |  NATIONAL TENDER PRELIMINARY REPORT`.
   - Sub-header in white: `אוניברסיטת חיפה — קורס יישומי AI ו-Vibe Coding (ד"ר יורם סגל)`.
   - **Central Vector Emblem (TikZ):** Concentric shield in `csTeal`/`csAmber` with an internal 6-node connected graph representing the multi-agent mesh.
   - Main Title: `\Huge\bfseries\color{white} CivicShield AI` and subtitle `\Large\bfseries\color{csAmber} מגן התודעה הלאומי`.
2. **Dual-Tone Divider Bar:** Full-width `4pt` `csAmber` stripe directly above a `3pt` `csTeal` stripe.
3. **White Body Section:**
   - Main Hebrew/English report title (`דוח מכין (Preliminary Design Report) להקמת מערכת רב-סוכנית לאומית`), blue subtitle (`להגנה על הספירה הציבורית, זיהוי מניפולציות תודעה ושמירה על טוהר הבחירות`), and interdisciplinary tagline.
   - Rounded bordered summary card (`csNavy` border, `csNavyBg` fill) containing 3 bolded bullets: `מענה למכרז ממשלתי משותף`, `פרדיגמת התכנון`, `מתודולוגיית הכנה`.
4. **Bottom Footer Band (full-bleed `csNavy` with top `3pt` `csTeal` accent):**
   - Course, Lecturer, Version (`v1.0-RFP-FINAL`), Date, and Author/Submitter metadata in white.

### 1.4 Chapter Banners & Custom Environments (`tcolorbox` + `environ`)
- **Chapter Banner:** Full-width rounded `csNavy` box with `3pt` bottom accent (`csAmber` for numbered chapters 1–8; `csTeal` for front/back matter such as TOC, LOF, LOT, Document Control, Bibliography). Displays small `csAmber` label `פרק \thechapter` above large white bold title.
- **Section Headings (`titlesec`):**
  - `\section`: `csNavy`, `\Large\bfseries`
  - `\subsection`: `csTeal`, `\large\bfseries`
  - `\subsubsection`: `csSlate`, `\normalsize\bfseries`
- **Callout Boxes (`tcolorbox`):**
  - `tenderbox` (`csAmber` header, `csAmberBg` fill): Tender identification, RFP mandate, executive callouts.
  - `constitutionalbox` (`csCrimson` header, `csRedBg` fill): Constitutional redlines, legal risks, anti-censorship guarantees.
  - `usecasebox` (`csTeal` header, `csTealBg` fill): Operational Use Cases (`UC-01`..`UC-04`).
  - `infobox` (`csNavy` header, `csNavyBg` fill): Roadmap summary, mathematical/RK4 insights, Entman translation.
  - `jsonlisting` (`listings` wrapped in `csNavy`-header `tcolorbox`, forced LTR via `\begin{otherlanguage}{english}`): For Hub JSON Envelopes (`Listing 4.1`).
- **BiDi-Safe TikZ Wrapper (`tikzhebrew`):**
  ```latex
  \NewEnviron{tikzhebrew}[1][]{%
    \begin{otherlanguage}{english}%
    \begin{tikzpicture}[#1]%
      \BODY%
    \end{tikzpicture}%
    \end{otherlanguage}%
  }
  ```
  *Design Rationale (RT-03 fix):* Forces TikZ coordinate math to execute strictly in LTR while allowing Hebrew node text inside `\foreignlanguage{hebrew}{...}` without reversing arrows, coordinates, or overflowing boxes.

---

## 2. Document Structure (8 Chapters + Front/Back Matter)

| Section | Title / Scope | Figures & Tables |
| :--- | :--- | :--- |
| **Front Matter** | Cover Page, Document Control & Tender Metadata Table, Institutional Abstract, TOC, List of Figures (12), List of Tables (13) | Document Control Table |
| **Chapter 1** | תקציר מנהלים, רקע המכרז וחוזה ההקמה הלאומי (CONOPS, Strategic Gap, RFP Compliance Matrix, 8-Chapter Roadmap) | Fig 1.1 (TikZ), Tables 1.1–1.2 |
| **Chapter 2** | תשתית תיאורטית: תקשורת פוליטית, מדעי המדינה ולוחמת תודעה (7 Theories mapped to AI components) | Fig 2.1 (TikZ), Table 2.1 |
| **Chapter 3** | אפיון דרישות המערכת, בעלי עניין ותרחישי ייחוס מבצעיים (Stakeholders, FR-01..FR-15, NFR-01..NFR-08, UC-01..UC-04, Spillover Sim) | Fig 3.1 (Python), Tables 3.1–3.5 |
| **Chapter 4** | ארכיטקטורת המערכת, תזמור רב-סוכנים וצינורות הנתונים (5 Layers, Hub/Inbox/TODO/ReAct, JSON Envelope, 250ms Latency Budget) | Fig 4.1 (TikZ), Fig 4.2 (TikZ), Listing 4.1, Table 4.1 |
| **Chapter 5** | מודלים מתמטיים, אלגוריתמיקה וסימולציות כמותיות ב-Python (SIRI ODEs, Hegselmann-Krause, Bayesian Deepfake Fusion, M/M/c Erlang-C) | Figs 5.1–5.4 (Python), Table 5.1 |
| **Chapter 6** | משפט חוקתי, דמוקרטיה מתגוננת, אתיקה והגנת הפרטיות (Constitutional Gate, 3-of-3 Ed25519 Quorum, $\epsilon$-DP, EU AI Act/DSA/NIST) | Fig 6.1 (TikZ), Table 6.1 |
| **Chapter 7** | ניהול סיכונים, תוכנית עבודה הנדסית, תקציב ומדדי הצלחה (Risk Matrix, 24-Month Gantt, 5-Year CAPEX/OPEX/ROI, KPI/SLA) | Fig 7.1 (TikZ), Fig 7.2 (Python), Tables 7.1–7.3 |
| **Chapter 8** | מתודולוגיית הפיתוח: ועדת המומחים של הסוכנים וביקורת איכות (Lesson 4 Multi-Agent Committee, `team.json`/`AGY.md`, Red Team Log RT-01..RT-04, Handover) | Fig 8.1 (TikZ), Tables 8.1–8.2 |
| **Back Matter** | ביבליוגרפיה ומקורות מדעיים והנדסיים (26 numbered academic & engineering references) | — |

---

## 3. TikZ Vector Diagrams Specification (6 Technical Diagrams + Cover Emblem)

1. **Cover Emblem (`cover_emblem`):** Shield contour (`csTeal` outer, `csAmber` inner) housing a 6-node mesh graph with glowing `csAmber` center node.
2. **Fig 1.1 — End-to-End CONOPS (`fig_conops`):** 4 horizontal rounded rectangles connected left-to-right:
   - `1. איסוף גלוי` (`csNavy` border: `OSINT + ε-DP Filter`)
   - `2. ועדת סוכני AI` (`csTeal` border: `SIRI + ReAct Engine`)
   - `3. שער חוקתי` (`csCrimson` border: `Triple-Key Human Sign`)
   - `4. תגובה ומגן` (`csAmber` border: `Prebunking + Audit`)
   - Bottom dashed feedback box (`csNavyBg`): `לולאת למידה וביקורת (Audit Log)` feeding back from Stage 4 to Stage 2.
3. **Fig 2.1 — Deliberative vs. FIMI-Attacked Public Sphere (`fig_public_sphere`):** Two parallel vertical columns separated by a dashed divider and central `VS` circle:
   - Left (`csTeal` header): `א. מרחב ציבורי חסין (דליברטיבי)` — 4 downward flow boxes ending in `תוצאה: לגיטימציה וטוהר בחירות`.
   - Right (`csCrimson` header): `ב. מרחב מורעל תחת מתקפת FIMI` — 4 downward flow boxes ending in `תוצאה: שחיקת הלגיטימציה הדמוקרטית`.
4. **Fig 4.1 — 5-Layer Architecture (`fig_5layer_arch`):** 5 stacked horizontal layers centered between two tall vertical sidebars:
   - Left sidebar (`csCrimson` border, `csRedBg`): `מעטפת אבטחה` (`Zero-Trust mTLS + HSM`, `ארגז חול נגד הזרקת Prompt`).
   - Right sidebar (`csTeal` border, `csTealBg`): `יומן ביקורת` (`Immutable Merkle Log`, `תיעוד חתום לביקורת בית המשפט`).
   - Center stack: Layer 1 (OSINT + $\epsilon$-DP) → Layer 2 (Embeddings, CIB, Deepfake Classifiers) → Layer 3 (`csTealBg`, Multi-Agent Mesh + ReAct Engine) → Layer 4 (`csRedBg`, Constitutional Guardrail + 3-of-3 Ed25519 Quorum) → Layer 5 (`csAmberBg`, Prebunking Feeds, Journalist API, Transparency Portal).
5. **Fig 4.2 — Layer 3 Multi-Agent Orchestration Topology (`fig_agent_topology`):**
   - Top node (`csNavy` fill, white text): `סוכן על-מתזמר (Master Orchestrator)`.
   - Mid row: `מרכז תקשורת (Communication Hub)` (`csTeal` border) and `לוח משימות משותף (Shared TODO)` (`csAmber` border).
   - Specialist row (5 boxes with `[Inbox]` & `Tools:`): `סוכן רשת ובוטים`, `סוכן מסגור אנטמן`, `סוכן פורנזיקה`, `סוכן סימולציה`, `בקרה חוקתית` (`csCrimson` border).
   - Bottom dashed bar: `לולאת ביצוע פנימית בכל סוכן (ReAct Loop): Thought -> Action (Python/DB) -> Observation -> Confidence`.
6. **Fig 6.1 — Constitutional Decision Tree (`fig_constitutional_tree`):** 4 sequential decision gates (`שער 1`..`שער 4`) with labeled `כן`/`לא` branches:
   - Gate 1 (Private Data?) → `כן`: `דחייה מיידית ומחיקה (Hard Drop)` | `לא (גלוי)` → Gate 2.
   - Gate 2 (Authentic Political Speech / Satire?) → `כן`: `ביטוי פוליטי מוגן` | `לא (CIB/FIMI)` → Gate 3.
   - Gate 3 ($R_0 > 1.5$ & $P(F|e) \ge 0.90$?) → `לא`: `ניטור מאקרו אנונימי בלבד` | `כן` → Gate 4.
   - Gate 4 (Proportionality & Less-Restrictive-Means Test) → splits into `נתיב א': חיסון תודעתי אובייקטיבי (Prebunking)` (`csAmber`) vs. `נתיב ב': עתירת הסרה קריפטוגרפית (חתימה משולשת)` (`csCrimson`).
7. **Fig 7.1 — 24-Month Engineering Roadmap Gantt (`fig_gantt`):** Dark navy header bar (`M1`, `M6`, `M12`, `M18`, `M24`), 4 staggered horizontal phase bars with milestone diamonds (`M1-M6`, `M6-M13`, `M12-M19`, `M18-M24`), plus full-span bottom amber bar (`ביקורת שופטים ומבדק הטיה דו-שבועי`).
8. **Fig 8.1 — Multi-Agent Production Workflow & Red Team Fix Loop (`fig_workflow`):** `Master` → parallel (`Theory`, `Architect`, `Simulator`) → `Red Team / LuaLaTeX BiDi Gate` → `Approved PDF` (green) with dashed red `Rejection / Fix Loop` returning to `Master`.

---

## 4. Architecture & Design Sections for Project Documentation

### 4.1 Section for `PLAN.md`
```markdown
## ארכיטקטורת מערכת, עיצוב LaTeX ותוכנית תרשימים (Architect)

### 1. תשתית התיעוד וההידור (`civicshield.cls`)
- **מנוע הידור:** LuaLaTeX עם `babel` (`hebrew, bidi=basic`) ו-`fontspec` (גופן `Heebo` לטקסט ו-`JetBrains Mono` לקוד/JSON).
- **זהות ויזואלית:** פלטת צבעים מוסדית (`csNavy #0B1F3A`, `csTeal #0F766E`, `csAmber #D97706`, `csCrimson #B91C1C`), שער מכרז דו-גווני עם סמל מגן וקטורי, באנרי פרקים מעוגלים, ותיבות תוכן ייעודיות (`tenderbox`, `constitutionalbox`, `usecasebox`, `infobox`, `jsonlisting`).
- **איטום דו-כיווניות (BiDi Isolation):** שימוש במעטפת `\NewEnviron{tikzhebrew}` להרצת קואורדינטות TikZ ב-LTR תוך שמירת תוויות בעברית ללא גלישה או היפוך.

### 2. ארכיטקטורת 5 השכבות (פרק 4)
1. **שכבה 1 — קליטה אנונימית:** `Kafka / Flink` (OSINT גלוי בלבד) + `PII Redactor` + הזרקת רעש $\epsilon$-DP ($\epsilon \le 1.2$).
2. **שכבה 2 — חילוץ מאפיינים ופורנזיקה מהירה:** וקטורים סמנטיים בעברית/ערבית, אשכול בוטים טמפורלי (`CIB`), ומסווגי Deepfake מולטי-מודאליים על `ONNX/Triton GPU`.
3. **שכבה 3 — מערך התזמור הרב-סוכני:** `Master Orchestrator`, `Communication Hub` (מעטפות `Pydantic JSON`), `Shared TODO`, וחמישה סוכנים מומחים בלולאת `ReAct` (סינון Triage חוסך 94% מעלויות ה-LLM).
4. **שכבה 4 — השער החוקתי:** `Constitutional Guardrail Agent` (`OPA/Rego`) + מנגנון חתימה קריפטוגרפית משולשת (`3-of-3 Ed25519 Quorum`: שופט עליון/ועדת בחירות, מערך הסייבר, נציג ציבור/אופוזיציה).
5. **שכבה 5 — הפצה, שקיפות וביקורת:** פיד חיסון תודעתי (`Prebunking`), API לעיתונאים, פורטל שקיפות ציבורי ויומן `Immutable Merkle Log`.

### 3. תרשימי TikZ וקטוריים באחריות ה-Architect
- `cover_emblem`: סמל מגן-רשת וקטורי לשער הדוח.
- `fig_conops` (איור 1.1): תפיסת ההפעלה המבצעית (CONOPS) מקצה לקצה + לולאת Audit.
- `fig_public_sphere` (איור 2.1): השוואת מרחב ציבורי דליברטיבי מול מתקפת FIMI.
- `fig_5layer_arch` (איור 4.1): ארכיטקטורת 5 השכבות + מעטפת Zero-Trust ויומן Merkle.
- `fig_agent_topology` (איור 4.2): טופולוגיית Hub, Inbox, TODO ולולאת ReAct.
- `fig_constitutional_tree` (איור 6.1): עץ ההחלטות החוקתי (4 שערים).
- `fig_gantt` (איור 7.1): מפת דרכים הנדסית (Gantt) ל-24 חודשים.
- `fig_workflow` (איור 8.1): זרימת הפקת הדוח ומעגל תיקוני הצוות האדום.
```

---

### 4.2 Section for `PRD.md`
```markdown
## מפרט ארכיטקטורה, דרישות פונקציונליות ולא-פונקציונליות (FR / NFR)

### דרישות פונקציונליות (FR-01 עד FR-15)
- **קבוצה א' — קליטה, ניטור וזיהוי פורנזי:**
  - `FR-01 (P0)`: קליטת זרמי OSINT פומביים בזמן אמת ללא גישה למסרים פרטיים.
  - `FR-02 (P0)`: סינון ומיסוך פרטיות בכניסה (`PII Redaction` + $\epsilon$-DP).
  - `FR-03 (P0)`: גילוי התנהגות מתואמת (`CIB`, $\Delta t < 2\text{s}$, גרף שיתוף זהה).
  - `FR-04 (P1)`: סיווג מסגור אנטמן אוטומטי ב-4 פונקציות בעברית וערבית.
  - `FR-05 (P0)`: גלאי Deepfake מולטי-מודאלי (אודיו, וידאו, מטא-דאטה `C2PA`).
- **קבוצה ב' — מידול תודעתי, קיטוב וחיזוי:**
  - `FR-06 (P0)`: מנוע הדבקה תודעתית (`SIRI ODEs` — חישוב $\beta(t), R_0, p_c$).
  - `FR-07 (P1)`: מדידת זליגה בין-ערוצית (`Spillover Lead Time`).
  - `FR-08 (P1)`: מדד קיטוב ותיבות תהודה (`Hegselmann-Krause`, `Bimodality`).
  - `FR-09 (P0)`: דירוג סמכותיות אפיסטמית מול מאגרי ועדת הבחירות המרכזית.
  - `FR-10 (P2)`: שיוך מבצע השפעה (`FIMI Attribution`).
- **קבוצה ג' — הגנה חוקתית, חיסון תודעתי ושקיפות:**
  - `FR-11 (P0)`: מחסום מניעת צנזורה אוטומטית ברמת חומרה ותוכנה.
  - `FR-12 (P0)`: מחולל חיסון תודעתי (`Prebunking` — 3 חלופות ניטרליות).
  - `FR-13 (P0)`: חתימה משולשת (`3-of-3 Ed25519 Quorum`) לפני כל פעולה פורמלית.
  - `FR-14 (P0)`: יומן ביקורת בלתי ניתן לשינוי (`Append-Only Merkle Log` + `ReAct Trace`).
  - `FR-15 (P1)`: דשבורד שקיפות פתוח לציבור בזמן אמת.

### דרישות לא-פונקציונליות (NFR-01 עד NFR-08)
- `NFR-01 (Latency)`: השהיית עיבוד ממוצעת `< 250 ms` בעומס שיא של `12,000 EPS` (תקציב שכבות: 18+38+45+115+22 = `238 ms`, יתרת אמינות `12 ms`).
- `NFR-02 (Availability)`: זמינות יום בחירות `99.99%` (`Active-Active Multi-AZ`, `Failover < 15s`).
- `NFR-03 (Deepfake Accuracy)`: `AUC > 0.96`, `Precision >= 0.90`.
- `NFR-04 (Privacy)`: תקציב פרטיות דיפרנציאלית $\epsilon \le 1.2$ ומחיקה אוטומטית (`TTL Purge`) כל 30 יום.
- `NFR-05 (Fairness)`: פער דיוק בין גושים פוליטיים `< 1.5%` (`Dual-Wing Parity Testing`).
- `NFR-06 (Multilingual)`: תמיכה מלאה בעברית, ערבית, רוסית ואמהרית כולל סלנג ותעתיקים.
- `NFR-07 (XAI)`: 100% נימוק ראיות ומפת פונקציות אנטמן לכל התראה.
- `NFR-08 (Security)`: עמידות נגד `Prompt Injection` (סכמת `Pydantic JSON` קשיחה + ארגז חול מבודד).
```

---

### 4.3 Section for `TODO.md`
```markdown
## משימות ארכיטקטורה, LaTeX ו-TikZ (`architect`)
- [ ] **ARC-01:** הקמת מחלקת `civicshield.cls` עבור LuaLaTeX (פלטת צבעים, גופני `Heebo`/`JetBrains Mono`, כותרות עמוד, באנרי פרקים, קופסאות `tcolorbox`, ומעטפת `tikzhebrew`).
- [ ] **ARC-02:** עיצוב שער הדוח המוסדי (`cover.tex`) עם רשת רקע, סמל מגן-רשת ב-TikZ, כרטיסיית תקציר ופס תחתון.
- [ ] **ARC-03:** כתיבת פרק 1 (תקציר מנהלים, CONOPS, מטריצת RFP) + תרשים TikZ איור 1.1 (`fig_conops`).
- [ ] **ARC-04:** הפקת תרשים TikZ איור 2.1 (`fig_public_sphere`) לשילוב בפרק 2.
- [ ] **ARC-05:** כתיבת פרק 3 (בעלי עניין, FR-01..FR-15, NFR-01..NFR-08, תרחישי ייחוס UC-01..UC-04).
- [ ] **ARC-06:** כתיבת פרק 4 (ארכיטקטורת 5 השכבות, טופולוגיית Hub/Inbox/TODO/ReAct, מפרט Hub JSON Envelope Listing 4.1, תקציב השהיה 238ms/250ms) + תרשימי TikZ איור 4.1 ואיור 4.2.
- [ ] **ARC-07:** הפקת תרשימי TikZ איור 6.1 (עץ החלטות חוקתי), איור 7.1 (Gantt ל-24 חודשים), ואיור 8.1 (זרימת הפקת הדוח ומעגל תיקוני Red Team).
- [ ] **ARC-08:** אימות הידור נקי ב-LuaLaTeX ללא אזהרות `Overfull \hbox` או שגיאות BiDi/RTL.
```

---

### 4.4 Updated `README.md` Table
```markdown
| קובץ / רכיב | תיאור ותפקיד במערכת | בעלים (Agent) |
| :--- | :--- | :--- |
| **[PRD.md](./PRD.md)** | מסמך דרישות המוצר: מפרט פונקציונלי (FR-01..15), דרישות ביצועים (NFR-01..08), עקרונות ברזל חוקתיים וקריטריוני הצלחה | master |
| **[PLAN.md](./PLAN.md)** | תוכנית ביצוע הנדסית: ארכיטקטורת 5 השכבות, תזמור רב-סוכנים, עיצוב LaTeX/TikZ ומפת דרכים | master / architect |
| **[TODO.md](./TODO.md)** | לוח משימות משותף (Shared TODO Board) לניהול מעקב ביצוע ומסירה בין חמשת הסוכנים | master |
| **[team.json](./team.json)** | הגדרת ועדת המומחים של הסוכנים, תחומי אחריות ופרוטוקול התקשורת ברשת | master |
| **[civicshield.cls](./civicshield.cls)** | מחלקת LuaLaTeX מוסדית: פלטת צבעים, טיפוגרפיה דו-כיוונית (BiDi), באנרים, קופסאות ומעטפת `tikzhebrew` | architect |
| **[main.tex](./main.tex)** | קובץ השורש המאחד את שער הדוח, 8 הפרקים, תרשימי ה-TikZ, הגרפים המדעיים והביבליוגרפיה | master |
| **[chapters/ch1_exec.tex](./chapters/ch1_exec.tex)** | פרק 1: תקציר מנהלים, רקע המכרז, תפיסת הפעלה (CONOPS) ומטריצת עמידה בדרישות | architect |
| **[chapters/ch2_theory.tex](./chapters/ch2_theory.tex)** | פרק 2: תשתית תיאורטית — 7 תיאוריות בתקשורת פוליטית ומדעי המדינה ומיפוין לרכיבי AI | theory |
| **[chapters/ch3_reqs.tex](./chapters/ch3_reqs.tex)** | פרק 3: בעלי עניין, מפרט FR/NFR, תרחישי ייחוס מבצעיים (UC-01..04) ובלימת זליגת סדר יום | architect |
| **[chapters/ch4_arch.tex](./chapters/ch4_arch.tex)** | פרק 4: ארכיטקטורת 5 השכבות, טופולוגיית Hub/ReAct, מפרט Hub JSON ותקציב השהיה (`238ms`) | architect |
| **[chapters/ch5_models.tex](./chapters/ch5_models.tex)** | פרק 5: מודלים מתמטיים וסימולציות Python (SIRI ODEs, Hegselmann-Krause, איחוד בייסיאני, M/M/c) | simulator |
| **[chapters/ch6_law.tex](./chapters/ch6_law.tex)** | פרק 6: משפט חוקתי, דמוקרטיה מתגוננת, חתימה משולשת (`3-of-3 Ed25519`) ופרטיות דיפרנציאלית ($\epsilon$-DP) | theory |
| **[chapters/ch7_roadmap.tex](./chapters/ch7_roadmap.tex)** | פרק 7: ניהול סיכונים, מפת דרכים (Gantt 24 חודשים), תקציב חמש-שנתי (CAPEX/OPEX/ROI) ו-KPI/SLA | simulator |
| **[chapters/ch8_method.tex](./chapters/ch8_method.tex)** | פרק 8: מתודולוגיית שיעור 4, ועדת הסוכנים ויומן ממצאי ביקורת הצוות האדום (`RT-01..04`) | redteam |
| **[scripts/generate_figures.py](./scripts/generate_figures.py)** | סקריפט Python דטרמיניסטי להרצת הסימולציות והפקת 6 הגרפים המדעיים (PDF/PNG) | simulator |
| **[scripts/verify_report.py](./scripts/verify_report.py)** | סקריפט אימות אוטומטי לצוות האדום: בדיקת הידור LuaLaTeX, שלמות BiDi, תאימות גרפים והפניות | redteam |
| **[CivicShield_AI_Preliminary_Report.pdf](./CivicShield_AI_Preliminary_Report.pdf)** | הדוח המכין הסופי המהודר (44 עמודים, 12 איורים, 13 טבלאות, 26 מקורות) | master / redteam |
```
