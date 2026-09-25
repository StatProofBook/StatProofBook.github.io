---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2026-09-11 10:34:53

title: "Odds ratio"
chapter: "Statistical Models"
section: "Count data"
topic: "$2 \times 2$ contingency table"
definition: "Odds ratio"

sources:
  - authors: "Wikipedia"
    year: 2026
    title: "Odds ratio"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2026-09-11"
    url: "https://en.wikipedia.org/wiki/Odds_ratio#Definition_in_terms_of_joint_and_conditional_probabilities"

def_id: "D240"
shortcut: "or"
username: "JoramSoch"
---


**Definition:** Consider a [2 $\times$ 2 contingency table](/D/ct2x2) characterized by [random events](/D/reve) $A$ and $B$. Then, the odds ratio (OR) is defined as the ratio of the odds of event $A$ taking place in the presence of $B$, and the odds of $A$ taking place in the absence of $B$:

$$ \label{eq:or}
\begin{split}
   \mathrm{OR}
&= \frac{\mathrm{Pr}(A|B)}{\mathrm{Pr}(\overline{A}|B)} \bigg/
   \frac{\mathrm{Pr}(A|\overline{B})}{\mathrm{Pr}(\overline{A}|\overline{B})} \\
&= \frac{p_{11}/(p_{11} + p_{01})}{p_{01}/(p_{11} + p_{01})} \bigg/
   \frac{p_{10}/(p_{10} + p_{00})}{p_{00}/(p_{10} + p_{00})} \\
&= \frac{p_{11} / p_{01}}{p_{10} / p_{00}}
 = \frac{p_{11} \, p_{00}}{p_{01} \, p_{10}} \; .
\end{split}
$$

Given observed data from a [2 $\times$ 2 contingency table](/D/ct2x2), its sample estimate is given by

$$ \label{eq:or-samp}
  \hat{\mathrm{OR}}
= \frac{y_{11} / y_{01}}{y_{10} / y_{00}}
= \frac{y_{11} \, y_{00}}{y_{01} \, y_{10}} \; .
$$