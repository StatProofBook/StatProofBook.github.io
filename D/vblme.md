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
  - authors: "Penny W, Flandin G, Trujillo-Barreto N"
    year: 2007
    title: "Bayesian Comparison of Spatially Regularised General Linear Models"
    in: "Human Brain Mapping"
    pages: "vol. 28, pp. 275–293, eqs. 2-9"
    url: "https://onlinelibrary.wiley.com/doi/full/10.1002/hbm.20327"
    doi: "10.1002/hbm.20327"

def_id: "D115"
shortcut: "vblme"
username: "JoramSoch"
---


**Definition:** Let $m$ be a [generative model](/D/gm) with model parameters $\theta$ implying the [likelihood function](/D/lf) $p(y \vert \theta, m)$ and [prior distribution](/D/prior) $p(\theta \vert m)$. Moreover, assume an [approximate](/D/vb) [posterior distribution](/D/post) $q(\theta)$. Then, the [Variational Bayesian](/D/vb) [log model evidence](/D/lme), also referred to as the "negative free energy", is the expectation of the [log-likelihood function](/D/llf) with respect to the approximate posterior, minus the [Kullback-Leibler divergence](/D/kl) between approximate posterior and the prior distribution:

$$ \label{eq:vbLME}
\mathrm{vbLME}(m) = \left\langle \log p(y \vert \theta, m) \right\rangle_{q(\theta)} - \mathrm{KL}\left[q(\theta) || p(\theta \vert m)\right]
$$

where

$$ \label{eq:ELL}
\left\langle \log p(y \vert \theta, m) \right\rangle_{q(\theta)} = \int q(\theta) \log p(y \vert \theta, m) \, \mathrm{d}\theta
$$

and

$$ \label{eq:KL}
\mathrm{KL}\left[q(\theta) || p(\theta \vert m)\right] = \int q(\theta) \log \frac{q(\theta)}{p(\theta \vert m)} \, \mathrm{d}\theta  \; .
$$
