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
topic: "Model evidence"
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


**Definition:** Let $m$ be a [generative model](/D/gm) with [model parameters](/D/para) $\theta \in \Theta$ implying the [likelihood function](/D/lf) $p(y \vert \theta, m)$ and [prior distribution](/D/prior) $p(\theta \vert m)$. Moreover, assume an [approximate](/D/vb) [posterior distribution](/D/post) $q(\theta)$. Then, the [Variational Bayesian](/D/vb) [log model evidence](/D/lme), also referred to as the "variational free energy", is defined as the expected logarithm of the likelihood function, divided by the approximate posterior:

$$ \label{eq:vbLME}
\mathrm{vbLME}(m) = \mathrm{F}_m[q(\theta)] = \int_{\Theta} q(\theta) \log \frac{p(\theta \vert y, m)}{q(\theta)} \, \mathrm{d}\theta \; .
$$

The variational free energy can be decomposed into the [difference between log model evidence and KL divergence of approximate from true posterior](/P/fren-dec) or, alternatively, as the [difference of expected log-likelihood and KL divergence of approximate posterior from prior](/P/fren-dec).