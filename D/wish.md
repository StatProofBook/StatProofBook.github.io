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


**Definition:** Let $Y$ be an $n \times p$ matrix following a [matrix-normal distribution](/D/matn) with mean zero, independence across rows and covariance across columns $V$:

$$ \label{eq:matn}
Y \sim \mathcal{MN}(0, I_n, V) \; .
$$

Define the scatter matrix $X$ as the product of the transpose of $Y$ with itself:

$$ \label{eq:scat-mat}
X = Y^T Y = \sum_{i=1}^n x_i^\mathrm{T} x_i \; .
$$

Then, the matrix $X$ is said to follow a Wishart distribution with scale matrix $V$ and [degrees of freedom](/D/dof) $n$

$$ \label{eq:wish}
X \sim \mathcal{W}(V, n)
$$

where $n > p - 1$ and $V$ is a positive-definite symmetric covariance matrix.