---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-02-17 22:07:00

title: "Cumulative distribution function"
chapter: "General Theorems"
section: "Probability theory"
topic: "Probability distributions"
definition: "Cumulative distribution function"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Probability density function"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-02-17"
    url: "https://en.wikipedia.org/wiki/Cumulative_distribution_function#Definition"

def_id: "D13"
shortcut: "cdf"
username: "JoramSoch"
---


**Definition:**

1) Let $X$ be a discrete [random variable](/D/rvar) with possible outcomes $\mathcal{X}$ and the [probability mass function](/D/pmf) $f_X(x)$. Then, the function $F_X(x): \mathbb{R} \to [0,1]$ with

$$ \label{eq:cdf-disc}
F_X(x) = \sum_{\overset{z \in \mathcal{X}}{z \leq x}} f_X(z)
$$

is the cumulative distribution function of $X$.

<br>
2) Let $X$ be a scalar continuous [random variable](/D/rvar) with the [probability density function](/D/pdf) $f_X(x)$. Then, the function $F_X(x): \mathbb{R} \to [0,1]$ with

$$ \label{eq:cdf-cont}
F_X(x) = \int_{-\infty}^{x} f_X(z) \, \mathrm{d}x
$$

is the cumulative distribution function of $X$.