---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-07-28 03:30:00

title: "Posterior model probability"
chapter: "Model Selection"
section: "Bayesian model selection"
topic: "Posterior model probability"
definition: "Definition"

sources:
  - authors: "Soch J, Allefeld C"
    year: 2018
    title: "MACS – a new SPM toolbox for model assessment, comparison and selection"
    in: "Journal of Neuroscience Methods"
    pages: "vol. 306, pp. 19-31, eq. 23"
    url: "https://www.sciencedirect.com/science/article/pii/S0165027018301468"
    doi: "10.1016/j.jneumeth.2018.05.017"

def_id: "D87"
shortcut: "pmp"
username: "JoramSoch"
---


**Definition:** Let $m_1, \ldots, m_M$ be $M$ [statistical models](/D/fpm) with [model evidences](/D/ml) $p(y \vert m_1), \ldots, p(y \vert m_M)$ and [prior probabilities](/D/prior)  $p(m_1), \ldots, p(m_M)$. Then, the [conditional probability](/D/prob-cond) of model $m_i$, given the data $y$, is called the [posterior probability](/D/post) of model $m_i$:

$$ \label{eq:PMP}
\mathrm{PP}(m_i) = p(m_i|y) \; .
$$