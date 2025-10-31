---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2025-09-25 09:35:20

title: "Jensen's inequality"
chapter: "General Theorems"
section: "Probability theory"
topic: "Expected value"
theorem: "Jensen's inequality"

sources:
  - authors: "Ostwald et al."
    year: 2014
    title: "A tutorial on variational Bayes for latent linear stochastic time-series models"
    in: "Journal of Mathematical Psychology"
    pages: "vol. 60, pp. 1-19, App. A"
    url: "https://www.sciencedirect.com/science/article/pii/S0022249614000352"
    doi: "10.1016/j.jmp.2014.04.0"

proof_id: "P514"
shortcut: "jens-ineq"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [univariate](/D/rvar-uni) [random variable](/D/rvar) with [probability mass function](/D/pmf) (if [discrete](/D/rvar-disc)) or [probability density function](/D/pdf) (if [continuous](/D/rvar-disc)) $f_X(x)$ and let $g(x)$ be a convex function. Then, the function value, evaluated at the [expected value](/D/mean) of $X$, is smaller than or equal to the [expected value](/D/mean) of the function value, evaluated at $X$:

$$ \label{eq:jens-ineq}
g(\mathrm{E}[X]) \leq \mathrm{E}[g(X)] \; .
$$


**Proof:** A function $g(x)$ is said to be convex on the interval $[x_1, x_2]$, if every straight line connecting two points of the function's graph lies above the function's graph:

$$ \label{eq:fct-conv}
g\left( q x_1 + (1-q) x_2 \right) \leq q g(x_1) + (1-q) g(x_2)
\quad \text{for any} \quad
q \in [0, 1] \; .
$$

This property can be extended to an arbitrary number of points $x_i, \, i = 1,\ldots,n$, with $q_i \geq 0, \, i = 1,\ldots,n$ and $\sum_{i=1}^n q_i = 1$, such that

$$ \label{eq:fct-conv-sum}
g\left( \sum_{i=1}^n q_i x_i \right) \leq \sum_{i=1}^n q_i g(x_i) \; .
$$

If $\left\lbrace x_1, \ldots, x_n \right\rbrace$ is the set of possible values for a [discrete random variable](/D/rvar-disc) $X$, then the $q_i$ fulfill the definition of a [probability mass function](/D/pmf) $f_X(x_i) = q_i$. With the [law of the unconscious statistician](/P/mean-lotus), it then follows that

$$ \label{eq:jens-ineq-disc}
g(\mathrm{E}[X]) \leq \mathrm{E}[g(X)] \; .
$$

The above property can be further extended to a continuum of points $x \in \mathcal{X}$, with $q(x) \geq 0$ and $\int_{\mathcal{X}} q(x) \, \mathrm{d}x = 1$, such that

$$ \label{eq:fct-conv-int}
g\left( \int_{\mathcal{X}} q(x) x \, \mathrm{d}x \right) \leq \int_{\mathcal{X}} q(x) g(x) \, \mathrm{d}x \; .
$$

If $\mathcal{X}$ is the set of possible values for a [continuous random variable](/D/rvar-disc) $X$, then $q(x)$ fulfill the definition of a [probability density function](/D/pdf) $f_X(x) = q(x)$. With the [law of the unconscious statistician](/P/mean-lotus), it then follows that

$$ \label{eq:jens-ineq-cont}
g(\mathrm{E}[X]) \leq \mathrm{E}[g(X)] \; .
$$

This completes the proof.