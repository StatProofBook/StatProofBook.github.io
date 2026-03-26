---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2026-03-26 10:25:28

title: "Partial correlation"
chapter: "General Theorems"
section: "Probability theory"
topic: "Correlation"
definition: "Partial correlation"

sources:
  - authors: "Ostwald D, Soch J"
    year: 2025
    title: "Partielle Korrelation"
    in: "Allgemeines Lineares Modell"
    pages: "Einheit (12), Folie 16"
    url: "https://www.ipsy.ovgu.de/ipsy_media/Methodenlehre+I/Sommersemester+2025/Allgemeines+Lineares+Modell/12_Partielle_Korrelation.pdf"

def_id: "D227"
shortcut: "corr-part"
username: "JoramSoch"
---


**Definition:** Let $X$, $Y$ and $Z$ be [random variables](/D/rvar), such that there are linear relationships

$$ \label{eq:xz-yz}
\begin{split}
X &= \beta_0^{(X)} + \beta_1^{(X)} Z + E^{(X)} \\
Y &= \beta_0^{(Y)} + \beta_1^{(Y)} Z + E^{(Y)}
\end{split}
$$

with the [residual](/P/slr-ressum) [random variables](/D/rvar)

$$ \label{eq:ex-ey}
\begin{split}
E^{(X)} &= X - \beta_0^{(X)} - \beta_1^{(X)} Z \\
E^{(Y)} &= Y - \beta_0^{(Y)} - \beta_1^{(Y)} Z
\end{split}
$$

Then, the partial correlation of $X$ and $Y$ controlling for $Z$ is defined as the [correlation](/D/corr) of the residual variables:

$$ \label{eq:corr-part}
\mathrm{Corr}(X,Y \backslash Z) = \mathrm{Corr}\left( E^{(X)}, E^{(Y)} \right) \; .
$$