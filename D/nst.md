---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-05-20 07:35:00

title: "Non-standardized t-distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "t-distribution"
definition: "Non-standardized t-distribution"

sources:
  - authors: "Wikipedia"
    year: 2021
    title: "Student's t-distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-05-20"
    url: "https://en.wikipedia.org/wiki/Student%27s_t-distribution#Generalized_Student's_t-distribution"

def_id: "D152"
shortcut: "nst"
username: "JoramSoch"
---


**Definition:** Let $X$ be a [random variable](/D/rvar) following a [Student's t-distribution](/D/t) with $\nu$ degrees of freedom. Then, the [random variable](/D/rvar)

$$ \label{eq:Y}
Y = \sigma X + \mu
$$

is said to follow a non-standardized t-distribution with non-centrality $\mu$, scale $\sigma^2$ and degrees of freedom $\nu$:

$$ \label{eq:nct}
Y \sim \mathrm{nst}(\mu, \sigma^2, \nu) \; .
$$