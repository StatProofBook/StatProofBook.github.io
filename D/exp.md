---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-02-08 23:48:00

title: "Exponential distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Exponential distribution"
definition: "Definition"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Exponential distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-02-08"
    url: "https://en.wikipedia.org/wiki/Exponential_distribution#Definitions"

def_id: "D8"
shortcut: "exp"
username: "JoramSoch"
---


**Definition:** Let $X$ be a [random variable](/D/rvar). Then, $X$ is said to be exponentially distributed with rate (or, inverse scale) $\lambda$

$$ \label{eq:exp}
X \sim \mathrm{Exp}(\lambda) \; ,
$$

if and only if its [probability density function](/D/pdf) is given by

$$ \label{eq:exp-pdf}
\mathrm{Exp}(x; \lambda) = \lambda \exp[-\lambda x], \quad x \geq 0
$$

where $\lambda > 0$, and the density is zero, if $x < 0$.