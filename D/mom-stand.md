---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-10-08 03:47:00

title: "Standardized moment"
chapter: "General Theorems"
section: "Probability theory"
topic: "Further moments"
definition: "Standardized moment"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Moment (mathematics)"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-10-08"
    url: "https://en.wikipedia.org/wiki/Moment_(mathematics)#Standardized_moments"

def_id: "D99"
shortcut: "mom-stand"
username: "JoramSoch"
---


**Definition:** Let $X$ be a [random variable](/D/rvar) with [expected value](/D/mean) $\mu$ and [standard deviation](/D/std) $\sigma$ and let $n$ be a positive integer. Then, the $n$-th standardized moment of $X$ is defined as the $n$-th [moment](/D/mom) of $X$ about the value $\mu$, divided by the $n$-th power of $\sigma$:

$$ \label{eq:mom-stand}
\mu_n^{*} = \frac{\mu_n}{\sigma^n} =  \frac{\mathrm{E}[(X-\mu)^n]}{\sigma^n} \; .
$$