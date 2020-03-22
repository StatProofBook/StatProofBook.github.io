---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-03-22 17:15:00

title: "Wishart distribution"
chapter: "Probability Distributions"
section: "Matrix-variate continuous distributions"
topic: "Wishart distribution"
definition: "Definition"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Wishart distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-03-22"
    url: "https://en.wikipedia.org/wiki/Wishart_distribution#Definition"

def_id: "D43"
shortcut: "wish"
username: "JoramSoch"
---


**Definition:** Let $X$ be an $n \times p$ matrix following a [matrix-normal distribution](/D/matn) with mean zero, independence across rows and covariance across columns $V$:

$$ \label{eq:matn}
X \sim \mathcal{MN}(0, I_n, V) \; .
$$

Define the scatter matrix $S$ as the product of the transpose of $X$ with itself:

$$ \label{eq:scat-mat}
S = X^T X = \sum_{i=1}^n x_i^\mathrm{T} x_i \; .
$$

Then, the matrix $S$ is said to follow a Wishart distribution with scale matrix $V$ and degrees of freedom $n$

$$ \label{eq:wish}
S \sim \mathcal{W}(V, n)
$$

where $n > p - 1$ and $V$ is a positive definite symmetric covariance matrix.