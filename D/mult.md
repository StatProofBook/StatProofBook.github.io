---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-03-22 17:52:00

title: "Multinomial distribution"
chapter: "Probability Distributions"
section: "Multivariate discrete distributions"
topic: "Multinomial distribution"
definition: "Definition"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Binomial distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-03-22"
    url: "https://en.wikipedia.org/wiki/Multinomial_distribution"

def_id: "D47"
shortcut: "mult"
username: "JoramSoch"
---


**Definition:** Let $X$ be a [random vector](/D/rvec). Then, $X$ is said to follow a multinomial distribution with number of trials $n$ and category probabilities $p_1, \ldots, p_k$

$$ \label{eq:mult}
X \sim \mathrm{Mult}(n, \left[p_1, \ldots, p_k \right]) \; ,
$$

if $X$ are the numbers of observations belonging to $k$ distinct categories in $n$ [independent](/D/ind) trials, where each trial has [$k$ possible outcomes](/D/cat) and the category probabilities are identical across trials.