---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-12-02 18:19:00

title: "Empirical Bayes prior distribution"
chapter: "General Theorems"
section: "Bayesian statistics"
topic: "Prior distributions"
definition: "Empirical Bayes priors"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Empirical Bayes method"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-12-02"
    url: "https://en.wikipedia.org/wiki/Empirical_Bayes_method#Introduction"

def_id: "D122"
shortcut: "prior-eb"
username: "JoramSoch"
---


**Definition:** Let $m$ be a [generative model](/D/gm) with [likelihood function](/D/lf) $p(y \vert \theta, m)$ and [prior distribution](/D/prior) $p(\theta \vert \lambda, m)$ using [prior hyperparameters](/D/prior) $\lambda$. Let $p(y \vert \lambda, m)$ be the [marginal likelihood](/D/ml) when [integrating the parameters out of the joint likelihood](/P/ml-jl). Then, the prior distribution is called an "[Empirical Bayes](/D/eb) prior", if it maximizes the logarithmized marginal likelihood:

$$ \label{eq:prior-eb}
\lambda_{\mathrm{EB}} = \operatorname*{arg\,max}_{\lambda} \log p(y \vert \lambda, m) \; .
$$