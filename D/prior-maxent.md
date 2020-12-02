---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-12-02 18:13:00

title: "Maximum entropy prior distribution"
chapter: "General Theorems"
section: "Bayesian statistics"
topic: "Prior distributions"
definition: "Maximum entropy priors"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Prior probability"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-12-02"
    url: "https://en.wikipedia.org/wiki/Prior_probability#Uninformative_priors"

def_id: "D121"
shortcut: "prior-maxent"
username: "JoramSoch"
---


**Definition:** Let $m$ be a [generative model](/D/gm) with [likelihood function](/D/lf) $p(y \vert \theta, m)$ and [prior distribution](/D/prior) $p(\theta \vert \lambda, m)$ using [prior hyperparameters](/D/prior) $\lambda$. Then, the prior distribution is called a "maximum entropy prior", if

1) when $\theta$ is a [discrete random variable](/D/rvar-disc), it maximizes the [entropy](/D/ent) of the prior [probability mass function](/D/pmf):

$$ \label{eq:prior-maxent-disc}
\lambda_{\mathrm{maxent}} = \operatorname*{arg\,max}_{\lambda} \mathrm{H}\left[ p(\theta \vert \lambda, m) \right] \; ;
$$

2) when $\theta$ is a [continuous random variable](/D/rvar-disc), it maximizes the [differential entropy](/D/dent) of the prior [probability density function](/D/pdf):

$$ \label{eq:prior-maxent-cont}
\lambda_{\mathrm{maxent}} = \operatorname*{arg\,max}_{\lambda} \mathrm{h}\left[ p(\theta \vert \lambda, m) \right] \; .
$$