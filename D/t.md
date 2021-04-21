---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-04-21 07:53:00

title: "t-distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "t-distribution"
definition: "Definition"

sources:
  - authors: "Wikipedia"
    year: 2021
    title: "Student's t-distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-04-21"
    url: "https://en.wikipedia.org/wiki/Student%27s_t-distribution#How_Student's_distribution_arises_from_sampling"

def_id: "D147"
shortcut: "t"
username: "JoramSoch"
---


**Definition:** Let $X_1, ..., X_n$ be [independent](/D/ind) [random variables](/D/rvar) where each of them is following a [normal distribution](/D/norm) with mean $\mu$ and variance $\sigma^2$:

$$ \label{eq:norm}
X_i \sim \mathcal{N}(\mu, \sigma^2) \quad \text{for} \quad i = 1, \ldots, n \; .
$$

Then, the following random variable with [sample mean](/D/mean-samp) $\bar{X}$ and [sample variance](/D/var-samp) $s^2$ is said to be $t$-distributed with $n-1$ degrees of freedom:

$$ \label{eq:t}
Y = \frac{\bar{X}-\mu}{s/\sqrt{n}} \sim t(n-1) \; .
$$

The $t$-distribution is also called "Student's $t$-distribution", after William S. Gosset a.k.a. "Student".