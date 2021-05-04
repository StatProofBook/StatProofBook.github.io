---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-04-29 06:46:00

title: "Empirical Bayes"
chapter: "General Theorems"
section: "Bayesian statistics"
topic: "Bayesian inference"
definition: "Empirical Bayes"

sources:
  - authors: "Wikipedia"
    year: 2021
    title: "Empirical Bayes method"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-04-29"
    url: "https://en.wikipedia.org/wiki/Empirical_Bayes_method#Introduction"
  - authors: "Bishop CM"
    year: 2006
    title: "The Evidence Approximation"
    in: "Pattern Recognition for Machine Learning"
    pages: "ch. 3.5, pp. 165-172"
    url: "https://www.springer.com/gp/book/9780387310732"

def_id: "D149"
shortcut: "eb"
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