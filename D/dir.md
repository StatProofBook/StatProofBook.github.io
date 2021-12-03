---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-05-10 20:36:00

title: "Dirichlet distribution"
chapter: "Probability Distributions"
section: "Multivariate continuous distributions"
topic: "Dirichlet distribution"
definition: "Definition"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Dirichlet distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-05-10"
    url: "https://en.wikipedia.org/wiki/Dirichlet_distribution#Probability_density_function"

def_id: "D54"
shortcut: "dir"
username: "JoramSoch"
---


**Definition:** Let $X$ be a $k \times 1$ [random vector](/D/rvec). Then, $X$ is said to follow a Dirichlet distribution with concentration parameters $\alpha = \left[ \alpha_1, \ldots, \alpha_k \right]$

$$ \label{eq:Dir}
X \sim \mathrm{Dir}(\alpha) \; ,
$$

if and only if its [probability density function](/D/pdf) is given by

$$ \label{eq:beta-pdf}
\mathrm{Dir}(x; \alpha) = \frac{\Gamma\left( \sum_{i=1}^k \alpha_i \right)}{\prod_{i=1}^k \Gamma(\alpha_i)} \, \prod_{i=1}^k {x_i}^{\alpha_i-1}
$$

where $\alpha_i > 0$ for all $i = 1, \ldots, k$, and the density is zero, if $x_i \notin [0,1]$ for any $i = 1, \ldots, k$ or $\sum_{i=1}^k x_i \neq 1$.