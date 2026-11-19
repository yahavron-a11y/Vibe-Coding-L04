#!/usr/bin/env python3
"""
CivicShield AI — Automated Red Team & LuaLaTeX BiDi QA Verification Script
Checks:
  1. Required project & chapter files
  2. Figure & TikZ file existence (from \\includegraphics and \\input{figures/...})
  3. LuaLaTeX log for fatal errors, undefined references (??), and severe overfull hboxes
  4. BiDi / tikzhebrew / \\NewEnviron sealing in civicshield.cls and TikZ figures
  5. Numeric & constitutional KPI consistency across chapters
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import List, Tuple


REQUIRED_FILES = [
    "main.tex",
    "civicshield.cls",
    "PRD.md",
    "PLAN.md",
    "TODO.md",
    "chapters/ch8_method.tex",
    "scripts/generate_figures.py",
    "scripts/verify_report.py",
]

KEY_METRICS = [
    ("E2E Latency SLA (250 ms)", r"250\s*\\?\,?ms|250\s*ms"),
    ("Peak Load (12,000 EPS / 12k EPS)", r"12,000|12k\s*EPS"),
    ("GPU Pools (34 Pools)", r"34\s+Pools|34\s+GPU"),
    ("SIRI R0 (4.86)", r"4\.86"),
    ("Critical Inoculation (79.4%)", r"79\.4"),
    ("Differential Privacy Budget (1.2)", r"1\.2"),
    ("Fairness Disparity (< 1.5%)", r"1\.5\s*\\%|1\.5%"),
    ("Triple-Key Quorum (Ed25519 / 3-of-3)", r"Ed25519|3-of-3"),
    ("Pluralism Anchor (0.28)", r"0\.28"),
]


def read_text_safe(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def check_required_files(root: Path) -> Tuple[List[str], List[str]]:
    errors, warnings = [], []
    for rel in REQUIRED_FILES:
        if not (root / rel).is_file():
            errors.append(f"Missing required file: {rel}")

    chapters_dir = root / "chapters"
    if chapters_dir.is_dir():
        ch_files = sorted(chapters_dir.glob("ch*.tex"))
        if len(ch_files) < 8:
            warnings.append(f"Expected 8 chapter files in chapters/, found {len(ch_files)}")
    else:
        errors.append("Missing directory: chapters/")
    return errors, warnings


def check_figures(root: Path) -> Tuple[List[str], List[str], int]:
    errors, warnings = [], []
    tex_files = list(root.glob("*.tex")) + list((root / "chapters").glob("*.tex"))
    checked = 0

    inc_graphics_re = re.compile(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}")
    input_fig_re = re.compile(r"\\input\{(figures/[^}]+)\}")

    for tf in tex_files:
        text = read_text_safe(tf)
        for match in inc_graphics_re.findall(text):
            checked += 1
            ref = match.strip()
            candidates = [
                root / ref,
                root / f"{ref}.pdf",
                root / f"{ref}.png",
                root / f"{ref}.jpg",
                root / "figures" / ref,
                root / "figures" / f"{ref}.pdf",
                root / "figures" / f"{ref}.png",
            ]
            if not any(c.is_file() for c in candidates):
                errors.append(f"Missing graphic '{ref}' referenced in {tf.relative_to(root)}")

        for match in input_fig_re.findall(text):
            checked += 1
            ref = match.strip()
            candidates = [root / ref, root / f"{ref}.tex"]
            if not any(c.is_file() for c in candidates):
                errors.append(f"Missing TikZ/figure '{ref}' referenced in {tf.relative_to(root)}")

    return errors, warnings, checked


def check_latex_log(root: Path) -> Tuple[List[str], List[str]]:
    errors, warnings = [], []
    log_path = root / "main.log"
    if not log_path.is_file():
        warnings.append("main.log not found (compile main.tex with lualatex to enable log QA)")
        return errors, warnings

    log_text = read_text_safe(log_path)

    fatal_patterns = [
        (r"^! .*", "Fatal LaTeX error"),
        (r"Emergency stop", "LaTeX Emergency stop"),
        (r"Fatal error occurred", "LaTeX fatal compilation failure"),
    ]
    for pat, label in fatal_patterns:
        matches = re.findall(pat, log_text, flags=re.MULTILINE)
        for m in matches[:5]:
            errors.append(f"{label}: {m.strip()}")

    undef_patterns = [
        r"LaTeX Warning: Reference `[^']+' on page \d+ undefined",
        r"LaTeX Warning: Citation `[^']+' on page \d+ undefined",
        r"LaTeX Warning: There were undefined references",
        r"There were undefined citations",
    ]
    for pat in undef_patterns:
        matches = re.findall(pat, log_text)
        for m in matches[:10]:
            errors.append(f"Undefined reference/citation: {m}")

    if "??" in log_text:
        warnings.append("Found '??' marker in main.log — verify no unresolved cross-references remain")

    overfull = re.findall(r"Overfull \\hbox \((\d+\.\d+)pt too wide\)", log_text)
    severe = [float(pt) for pt in overfull if float(pt) > 20.0]
    if severe:
        warnings.append(
            f"Found {len(severe)} severe Overfull \\hbox warnings (>20pt; max={max(severe):.1f}pt)"
        )

    return errors, warnings


def check_bidi_and_tikz(root: Path) -> Tuple[List[str], List[str]]:
    errors, warnings = [], []
    cls_path = root / "civicshield.cls"
    if cls_path.is_file():
        cls_text = read_text_safe(cls_path)
        if "tikzhebrew" not in cls_text and "NewEnviron" not in cls_text:
            warnings.append(
                "civicshield.cls does not appear to define 'tikzhebrew' or '\\NewEnviron' BiDi wrappers (RT-03)"
            )
        if not any(k in cls_text for k in ("polyglossia", "babel", "luabidi", "bidi")):
            warnings.append("civicshield.cls does not load polyglossia/babel/bidi for Hebrew RTL support")

    fig_dir = root / "figures"
    if fig_dir.is_dir():
        for tikz_file in sorted(fig_dir.glob("*.tex")):
            txt = read_text_safe(tikz_file)
            has_hebrew = bool(re.search(r"[\u0590-\u05FF]", txt))
            if has_hebrew and "tikzhebrew" not in txt and "textdir" not in txt and "texthebrew" not in txt:
                warnings.append(
                    f"TikZ file {tikz_file.relative_to(root)} contains Hebrew without explicit tikzhebrew/BiDi wrapper"
                )
    return errors, warnings


def check_numeric_consistency(root: Path) -> Tuple[List[str], List[str]]:
    errors, warnings = [], []
    tex_files = list(root.glob("*.tex")) + list((root / "chapters").glob("*.tex"))
    combined = "\n".join(read_text_safe(f) for f in tex_files)

    if not combined.strip():
        warnings.append("No .tex content found to verify numeric consistency")
        return errors, warnings

    for label, pat in KEY_METRICS:
        if not re.search(pat, combined):
            warnings.append(f"Expected key metric not found in .tex sources: {label}")

    # Specific Red Team check: AUC > 0.96 vs 0.942 discrepancy
    has_096 = bool(re.search(r"0\.96", combined))
    has_0942 = bool(re.search(r"0\.942", combined))
    if has_096 and has_0942:
        warnings.append(
            "Numeric discrepancy detected: both AUC 0.96 and 0.942 appear in sources — reconcile Fig 5.3A with NFR-03"
        )

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description="CivicShield AI Report QA Verifier")
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parent.parent,
        help="Project root directory (default: parent of scripts/)",
    )
    args = parser.parse_args()
    root = args.root.resolve()

    print(f"=== CivicShield AI Red Team QA Verification ===")
    print(f"Project Root: {root}\n")

    all_errors: List[str] = []
    all_warnings: List[str] = []

    e, w = check_required_files(root)
    all_errors.extend(e)
    all_warnings.extend(w)

    e, w, fig_count = check_figures(root)
    all_errors.extend(e)
    all_warnings.extend(w)

    e, w = check_latex_log(root)
    all_errors.extend(e)
    all_warnings.extend(w)

    e, w = check_bidi_and_tikz(root)
    all_errors.extend(e)
    all_warnings.extend(w)

    e, w = check_numeric_consistency(root)
    all_errors.extend(e)
    all_warnings.extend(w)

    print(f"Figures / TikZ references checked: {fig_count}")
    print(f"Critical Errors: {len(all_errors)}")
    print(f"Warnings:        {len(all_warnings)}\n")

    if all_errors:
        print("[CRITICAL ERRORS]")
        for item in all_errors:
            print(f"  - {item}")
        print()

    if all_warnings:
        print("[WARNINGS]")
        for item in all_warnings:
            print(f"  - {item}")
        print()

    if all_errors:
        print("RESULT: FAIL (Red Team QA blocked delivery — resolve critical errors)")
        return 1

    print("RESULT: PASS (Zero critical Red Team QA errors)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
