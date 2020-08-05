---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-08-03 21:34:00

title: "Bayesian model averaging"
chapter: "Model Selection"
section: "Bayesian model selection"
topic: "Bayesian model averaging"
definition: "Definition"

sources:
  - authors: "Hoeting JA, Madigan D, Raftery AE, Volinsky CT"
    year: 1999
    title: "Bayesian Model Averaging: A Tutorial"
    in: "Statistical Science"
    pages: "vol. 14, no. 4, pp. 382–417, eq. 1"
    url: "https://projecteuclid.org/euclid.ss/1009212519"
    doi: "10.1214/ss/1009212519"

def_id: "D89"
shortcut: "bma"
username: "JoramSoch"
---


**Definition:** Let $m_1, \ldots, m_M$ be $M$ [statistical models](/D/fpm) with [posterior model probabilities](/D/pmp) $p(m_1 \vert y), \ldots, p(m_M \vert y)$ and [posterior distributions](/D/post) $p(\theta \vert y, m_1), \ldots, p(\theta \vert y, m_M)$. Then, Bayesian model averaging (BMA) consists in finding the [marginal](/D/dist-marg) [posterior](/D/post) [density](/D/pdf), [conditional](/D/prob-cond) on the measured data $y$, but [unconditional](/D/prob-marg) on the modelling approach $m$:

$$ \label{eq:BMA}
p(\theta|y) = \sum_{i=1}^{M} p(\theta|y,m_i) \cdot p(m_i|y) \; .
$$