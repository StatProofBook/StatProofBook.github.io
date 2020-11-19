---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-11-12 07:48:00

title: "Quantile function is inverse of strictly monotonically increasing cumulative distribution function"
chapter: "General Theorems"
section: "Probability theory"
topic: "Probability functions"
theorem: "Quantile function in terms of cumulative distribution function"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Quantile function"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-11-12"
    url: "https://en.wikipedia.org/wiki/Quantile_function#Definition"

proof_id: "P192"
shortcut: "qf-cdf"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [continuous](/D/rvar-disc) [random variable](/D/rvar) with the [cumulative distribution function](/D/cdf) $F_X(x)$. If the cumulative distribution function is strictly monotonically increasing, then the [quantile function](/D/qf)  is identical to the inverse of $F_X(x)$:

$$ \label{eq:qf-cdf}
Q_X(p) = F_X^{-1}(x) \; .
$$


**Proof:** The [quantile function](/D/qf) $Q_X(p)$ is defined as the function that, for a given quantile $p \in [0,1]$, returns the smallest $x$ for which $F_X(x) = p$:

$$ \label{eq:qf}
Q_X(p) = \min \left\lbrace x \in \mathbb{R} \, \vert \, F_X(x) = p \right\rbrace \; .
$$

If $F_X(x)$ is continuous and strictly monotonically increasing, then there is exactly one $x$ for which $F_X(x) = p$ and $F_X(x)$ is an invertible function, such that

$$ \label{eq:qf-cdf-qed}
Q_X(p) = F_X^{-1}(x) \; .
$$