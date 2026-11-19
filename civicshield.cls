% ============================================================================
% civicshield.cls - Institutional LuaLaTeX Class for CivicShield AI Report
% ============================================================================
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{civicshield}[2026/11/19 v1.0 CivicShield AI National Tender Report Class]

\LoadClass[11pt,a4paper,oneside]{report}

% --- Core Packages ---
\RequirePackage{iftex}
\RequireLuaTeX

\RequirePackage[a4paper, top=2.4cm, bottom=2.4cm, left=2.1cm, right=2.1cm, headheight=24pt, footskip=1.2cm]{geometry}
\RequirePackage[bidi=basic, layout=tabular]{babel}
\babelprovide[main, import]{hebrew}
\babelprovide[import]{english}

\RequirePackage{fontspec}
\IfFontExistsTF{Heebo}{%
  \babelfont{rm}[AutoFakeSlant=0.18]{Heebo}%
  \babelfont{sf}[AutoFakeSlant=0.18]{Heebo}%
}{%
  \IfFontExistsTF{Assistant}{%
    \babelfont{rm}[AutoFakeSlant=0.18]{Assistant}%
    \babelfont{sf}[AutoFakeSlant=0.18]{Assistant}%
  }{%
    \babelfont{rm}[AutoFakeSlant=0.18]{Arial}%
    \babelfont{sf}[AutoFakeSlant=0.18]{Arial}%
  }%
}
\IfFontExistsTF{JetBrains Mono}{%
  \babelfont{tt}[Scale=0.86]{JetBrains Mono}%
}{%
  \IfFontExistsTF{Consolas}{%
    \babelfont{tt}[Scale=0.88]{Consolas}%
  }{%
    \babelfont{tt}[Scale=0.88]{Courier New}%
  }%
}

\RequirePackage{xcolor}
\RequirePackage{graphicx}
\RequirePackage{amsmath,amssymb,amsthm}
\RequirePackage{booktabs,array,tabularx,multirow,colortbl}
\RequirePackage{enumitem}
\RequirePackage{float}
\RequirePackage{caption}
\RequirePackage{subcaption}
\RequirePackage{fancyhdr}
\RequirePackage[explicit]{titlesec}
\RequirePackage{titletoc}
\RequirePackage{environ}
\RequirePackage[most]{tcolorbox}
\RequirePackage{listings}
\RequirePackage{tikz}
\usetikzlibrary{arrows.meta,positioning,shapes.geometric,shapes.multipart,fit,backgrounds,calc,shadows.blur}

\RequirePackage[hidelinks, unicode=true]{hyperref}

% --- Official Color Palette ---
\definecolor{csNavy}{HTML}{0B1F3A}
\definecolor{csTeal}{HTML}{0F766E}
\definecolor{csAmber}{HTML}{D97706}
\definecolor{csCrimson}{HTML}{B91C1C}
\definecolor{csSlate}{HTML}{334155}
\definecolor{csNavyBg}{HTML}{F0F4F8}
\definecolor{csTealBg}{HTML}{F0FDFA}
\definecolor{csAmberBg}{HTML}{FFFBEB}
\definecolor{csRedBg}{HTML}{FEF2F2}
\definecolor{csBorder}{HTML}{CBD5E1}

% --- Paragraph & List Spacing ---
\setlength{\parindent}{0pt}
\setlength{\parskip}{0.55em}
\renewcommand{\baselinestretch}{1.18}
\setlist[itemize]{topsep=4pt, itemsep=3pt, parsep=0pt}
\setlist[enumerate]{topsep=4pt, itemsep=3pt, parsep=0pt}

% --- Captions ---
\captionsetup{
  font={small,color=csSlate},
  labelfont={bf,color=csNavy},
  justification=centering,
  skip=8pt
}

% --- Headers & Footers ---
\pagestyle{fancy}
\fancyhf{}
\renewcommand{\chaptermark}[1]{\markboth{\thechapter.\ #1}{}}
\fancyhead[R]{\small\textcolor{csSlate}{\textbf{\textcolor{csNavy}{CivicShield AI}} --- מגן התודעה הלאומי (מטלה 2: דוח מכין)}}
\fancyhead[L]{\small\textcolor{csSlate}{\leftmark}}
\renewcommand{\headrulewidth}{0.8pt}
\renewcommand{\headrule}{\hbox to\headwidth{\color{csTeal}\leaders\hrule height \headrulewidth\hfill}}

\fancyfoot[L]{\small\textcolor{csSlate}{עמוד \thepage}}
\fancyfoot[R]{\small\textcolor{csSlate}{אוניברסיטת חיפה | יישומי AI ו-Vibe Coding (ד"ר יורם סגל)}}
\renewcommand{\footrulewidth}{0.5pt}
\renewcommand{\footrule}{\hbox to\headwidth{\color{csBorder}\leaders\hrule height \footrulewidth\hfill}}

\fancypagestyle{plain}{%
  \fancyhf{}
  \fancyfoot[L]{\small\textcolor{csSlate}{עמוד \thepage}}
  \fancyfoot[R]{\small\textcolor{csSlate}{CivicShield AI --- מסמך חזוי והצעה למכרז לאומי}}
  \renewcommand{\headrulewidth}{0pt}
  \renewcommand{\footrulewidth}{0.5pt}
  \renewcommand{\footrule}{\hbox to\headwidth{\color{csBorder}\leaders\hrule height \footrulewidth\hfill}}
}

% --- Chapter Banners ---
\titleformat{\chapter}[display]
  {\normalfont}
  {}
  {0pt}
  {%
    \begin{tcolorbox}[
      enhanced,
      colback=csNavy,
      colframe=csNavy,
      arc=4pt,
      boxrule=0pt,
      left=14pt, right=14pt, top=12pt, bottom=12pt,
      borderline south={3pt}{0pt}{csAmber}
    ]
      \textcolor{csAmber}{\small\bfseries פרק \thechapter}\\[4pt]
      \textcolor{white}{\LARGE\bfseries #1}
    \end{tcolorbox}%
  }
\titlespacing*{\chapter}{0pt}{-16pt}{14pt}

\titleformat{name=\chapter,numberless}[display]
  {\normalfont}
  {}
  {0pt}
  {%
    \begin{tcolorbox}[
      enhanced,
      colback=csNavy,
      colframe=csNavy,
      arc=4pt,
      boxrule=0pt,
      left=14pt, right=14pt, top=12pt, bottom=12pt,
      borderline south={3pt}{0pt}{csTeal}
    ]
      \textcolor{white}{\LARGE\bfseries #1}
    \end{tcolorbox}%
  }

% --- Section Headings ---
\titleformat{\section}
  {\Large\bfseries\color{csNavy}}
  {\thesection}
  {0.7em}
  {#1}
\titlespacing*{\section}{0pt}{14pt}{6pt}

\titleformat{\subsection}
  {\large\bfseries\color{csTeal}}
  {\thesubsection}
  {0.7em}
  {#1}
\titlespacing*{\subsection}{0pt}{10pt}{4pt}

\titleformat{\subsubsection}
  {\normalsize\bfseries\color{csSlate}}
  {\thesubsubsection}
  {0.6em}
  {#1}
\titlespacing*{\subsubsection}{0pt}{8pt}{3pt}

% --- Custom Callout Boxes ---
\newtcolorbox{tenderbox}[1]{
  enhanced,
  breakable,
  colback=csAmberBg,
  colframe=csAmber,
  colbacktitle=csAmber,
  coltitle=white,
  fonttitle=\bfseries,
  title={#1},
  arc=3pt,
  boxrule=0.8pt,
  left=10pt, right=10pt, top=8pt, bottom=8pt
}

\newtcolorbox{constitutionalbox}[1]{
  enhanced,
  breakable,
  colback=csRedBg,
  colframe=csCrimson,
  colbacktitle=csCrimson,
  coltitle=white,
  fonttitle=\bfseries,
  title={#1},
  arc=3pt,
  boxrule=0.8pt,
  left=10pt, right=10pt, top=8pt, bottom=8pt
}

\newtcolorbox{usecasebox}[1]{
  enhanced,
  breakable,
  colback=csTealBg,
  colframe=csTeal,
  colbacktitle=csTeal,
  coltitle=white,
  fonttitle=\bfseries,
  title={#1},
  arc=3pt,
  boxrule=0.8pt,
  left=10pt, right=10pt, top=8pt, bottom=8pt
}

\newtcolorbox{infobox}[1]{
  enhanced,
  breakable,
  colback=csNavyBg,
  colframe=csNavy,
  colbacktitle=csNavy,
  coltitle=white,
  fonttitle=\bfseries,
  title={#1},
  arc=3pt,
  boxrule=0.8pt,
  left=10pt, right=10pt, top=8pt, bottom=8pt
}

% --- JSON / Code Listing Environment (Forced LTR) ---
\lstdefinelanguage{json}{
  basicstyle=\ttfamily\footnotesize,
  showstringspaces=false,
  breaklines=true,
  string=[b]",
  stringstyle=\color{csTeal},
  morecomment=[l]{//},
  commentstyle=\color{csSlate},
  literate=
    *{0}{{{\color{csAmber}0}}}{1}
     {1}{{{\color{csAmber}1}}}{1}
     {2}{{{\color{csAmber}2}}}{1}
     {3}{{{\color{csAmber}3}}}{1}
     {4}{{{\color{csAmber}4}}}{1}
     {5}{{{\color{csAmber}5}}}{1}
     {6}{{{\color{csAmber}6}}}{1}
     {7}{{{\color{csAmber}7}}}{1}
     {8}{{{\color{csAmber}8}}}{1}
     {9}{{{\color{csAmber}9}}}{1}
     {:}{{{\color{csNavy}{:}}}}{1}
     {,}{{{\color{csNavy}{,}}}}{1}
     {\{}{{{\color{csNavy}{\{}}}}{1}
     {\}}{{{\color{csNavy}{\}}}}}{1}
     {[}{{{\color{csNavy}{[}}}}{1}
     {]}{{{\color{csNavy}{]}}}}{1}
}

\newtcblisting{jsonlisting}[1]{
  enhanced,
  breakable,
  colback=csNavyBg,
  colframe=csNavy,
  colbacktitle=csNavy,
  coltitle=white,
  fonttitle=\bfseries\small,
  title={\foreignlanguage{english}{#1}},
  arc=3pt,
  boxrule=0.8pt,
  left=8pt, right=8pt, top=4pt, bottom=4pt,
  listing only,
  listing options={language=json, basicstyle=\ttfamily\footnotesize, breaklines=true},
  before upper=\begin{otherlanguage}{english},
  after upper=\end{otherlanguage}
}

% --- BiDi-Safe TikZ Wrapper (RT-03 Fix) & Language Aliases ---
\newcommand{\heb}[1]{\foreignlanguage{hebrew}{#1}}
\newcommand{\en}[1]{\foreignlanguage{english}{#1}}
\providecommand{\textenglish}[1]{\foreignlanguage{english}{#1}}
\providecommand{\texthebrew}[1]{\foreignlanguage{hebrew}{#1}}

\NewEnviron{tikzhebrew}[1][]{%
  \begin{otherlanguage}{english}%
  \begin{tikzpicture}[#1]%
    \BODY%
  \end{tikzpicture}%
  \end{otherlanguage}%
}

\endinput
