---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-11-12 05:33:00

title: "Maximum"
chapter: "General Theorems"
section: "Probability theory"
topic: "Further summary statistics"
definition: "Maximum"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Sample maximum and minimum"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-11-12"
    url: "https://en.wikipedia.org/wiki/Sample_maximum_and_minimum"

def_id: "D108"
shortcut: "max"
username: "JoramSoch"
---


**Definition:** The maximum of a sample or random variable is its highest observed or possible value.

<br>
1) Let $x = \left\lbrace x_1, \ldots, x_n \right\rbrace$ be a [sample](/D/samp) from a [random variable](/D/rvar) $X$. Then, the maximum of $x$ is

$$ \label{eq:max-samp}
\mathrm{max}(x) = x_j, \quad \text{such that} \quad x_j \geq x_i \quad \text{for all} \quad i = 1, \ldots, n, \; i \neq j \; ,
$$

i.e. the maximum is the value which is larger than or equal to all other observed values.

<br>
2) Let $X$ be a [random variable](/D/rvar) with possible values $\mathcal{X}$. Then, the maximum of $X$ is

$$ \label{eq:max-rvar}
\mathrm{max}(X) = \tilde{x}, \quad \text{such that} \quad \tilde{x} > x \quad \text{for all} \quad x \in \mathcal{X}\setminus\left\lbrace \tilde{x} \right\rbrace \; ,
$$

i.e. the maximum is the value which is larger than all other possible values.