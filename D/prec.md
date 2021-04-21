---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-04-21 07:04:00

title: "Precision"
chapter: "General Theorems"
section: "Probability theory"
topic: "Variance"
definition: "Precision"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Precision (statistics)"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-04-21"
    url: "https://en.wikipedia.org/wiki/Precision_(statistics)"

def_id: "D145"
shortcut: "prec"
username: "JoramSoch"
---


**Definition:** The precision of a [random variable](/D/rvar) $X$ is defined as the inverse of the [variance](/D/var), i.e. one divided by the [expected value](/D/mean) of the squared deviation from its [expected value](/D/mean):

$$ \label{eq:prec}
\mathrm{Prec}(X) = \mathrm{Var}(X)^{-1} = \frac{1}{\mathrm{E}\left[ (X-\mathrm{E}(X))^2 \right]} \; .
$$