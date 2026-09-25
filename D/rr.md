---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2026-09-11 10:47:52

title: "Relative risk"
chapter: "Statistical Models"
section: "Count data"
topic: "Binary contingency table"
definition: "Relative risk"

sources:
  - authors: "Wikipedia"
    year: 2026
    title: "Relative risk"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2026-09-11"
    url: "https://en.wikipedia.org/wiki/Relative_risk#Inference"

def_id: "D241"
shortcut: "rr"
username: "JoramSoch"
---


**Definition:** Consider a [$2 \times 2$ contingency table](/D/ct2x2) characterized by [random events](/D/reve) $A$ and $B$. Then, the relative risk (RR) is defined as the ratio of the probability of $A$ happening in the presence of $B$, and the probability of $A$ happening in the absence of $B$:

$$ \label{eq:rr}
\begin{split}
   \mathrm{RR}
&= \frac{\mathrm{Pr}(A|B)}{\mathrm{Pr}(A|\overline{B})} \\
&= \frac{p_{11}/(p_{11} + p_{01})}{p_{10}/(p_{10} + p_{00})} \\
&= \frac{p_{11}\, (p_{10} + p_{00})}{p_{10} \, (p_{11} + p_{01})} \; .
\end{split}
$$

Given observed data from a [$2 \times 2$ contingency table](/D/ct2x2), its sample estimate is given by

$$ \label{eq:or-samp}
\begin{split}
   \hat{\mathrm{RR}}
&= \frac{y_{11}/(y_{11} + y_{01})}{y_{10}/(y_{10} + y_{00})} \\
&= \frac{y_{11}\, (y_{10} + y_{00})}{y_{10} \, (y_{11} + y_{01})} \; .
\end{split}
$$