---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-12-02 18:26:00

title: "Reference prior distribution"
chapter: "General Theorems"
section: "Bayesian statistics"
topic: "Prior distributions"
definition: "Reference priors"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Prior probability"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-12-02"
    url: "https://en.wikipedia.org/wiki/Prior_probability#Uninformative_priors"

def_id: "D123"
shortcut: "prior-ref"
username: "JoramSoch"
---


**Definition:** Let $m$ be a [generative model](/D/gm) with [likelihood function](/D/lf) $p(y \vert \theta, m)$ and [prior distribution](/D/prior) $p(\theta \vert \lambda, m)$ using [prior hyperparameters](/D/prior) $\lambda$. Let $p(\theta \vert y, \lambda, m)$ be the [posterior distribution](/D/post) that is [proportional to the the joint likelihood](/P/post-jl). Then, the prior distribution is called a "reference prior", if it maximizes the [expected](/D/mean) [Kullback-Leibler divergence](/D/kl) of the posterior distribution relative to the prior distribution:

$$ \label{eq:prior-ref}
\lambda_{\mathrm{ref}} = \operatorname*{arg\,max}_{\lambda} \left\langle \mathrm{KL} \left[ p(\theta \vert y, \lambda, m) \, || \, p(\theta \vert \lambda, m) \right] \right\rangle \; .
$$