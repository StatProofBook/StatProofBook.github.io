---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-11-25 07:43:00

title: "Empirical Bayesian log model evidence"
chapter: "Model Selection"
section: "Bayesian model selection"
topic: "Log model evidence"
definition: "Empirical Bayesian log model evidence"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Empirical Bayes method"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-11-25"
    url: "https://en.wikipedia.org/wiki/Empirical_Bayes_method#Introduction"
  - authors: "Penny, W.D. and Ridgway, G.R."
    year: 2013
    title: "Efficient Posterior Probability Mapping Using Savage-Dickey Ratios"
    in: "PLoS ONE"
    pages: "vol. 8, iss. 3, art. e59655, eqs. 7/11"
    url: "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0059655"
    doi: "10.1371/journal.pone.0059655"

def_id: "D114"
shortcut: "eblme"
username: "JoramSoch"
---


**Definition:** Let $m$ be a [generative model](/D/gm) with model parameters $\theta$ and hyper-parameters $\lambda$ implying the [likelihood function](/D/lf) $p(y \vert \theta, \lambda, m)$ and [prior distribution](/D/prior) $p(\theta \vert \lambda, m)$. Then, the [Empirical Bayesian](/D/eb) [log model evidence](/D/lme) is the logarithm of the [marginal likelihood](/D/ml), maximized with respect to the hyper-parameters:

$$ \label{eq:ebLME}
\mathrm{ebLME}(m) = \log p(y \vert \hat{\lambda}, m)
$$

where

$$ \label{eq:ML}
p(y \vert \lambda, m) = \int p(y \vert \theta, \lambda, m) \, (\theta \vert \lambda, m) \, \mathrm{d}\theta
$$

[and](/D/prior-eb)

$$ \label{eq:EB}
\hat{\lambda} = \operatorname*{arg\,max}_{\lambda} \log p(y \vert \lambda, m) \; .
$$