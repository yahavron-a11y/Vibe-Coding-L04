# Red Team Audit & QA Specification — CivicShield AI (`GOV-IL-RFP-2026-CSAI`)

**Source Inspected:** `CivicShield_AI_Preliminary_Report.pdf` (v1.0-RFP-FINAL, 44 pages, 8 chapters + Bibliography)  
**Agent Role:** Constitutional Safeguards Audit, Anti-Censorship Review & LuaLaTeX BiDi QA (`redteam`)

---

## 1. Constitutional Safeguards (For `PRD.md` & Architecture Alignment)

Derived from Chapter 6, Section 2.3.3, Table 3.1, Table 3.4, Table 6.1, and Figure 6.1:

1. **Defensive Democracy & Israeli Constitutional Standard (Section 2.3.3, 6.1):**
   - Grounded in Loewenstein's *Militant Democracy* (1937) and Justice Aharon Barak's *Defensive Democracy* doctrine (1988).
   - Enforces the **"Near Certainty" (*HaVada'ut HaKrova*)** threshold for threats to the democratic electoral process and strict **Proportionality / Less-Restrictive-Means** testing.
2. **Layer 4 Constitutional Guardrail Engine (Section 6.2, Figure 6.1):**
   - Deterministic policy enforcement via **Open Policy Agent (OPA / Rego)**—never free-form LLM judgment.
   - **4-Gate Constitutional Decision Tree:**
     - **Gate 1 (Privacy / OSINT Boundary):** Private DMs or non-public personal data -> **Immediate Hard Drop & Deletion**.
     - **Gate 2 (Protected Speech Exemption):** Authentic civic political opinion, satire, or protest without CIB/Deepfake -> **No tagging, no tracking, immediate case closure**.
     - **Gate 3 (Contagion & Judicial Precision Gate):** Requires $R_0 > 1.5$ (SIRI contagion risk) **AND** forensic posterior $P(F \mid \mathbf{e}) \ge 0.90$. Below threshold -> **Anonymous $\epsilon$-DP macro-monitoring only (no intervention)**.
     - **Gate 4 (Proportionality & Less-Restrictive Means):**
       - *Path A (Default / Primary):* Objective, non-partisan **Cognitive Prebunking** + public transparency.
       - *Path B (Severe Criminal Election Fraud / FIMI only):* **Triple-Key Cryptographic Removal Petition** to platforms.
3. **Triple-Key Cryptographic Quorum — `3-of-3 Ed25519` (Section 6.3, FR-13):**
   - Any formal platform tagging/restriction request requires three independent hardware-backed Ed25519 signatures:
     - **Key A (Judicial Authority):** Chair of the Central Elections Committee (Supreme Court Justice) — verifies criminal/legal threshold and proportionality.
     - **Key B (Technical Authority):** National Cyber Directorate (INCD) representative — verifies C2PA, foreign server attribution, and bot-network forensics.
     - **Key C (Public / Parliamentary Balance):** State Comptroller representative or approved Opposition representative — institutional veto preventing executive overreach.
   - Layer 5 outbound enforcement API is **physically/cryptographically locked** without all 3 signatures recorded in the Merkle Log.
4. **Mathematical Privacy Protection & Data Minimization (Section 6.4, FR-02, NFR-04):**
   - **$\epsilon$-Differential Privacy** (Dwork & Roth, 2014) enforced at Layer 1 ingestion with cumulative privacy budget $\epsilon \le 1.2$ and calibrated Laplace noise $\text{Lap}(\Delta f / \epsilon)$ on all transparency dashboards.
   - Mandatory **PII Redaction & Phone/ID Hashing** at ingestion; zero access to private messages (OSINT only).
   - **30-Day Irreversible TTL Purge** of raw public message caches (exempting only sealed judicial evidence files).
5. **Algorithmic Fairness, Pluralism & Regulatory Compliance (Section 6.5, Table 6.1, Eq. 5.8):**
   - **Pluralism Anchor (RT-01 fix):** Hegselmann-Krause bridging protocol retains a $0.28\,x_i(0)$ authenticity anchor to prevent anti-pluralistic "Uniform Consensus."
   - **Partisan Reversal Test:** Constitutional & RedTeam Agent runs a counterfactual check ("would we flag this if written by a political opponent under identical circumstances?").
   - **Bi-Weekly Dual-Wing Parity Testing:** Enforces $\Delta\text{FPR} < 1.5\%$ across all political camps and demographic groups.
   - **International Regulatory Alignment:** EU AI Act (2024/1689 High-Risk Election AI), EU DSA (2022/2065 algorithmic transparency & rapid appeal), NIST AI RMF 1.0 (bias, XAI, adversarial robustness).

---

## 2. Anti-Censorship Ironclad Principles (For `PRD.md`)

Derived from Section 6.1 (*Ironclad Constitutional Principle*), FR-11, FR-13, FR-14, and Listing 4.1:

1. **Absolute Separation of Powers Inside the Architecture:** CivicShield AI has **zero authority** to delete posts, ban users, or take down channels autonomously (`"auto_censor_permitted": false` in Hub JSON Envelope). AI is strictly confined to detection, pattern measurement, and generating neutral Prebunking recommendations.
2. **Absolute Immunity of Legitimate Political Speech:** The system is strictly prohibited from flagging authentic civic criticism, political satire, social protest, or controversial ideological interpretation as threats—even when language is harsh or polarized.
3. **Elimination of Executive Compartmentalization:** No executive or technical body may unilaterally issue official warnings or platform takedown petitions; every formal action requires the 3-of-3 cryptographic quorum with judicial and opposition/public veto.
4. **Hardware & Software Enforcement Lock (FR-11):** All API calls capable of requesting content removal are hard-blocked at both software and hardware (HSM) layers unless accompanied by a valid 3-of-3 Ed25519 quorum proof.
5. **Immutable Judicial Auditability (FR-14):** Every agent's `ReAct Trace` (Thought -> Action -> Observation -> Confidence) is written to an **Append-Only Merkle Log** open to judicial inspection.

---

## 3. Acceptance & QA Criteria (For `PRD.md`)

| ID | Category | Acceptance / QA Criterion | Verification Method |
| :--- | :--- | :--- | :--- |
| **QA-01** | **Anti-Censorship (FR-11, FR-13)** | **0** unauthorized enforcement or takedown calls without `3-of-3 Ed25519` Quorum; `auto_censor_permitted` strictly `false`. | Continuous crypto-gate & Merkle Log integrity audit |
| **QA-02** | **E2E Latency (NFR-01)** | Mean & P95 latency $\le 250\text{ ms}$ under peak load of **12,000 EPS** (critical path budgeted at $238\text{ ms}$ with 34 GPU Pools). | M/M/c Erlang-C model + 12k EPS load test |
| **QA-03** | **Election-Day Availability (NFR-02)** | **99.99%** Active-Active Multi-AZ availability; automatic failover $< 15\text{ s}$. | Multi-AZ chaos / failover testing |
| **QA-04** | **Deepfake Detection (NFR-03)** | Multimodal Bayesian Fusion $\text{AUC} > 0.96$ and **$\text{Precision} \ge 0.90$** for judicial escalation. *(Red Team Flag: reconcile Fig 5.3A showing `AUC = 0.942` vs text/Table 3.5 `AUC > 0.96`.)* | Monthly blind audit on curated deepfake corpus + academic review |
| **QA-05** | **Prebunking SLA (FR-12, Table 7.3)** | $\le 30\text{ min}$ from Telegram seed detection to neutral, non-partisan Prebunking template (3 alternatives). | End-to-end timestamping on critical incident drills |
| **QA-06** | **Privacy Budget (FR-02, NFR-04)** | Cumulative $\epsilon \le 1.2$, PII redacted at Layer 1, 0 re-identification on dashboards, 30-day irreversible TTL purge. | Formal $\epsilon$-DP proof + automated TTL purge check |
| **QA-07** | **Political Fairness (NFR-05)** | False-positive disparity **$\Delta\text{FPR} < 1.5\%$** across political camps & demographics; pluralism anchor $0.28\,x_i(0)$ active. | Bi-weekly Dual-Wing Parity Testing + Partisan Reversal Test |
| **QA-08** | **Multilingual Coverage (NFR-06)** | Full support for **Hebrew, Arabic, Russian, and Amharic**, including political slang, dialects, and encoded transliterations. | Multilingual adversarial benchmark suite |
| **QA-09** | **Explainability (FR-14, NFR-07)** | **100% XAI** justification per alert: raw sources, confidence score, Entman 4-function frame map, and Merkle-logged `ReAct Trace`. | Automated schema & audit-log completeness check |
| **QA-10** | **Prompt Injection Defense (NFR-08)** | Strict **Pydantic JSON Schema** validation on all Hub envelopes; sandboxed execution for external text analysis. | Red Team adversarial prompt-injection wargames |
| **QA-11** | **Red Team Sign-Off (Table 8.2)** | Zero unresolved critical findings; all prior audit items (`RT-01`–`RT-04`) verified closed. | Red Team Audit Pass sign-off before handover |

---

## 4. LuaLaTeX BiDi QA Verification Checklist (For `PLAN.md` & `TODO.md`)

Derived from Chapter 8, Table 8.1, Table 8.2 (`RT-03`, `RT-04`), Figure 8.1, and visual inspection of `CivicShield_AI_Preliminary_Report.pdf`:

### A. Compilation & Structural Integrity
- [ ] **Clean Multi-Pass LuaLaTeX Build:** Compile `main.tex` with `lualatex` (2+ passes + bibliography) with **0 fatal errors** and **0 undefined references (`??`)** or missing citations.
- [ ] **Document Structure & Numbering:** Verify sequential numbering across Cover, Document Control, TOC, LOF, LOT, Chapters 1–8, and 26-entry Bibliography; confirm headers/footers and page numbers match TOC/LOF/LOT.
- [ ] **Class & Package Hygiene:** Confirm `civicshield.cls` loads cleanly without font-fallback warnings for Hebrew/English glyphs.

### B. Bidirectional (BiDi / RTL) & Typography QA (`RT-03`)
- [ ] **RTL Sealing in Callouts & TikZ:** Verify `\NewEnviron` wrappers and `tikzhebrew` in `civicshield.cls` prevent Hebrew text overflow, reversed word order, or misplaced punctuation/direction markers inside callout boxes and TikZ diagrams.
- [ ] **LTR Isolation for Technical Tokens:** Ensure inline English acronyms (`FIMI`, `C2PA`, `Ed25519`, `OPA/Rego`, `OSINT`, `M/M/c`), code blocks (`Listing 4.1`), and URLs are wrapped in proper LTR contexts with no inverted parentheses or hyphens.
- [ ] **Math & Equation Directionality:** Verify all equations (Eq. 5.1–5.12, Eq. 6.1) render left-to-right with properly aligned equation numbers, intact minus signs, and crisp Greek symbols ($\beta, \gamma, \nu, \epsilon, \rho, \lambda, \mu$).
- [ ] **Table RTL Column Ordering:** Confirm all tables (Tables 1.1–8.2) follow consistent RTL column flow, have no cell text overflow/clipping, and avoid awkward page-break splits.

### C. Quantitative Figures & Cross-Reference QA (`RT-04`)
- [ ] **Python Figure Generation & Sync:** Run `scripts/generate_figures.py` and verify all 6 figures (`fig1`–`fig6` / Figures 3.1, 5.1–5.4, 7.2) render at high DPI with zero clipped labels, overlapping legends, or truncated titles.
- [ ] **Numeric Consistency Check:** Cross-check every figure annotation against body text and tables (specifically resolve the minor discrepancy between **Figure 5.3A `Bayesian Fusion (AUC = 0.942)`** and **Table 3.5 / Section 5.4.2 / Table 5.1 `AUC > 0.96`**).
- [ ] **Automated Verification Gate (`verify_report.py`):** Execute `verify_report.py` to automatically validate figure-tag cross-references, LaTeX log cleanliness, and required file presence before final approval.

### D. Red Team Rejection / Fix Loop (`Figure 8.1`)
- [ ] **Visual Page-by-Page PDF Audit:** Inspect rendered PDF pages for orphaned headings, excessive whitespace (e.g., short trailing pages like p. 3 / p. 23), or broken box borders.
- [ ] **Final Sign-Off:** Record zero critical findings in the Red Team Audit Log (Table 8.2) prior to final delivery / GitHub push.
