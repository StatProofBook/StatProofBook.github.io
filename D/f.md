---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-04-21 07:26:00

title: "F-distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "F-distribution"
definition: "Definition"

sources:
  - authors: "Wikipedia"
    year: 2021
    title: "F-distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-04-21"
    url: "https://en.wikipedia.org/wiki/F-distribution#Characterization"

def_id: "D146"
shortcut: "f"
username: "JoramSoch"
---


**Definition:** Let $X_1$ and $X_2$ be [independent](/D/ind) [random variables](/D/rvar) following a [chi-squared distribution](/D/chi2) with $\nu_1$ and $\nu_2$ [degrees of freedom](/D/dof), respectively:

$$ \label{eq:chi2}
\begin{split}
X_1 &\sim \chi^{2}(\nu_1) \\
X_2 &\sim \chi^{2}(\nu_2) \; .
\end{split}
$$

Then, the ratio of $X_1$ to $X_2$, divided by their respective degrees of freedom, is said to be $F$-distributed with numerator degrees of freedom $\nu_1$ and denominator degrees of freedom $\nu_2$:

$$\label{eq:F}
Y = \frac{X_1 / \nu_1}{X_2 / \nu_2} \sim F(\nu_1, \nu_2) \quad \text{where} \quad \nu_1, \nu_2 > 0 \; .
$$

The $F$-distribution is also called "Snedecor's $F$-distribution" or "Fisher–Snedecor distribution", after Ronald A. Fisher and George W. Snedecor.