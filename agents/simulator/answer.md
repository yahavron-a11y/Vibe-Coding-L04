# CivicShield AI — Quantitative Modeling Plan, PRD Success Criteria & Simulation Milestones

**Source Inspected:** `CivicShield_AI_Preliminary_Report.pdf` (v1.0-RFP-FINAL, `GOV-IL-RFP-2026-CSAI`, Chapters 3, 4, 5, 6, 7, 8)  
**Author Role:** `simulator` (SIRI ODEs, Hegselmann-Krause Opinions, Bayesian Fusion, M/M/c Queueing & 5Y ROI)

---

## 1. Quantitative Modeling Plan

All quantitative models are implemented as deterministic Python mathematical tools (no LLM numeric estimation) using `numpy`, `scipy` (or custom RK4), and `matplotlib`, feeding verified metrics into the ReAct agent loop and `PRD.md` / `PLAN.md` deliverables.

### 1.1 Model 1: Epidemiological-Cognitive Contagion (SIRI ODEs)
- **Purpose:** Forecast disinformation narrative spread, derive outbreak threshold $R_0$ and critical inoculation rate $p_c$, and prove the advantage of proactive Cognitive Prebunking over reactive fact-checking (supports **FR-06, FR-12, RFP-04**).
- **State Space:** Normalized electorate $S(t) + I(t) + V(t) + R(t) = 1$ (Susceptible, Infected/Sharers, Prebunked/Vaccinated, Removed/Recovered).
- **Governing ODEs (Eq. 5.1–5.4):**
  $$\frac{dS}{dt} = -\beta S(t)I(t) - \nu(t) S(t), \quad \frac{dI}{dt} = \beta S(t)I(t) - \gamma_{\text{eff}}(t) I(t)$$
  $$\frac{dV}{dt} = \nu(t) S(t), \quad \frac{dR}{dt} = \gamma_{\text{eff}}(t) I(t), \quad \gamma_{\text{eff}}(t) = \gamma + \Delta\gamma \cdot \mathbb{I}(t \ge t_{\text{boost}})$$
- **Thresholds (Eq. 5.5–5.6):** $R_0 = \beta / \gamma$, $p_c = 1 - 1/R_0 = 1 - \gamma/\beta$.
- **Calibration & Numerical Scheme:**
  - RK4 integrator with step $\Delta t = 0.1\text{ day}$ over $T = 30\text{ days}$.
  - Initial conditions: $S(0) = 0.985$, $I(0) = 0.015$, $V(0) = R(0) = 0$.
  - Baseline bot-amplified FIMI parameters: $\beta = 0.68\text{ day}^{-1}$, $\gamma = 0.14\text{ day}^{-1} \implies R_0 \approx 4.86$, $p_c \approx 79.4\%$.
  - Scenarios: (a) Unmitigated FIMI (Peak $I(t) = 47.2\%$); (b) Reactive Fact-Check starting Day 6+; (c) CivicShield Prebunking starting Day 1.5+ with $\nu = 0.22\text{ day}^{-1}$ (Capped Peak $I(t) = 7.6\%$); (d) Sensitivity sweep $\nu \in [0, 35]\%/\text{day}$ verifying cumulative exposure $R(T=30) < 20\%$ for $\nu \ge 15\%/\text{day}$.

### 1.2 Model 2: Bounded-Confidence Polarization & Pluralistic Bridging (Hegselmann-Krause)
- **Purpose:** Quantify echo-chamber formation, affective polarization, and Spiral of Silence dynamics, and validate CivicShield's pluralistic bridging protocol without inducing artificial uniform consensus (supports **FR-08, RFP-04, RT-01**).
- **Population & Horizon:** $N = 200$ citizen agents, $x_i(0) \sim \mathcal{U}(-1, +1)$, $T = 60$ discrete steps.
- **Unmitigated Polarized Regime (Eq. 5.7):**
  - Confidence radius $\epsilon = 0.22$; out-group repulsion $\delta_{\text{rep}} = 0.03$ for $O_i(t) = \{j : |x_j(t) - x_i(t)| > 0.65\}$:
    $$x_i^{\text{pol}}(t+1) = \text{clip}_{[-1,1]}\!\left(\frac{1}{|N_i(t)|}\sum_{j \in N_i(t)} x_j(t) + \delta_{\text{rep}} \cdot \text{sgn}\big(x_i(t) - \bar{x}_{O_i}(t)\big)\right)$$
- **CivicShield Pluralistic Bridging Protocol (Eq. 5.8):**
  - Expanded listening radius $\epsilon_{\text{eff}} = \epsilon + 0.28 b$ ($b = 0.65 \implies \epsilon_{\text{eff}} = 0.402$) with a $28\%$ authenticity anchor $x_i(0)$:
    $$x_i^{\text{bridge}}(t+1) = \text{clip}_{[-1,1]}\!\left(0.72 \cdot \frac{1}{|N_i^{\text{eff}}(t)|}\sum_{j \in N_i^{\text{eff}}(t)} x_j(t) + 0.28 \cdot x_i(0)\right)$$
- **Output Metrics:** Bimodality index, opinion distribution entropy, and extreme-pole mass at $t = 60$ confirming prevention of extreme polarization while preserving pluralistic diversity.

### 1.3 Model 3: Multimodal Bayesian Evidence Fusion (Deepfake & Synthetic Media)
- **Purpose:** Fuse $M = 4$ conditionally independent forensic modalities—text stylometry ($e_T$), acoustic spectral analysis ($e_A$), visual/optical flow ($e_V$), and network sync + C2PA provenance ($e_N$)—to overcome the Base-Rate Fallacy in imbalanced streams (supports **FR-05, NFR-03, RFP-03**).
- **Formulation (Eq. 5.9–5.10):**
  $$\log\frac{P(F \mid \mathbf{e})}{1 - P(F \mid \mathbf{e})} = \log\frac{P(F)}{1 - P(F)} + \sum_{m=1}^{4} \log\frac{P(e_m \mid F)}{P(e_m \mid \neg F)}$$
- **Calibration & Evaluation:**
  - Imbalanced stream prior $P(F) = 0.05$ (5% threat base rate).
  - Evaluate ROC curves (AUC) and Precision-Recall curves against single-modality baselines.
  - **Calibration Note (Audit Flag):** In the preliminary report, NFR-03 and Table 5.1 mandate `AUC > 0.96` and `Precision >= 0.90`, whereas Fig. 5.3A's legend displays `Bayesian Fusion (AUC = 0.942)`. The implementation must calibrate the 4-modality likelihood distributions / fusion simulation so verified empirical AUC strictly satisfies `AUC > 0.96` and `Precision >= 0.90` at the judicial escalation gate.

### 1.4 Model 4: Election-Day Capacity & Latency Queueing (M/M/c Erlang-C)
- **Purpose:** Dimension GPU worker pools and predictive auto-scaling to guarantee `< 250 ms` end-to-end latency under election-day peak load of `12,000 EPS` (supports **NFR-01, NFR-02, RFP-05**).
- **Formulation (Eq. 5.11–5.12):**
  - Service rate per GPU worker pool: $\mu = 480\text{ EPS/Pool}$, offered load $a = \lambda/\mu$, utilization $\rho = \lambda/(c\mu) < 1$.
  - Erlang-C waiting probability $C(c, a) = P_0 \frac{a^c}{c!(1-\rho)}$, mean queue wait $W_q = \frac{C(c,a)}{c\mu - \lambda}$.
  - Total system latency: $\mathbb{E}[T_{\text{sys}}] = T_{\text{pipe}} + W_q \cdot K_{\text{batch}} + 38\rho^2 \le 250\text{ ms}$ (with $T_{\text{pipe}} = 38\text{ ms}$).
- **Configurations & 24h Auto-Scaling:**
  - Compare $c = 16$ pools (cap $7.7\text{k EPS}$, unstable), $c = 24$ pools (cap $11.5\text{k EPS}$, asymptotic blowup near 20:00), and $c = 34$ pools (cap $16.3\text{k EPS}$, $\rho \approx 0.735$ at $12\text{k EPS}$, stable well below $250\text{ ms}$).
  - Model 24-hour election-day traffic profile with predictive auto-scaling buffer over midday surge and polls-closing peak (19:00–22:00 UTC+2).
  - Align with Layer Latency Budget (Table 4.1): Layer 1 (`18 ms`, 100%) + Layer 2 (`38 ms`, 100%) + Layer 3a Triage (`45 ms`, 6%) + Layer 3b ReAct (`115 ms`, 0.8%) + Layer 4–5 Gate/Merkle (`22 ms`, 0.8%) = `238 ms` critical path (`12 ms` margin).

### 1.5 Model 5: 5-Year Budget, Tokenomics & Socio-Democratic ROI (and Cross-Platform Spillover)
- **5-Year TCO & ROI Model (Table 7.2, Fig. 7.2):**
  - Tiered triage saves `94%` of LLM inference costs (only `6%` to Layer 3a Triage, `0.8%` to Layer 3b ReAct).
  - **5-Year Financials (Million NIS):**
    - Year 1 (Setup): CAPEX `14.5`, OPEX `6.5`, Total `21.0`, Resilience Value `8.0`
    - Year 2 (Integration): CAPEX `4.0`, OPEX `8.2`, Total `12.2`, Resilience Value `22.0`
    - Year 3 (Election): CAPEX `2.5`, OPEX `8.8`, Total `11.3`, Resilience Value `31.0`
    - Year 4 (Expansion): CAPEX `3.0`, OPEX `9.4`, Total `12.4`, Resilience Value `38.0`
    - Year 5 (Maintenance): CAPEX `2.0`, OPEX `9.8`, Total `11.8`, Resilience Value `46.0`
  - **Totals:** Cumulative TCO = `68.7M NIS` (CAPEX `26.0M`, OPEX `42.7M`), Cumulative Institutional Resilience Value = `145.0M NIS`, **Break-Even = Year 2.2** (Net Surplus = `76.3M NIS`).
- **Auxiliary Spillover & Framing Containment Model (Section 3.5, Fig. 3.1):**
  - 72-hour cross-platform spillover from fringe channels ($t = 10\text{h}$ peak) and bot amplification ($t = 22\text{h}$) to mainstream media ($t = 28\text{–}38\text{h}$). Prebunking triggered at $t = 8\text{h}$ caps mainstream salience at ~13 points and reduces Entman hostile framing adoption from `78%/82%/88%/74%` down to `24%/19%/27%/16%`.

---

## 2. Measurable Success Criteria for `PRD.md`

| ID | Category | Metric / KPI | Mandatory Target (SLA / Threshold) | Verification Method |
|---|---|---|---|---|
| **SC-01** | Performance (`NFR-01`) | End-to-End Processing Latency | Mean & P95 $\le 250\text{ ms}$ at `12,000 EPS` (Critical path $\le 238\text{ ms}$) | M/M/c Erlang-C ($c=34$ pools, $\rho \approx 0.735$) + continuous 12k EPS load test |
| **SC-02** | Availability (`NFR-02`) | Election-Day Uptime & Failover | `99.99%` Active-Active; Multi-AZ failover `< 15 s` | Chaos/failover drill across Multi-AZ cluster |
| **SC-03** | Forensics (`NFR-03`, `FR-05`) | Multimodal Deepfake Detection | `AUC > 0.96` and `Precision >= 0.90` at 5% threat base rate | Blind academic audit on benchmark dataset + Bayesian PR/ROC validation |
| **SC-04** | Contagion (`FR-06`, `FR-12`) | SIRI Prebunking Containment | Peak active share $I(t) \le 8\%$ (vs. 47.2% unmitigated); cumulative $R(30) < 20\%$ at $\nu \ge 15\%/\text{day}$ | Deterministic RK4 SIRI simulation + `t <= 30 min` detection-to-prebunking SLA |
| **SC-05** | Polarization (`FR-08`) | Pluralistic Bridging & Bimodality | Prevent extreme-pole collapse while preserving $\ge 28\%$ authenticity anchor (no uniform consensus) | Hegselmann-Krause simulation ($N=200, T=60$) Bimodality & entropy check |
| **SC-06** | Spillover (`FR-07`) | Cross-Platform Agenda Containment | Mainstream spillover salience capped $\le 15/100$; hostile Entman framing adoption $< 30\%$ across all 4 dimensions | 72h spillover simulation & prebunking trigger at $t \le 8\text{h}$ |
| **SC-07** | Privacy (`NFR-04`, `FR-02`) | Differential Privacy & Retention | Cumulative privacy budget $\epsilon \le 1.2$; automatic raw-data TTL purge at `30 days` | Formal $\epsilon$-DP accounting (`Lap(\Delta f/\epsilon)`) + retention audit |
| **SC-08** | Fairness (`NFR-05`) | Political Parity & Bias | Cross-bloc error gap $\Delta\text{FPR} < 1.5\%$ across political spectrum & 4 languages (HE/AR/RU/AM) | Bi-weekly Dual-Wing Parity Testing on curated political corpus |
| **SC-09** | Governance (`FR-11`, `FR-13`, `FR-14`) | Zero Autonomous Censorship | `0` enforcement/takedown actions without 3-of-3 Ed25519 Quorum; `100%` XAI trace in Append-Only Merkle Log | Continuous cryptographic gate & Merkle log integrity verification |
| **SC-10** | Economics (`RFP-07`) | Tokenomics & 5Y ROI | $\ge 94\%$ LLM cost reduction via tiered triage; 5Y TCO $\le 68.7\text{M NIS}$; Break-Even $\le \text{Year } 2.2$ | Quarterly CAPEX/OPEX & Tokenomics telemetry reconciliation |

---

## 3. Simulation Milestones for `PLAN.md` and `TODO.md`

### 3.1 `PLAN.md` — Phased Simulation & Quantitative Engineering Roadmap (24 Months)
- **Phase 1 (Months 1–6) — Foundation, Privacy & Baseline Calibration:**
  - Build deterministic Python simulation package (`numpy`/`matplotlib`) with reproducible seeds and unit tests.
  - Validate $\epsilon$-DP noise calibration ($\epsilon \le 1.2$) and ingestion throughput baseline (`18 ms` budget) on historical 3-language corpus.
- **Phase 2 (Months 7–12) — Core Quantitative Engines & Agent Tool Integration:**
  - Implement and expose **SIRI ODE (RK4)**, **Hegselmann-Krause Bridging**, and **4-Modality Bayesian Fusion** as deterministic ReAct tools (`simulator_siri_agent`, `forensic_agent`) with Pydantic JSON Hub envelopes.
  - Resolve the Fig. 5.3A vs. NFR-03 calibration gap so Bayesian Fusion empirically achieves `AUC > 0.96` and `Precision >= 0.90` at 5% base rate.
  - Deploy Shadow Mode for live parameter estimation ($\beta(t)$, $R_0$, spillover lead time).
- **Phase 3 (Months 13–18) — Constitutional Gate, Fairness & Adversarial Wargames:**
  - Run bi-weekly **Dual-Wing Parity** simulations verifying $\Delta\text{FPR} < 1.5\%$.
  - Execute Red-Team Wargames (UC-01..UC-04: Telegram bot swarm, election-morning audio deepfake, 48h silence-period hijacking, balanced prebunking) validating alert-fatigue gating ($R_0 > 1.5$, $P(F|\mathbf{e}) \ge 0.90$).
- **Phase 4 (Months 19–24) — Election-Day Scale, Load Validation & ROI Sign-Off:**
  - Validate **M/M/c Erlang-C** model against live `12,000 EPS` load tests on `34 GPU Pools` (confirming P95 $\le 250\text{ ms}$ and predictive auto-scaling across 19:00–22:00 peak).
  - Finalize 5-Year TCO/ROI & Tokenomics telemetry audit (`<= 68.7M NIS`, `>= 94%` triage savings) for CEC/INCD operational certification.

### 3.2 `TODO.md` — Actionable Simulation Tasks
- [ ] **SIM-01 (SIRI Engine):** Implement RK4 solver (`dt=0.1`, `T=30d`, `beta=0.68`, `gamma=0.14`, `nu=0.22/day`) and sensitivity sweep (`nu in [0, 35]%/day`); assert `R0=4.86`, `pc=79.4%`, `Peak I(t)<=7.6%`, `R(30)<20%` at `nu>=15%`.
- [ ] **SIM-02 (Hegselmann-Krause Engine):** Implement polarized baseline (`eps=0.22`, `delta_rep=0.03`) vs. CivicShield bridging (`eps_eff=0.402`, `0.28*x_i(0)` anchor) for `N=200, T=60`; compute Bimodality index and entropy; assert no uniform consensus.
- [ ] **SIM-03 (Bayesian Fusion Engine):** Implement 4-modality log-odds fusion (`P(F)=0.05`); calibrate modality likelihoods so ROC `AUC > 0.96` and PR `Precision >= 0.90` (fixing the `0.942` legend discrepancy from preliminary Fig. 5.3A).
- [ ] **SIM-04 (M/M/c Queueing & Auto-Scaler):** Implement Erlang-C latency model (`mu=480 EPS/Pool`, `T_pipe=38 ms`) for `c in {16, 24, 34}` pools + 24h election-day traffic profile; assert `E[T_sys] <= 250 ms` at `12,000 EPS` for `c=34`.
- [ ] **SIM-05 (Spillover & 5Y ROI Models):** Implement 72h cross-platform spillover + Entman framing containment model and 5-year CAPEX/OPEX/ROI calculator (`TCO=68.7M`, `Value=145.0M`, `Break-Even=2.2y`).
- [ ] **SIM-06 (Agent Tooling & Verification):** Wrap models as deterministic Python CLI/tool endpoints returning typed Pydantic JSON envelopes (Listing 4.1) and add automated `pytest` assertions + `verify_report.py` numeric consistency checks.
