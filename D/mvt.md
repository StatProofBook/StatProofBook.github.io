---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-04-21 08:16:00

title: "Multivariate t-distribution"
chapter: "Probability Distributions"
section: "Multivariate continuous distributions"
topic: "Multivariate t-distribution"
definition: "Definition"

sources:
  - authors: "Koch KR"
    year: 2007
    title: "Multivariate t-Distribution"
    in: "Introduction to Bayesian Statistics"
    pages: "ch. 2.5.2, pp. 53-55"
    url: "https://www.springer.com/gp/book/9783540727231"
    doi: "10.1007/978-3-540-72726-2"

def_id: "D148"
shortcut: "mvt"
username: "JoramSoch"
---


**Definition:** Let $X$ be an $n \times 1$ [random vector](/D/rvec). Then, $X$ is said to follow a multivariate $t$-distribution with mean $\mu$, scale matrix $\Sigma$ and degrees of freedom $\nu$

$$ \label{eq:mvt}
X \sim t(\mu, \Sigma, \nu) \; ,
$$

if and only if its [probability density function](/D/pdf) is given by

$$ \label{eq:mvt-pdf}
t(x; \mu, \Sigma, \nu) = \sqrt{\frac{1}{(\nu \pi)^{n} |\Sigma|}} \, \frac{\Gamma([\nu+n]/2)}{\Gamma(\nu/2)} \, \left[ 1 + \frac{1}{\nu} (x-\mu)^\mathrm{T} \Sigma^{-1} (x-\mu) \right]^{-(\nu+n)/2}
$$

where $\mu$ is an $n \times 1$ real vector, $\Sigma$ is an $n \times n$ positive definite matrix and $\nu > 0$.