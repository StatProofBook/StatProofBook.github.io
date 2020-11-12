---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-11-12 05:25:00

title: "Minimum"
chapter: "General Theorems"
section: "Probability theory"
topic: "Further summary statistics"
definition: "Minimum"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Sample maximum and minimum"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-11-12"
    url: "https://en.wikipedia.org/wiki/Sample_maximum_and_minimum"

def_id: "D107"
shortcut: "min"
username: "JoramSoch"
---


**Definition:** The minimum of a sample or random variable is its lowest observed or possible value.

<br>
1) Let $x = \left\lbrace x_1, \ldots, x_n \right\rbrace$ be a [sample](/D/samp) from a [random variable](/D/rvar) $X$. Then, the minimum of $x$ is

$$ \label{eq:min-samp}
\mathrm{min}(x) = x_j, \quad \text{such that} \quad x_j \leq x_i \quad \text{for all} \quad i = 1, \ldots, n, \; i \neq j \; ,
$$

i.e. the minimum is the value which is smaller than or equal to all other observed values.

<br>
2) Let $X$ be a [random variable](/D/rvar) with possible values $\mathcal{X}$. Then, the minimum of $X$ is

$$ \label{eq:min-rvar}
\mathrm{min}(X) = \tilde{x}, \quad \text{such that} \quad \tilde{x} < x \quad \text{for all} \quad x \in \mathcal{X}\setminus\left\lbrace \tilde{x} \right\rbrace \; ,
$$

i.e. the minimum is the value which is smaller than all other possible values.