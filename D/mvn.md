---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-01-22 05:20:00

title: "Multivariate normal distribution"
chapter: "Probability Distributions"
section: "Multivariate continuous distributions"
topic: "Multivariate normal distribution"
definition: "Definition"

sources:
  - authors: "Koch KR"
    year: 2007
    title: "Multivariate Normal Distribution"
    in: "Introduction to Bayesian Statistics"
    pages: "ch. 2.5.1, pp. 51-53, eq. 2.195"
    url: "https://www.springer.com/gp/book/9783540727231"
    doi: "10.1007/978-3-540-72726-2"

def_id: "D1"
shortcut: "mvn"
username: "JoramSoch"
---


**Definition:** Let $X$ be an $n \times 1$ [random vector](/D/rvec). Then, $X$ is said to be multivariate normally distributed with mean $\mu$ and covariance $\Sigma$

$$ \label{eq:mvn}
X \sim \mathcal{N}(\mu, \Sigma) \; ,
$$

if and only if its [probability density function](/D/pdf) is given by

$$ \label{eq:mvn-pdf}
\mathcal{N}(x; \mu, \Sigma) = \frac{1}{\sqrt{(2 \pi)^n |\Sigma|}} \cdot \exp \left[ -\frac{1}{2} (x-\mu)^\mathrm{T} \Sigma^{-1} (x-\mu) \right]
$$

where $\mu$ is an $n \times 1$ real vector and $\Sigma$ is an $n \times n$ positive definite matrix.