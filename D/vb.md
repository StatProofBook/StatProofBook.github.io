---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-04-29 07:15:00

title: "Variational Bayes"
chapter: "General Theorems"
section: "Bayesian statistics"
topic: "Bayesian inference"
definition: "Variational Bayes"

sources:
  - authors: "Wikipedia"
    year: 2021
    title: "Variational Bayesian methods"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-04-29"
    url: "https://en.wikipedia.org/wiki/Variational_Bayesian_methods#Evidence_lower_bound"
  - authors: "Penny W, Flandin G, Trujillo-Barreto N"
    year: 2007
    title: "Bayesian Comparison of Spatially Regularised General Linear Models"
    in: "Human Brain Mapping"
    pages: "vol. 28, pp. 275–293, eqs. 2-9"
    url: "https://onlinelibrary.wiley.com/doi/full/10.1002/hbm.20327"
    doi: "10.1002/hbm.20327"

def_id: "D150"
shortcut: "vb"
username: "JoramSoch"
---


**Definition:** Let $m$ be a [generative model](/D/gm) with model parameters $\theta$ and hyper-parameters $\lambda$ implying the [likelihood function](/D/lf) $p(y \vert \theta, \lambda, m)$ and [prior distribution](/D/prior) $p(\theta \vert \lambda, m)$. Then, an Empirical Bayes treatment of $m$, also referred to as "type II [maximum likelihood](/D/mle)" or "[evidence](/D/lme) approximation", consists in

<br>
1) evaluating the [marginal likelihood](/D/ml) of the model $m$

$$ \label{eq:ML}
p(y \vert \lambda, m) = \int p(y \vert \theta, \lambda, m) \, (\theta \vert \lambda, m) \, \mathrm{d}\theta \; ,
$$

<br>
2) maximizing the [log model evidence](/D/lme) with respect to $\lambda$

$$ \label{eq:EB}
\hat{\lambda} = \operatorname*{arg\,max}_{\lambda} \log p(y \vert \lambda, m)
$$

<br>
3) and using the [prior distribution](/D/prior) at this maximum

$$ \label{eq:prior-eb}
p(\theta \vert m) = p(\theta \vert \hat{\lambda}, m)
$$

for [Bayesian inference](/P/bayes-th), i.e. [obtaining the posterior distribution](/P/post-jl) and [computing the marginal likelihood](/P/ml-jl).