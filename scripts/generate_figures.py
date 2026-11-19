#!/usr/bin/env python3
"""
CivicShield AI — Deterministic Quantitative Simulation & Figure Generator
Generates 6 high-DPI PNG and PDF scientific figures into figures/:
  1. fig1_spillover.{png,pdf}  — Cross-platform agenda spillover & Entman hostile framing containment
  2. fig2_siri.{png,pdf}       — SIRI ODEs (RK4) epidemiological-cognitive contagion & prebunking
  3. fig3_hk.{png,pdf}         — Hegselmann-Krause bounded-confidence polarization vs. pluralistic bridging
  4. fig4_bayesian.{png,pdf}   — 4-modality Bayesian fusion ROC (AUC > 0.96) & Precision-Recall (P >= 0.90)
  5. fig5_mmc.{png,pdf}        — M/M/c Erlang-C latency & 24h election-day predictive auto-scaling
  6. fig6_roi.{png,pdf}        — 5-Year CAPEX/OPEX budget, TCO (68.7M NIS) & Socio-Democratic ROI (145.0M NIS)
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# ---------------------------------------------------------------------------
# Global deterministic configuration & styling
# ---------------------------------------------------------------------------
SEED = 42
DPI = 300

ROOT_DIR = Path(__file__).resolve().parent.parent
FIG_DIR = ROOT_DIR / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10,
    "axes.titlesize": 11,
    "axes.titleweight": "bold",
    "axes.labelsize": 10,
    "legend.fontsize": 8.5,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "axes.grid": True,
    "grid.alpha": 0.3,
    "grid.linestyle": "--",
    "figure.facecolor": "white",
    "axes.facecolor": "white",
})

NAVY = "#0F2942"
TEAL = "#0E7C7B"
RED = "#C83E3B"
AMBER = "#D97706"
SLATE = "#475569"
BLUE = "#2563EB"
PURPLE = "#7C3AED"


def save_figure(fig: plt.Figure, stem: str) -> None:
    png_path = FIG_DIR / f"{stem}.png"
    pdf_path = FIG_DIR / f"{stem}.pdf"
    fig.savefig(png_path, dpi=DPI, bbox_inches="tight")
    fig.savefig(pdf_path, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Figure 1: Cross-Platform Agenda Spillover & Entman Hostile Framing Containment
# ---------------------------------------------------------------------------
def generate_fig1_spillover() -> dict:
    t = np.linspace(0, 72, 361)

    # Normalized Salience Index (0-100)
    fringe = 92.0 * np.exp(-0.5 * ((t - 10.0) / 4.2) ** 2)
    bot_amp = 96.0 * np.exp(-0.5 * ((t - 22.0) / 7.5) ** 2) * (1.0 / (1.0 + np.exp(-(t - 8.0) / 2.0)))
    mainstream_unmit = 76.0 * np.exp(-0.5 * ((t - 33.0) / 14.0) ** 2) * (1.0 / (1.0 + np.exp(-(t - 14.0) / 3.0)))
    mainstream_shield = 13.0 * np.exp(-0.5 * ((t - 30.0) / 9.5) ** 2) * (1.0 / (1.0 + np.exp(-(t - 12.0) / 3.0)))

    dims = ["Problem\nDefinition", "Causal\nAttribution", "Moral\nPanic", "Institutional\nDistrust"]
    without_cs = [78.0, 82.0, 88.0, 74.0]
    with_cs = [24.0, 19.0, 27.0, 16.0]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.2, 4.6))
    fig.suptitle("Agenda-Setting Dynamics & Hostile Framing Containment Analysis", fontsize=12.5, fontweight="bold", y=1.02)

    # Panel A
    ax1.plot(t, fringe, linestyle=":", color=PURPLE, lw=2.0, label="Seed Origin (Fringe Channels)")
    ax1.plot(t, bot_amp, linestyle="--", color=AMBER, lw=2.0, label="Bot Amplification (No Shield)")
    ax1.plot(t, mainstream_unmit, color=RED, lw=2.4, label="Mainstream Spillover (Unmitigated)")
    ax1.plot(t, mainstream_shield, color=TEAL, lw=2.6, label="Mainstream Spillover (CivicShield)")
    ax1.axvline(8.0, color=NAVY, linestyle="-.", lw=1.4)
    ax1.annotate("Prebunking\nTriggered (t=8h)", xy=(8.0, 86), xytext=(12.5, 90),
                 arrowprops=dict(arrowstyle="->", color=NAVY, lw=1.1),
                 fontsize=8.5, fontweight="bold", color=NAVY)
    ax1.set_title("A. Cross-Platform Narrative Spillover (72h)")
    ax1.set_xlabel("Hours After Seed Injection")
    ax1.set_ylabel("Normalized Salience Index (0-100)")
    ax1.set_xlim(0, 72)
    ax1.set_ylim(0, 108)
    ax1.legend(loc="upper right", frameon=True)

    # Panel B
    x = np.arange(len(dims))
    w = 0.36
    b1 = ax2.bar(x - w / 2, without_cs, w, color=RED, alpha=0.9, label="Without CivicShield")
    b2 = ax2.bar(x + w / 2, with_cs, w, color=TEAL, alpha=0.92, label="With CivicShield")
    for bar in b1:
        ax2.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1.8, f"{bar.get_height():.0f}%",
                 ha="center", va="bottom", fontsize=8.5, fontweight="bold", color=RED)
    for bar in b2:
        ax2.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1.8, f"{bar.get_height():.0f}%",
                 ha="center", va="bottom", fontsize=8.5, fontweight="bold", color=TEAL)
    ax2.set_title("B. Hostile Framing Adoption (Entman Dimensions)")
    ax2.set_xticks(x)
    ax2.set_xticklabels(dims)
    ax2.set_ylabel("Public Frame Adoption Rate (%)")
    ax2.set_ylim(0, 104)
    ax2.legend(loc="upper right", frameon=True)

    fig.tight_layout()
    save_figure(fig, "fig1_spillover")

    return {
        "mainstream_peak_unmitigated": round(float(np.max(mainstream_unmit)), 2),
        "mainstream_peak_civicshield": round(float(np.max(mainstream_shield)), 2),
        "framing_without": without_cs,
        "framing_with": with_cs,
    }


# ---------------------------------------------------------------------------
# Figure 2: SIRI ODEs (RK4) Epidemiological-Cognitive Contagion Simulation
# ---------------------------------------------------------------------------
def run_siri_rk4(
    beta: float = 0.68,
    gamma: float = 0.14,
    nu_rate: float = 0.0,
    t_nu_start: float = 1.5,
    delta_gamma: float = 0.0,
    t_boost: float = 6.0,
    s0: float = 0.985,
    i0: float = 0.015,
    dt: float = 0.1,
    t_max: float = 30.0,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    steps = int(round(t_max / dt))
    t = np.linspace(0.0, t_max, steps + 1)
    y = np.zeros((steps + 1, 4), dtype=float)
    y[0] = [s0, i0, 0.0, 0.0]

    def deriv(ti: float, state: np.ndarray) -> np.ndarray:
        s, inf, v, r = state
        nu = nu_rate if ti >= t_nu_start else 0.0
        g_eff = gamma + (delta_gamma if ti >= t_boost else 0.0)
        ds = -beta * s * inf - nu * s
        di = beta * s * inf - g_eff * inf
        dv = nu * s
        dr = g_eff * inf
        return np.array([ds, di, dv, dr], dtype=float)

    for k in range(steps):
        ti = t[k]
        yk = y[k]
        k1 = deriv(ti, yk)
        k2 = deriv(ti + 0.5 * dt, yk + 0.5 * dt * k1)
        k3 = deriv(ti + 0.5 * dt, yk + 0.5 * dt * k2)
        k4 = deriv(ti + dt, yk + dt * k3)
        y[k + 1] = yk + (dt / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)

    return t, y[:, 0], y[:, 1], y[:, 2], y[:, 3]


def generate_fig2_siri() -> dict:
    beta, gamma = 0.68, 0.14
    r0 = beta / gamma
    pc = 1.0 - 1.0 / r0

    t, _, i_unmit, _, r_unmit = run_siri_rk4(beta=beta, gamma=gamma, nu_rate=0.0)
    _, _, i_react, _, r_react = run_siri_rk4(beta=beta, gamma=gamma, nu_rate=0.0, delta_gamma=0.18, t_boost=6.0)
    _, _, i_preb, _, r_preb = run_siri_rk4(beta=beta, gamma=gamma, nu_rate=0.22, t_nu_start=1.5)

    nu_grid = np.linspace(0.0, 0.35, 36)
    cum_exp = []
    for nu in nu_grid:
        _, _, i_s, _, r_s = run_siri_rk4(beta=beta, gamma=gamma, nu_rate=float(nu), t_nu_start=1.5)
        cum_exp.append(100.0 * float(r_s[-1] + i_s[-1]))
    cum_exp_arr = np.array(cum_exp)

    peak_unmit = 100.0 * float(np.max(i_unmit))
    peak_preb = 100.0 * float(np.max(i_preb))
    exp_at_15 = float(np.interp(0.15, nu_grid, cum_exp_arr))

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.2, 4.6))
    fig.suptitle("CivicShield AI Epidemiological-Cognitive Contagion Simulation (SIRI Model)", fontsize=12.5, fontweight="bold", y=1.02)

    # Panel A
    ax1.plot(t, 100.0 * i_unmit, color=RED, lw=2.4, label=f"Unmitigated FIMI ($R_0$ = {r0:.2f})")
    ax1.plot(t, 100.0 * i_react, color=AMBER, lw=2.2, linestyle="--", label="Reactive Fact-Check (Day 6+)")
    ax1.plot(t, 100.0 * i_preb, color=TEAL, lw=2.6, label="CivicShield Prebunking (Day 1.5+)")
    ax1.fill_between(t, 100.0 * i_preb, 100.0 * i_unmit, color=TEAL, alpha=0.12, label="Prevented Exposure")

    t_pk_u = t[int(np.argmax(i_unmit))]
    t_pk_p = t[int(np.argmax(i_preb))]
    ax1.annotate(f"Peak: {peak_unmit:.1f}%", xy=(t_pk_u, peak_unmit), xytext=(t_pk_u - 4.0, peak_unmit + 5.0),
                 fontsize=8.5, fontweight="bold", color=RED)
    ax1.annotate(f"Capped Peak: {peak_preb:.1f}%", xy=(t_pk_p, peak_preb), xytext=(t_pk_p + 7.0, peak_preb + 6.0),
                 arrowprops=dict(arrowstyle="->", color=TEAL, lw=1.1),
                 fontsize=8.5, fontweight="bold", color=TEAL)
    ax1.set_title("A. Active Disinformation Share $I(t)$")
    ax1.set_xlabel("Days Since Campaign Launch")
    ax1.set_ylabel("Infected Electorate Share (%)")
    ax1.set_xlim(0, 30)
    ax1.set_ylim(0, 62)
    ax1.legend(loc="upper right", frameon=True)

    # Panel B
    ax2.plot(100.0 * nu_grid, cum_exp_arr, color=NAVY, lw=2.2, marker="o", markersize=3.5, label="Total Cumulative Exposure")
    ax2.axvline(15.0, color=AMBER, linestyle=":", lw=2.0, label="Operational Target (15%/day)")
    ax2.axhline(20.0, color=TEAL, linestyle="--", lw=1.8, label="Containment Ceiling (20%)")
    ax2.set_title("B. Cumulative Exposure vs. Inoculation Rate")
    ax2.set_xlabel("Daily Cognitive Inoculation Rate $\\nu$ (%/day)")
    ax2.set_ylabel("Cumulative Infected Electorate (%)")
    ax2.set_xlim(0, 36)
    ax2.set_ylim(0, 105)
    ax2.legend(loc="upper right", frameon=True)

    fig.tight_layout()
    save_figure(fig, "fig2_siri")

    return {
        "R0": round(r0, 2),
        "critical_vax_pc_pct": round(100.0 * pc, 1),
        "peak_unmitigated_pct": round(peak_unmit, 1),
        "peak_prebunking_pct": round(peak_preb, 1),
        "cum_exposure_at_15pct_nu": round(exp_at_15, 1),
    }


# ---------------------------------------------------------------------------
# Figure 3: Hegselmann-Krause Bounded-Confidence Polarization & Bridging
# ---------------------------------------------------------------------------
def generate_fig3_hk() -> dict:
    rng = np.random.default_rng(SEED)
    n_agents = 200
    t_steps = 60
    x0 = rng.uniform(-1.0, 1.0, size=n_agents)

    # Regime A: Unmitigated Echo Chambers (Eq. 5.7)
    eps = 0.22
    delta_rep = 0.03
    hist_pol = np.zeros((t_steps + 1, n_agents))
    hist_pol[0] = x0.copy()
    for t in range(t_steps):
        x = hist_pol[t]
        x_next = np.empty_like(x)
        for i in range(n_agents):
            diff = np.abs(x - x[i])
            neighbors = x[diff <= eps]
            outgroup = x[diff > 0.65]
            avg_n = np.mean(neighbors)
            rep = 0.0
            if outgroup.size > 0:
                rep = delta_rep * np.sign(x[i] - np.mean(outgroup))
            x_next[i] = np.clip(avg_n + rep, -1.0, 1.0)
        hist_pol[t + 1] = x_next

    # Regime B: CivicShield Pluralistic Bridging Protocol (Eq. 5.8)
    b_bridge = 0.65
    eps_eff = eps + 0.28 * b_bridge  # 0.402
    hist_bridge = np.zeros((t_steps + 1, n_agents))
    hist_bridge[0] = x0.copy()
    for t in range(t_steps):
        x = hist_bridge[t]
        x_next = np.empty_like(x)
        for i in range(n_agents):
            diff = np.abs(x - x[i])
            neighbors = x[diff <= eps_eff]
            x_next[i] = np.clip(0.72 * np.mean(neighbors) + 0.28 * x0[i], -1.0, 1.0)
        hist_bridge[t + 1] = x_next

    final_pol = hist_pol[-1]
    final_bridge = hist_bridge[-1]
    extreme_pol_pct = 100.0 * float(np.mean(np.abs(final_pol) >= 0.85))
    extreme_bridge_pct = 100.0 * float(np.mean(np.abs(final_bridge) >= 0.85))
    std_bridge = float(np.std(final_bridge))

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(13.5, 4.3))
    fig.suptitle("Affective Polarization & Echo-Chamber Trajectory Simulation (Bounded Confidence Model)",
                 fontsize=12.5, fontweight="bold", y=1.02)

    steps_axis = np.arange(t_steps + 1)
    for i in range(0, n_agents, 3):
        ax1.plot(steps_axis, hist_pol[:, i], color=RED, alpha=0.22, lw=0.9)
        ax2.plot(steps_axis, hist_bridge[:, i], color=TEAL, alpha=0.24, lw=0.9)

    ax1.set_title("A. Unmitigated Echo Chambers")
    ax1.set_xlabel("Simulation Step $t$")
    ax1.set_ylabel("Ideological Position $x_i \\in [-1, +1]$")
    ax1.set_ylim(-1.05, 1.05)

    ax2.set_title("B. CivicShield Bridging Protocol")
    ax2.set_xlabel("Simulation Step $t$")
    ax2.set_ylabel("Ideological Position $x_i$")
    ax2.set_ylim(-1.05, 1.05)

    bins = np.linspace(-1.0, 1.0, 17)
    ax3.hist(final_pol, bins=bins, color=RED, alpha=0.65, label="Polarized Baseline")
    ax3.hist(final_bridge, bins=bins, color=TEAL, alpha=0.75, label="CivicShield Active")
    ax3.set_title("C. Final Opinion Distribution ($t = 60$)")
    ax3.set_xlabel("Ideological Spectrum")
    ax3.set_ylabel("Citizen Agent Count")
    ax3.legend(loc="upper center", frameon=True)

    fig.tight_layout()
    save_figure(fig, "fig3_hk")

    return {
        "eps_eff": round(eps_eff, 3),
        "extreme_pol_pct": round(extreme_pol_pct, 1),
        "extreme_bridge_pct": round(extreme_bridge_pct, 1),
        "bridge_std_diversity": round(std_bridge, 3),
    }


# ---------------------------------------------------------------------------
# Figure 4: Multimodal Bayesian Evidence Fusion (AUC > 0.96, Precision >= 0.90)
# ---------------------------------------------------------------------------
def compute_roc_pr(y_true: np.ndarray, scores: np.ndarray) -> tuple[np.ndarray, np.ndarray, float, np.ndarray, np.ndarray]:
    order = np.argsort(-scores)
    y_sorted = y_true[order]
    n_pos = np.sum(y_sorted == 1)
    n_neg = np.sum(y_sorted == 0)

    tp = np.cumsum(y_sorted == 1)
    fp = np.cumsum(y_sorted == 0)

    tpr = np.concatenate([[0.0], tp / n_pos])
    fpr = np.concatenate([[0.0], fp / n_neg])
    auc = float(np.trapezoid(tpr, fpr))

    precision = tp / np.maximum(tp + fp, 1)
    recall = tp / n_pos
    return fpr, tpr, auc, recall, precision


def generate_fig4_bayesian() -> dict:
    rng = np.random.default_rng(SEED)
    n_samples = 40000
    prior_f = 0.05
    y = (rng.random(n_samples) < prior_f).astype(int)

    # 4 conditionally independent modalities calibrated for realistic single-modality
    # performance and strong multimodal Bayesian fusion (AUC > 0.96, Precision >= 0.90).
    # Each modality score s_m ~ N(mu_1, 1) if F else N(0, 1), so log-LR = mu_1 * s_m - 0.5 * mu_1^2.
    modalities = {
        "Stylometry / Text": 1.15,
        "Acoustic Spectral": 1.45,
        "Visual / Optical Flow": 1.65,
        "Network Sync + C2PA": 1.75,
    }

    scores = {}
    log_odds = np.full(n_samples, math.log(prior_f / (1.0 - prior_f)), dtype=float)
    for name, mu in modalities.items():
        s = rng.normal(loc=mu * y, scale=1.0, size=n_samples)
        scores[name] = s
        log_odds += mu * s - 0.5 * (mu ** 2)

    posterior = 1.0 / (1.0 + np.exp(-np.clip(log_odds, -30.0, 30.0)))

    roc_data = {}
    pr_data = {}
    for name in ["Stylometry / Text", "Acoustic Spectral", "Visual / Optical Flow"]:
        fpr, tpr, auc, rec, prec = compute_roc_pr(y, scores[name])
        roc_data[name] = (fpr, tpr, auc)
        pr_data[name] = (rec, prec)

    fpr_f, tpr_f, auc_f, rec_f, prec_f = compute_roc_pr(y, posterior)
    roc_data["Bayesian Fusion"] = (fpr_f, tpr_f, auc_f)
    pr_data["Bayesian Fusion"] = (rec_f, prec_f)

    # Precision at judicial escalation threshold P(F|e) >= 0.90
    gate_mask = posterior >= 0.90
    prec_at_gate = float(np.mean(y[gate_mask] == 1)) if np.any(gate_mask) else 0.0
    rec_at_gate = float(np.sum(y[gate_mask] == 1) / np.sum(y == 1))

    assert auc_f > 0.96, f"Expected Bayesian Fusion AUC > 0.96, got {auc_f:.4f}"
    assert prec_at_gate >= 0.90, f"Expected Precision >= 0.90 at gate, got {prec_at_gate:.4f}"

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.2, 4.6))
    fig.suptitle("Multimodal Deepfake & Synthetic Media Detection Performance Analysis",
                 fontsize=12.5, fontweight="bold", y=1.02)

    # Panel A: ROC
    ax1.plot([0, 1], [0, 1], linestyle=":", color=SLATE, lw=1.4, label="Random Baseline (AUC = 0.500)")
    styles = [
        ("Stylometry / Text", AMBER, "--", 1.8),
        ("Acoustic Spectral", BLUE, "-.", 1.9),
        ("Visual / Optical Flow", PURPLE, "-", 2.0),
        ("Bayesian Fusion", NAVY, "-", 2.8),
    ]
    for name, col, ls, lw in styles:
        fpr, tpr, auc = roc_data[name]
        ax1.plot(fpr, tpr, color=col, linestyle=ls, lw=lw, label=f"{name} (AUC = {auc:.3f})")
    ax1.set_title("A. ROC: Single Modality vs. Multi-Agent Fusion")
    ax1.set_xlabel("False Positive Rate (FPR)")
    ax1.set_ylabel("True Positive Rate (Recall)")
    ax1.legend(loc="lower right", frameon=True)

    # Panel B: Precision-Recall
    step = 40
    ax2.plot(pr_data["Stylometry / Text"][0][::step], pr_data["Stylometry / Text"][1][::step],
             color=AMBER, linestyle="--", lw=1.9, label="Single Text Detector")
    ax2.plot(pr_data["Visual / Optical Flow"][0][::step], pr_data["Visual / Optical Flow"][1][::step],
             color=PURPLE, linestyle="-.", lw=2.0, label="Visual Deepfake Detector")
    ax2.plot(rec_f[::step], prec_f[::step], color=TEAL, lw=2.8, label="CivicShield Multimodal Ensemble")
    ax2.axhline(0.90, color=RED, linestyle=":", lw=1.8, label="Judicial Escalation Min. Precision (90%)")
    ax2.set_title("B. Precision-Recall (Imbalanced Stream, 5% Threat)")
    ax2.set_xlabel("Recall (Detected Threats Fraction)")
    ax2.set_ylabel("Precision (Verified Threat Purity)")
    ax2.set_xlim(0.0, 1.0)
    ax2.set_ylim(0.25, 1.02)
    ax2.legend(loc="lower left", frameon=True)

    fig.tight_layout()
    save_figure(fig, "fig4_bayesian")

    return {
        "auc_text": round(roc_data["Stylometry / Text"][2], 3),
        "auc_acoustic": round(roc_data["Acoustic Spectral"][2], 3),
        "auc_visual": round(roc_data["Visual / Optical Flow"][2], 3),
        "auc_bayesian_fusion": round(auc_f, 3),
        "precision_at_judicial_gate": round(prec_at_gate, 3),
        "recall_at_judicial_gate": round(rec_at_gate, 3),
    }


# ---------------------------------------------------------------------------
# Figure 5: M/M/c Erlang-C Latency & 24h Election-Day Auto-Scaling
# ---------------------------------------------------------------------------
def erlang_c_latency_ms(lam: float, c: int, mu: float = 480.0, t_pipe_ms: float = 38.0, k_batch: float = 6.0) -> float:
    rho = lam / (c * mu)
    if rho >= 0.995:
        return np.nan
    a = lam / mu
    # Numerically stable log-space computation for P0 and Erlang-C
    log_terms = [k * math.log(a) - math.lgamma(k + 1) for k in range(c)]
    log_last = c * math.log(a) - math.lgamma(c + 1) - math.log(1.0 - rho)
    max_log = max(max(log_terms), log_last)
    sum_terms = sum(math.exp(lt - max_log) for lt in log_terms)
    last_val = math.exp(log_last - max_log)
    c_erlang = last_val / (sum_terms + last_val)
    wq_ms = 1000.0 * c_erlang / (c * mu - lam)
    return t_pipe_ms + wq_ms * k_batch + 38.0 * (rho ** 2)


def generate_fig5_mmc() -> dict:
    mu = 480.0
    lam_grid = np.linspace(1000.0, 14500.0, 271)

    lat_16 = np.array([erlang_c_latency_ms(l, 16, mu) for l in lam_grid])
    lat_24 = np.array([erlang_c_latency_ms(l, 24, mu) for l in lam_grid])
    lat_34 = np.array([erlang_c_latency_ms(l, 34, mu) for l in lam_grid])

    lat_34_at_12k = erlang_c_latency_ms(12000.0, 34, mu)
    rho_34_at_12k = 12000.0 / (34 * mu)
    assert lat_34_at_12k <= 250.0, f"Expected latency <= 250 ms at 12k EPS, got {lat_34_at_12k:.2f} ms"

    # 24-hour election-day traffic profile
    hours = np.arange(0, 24)
    load_eps = np.array([
        2100, 1900, 1850, 1950, 2200, 2800, 3900, 5100,
        6100, 6600, 6800, 6500, 6100, 5600, 5200, 5400,
        6100, 7400, 8900, 10800, 12000, 11200, 9100, 6400,
    ], dtype=float)
    # Predictive auto-scaler keeps capacity >= 1.25x load (in discrete GPU pool steps)
    pools_needed = np.maximum(8, np.ceil((load_eps * 1.28) / mu))
    cap_eps = pools_needed * mu

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.2, 4.6))
    fig.suptitle("High-Availability Performance & Election-Day Queueing Simulation",
                 fontsize=12.5, fontweight="bold", y=1.02)

    # Panel A
    ax1.plot(lam_grid, lat_16, color=RED, linestyle="--", lw=2.2, label="16 GPU Pools (Baseline, Cap 7.7k)")
    ax1.plot(lam_grid, lat_24, color=AMBER, linestyle="-", lw=2.2, label="24 GPU Pools (Standard, Cap 11.5k)")
    ax1.plot(lam_grid, lat_34, color=TEAL, linestyle="-", lw=2.6, label="34 GPU Pools (Election Peak, Cap 16.3k)")
    ax1.axhline(250.0, color=NAVY, linestyle=":", lw=1.8, label="SLA Max Latency Threshold (250 ms)")
    ax1.axvline(12000.0, color=SLATE, linestyle="-.", lw=1.3)
    ax1.annotate("Election Peak\n(12k EPS)", xy=(12000.0, lat_34_at_12k), xytext=(12250.0, 340.0),
                 fontsize=8.5, fontweight="bold", color=NAVY)
    ax1.set_title("A. Inference Latency (M/M/c Queue Model)")
    ax1.set_xlabel("Incoming Social & Media Stream Rate (Events / Sec)")
    ax1.set_ylabel("Mean Processing Latency (ms)")
    ax1.set_xlim(1000, 14500)
    ax1.set_ylim(0, 550)
    ax1.legend(loc="upper left", frameon=True)

    # Panel B
    ax2.plot(hours, load_eps, color=BLUE, lw=2.4, label="Actual Stream Load (EPS)")
    ax2.step(hours, cap_eps, where="mid", color=NAVY, linestyle="--", lw=2.0, label="Auto-Scaled Mesh Capacity")
    ax2.axvspan(19, 22, color=AMBER, alpha=0.18, label="Polls Closing Peak (19:00-22:00)")
    ax2.set_title("B. Election Day 24h Dynamic Auto-Scaling")
    ax2.set_xlabel("Hour of Election Day (UTC+2)")
    ax2.set_ylabel("Events Per Second (EPS)")
    ax2.set_xlim(0, 23)
    ax2.set_ylim(0, 16800)
    ax2.set_xticks([0, 4, 8, 12, 16, 20, 23])
    ax2.legend(loc="upper left", frameon=True)

    fig.tight_layout()
    save_figure(fig, "fig5_mmc")

    return {
        "c34_utilization_at_12k": round(rho_34_at_12k, 3),
        "c34_latency_ms_at_12k": round(lat_34_at_12k, 2),
        "c34_capacity_eps": int(34 * mu),
    }


# ---------------------------------------------------------------------------
# Figure 6: 5-Year CAPEX/OPEX Budget, TCO & Socio-Democratic ROI
# ---------------------------------------------------------------------------
def generate_fig6_roi() -> dict:
    years = np.array([1, 2, 3, 4, 5])
    capex = np.array([14.5, 4.0, 2.5, 3.0, 2.0])
    opex = np.array([6.5, 8.2, 8.8, 9.4, 9.8])
    total_cost = capex + opex
    value = np.array([8.0, 22.0, 31.0, 38.0, 46.0])

    cum_tco = np.cumsum(total_cost)
    cum_val = np.cumsum(value)

    # Linear interpolation of Break-Even year
    diff = cum_val - cum_tco
    idx = int(np.where(diff >= 0)[0][0])
    y_prev, y_curr = years[idx - 1], years[idx]
    d_prev, d_curr = diff[idx - 1], diff[idx]
    break_even_year = float(y_prev + (-d_prev) / (d_curr - d_prev))

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.2, 4.6))
    fig.suptitle("5-Year Tender Budget Allocation, TCO & Socio-Democratic ROI Model",
                 fontsize=12.5, fontweight="bold", y=1.02)

    # Panel A
    w = 0.36
    ax1.bar(years - w / 2, capex, w, color=NAVY, label="CAPEX (Infra & R&D)")
    ax1.bar(years - w / 2, opex, w, bottom=capex, color=BLUE, alpha=0.85, label="OPEX (Cloud, Tokens & Ops)")
    ax1.bar(years + w / 2, value, w, color=TEAL, alpha=0.9, label="Institutional Resilience Value")
    ax1.set_title("A. Annual Budget vs. Institutional Value")
    ax1.set_xlabel("Deployment Year")
    ax1.set_ylabel("Million NIS")
    ax1.set_xticks(years)
    ax1.set_xticklabels([f"Year {y}" for y in years])
    ax1.set_ylim(0, 52)
    ax1.legend(loc="upper left", frameon=True)

    # Panel B
    ax2.plot(years, cum_tco, color=RED, lw=2.4, marker="s", markersize=5, label="Cumulative TCO (Cost)")
    ax2.plot(years, cum_val, color=TEAL, lw=2.6, marker="o", markersize=5, label="Cumulative Prevented Crisis Loss")
    ax2.fill_between(years, cum_tco, cum_val, where=(cum_val >= cum_tco), interpolate=True,
                     color=TEAL, alpha=0.15, label="Net Positive Resilience Surplus")
    be_val = float(np.interp(break_even_year, years, cum_tco))
    ax2.annotate(f"Break-Even\n(Year {break_even_year:.1f})", xy=(break_even_year, be_val),
                 xytext=(1.35, 78.0),
                 arrowprops=dict(arrowstyle="->", color=NAVY, lw=1.2),
                 fontsize=8.5, fontweight="bold", color=NAVY)
    ax2.set_title("B. 5-Year Cumulative TCO & Democratic ROI")
    ax2.set_xlabel("Program Horizon (Years)")
    ax2.set_ylabel("Cumulative Value (Million NIS)")
    ax2.set_xticks(years)
    ax2.set_xticklabels([f"Y{y}" for y in years])
    ax2.set_ylim(0, 158)
    ax2.legend(loc="upper left", frameon=True)

    fig.tight_layout()
    save_figure(fig, "fig6_roi")

    return {
        "total_capex_mnis": round(float(np.sum(capex)), 1),
        "total_opex_mnis": round(float(np.sum(opex)), 1),
        "total_tco_mnis": round(float(cum_tco[-1]), 1),
        "total_value_mnis": round(float(cum_val[-1]), 1),
        "net_surplus_mnis": round(float(cum_val[-1] - cum_tco[-1]), 1),
        "break_even_year": round(break_even_year, 2),
    }


def main() -> None:
    metrics = {
        "fig1_spillover": generate_fig1_spillover(),
        "fig2_siri": generate_fig2_siri(),
        "fig3_hk": generate_fig3_hk(),
        "fig4_bayesian": generate_fig4_bayesian(),
        "fig5_mmc": generate_fig5_mmc(),
        "fig6_roi": generate_fig6_roi(),
    }
    print(json.dumps(metrics, indent=2))


if __name__ == "__main__":
    main()
