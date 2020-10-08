---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-08-19 05:24:00

title: "Moment"
chapter: "General Theorems"
section: "Probability theory"
topic: "Further moments"
definition: "Moment"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Moment (mathematics)"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-08-19"
    url: "https://en.wikipedia.org/wiki/Moment_(mathematics)#Significance_of_the_moments"

def_id: "D90"
shortcut: "mom"
username: "JoramSoch"
---


**Definition:** Let $X$ be a [random variable](/D/rvar), let $c$ be a [constant](/D/const) and let $n$ be a positive integer. Then, the $n$-th moment of $X$ about $c$ is defined as the [expected value](/D/mean) of the $n$-th power of $X$ minus $c$:

$$ \label{eq:mom}
\mu_n(c) = \mathrm{E}[(X-c)^n] \; .
$$

The "$n$-th moment of $X$" may also refer to:

* the $n$-th [raw moment](/D/mom-raw) $\mu_n' = \mu_n(0)$;

* the $n$-th [central moment](/D/mom-cent) $\mu_n = \mu_n(\mu)$;

* the $n$-th [standardized moment](/D/mom-stand) $\mu_n^{*} = \mu_n/\sigma^n$.