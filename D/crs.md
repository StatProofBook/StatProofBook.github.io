---
layout: definition
mathjax: true

author: "Kenneth Petrykowski"
affiliation: "University of Warsaw"
e_mail: "kenneth.petrykowski@gmail.com"
date: 2026-10-28 22:57:24

title: "Bayesian credible set"
chapter: "General Theorems"
section: "Estimation theory"
topic: "Interval estimates"
definition: "Bayesian credible set"

sources:
  - authors: "George Casella, Roger L. Berger"
    year: 2002
    title: "Bayesian intervals"
    in: "Statistical Inference"
    pages: "Second edition, Section 9.2.4, pp. 435-436"

def_id: "D246"
shortcut: "crs"
username: "kjpetrykowski"
---

**Definition:** Let $x$ be the observed value of the data $X$ and $\theta$ the parameter. For $0<\alpha<1$, a set $C(x)$ of parameter values is a credible set of level $1-\alpha$ if its [posterior probability](/D/post) is defined and is at least $1-\alpha$:

$$ \label{eq:credible-set}
\mathrm{Pr}(\theta\in C(x)\mid X=x)\geq1-\alpha \; .
$$

When equality holds, the set has posterior probability exactly $1-\alpha$. A credible set that is an interval is called a credible interval. If the posterior has density $p(\theta\mid x)$, the probability of $C(x)$ is

$$ \label{eq:credible-probability}
\mathrm{Pr}(\theta\in C(x)\mid X=x)
=\int_{C(x)}p(\theta\mid x)\,\mathrm{d}\theta \; .
$$

For a discrete parameter, sum the posterior probabilities of the values in $C(x)$. Here the data are fixed. For a [confidence interval](/D/ci), coverage is assessed over repeated samples with the parameter fixed.
