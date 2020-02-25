---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-02-25 12:31:00

title: "Akaike information criterion"
chapter: "Model Selection"
section: "Classical information criteria"
topic: "Akaike information criterion"
definition: "Definition"

sources:
  - authors: "Akaike H"
    year: 1974
    title: "A New Look at the Statistical Model Identification"
    in: "IEEE Transactions on Automatic Control"
    pages: "vol. AC-19, no. 6, pp. 716-723"
    url: "https://ieeexplore.ieee.org/document/1100705"
    doi: "10.1109/TAC.1974.1100705"

def_id: "D23"
shortcut: "aic"
username: "JoramSoch"
---


**Definition:** Let $m$ be a [generative model](/D/gm) with [likelihood function](/D/lf) $p(y \vert \theta, m)$ and [maximum likelihood estimates](/D/mle)

$$ \label{eq:MLE}
\hat{\theta} = \operatorname*{arg\,max}_\theta \log p(y | \theta, m) \; .
$$

Then, the Akaike information criterion (AIC) of this model is defined as

$$ \label{eq:AIC}
\mathrm{AIC}(m) = -2 \log p(y | \hat{\theta}, m) + 2 \, p
$$

where $p$ is the number of free parameters estimated via \eqref{eq:MLE}.