---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-02-25 12:56:00

title: "Log model evidence"
chapter: "Model Selection"
section: "Bayesian model selection"
topic: "Log model evidence"
definition: "Definition"

sources:
  - authors: "Soch J, Allefeld C"
    year: 2018
    title: "MACS – a new SPM toolbox for model assessment, comparison and selection"
    in: "Journal of Neuroscience Methods"
    pages: "vol. 306, pp. 19-31, eq. 13"
    url: "https://www.sciencedirect.com/science/article/pii/S0165027018301468"
    doi: "10.1016/j.jneumeth.2018.05.017"

def_id: "D26"
shortcut: "lme"
username: "JoramSoch"
---


**Definition:** Let $m$ be a [generative model](/D/gm) with [likelihood function](/D/lf) $p(y \vert \theta, m)$ and [prior distribution](/D/prior) $p(\theta \vert m)$. Then, the log model evidence (LME) of this model is defined as the logarithm of the [marginal likelihood](/D/ml):

$$ \label{eq:LME}
\mathrm{LME}(m) = \log p(y|m) \; .
$$