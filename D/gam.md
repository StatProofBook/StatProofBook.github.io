---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-02-08 23:29:00

title: "Gamma distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Gamma distribution"
definition: "Definition"

sources:
  - authors: "Koch, Karl-Rudolf"
    year: 2007
    title: "Gamma Distribution"
    in: "Introduction to Bayesian Statistics"
    pages: "Springer, Berlin/Heidelberg, 2007, p. 47, eq. 2.172"
    url: "https://www.springer.com/de/book/9783540727231"
    doi: "10.1007/978-3-540-72726-2"

def_id: "D7"
shortcut: "gam"
username: "JoramSoch"
---


**Definition:** Let $X$ be a [random variable](/D/rvar). Then, $X$ is said to follow a gamma distribution with shape $a$ and rate $b$

$$ \label{eq:gam}
X \sim \mathrm{Gam}(a, b) \; ,
$$

if and only if its [probability density function](/D/pdf) is given by

$$ \label{eq:gam-pdf}
\mathrm{Gam}(x; a, b) = \frac{b^a}{\Gamma(a)} x^{a-1} \exp[-b x], \quad x > 0
$$

where $a > 0$ and $b > 0$, and the density is zero, if $x \leq 0$.