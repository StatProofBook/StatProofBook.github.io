---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2019-09-27 16:40:00

title: "Template for The Book of Statistical Proofs"
chapter: "enter chapter here"
section: "enter section here"
topic: "enter topic here"
theorem: "enter theorem here"

dependencies:
  - theorem: "a theorem this proof depends on (with internal reference)"
    shortcut: "-temp-"
  - theorem: "another theorem this proof requires (without reference)"
    shortcut: 

sources:
  - authors: "Author(s) of the source of the proof*"
    year: year when published*
    title: "title of the source of the proof*"
    in: "title of monography or name of journal**"
    pages: "volume, issue and/or page information** (* required, ** optional)"
    url: "https://optional.url/to-source/"
    doi: "optional.doi/of.source"

proof_id: "P0"
shortcut: "-temp-"
username: "JoramSoch"
---


**Theorem:** Statement of the theorem.

\begin{equation} \label{eq:Theorem}
\textbf{an equation belonging to the theorem}
\end{equation}

This holds under some conditions.


**Proof:** Statement of the proof.

\begin{equation} \label{eq:Proof}
\textbf{an equation belonging to the proof}
\end{equation}

This completes the proof of \eqref{eq:Theorem}.