---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-10-15 11:10:00

title: "Mode"
chapter: "General Theorems"
section: "Probability theory"
topic: "Measures of central tendency"
definition: "Mode"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Mode (statistics)"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-10-15"
    url: "https://en.wikipedia.org/wiki/Mode_(statistics)"

def_id: "D102"
shortcut: "mode"
username: "JoramSoch"
---


**Definition:** The mode of a sample or random variable is the value which occurs most often or with largest probability among all its values.

<br>
1) Let $x = \left\lbrace x_1, \ldots, x_n \right\rbrace$ be a [sample](/D/samp) from a [random variable](/D/rvar) $X$. Then, the mode of $x$ is the value which occurs most often in the list $x_1, \ldots, x_n$.

<br>
2) Let $X$ be a [random variable](/D/rvar) with [probability mass function](/D/pmf) or [probability density function](/D/pdf) $f_X(x)$. Then, the mode of $X$ is the the value which maximizes the PMF or PDF:

$$ \label{eq:mode-rvar}
\mathrm{mode}(X) = \operatorname*{arg\,max}_x f_X(x) \; .
$$