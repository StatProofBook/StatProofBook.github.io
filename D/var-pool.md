---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2025-01-10 17:40:55

title: "Pooled sample variance"
chapter: "General Theorems"
section: "Probability theory"
topic: "Variance"
definition: "Pooled sample variance"

sources:
  - authors: "Soch, Joram; Ostwald, Dirk"
    year: 2024
    title: "Einfaktorielle Varianzanalyse"
    in: "Allgemeines Lineares Modell"
    pages: "Einheit (10), Folien 27-29"
    url: "https://www.ipsy.ovgu.de/ipsy_media/Methodenlehre+I/Sommersemester+2024/Allgemeines+Lineares+Modell/10_Einfaktorielle_Varianzanalyse.pdf"
  - authors: "Wikipedia"
    year: 2025
    title: "Pooled variance"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2025-01-10"
    url: "https://en.wikipedia.org/wiki/Pooled_variance#Definition_and_computation"

def_id: "D212"
shortcut: "var-pool"
username: "JoramSoch"
---


**Definition:** Let $x_i = \left\lbrace x_{11}, \ldots, x_{1n_i} \right\rbrace$ for $i = 1,\ldots,k$ be [samples](/D/samp) from a [random variable](/D/rvar) $X$ whose [expected value](/D/mean), but not [variance](/D/var) potentially depends on sample index $i$. Then, the pooled [sample variance](/D/var-samp) of $x = \left\lbrace x_1, \ldots, x_k \right\rbrace$ is given by

$$ \label{eq:var-pool}
s^2_{1...k} = \frac{1}{n-k} \sum_{i=1}^{k} \sum_{j=1}^{n_i} (x_{ij} - \bar{x}_i)^2
$$

where $\bar{x}_i$ is the [sample mean](/D/mean-samp) of the $i$-th sample

$$ \label{eq:mean-samp}
\bar{x}_i = \frac{1}{n_i} \sum_{j=1}^{n_i} x_{ij}
$$

and $n$ is the [total sample size](/D/samp-size):

$$ \label{eq:samp-size}
n = \sum_{i=1}^{k} n_i \; .
$$