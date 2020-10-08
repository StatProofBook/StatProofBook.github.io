---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-01-27 14:37:00

title: "Matrix-normal distribution"
chapter: "Probability Distributions"
section: "Matrix-variate continuous distributions"
topic: "Matrix-normal distribution"
definition: "Definition"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Matrix normal distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-01-27"
    url: "https://en.wikipedia.org/wiki/Matrix_normal_distribution#Definition"

def_id: "D6"
shortcut: "matn"
username: "JoramSoch"
---


**Definition:** Let $X$ be an $n \times p$ [random matrix](/D/rmat). Then, $X$ is said to be matrix-normally distributed with mean $M$, [covariance](/D/covmat) across rows $U$ and [covariance](/D/covmat) across columns $V$

$$ \label{eq:matn}
X \sim \mathcal{MN}(M, U, V) \; ,
$$

if and only if its [probability density function](/D/pdf) is given by

$$ \label{eq:matn-pdf}
\mathcal{MN}(X; M, U, V) = \frac{1}{\sqrt{(2\pi)^{np} |V|^n |U|^p}} \cdot \exp\left[-\frac{1}{2} \mathrm{tr}\left( V^{-1} (X-M)^\mathrm{T} \, U^{-1} (X-M) \right) \right]
$$

where $M$ is an $n \times p$ real matrix, $U$ is an $n \times n$ positive definite matrix and $V$ is a $p \times p$ positive definite matrix.