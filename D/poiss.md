---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-05-25 23:34:00

title: "Poisson distribution"
chapter: "Probability Distributions"
section: "Univariate discrete distributions"
topic: "Poisson distribution"
definition: "Definition"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Poisson distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-05-25"
    url: "https://en.wikipedia.org/wiki/Poisson_distribution#Definitions"

def_id: "D62"
shortcut: "poiss"
username: "JoramSoch"
---


**Definition:** Let $X$ be a [random variable](/D/rvar). Then, $X$ is said to follow a Poisson distribution with rate $\lambda$

$$ \label{eq:poiss}
X \sim \mathrm{Poiss}(\lambda) \; ,
$$

if and only if its [probability mass function](/D/pmf) is given by

$$ \label{eq:poiss-pmf}
\mathrm{Poiss}(x; \lambda) = \frac{\lambda^x \, e^{-\lambda}}{x!}
$$

where $x \in \mathbb{N}_0$ and $\lambda > 0$.