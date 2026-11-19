# Red Team — Expanded PDR Hebrew LaTeX Sections (`redteam_sections.tex`)

**Updated file path (expanded in-place):**
`C:\Users\ron\OneDrive - University of Haifa\SecondYear\MyProjects\L04\agents\redteam\redteam_sections.tex`

## Summary of Expansion (~10+ pages when compiled in A4 LuaLaTeX)
1. **Constitutional Safeguards Audit (`\label{sec:constitutional-audit}`):**
   - 6 binding constitutional principles, 3-layer Defense-in-Depth architecture (`Pre-Inference`, `Runtime PEP`, `Post-Inference`), CDR Gate Criteria.
   - 2 comprehensive audit matrices: Structural Controls (`CS-01`–`CS-06`) and Operational Controls (`CS-07`–`CS-12`).
2. **Adversarial Threat Modeling -- STRIDE & MITRE ATLAS (`\label{sec:adversarial-threat-modeling}`):**
   - 4-layer Attack Surface Analysis (Input, RAG/Memory, Mesh/Orchestration, Output/Document).
   - Full `STRIDE` + `MITRE ATLAS` mapping table (`AML.T0051`, `AML.T0020`, `AML.T0048`, `AML.T0056`, `AML.T0029`, `AML.T0054`) with quantitative risk scores.
   - Dedicated analysis of `BiDi Spoofing / Trojan Source` (`U+202E`, `U+2066`) and `LaTeX Injection` (`\directlua`, `\write18`).
3. **Red-Team Attack Scenarios & Mitigations (`\label{sec:redteam-scenarios}`):**
   - 8 detailed scenarios (`RT-01`–`RT-08`) with attack vectors, IOCs, and architectural mitigations, plus a summary verification matrix.
4. **Anti-Censorship & Viewpoint-Neutrality Stress Tests (`\label{sec:anti-censorship}`):**
   - Legitimate Harm Prevention vs. Over-Refusal, No Shadow Suppression, Explainable Refusals, Multi-Agent Appeal Protocol, Cross-Lingual Parity.
   - Stress-testing methodology (Symmetric Prompt Pairs, Adversarial Framing, Benign Trigger Suite, Cross-Lingual Consistency).
   - Quantitative KPIs table (`FRR < 3%`, `Symmetry Gap < 2%`, `Explainability 100%`, `Lang Parity < 1.5%`, `Override < 5%`) and 6-category Stress Test Suite (`ST-01`–`ST-06`).
5. **Governance, Oversight & Accountability Framework (`\label{sec:governance-oversight}`):**
   - Three Lines of Defense (`NIST AI RMF`-aligned), 4-level Escalation & Safe Fallback / Kill Switch protocol, and a full `RACI` Governance Matrix.
6. **Expanded LuaLaTeX BiDi QA & MiKTeX Verification Protocol (`\label{sec:lualatex-bidi-qa}`):**
   - Standard `MiKTeX + LuaLaTeX + babel (bidi=basic)` build architecture, component-level BiDi rules, 12-item `BiDi QA Checklist` (`QA-01`–`QA-12`), and automated `.log` verification protocol.

## LuaLaTeX BiDi Compatibility Verified
- Uses only standard `booktabs`, `amssymb`, `amsmath`, and `\textenglish{...}` (no `polyglossia`, no XeLaTeX `bidi`, no `longtable` dependencies).
- All inline English terms/acronyms/commands are wrapped in `\textenglish{...}`; all inequalities are in math mode; table column widths sum to $\approx 14.2\text{--}14.5\text{cm}$ to prevent `Overfull \hbox` on A4.
