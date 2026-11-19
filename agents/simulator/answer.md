# Expanded `simulator_sections.tex` (10+ Pages Quantitative Hebrew LaTeX)

Updated in-place:
`C:\Users\ron\OneDrive - University of Haifa\SecondYear\MyProjects\L04\agents\simulator\simulator_sections.tex`

## Summary of Added Content (Full LuaLaTeX BiDi Compatible)
All `pgfplots` figures and multi-line display equations are wrapped in `\begin{english}...\end{english}` for clean LuaLaTeX BiDi rendering.

1. **SIRI ODEs (`subsec:siri-ode`)**: Full nonlinear system derivation, Disease-Free & Endemic equilibria, Jacobian eigenvalues, Lyapunov stability proof, RK4 numerical scheme, 6-regime parameter sensitivity table (`tab:siri-sensitivity`), and two `pgfplots` figures (`fig:siri-trajectories`, `fig:siri-sensitivity-plot`).
2. **Hegselmann-Krause Opinions (`subsec:hk-opinions`)**: Weighted-trust HK formulation with zealots/bots $Z$ and official verifiers $V$, Lyapunov energy convergence proof, normalized polarization index $\mathcal{P}(t)$, 5-regime sensitivity table (`tab:hk-regimes`), and two `pgfplots` figures (`fig:hk-bifurcation`, `fig:hk-polarization-time`).
3. **Bayesian Belief Fusion (`subsec:bayesian-fusion`)**: Full Log-Linear Opinion Pool derivation, conjugate Beta-Binomial online reliability update, Brier Score calibration metric, 6-row detector ablation table (`tab:bayesian-perf`), and sequential posterior convergence `pgfplots` figure (`fig:bayesian-convergence`).
4. **M/M/c Queueing & Erlang-C (`subsec:mmc-queue`)**: Birth-death steady-state derivation, Erlang-C, $L_q, W_q, W$, exact tail SLA bound $P(W_q > \tau)$, 5-tier analyst sizing table (`tab:mmc-sizing`), and latency vs. arrival-rate `pgfplots` figure (`fig:mmc-latency`).
5. **Monte Carlo Scenario Comparisons (`subsec:monte-carlo`)**: Coupled $M=1{,}000$-run simulation across 4 operational scenarios (Routine, Bot Campaign, Flash Crisis, Adaptive Evasion), Mean/P95 summary table (`tab:monte-carlo`), and grouped bar `pgfplots` chart (`fig:mc-scenarios`).
6. **5-Year ROI / TCO / NPV / IRR Financial Model (`subsec:five-year-roi`)**: Full CAPEX/OPEX TCO breakdown, 5-year cash flow table (`tab:roi-5y`), 2D sensitivity matrix across discount rate $r \in \{6\%,8\%,10\%,12\%\}$ and benefit realization $\Delta B \in [-30\%, +15\%]$ (`tab:roi-sensitivity`), and 4-scenario cumulative discounted cash flow `pgfplots` chart (`fig:roi-cashflow`).
