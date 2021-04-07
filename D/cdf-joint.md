---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-04-07 08:17:00

title: "Joint cumulative distribution function"
chapter: "General Theorems"
section: "Probability theory"
topic: "Probability functions"
definition: "Joint cumulative distribution function"

sources:
  - authors: "Wikipedia"
    year: 2021
    title: "Cumulative distribution function"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-04-07"
    url: "https://en.wikipedia.org/wiki/Cumulative_distribution_function#Definition_for_more_than_two_random_variables"

def_id: "D141"
shortcut: "cdf-joint"
username: "JoramSoch"
---


**Definition:** Let $X \in \mathbb{R}^{n \times 1}$ be an $n \times 1$ [random vector](/D/rvec). Then, the [joint](/D/dist-joint) [cumulative distribution function](/D/cdf) of $X$ is defined as the [probability](/D/prob) that each entry $X_i$ is smaller than a specific value $x_i$ for $i = 1, \ldots, n$:

$$ \label{eq:cdf-joint}
F_X(x) = \mathrm{Pr}(X_1 \leq x_1, \ldots, X_n \leq x_n) \; .
$$