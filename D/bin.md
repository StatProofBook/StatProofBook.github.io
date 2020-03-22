---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-03-22 17:52:00

title: "Binomial distribution"
chapter: "Probability Distributions"
section: "Univariate discrete distributions"
topic: "Binomial distribution"
definition: "Definition"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Binomial distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-03-22"
    url: "https://en.wikipedia.org/wiki/Binomial_distribution"

def_id: "D45"
shortcut: "bin"
username: "JoramSoch"
---


**Definition:** Let $X$ be a [random variable](/D/rvar). Then, $X$ is said to follow a binomial distribution with number of trials $n$ and success probability $p$

$$ \label{eq:bin}
X \sim \mathrm{Bin}(n, p) \; ,
$$

if $X$ is the number of successes observed in $n$ [independent](/D/ind) trials, where each trial has [two possible outcomes](/D/bern) (success/failure) and the probability of success and failure are identical across trials ($p$/$q = 1-p$).