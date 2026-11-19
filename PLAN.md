# תוכנית האדריכלות, שלבי הביצוע ההנדסיים ומיפוי המודלים (`PLAN.md`)

**פרויקט:** CivicShield AI — מגן התודעה הלאומי (`GOV-IL-RFP-2026-CSAI`)  
**מבוסס על עיצוב ומבנה:** `CivicShield_AI_Preliminary_Report.pdf` (`v1.0-RFP-FINAL`)  
**בעלים:** `master` (איחוד תוצרי `architect`, `theory`, `simulator`, `redteam`)

---

## 1. תשתית התיעוד, עיצוב ה-PDF וההידור (`civicshield.cls`)

- **מנוע הידור:** `LuaLaTeX` עם `\usepackage[bidi=basic, layout=tabular]{babel}` (עברית כשפה ראשית, אנגלית כשפה משנית) ו-`fontspec`.
- **טיפוגרפיה וגאומטריה:** גופן `Heebo` (חלופה: `Assistant` / `Arial`) לטקסט מוסדי, `JetBrains Mono` (`Scale=0.88`) ל-JSON וקוד; `a4paper`, שוליים `top/bottom=2.4cm`, `left/right=2.1cm`.
- **פלטת צבעים מוסדית (`xcolor`):**
  - `csNavy` (`#0B1F3A`), `csTeal` (`#0F766E`), `csAmber` (`#D97706`), `csCrimson` (`#B91C1C`), `csSlate` (`#334155`), וגווני רקע רכים (`csNavyBg`, `csTealBg`, `csAmberBg`, `csRedBg`, `csBorder`).
- **רכיבי עיצוב (`tcolorbox` + `environ`):**
  - שער מוסדי עם פס עליון מלא ב-`csNavy`, רשת גאומטרית, סמל מגן-רשת וקטורי ב-TikZ, מפריד דו-גווני (`csAmber`/`csTeal`), כרטיסיית תקציר ופס תחתון.
  - באנרי פרקים מעוגלים (`csAmber` לפרקים 1–8; `csTeal` לחלקי הפתיחה והסיום) וקופסאות `tenderbox`, `constitutionalbox`, `usecasebox`, `infobox`, `jsonlisting`.
  - **איטום BiDi (`RT-03`):** מעטפת `\NewEnviron{tikzhebrew}` המריצה קואורדינטות TikZ ב-LTR תוך שמירה על תוויות עברית תקינות.

---

## 2. ארכיטקטורת 5 השכבות (פרק 4)

1. **שכבה 1 — קליטה אנונימית (`18 ms`, 100%):** `Kafka / Flink` (OSINT גלוי בלבד) + `PII Redactor` + הזרקת רעש $\epsilon$-DP ($\epsilon \le 1.2$).
2. **שכבה 2 — חילוץ מאפיינים ופורנזיקה מהירה (`38 ms`, 100%):** וקטורים סמנטיים בעברית/ערבית, אשכול בוטים טמפורלי (`CIB`), ומסווגי Deepfake על `ONNX/Triton GPU`.
3. **שכבה 3 — מערך התזמור הרב-סוכני (`45 ms` Triage / `115 ms` ReAct):** `Master Orchestrator`, `Communication Hub` (מעטפות `Pydantic JSON`), `Shared TODO`, וחמישה סוכנים מומחים בלולאת `ReAct` (סינון Triage חוסך `94%` מעלויות LLM).
4. **שכבה 4 — השער החוקתי (`22 ms` עם שכבה 5):** `Constitutional Guardrail Agent` (`OPA/Rego`, עץ 4 שערים) + `3-of-3 Ed25519 Quorum`.
5. **שכבה 5 — הפצה, שקיפות וביקורת:** פיד חיסון תודעתי (`Prebunking`), API לעיתונאים, פורטל שקיפות ציבורי ויומן `Immutable Merkle Log`.

---

## 3. מיפוי המודלים המתמטיים והתרשימים

### א. מודלים כמותיים ב-Python (`simulator` — `scripts/generate_figures.py`)
1. **SIRI ODEs (RK4, $\Delta t = 0.1\text{d}, T = 30\text{d}$):** $\beta = 0.68, \gamma = 0.14 \implies R_0 = 4.86, p_c = 79.4\%$; הוכחת בלימת שיא $I(t)$ מ-$47.2\%$ ל-$7.6\%$ באמצעות Prebunking ($\nu = 0.22/\text{day}$).
2. **Hegselmann-Krause ($N = 200, T = 60$):** השוואת משטר מקוטב ($\epsilon = 0.22, \delta_{\text{rep}} = 0.03$) מול גישור פלורליסטי ($\epsilon_{\text{eff}} = 0.402$ ועוגן אותנטיות $28\%$).
3. **איחוד ראיות בייסיאני (4 מודאליות, $P(F) = 0.05$):** איחוד טקסט, אודיו, וידאו ורשת/C2PA; כיול מדויק להבטחת `AUC > 0.96` ו-`Precision >= 0.90` (פתרון פער `0.942` מאיור 5.3A).
4. **תורת התורים `M/M/c Erlang-C`:** $\mu = 480\text{ EPS/Pool}$, השוואת $c \in \{16, 24, 34\}$ קבוצות GPU ופרופיל עומס 24 שעות ביום בחירות (`12,000 EPS`, השהיה $\le 250\text{ ms}$).
5. **זליגה בין-ערוצית ו-ROI חמש-שנתי:** מודל 72 שעות לזליגה ומסגור אנטמן + מודל CAPEX/OPEX (`TCO = 68.7M NIS`, ערך חוסן `145.0M NIS`, נקודת איזון `שנה 2.2`).

### ב. תרשימי TikZ וקטוריים (`architect`)
- `cover_emblem`, `fig_conops` (איור 1.1), `fig_public_sphere` (איור 2.1), `fig_5layer_arch` (איור 4.1), `fig_agent_topology` (איור 4.2), `fig_constitutional_tree` (איור 6.1), `fig_gantt` (איור 7.1), ו-`fig_workflow` (איור 8.1).

---

## 4. שלבי הביצוע ההנדסיים (מפת דרכים 24 חודשים)

1. **שלב 1 (חודשים 1–6) — תשתית, פרטיות וכיול בסיס:** הקמת `civicshield.cls`, חבילת סימולציה דטרמיניסטית ב-Python, ואימות $\epsilon$-DP ($\epsilon \le 1.2$) וקליטת OSINT (`18 ms`).
2. **שלב 2 (חודשים 7–12) — מנועי הליבה ותזמור סוכנים:** שילוב `SIRI`, `Hegselmann-Krause` ואיחוד בייסיאני ככלי `ReAct` עם מעטפות `Pydantic JSON`, סגירת פער כיול `AUC > 0.96`, והרצת Shadow Mode.
3. **שלב 3 (חודשים 13–18) — שער חוקתי, הגינות ותרגילי Red Team:** הטמעת `OPA/Rego` ו-`3-of-3 Ed25519`, מבדקי `Dual-Wing Parity` דו-שבועיים ($\Delta\text{FPR} < 1.5\%$), ותרגילי יריבות `UC-01`..`UC-04`.
4. **שלב 4 (חודשים 19–24) — קנה מידה ליום הבחירות, QA והסמכה:** בדיקות עומס `12,000 EPS` על `34 GPU Pools`, ביקורת LuaLaTeX BiDi מלאה (`verify_report.py`), ואימות ROI/SLA להסמכת CEC ו-INCD.
