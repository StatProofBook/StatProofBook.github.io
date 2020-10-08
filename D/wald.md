---
layout: definition
mathjax: true

author: "Thomas J. Faulkenberry"
affiliation: "Tarleton State University"
e_mail: "faulkenberry@tarleton.edu"
date: 2020-09-04 12:00:00

title: "Wald distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Wald distribution"
definition: "Definition"

sources:
  - authors: "Anders, R., Alario, F.-X., and van Maanen, L."
    year: 2016
    title: "The Shifted Wald Distribution for Response Time Data Analysis"
    in: "Psychological Methods"
    pages: "vol. 21, no. 3, pp. 309-327"
    url: "https://dx.doi.org/10.1037/met0000066"
    doi: "10.1037/met0000066"

def_id: "D95"
shortcut: "wald"
username: "tomfaulkenberry"
---


**Definition:** Let $X$ be a [random variable](/D/rvar). Then, $X$ is said to follow a Wald distribution with drift rate $\gamma$ and threshold $\alpha$

$$ \label{eq:wald}
X \sim \mathrm{Wald}(\gamma, \alpha) \; ,
$$

if and only if its [probability density function](/D/pdf) is given by

$$ \label{eq:wald-pdf}
\mathrm{Wald}(x; \gamma, \alpha) = \frac{\alpha}{\sqrt{2\pi x^3}}\exp\left(-\frac{(\alpha-\gamma x)^2}{2x}\right)
$$

where $\gamma > 0$, $\alpha > 0$, and the density is zero if $x \leq 0$.