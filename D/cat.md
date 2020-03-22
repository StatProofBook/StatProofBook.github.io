---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-03-22 18:09:00

title: "Categorical distribution"
chapter: "Probability Distributions"
section: "Multivariate discrete distributions"
topic: "Categorical distribution"
definition: "Definition"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Categorical distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-03-22"
    url: "https://en.wikipedia.org/wiki/Categorical_distribution"

def_id: "D46"
shortcut: "cat"
username: "JoramSoch"
---


**Definition:** Let $X$ be a [random vector](/D/rvec). Then, $X$ is said to follow a categorical distribution with success probability $p_1, \ldots, p_k$

$$ \label{eq:cat}
X \sim \mathrm{Cat}(\left[p_1, \ldots, p_k \right]) \; ,
$$

if $X = e_i$ with [probability](/D/prob) $p_i$ for all $i = 1, \ldots, k$, where $e_i$ is the $i$-th elementary row vector, i.e. a $1 \times k$ vector of zeros with a one in $i$-th position.