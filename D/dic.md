---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-02-25 12:46:00

title: "Deviance information criterion"
chapter: "Model Selection"
section: "Classical information criteria"
topic: "Deviance information criterion"
definition: "Definition"

sources:
  - authors: "Spiegelhalter DJ, Best NG, Carlin BP, Van Der Linde A"
    year: 2002
    title: "Bayesian measures of model complexity and fit"
    in: "Journal of the Royal Statistical Society, Series B: Statistical Methodology"
    pages: "vol. 64, iss. 4, pp. 583-639"
    url: "https://rss.onlinelibrary.wiley.com/doi/10.1111/1467-9868.00353"
    doi: "10.1111/1467-9868.00353"
  - authors: "Soch J, Allefeld C"
    year: 2018
    title: "MACS – a new SPM toolbox for model assessment, comparison and selection"
    in: "Journal of Neuroscience Methods"
    pages: "vol. 306, pp. 19-31, eqs. 10-12"
    url: "https://www.sciencedirect.com/science/article/pii/S0165027018301468"
    doi: "10.1016/j.jneumeth.2018.05.017"

def_id: "D25"
shortcut: "dic"
username: "JoramSoch"
---


**Definition:** Let $m$ be a [full probability model](/D/fpm) with [likelihood function](/D/lf) $p(y \vert \theta, m)$ and [prior distribution](/D/prior) $p(\theta \vert m)$. Together, likelihood function and prior distribution [imply a posterior distribution](/P/post-jl) $p(\theta \vert y, m)$. Consider the [deviance](/D/dev) which is minus two times the [log-likelihood function](/D/llf):

$$ \label{eq:dev}
D(\theta) = -2 \log p(y|\theta,m) \; .
$$

Then, the deviance information criterion (DIC) of the model $m$ is defined as

$$ \label{eq:DIC}
\mathrm{DIC}(m) = -2 \log p(y|\left\langle \theta \right\rangle, m) + 2 \, p_D
$$

where $\log p(y \vert \left\langle \theta \right\rangle, m)$ is the [log-likelihood function](/D/llf) at the [posterior](/D/post) [expectation](/D/mean) and the "effective number of parameters" $p_D$ is the [difference between the expectation of the deviance and the deviance at the expectation](/D/dic):

$$ \label{eq:DIC-pD}
p_D = \left\langle D(\theta) \right\rangle - D(\left\langle \theta \right\rangle) \; .
$$

In these equations, $\left\langle \cdot \right\rangle$ denotes [expected values](/D/mean) across the [posterior distribution](/D/post).