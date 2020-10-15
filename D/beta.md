---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-05-10 20:29:00

title: "Beta distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Beta distribution"
definition: "Definition"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Beta distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-05-10"
    url: "https://en.wikipedia.org/wiki/Beta_distribution#Definitions"

def_id: "D53"
shortcut: "beta"
username: "JoramSoch"
---


**Definition:** Let $X$ be a [random variable](/D/rvar). Then, $X$ is said to follow a beta distribution with shape parameters $\alpha$ and $\beta$

$$ \label{eq:beta}
X \sim \mathrm{Bet}(\alpha, \beta) \; ,
$$

if and only if its [probability density function](/D/pdf) is given by

$$ \label{eq:beta-pdf}
\mathrm{Bet}(x; \alpha, \beta) = \frac{1}{\mathrm{B}(\alpha, \beta)} \, x^{\alpha-1} \, (1-x)^{\beta-1}
$$

where $\alpha > 0$ and $\beta > 0$, and the density is zero, if $x \notin [0,1]$.