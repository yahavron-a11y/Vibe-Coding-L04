# CivicShield AI — Simulation Script, Figures & Chapters Completed

## 1. Created Files
- **Simulation Script:** `C:\Users\ron\OneDrive - University of Haifa\SecondYear\MyProjects\Vibe-Coding-L04\scripts\generate_figures.py`
- **Generated Figures (300 DPI PNG + PDF):**
  - `C:\Users\ron\OneDrive - University of Haifa\SecondYear\MyProjects\Vibe-Coding-L04\figures\fig1_spillover.png` (and `.pdf`)
  - `C:\Users\ron\OneDrive - University of Haifa\SecondYear\MyProjects\Vibe-Coding-L04\figures\fig2_siri.png` (and `.pdf`)
  - `C:\Users\ron\OneDrive - University of Haifa\SecondYear\MyProjects\Vibe-Coding-L04\figures\fig3_hk.png` (and `.pdf`)
  - `C:\Users\ron\OneDrive - University of Haifa\SecondYear\MyProjects\Vibe-Coding-L04\figures\fig4_bayesian.png` (and `.pdf`)
  - `C:\Users\ron\OneDrive - University of Haifa\SecondYear\MyProjects\Vibe-Coding-L04\figures\fig5_mmc.png` (and `.pdf`)
  - `C:\Users\ron\OneDrive - University of Haifa\SecondYear\MyProjects\Vibe-Coding-L04\figures\fig6_roi.png` (and `.pdf`)
- **LaTeX Chapters:**
  - `C:\Users\ron\OneDrive - University of Haifa\SecondYear\MyProjects\Vibe-Coding-L04\chapters\ch5_models.tex` (SIRI ODEs, Hegselmann-Krause, Bayesian Fusion, M/M/c Erlang-C, Table 5.1, referencing `figures/fig2_siri.png`..`figures/fig5_mmc.png`)
  - `C:\Users\ron\OneDrive - University of Haifa\SecondYear\MyProjects\Vibe-Coding-L04\chapters\ch7_roadmap.tex` (Risk Matrix Table 7.1, 24-month Gantt `\input{figures/fig_gantt}`, 5Y CAPEX/OPEX/ROI Table 7.2 + `figures/fig6_roi.png`, KPI/SLA Table 7.3)

## 2. Verified Numeric Metrics (Deterministic Execution, `SEED=42`)
Executed via `uv run --with numpy --with matplotlib python scripts/generate_figures.py` (exit code 0, all SLA assertions passed):

| Model / Figure | Key Verified Metrics | SLA / Requirement Status |
|---|---|---|
| **Fig 1: Spillover & Framing** | Mainstream peak salience: `75.87` (unmitigated) $\to$ `12.97` (CivicShield); Entman framing adoption: `78% / 82% / 88% / 74%` $\to$ `24% / 19% / 27% / 16%` | PASS (`FR-07`, `SC-06`) |
| **Fig 2: SIRI ODEs (RK4)** | $R_0 = 4.86$, $p_c = 79.4\%$; Unmitigated peak $I(t) = 47.2\%$, Prebunking (Day 1.5+, $\nu=0.22$) peak $I(t) = 10.2\%$ | PASS (`FR-06`, `FR-12`) |
| **Fig 3: Hegselmann-Krause** | $\epsilon_{\text{eff}} = 0.402$; Extreme-pole share ($|x_i| \ge 0.85$): `100.0%` (baseline) $\to$ `0.0%` (bridging); Pluralistic spread $\sigma = 0.496$ (no uniform consensus) | PASS (`FR-08`, `RT-01`) |
| **Fig 4: Bayesian Fusion** | Single-modality AUCs: Text `0.790`, Acoustic `0.840`, Visual `0.886`; **Bayesian Fusion `AUC = 0.983`** ($> 0.96$); **Judicial Gate `Precision = 0.977`** ($\ge 0.90$, Recall `0.417`) at 5% threat base rate | PASS (`NFR-03`, `FR-05`) |
| **Fig 5: M/M/c Erlang-C** | `c = 34` GPU Pools (capacity `16,320 EPS`): utilization $\rho = 0.735$ and mean latency `58.63 ms` ($\le 250\text{ ms}$) at `12,000 EPS` election peak | PASS (`NFR-01`, `NFR-02`) |
| **Fig 6: 5Y CAPEX/OPEX/ROI** | 5Y CAPEX `26.0M`, OPEX `42.7M`, **TCO `68.7M NIS`** vs. **Resilience Value `145.0M NIS`** (Net Surplus `76.3M NIS`); **Break-Even = Year `2.16` (~2.2)** | PASS (`RFP-07`, `SC-10`) |
