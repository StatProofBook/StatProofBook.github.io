---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-02-25 12:21:00

title: "Bayesian information criterion"
chapter: "Model Selection"
section: "Classical information criteria"
topic: "Bayesian information criterion"
definition: "Definition"

sources:
  - authors: "Schwarz G"
    year: 1978
    title: "Estimating the Dimension of a Model"
    in: "The Annals of Statistics"
    pages: "vol. 6, no. 2, pp. 461-464"
    url: "https://www.jstor.org/stable/2958889"

def_id: "D24"
shortcut: "bic"
username: "JoramSoch"
---


**Definition:** Let $m$ be a [generative model](/D/gm) with [likelihood function](/D/lf) $p(y \vert \theta, m)$ and [maximum likelihood estimates](/D/mle)

$$ \label{eq:MLE}
\hat{\theta} = \operatorname*{arg\,max}_\theta \log p(y | \theta, m) \; .
$$

Then, the Bayesian information criterion (BIC) of this model is defined as

$$ \label{eq:BIC}
\mathrm{BIC}(m) = -2 \log p(y | \hat{\theta}, m) + p \log n
$$

where $n$ is the number of data points and $p$ is the number of free parameters estimated via \eqref{eq:MLE}.