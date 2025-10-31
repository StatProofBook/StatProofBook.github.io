---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2025-01-10 17:42:26

title: "Pooled sample standard deviation"
chapter: "General Theorems"
section: "Probability theory"
topic: "Measures of statistical dispersion"
definition: "Pooled sample standard deviation"

sources:
  - authors: "Ostwald, Dirk"
    year: 2023
    title: "T-Tests"
    in: "Allgemeines Lineares Modell"
    pages: "Einheit (9), Folien 66/73"
    url: "https://www.ipsy.ovgu.de/ipsy_media/Methodenlehre+I/Sommersemester+2023/Allgemeines+Lineares+Modell/9_T_Tests.pdf"
  - authors: "Wikipedia"
    year: 2025
    title: "Pooled variance"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2025-01-10"
    url: "https://en.wikipedia.org/wiki/Pooled_variance#Definition_and_computation"

def_id: "D213"
shortcut: "std-pool"
username: "JoramSoch"
---


**Definition:** Let $x_i = \left\lbrace x_{11}, \ldots, x_{1n_i} \right\rbrace$ for $i = 1,\ldots,k$ be [samples](/D/samp) from a [random variable](/D/rvar) $X$ whose [expected value](/D/mean), but not [variance](/D/var) potentially depends on sample index $i$. Then, the pooled [sample standard deviation](/D/std-samp) is defined as the square root of the [pooled sample variance](/D/var-pool), i.e.

$$ \label{eq:std-pool}
s_{1...k} = \sqrt{s^2_{1...k}} = \sqrt{\frac{1}{n-k} \sum_{i=1}^{k} \sum_{j=1}^{n_i} (x_{ij} - \bar{x}_i)^2}
$$

where $\bar{x}_i$ is the [sample mean](/D/mean-samp) of the $i$-th sample

$$ \label{eq:mean-samp}
\bar{x}_i = \frac{1}{n_i} \sum_{j=1}^{n_i} x_{ij}
$$

and $n$ is the [total sample size](/D/samp-size):

$$ \label{eq:samp-size}
n = \sum_{i=1}^{k} n_i \; .
$$