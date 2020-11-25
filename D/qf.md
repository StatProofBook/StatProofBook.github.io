---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-02-17 22:18:00

title: "Quantile function"
chapter: "General Theorems"
section: "Probability theory"
topic: "Probability functions"
definition: "Quantile function"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Probability density function"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-02-17"
    url: "https://en.wikipedia.org/wiki/Quantile_function#Definition"

def_id: "D14"
shortcut: "qf"
username: "JoramSoch"
---


**Definition:** Let $X$ be a [random variable](/D/rvar) with the [cumulative distribution function](/D/cdf) (CDF) $F_X(x)$. Then, the function $Q_X(p): [0,1] \to \mathbb{R}$ which is the inverse CDF is the quantile function (QF) of $X$. More precisely, the QF is the function that, for a given quantile $p \in [0,1]$, returns the smallest $x$ for which $F_X(x) = p$:

$$ \label{eq:qf}
Q_X(p) = \min \left\lbrace x \in \mathbb{R} \, \vert \, F_X(x) = p \right\rbrace \; .
$$