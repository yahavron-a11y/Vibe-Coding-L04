% !TEX TS-program = lualatex
% pdr_hebrew.cls - Hebrew BiDi Preliminary Design Report Class for LuaLaTeX (MiKTeX / Windows)
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{pdr_hebrew}[2026/11/18 v1.0 Hebrew BiDi PDR Class for LuaLaTeX]

\LoadClass[11pt,a4paper,oneside]{article}

% ==============================================================================
% 1. Page Geometry & Margins
% ==============================================================================
\RequirePackage[
  a4paper,
  top=2.5cm,
  bottom=2.5cm,
  left=2.2cm,
  right=2.2cm,
  headheight=15pt
]{geometry}

% ==============================================================================
% 2. Language, BiDi & Fonts (LuaLaTeX + MiKTeX Windows compatible)
% ==============================================================================
\RequirePackage{fontspec}
\RequirePackage[bidi=basic, layout=tabular.lists.sectioning]{babel}
\babelprovide[main, import]{hebrew}
\babelprovide[import]{english}

% Standard Windows / MiKTeX fonts with full Hebrew & Latin glyph coverage
\babelfont{rm}[Renderer=HarfBuzz]{David}
\babelfont{sf}[Renderer=HarfBuzz]{Arial}
\babelfont{tt}[Renderer=HarfBuzz]{Consolas}

\babelfont[english]{rm}{Times New Roman}
\babelfont[english]{sf}{Arial}
\babelfont[english]{tt}{Consolas}

% Convenience macros for inline English / LTR snippets inside Hebrew text
\newcommand{\en}[1]{\foreignlanguage{english}{#1}}
\newcommand{\code}[1]{\en{\texttt{#1}}}

% ==============================================================================
% 3. Graphics, Colors & TikZ (with safe LTR wrapper for BiDi)
% ==============================================================================
\RequirePackage[dvipsnames,table]{xcolor}
\definecolor{pdrPrimary}{HTML}{1B365D}
\definecolor{pdrSecondary}{HTML}{2B6CB0}
\definecolor{pdrAccent}{HTML}{0D9488}
\definecolor{pdrLightBg}{HTML}{F1F5F9}
\definecolor{pdrBorder}{HTML}{CBD5E1}
\definecolor{pdrWarn}{HTML}{B45309}

\RequirePackage{tikz}
\usetikzlibrary{
  arrows.meta,
  positioning,
  shapes.geometric,
  shapes.multipart,
  fit,
  backgrounds,
  calc,
  shadows.blur
}

% Safe LTR environment for TikZ diagrams under LuaLaTeX BiDi
\newenvironment{ltrtikz}{%
  \begin{otherlanguage}{english}%
  \centering
}{%
  \end{otherlanguage}%
}

% ==============================================================================
% 4. Tables, Lists, Boxes & Math
% ==============================================================================
\RequirePackage{amsmath,amssymb}
\RequirePackage{booktabs}
\RequirePackage{tabularx}
\RequirePackage{longtable}
\RequirePackage{array}
\RequirePackage{multirow}
\RequirePackage{enumitem}
\RequirePackage{float}
\RequirePackage{caption}
\RequirePackage[most]{tcolorbox}

\captionsetup{
  font=small,
  labelfont={bf,color=pdrPrimary},
  justification=centering
}

\newtcolorbox{archbox}[1]{
  colback=pdrLightBg,
  colframe=pdrPrimary,
  coltitle=white,
  fonttitle=\bfseries,
  title=#1,
  arc=3pt,
  boxrule=0.8pt,
  left=8pt,
  right=8pt,
  top=6pt,
  bottom=6pt
}

% ==============================================================================
% 5. Headers, Footers & Section Styling
% ==============================================================================
\RequirePackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[R]{\small\color{pdrPrimary}\textbf{דוח תכנון ראשוני (PDR)}}
\fancyhead[L]{\small\color{gray}\en{Multi-Agent Architecture \& Hub Spec}}
\fancyfoot[C]{\small\thepage}
\renewcommand{\headrulewidth}{0.5pt}
\renewcommand{\headrule}{\hbox to\headwidth{\color{pdrBorder}\leaders\hrule height \headrulewidth\hfill}}

\RequirePackage{titlesec}
\titleformat{\section}
  {\Large\bfseries\color{pdrPrimary}}
  {\thesection}{0.8em}{}
  [\titlerule]
\titleformat{\subsection}
  {\large\bfseries\color{pdrSecondary}}
  {\thesubsection}{0.7em}{}
\titleformat{\subsubsection}
  {\normalsize\bfseries\color{pdrAccent}}
  {\thesubsubsection}{0.6em}{}

% ==============================================================================
% 6. Hyperref (loaded last)
% ==============================================================================
\RequirePackage[
  colorlinks=true,
  linkcolor=pdrPrimary,
  citecolor=pdrSecondary,
  urlcolor=pdrAccent,
  unicode=true
]{hyperref}

\setlength{\parindent}{0pt}
\setlength{\parskip}{6pt}
