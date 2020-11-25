---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-11-25 08:10:00

title: "Variational Bayesian log model evidence"
chapter: "Model Selection"
section: "Bayesian model selection"
topic: "Log model evidence"
definition: "Variational Bayesian log model evidence"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Variational Bayesian methods"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-11-25"
    url: "https://en.wikipedia.org/wiki/Variational_Bayesian_methods#Evidence_lower_bound"
  - authors: "Bishop CM"
    year: 2006
    title: "Variational Inference"
    in: "Pattern Recognition for Machine Learning"
    pages: "pp. 462-474, eqs. 10.2-10.4"
    url: "https://www.springer.com/gp/book/9780387310732"

def_id: "D115"
shortcut: "vblme"
username: "JoramSoch"
---


**Definition:** Let $m$ be a [generative model](/D/gm) with model parameters $\theta$ implying the [likelihood function](/D/lf) $p(y \vert \theta, m)$. Moreover, assume a [prior distribution](/D/prior) $p(\theta \vert m)$, a resulting [posterior distribution](/D/post) $p(\theta \vert y, m)$ and an [approximate](/D/vb) [posterior distribution](/D/post) $q(\theta)$. Then, the [Variational Bayesian](/D/vb) [log model evidence](/D/lme) is the expectation of the [log-likelihood function](/D/llf) with respect to the approximate posterior, minus the [Kullback-Leibler divergence](/D/kl) between approximate posterior and true posterior distribution:

$$ \label{eq:vbLME}
\mathrm{vbLME}(m) = \mathcal{L}\left[q(\theta)\right] - \mathrm{KL}\left[q(\theta) || p(\theta \vert y)\right]
$$

where

$$ \label{eq:ELL}
\mathcal{L}\left[q(\theta)\right] = \int q(\theta) \log \frac{p(y,\theta|m)}{q(\theta)} \, \mathrm{d}\theta
$$

and

$$ \label{eq:KL}
\mathrm{KL}\left[q(\theta) || p(\theta \vert y)\right] = \int q(\theta) \log \frac{q(\theta)}{p(\theta|y,m)} \, \mathrm{d}\theta  \; .
$$