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
  - authors: "Bishop CM"
    year: 2006
    title: "Variational Inference"
    in: "Pattern Recognition for Machine Learning"
    pages: "ch. 10.1, pp. 462-474"
    url: "https://www.springer.com/gp/book/9780387310732"
  - authors: "Penny W, Flandin G, Trujillo-Barreto N"
    year: 2007
    title: "Bayesian Comparison of Spatially Regularised General Linear Models"
    in: "Human Brain Mapping"
    pages: "vol. 28, pp. 275–293, eqs. 2-9"
    url: "https://onlinelibrary.wiley.com/doi/full/10.1002/hbm.20327"
    doi: "10.1002/hbm.20327"
  - authors: "Ostwald D, Kirilina E, Starke L, Blankenburg F"
    year: 2014
    title: "A tutorial on variational Bayes for latent linear stochastic time-series models"
    in: "Journal of Mathematical Psychology"
    pages: "vol. 60, pp. 1-14, eqs. 10-17"
    url: "https://www.sciencedirect.com/science/article/abs/pii/S0022249614000352"
    doi: "10.1016/j.jmp.2014.04.003"

def_id: "D150"
shortcut: "vb"
username: "JoramSoch"
---


**Definition:** Let $m$ be a [generative model](/D/gm) with [model parameters](/D/para) $\theta \in \Theta$ implying the [likelihood function](/D/lf) $p(y \vert \theta, m)$ and [prior distribution](/D/prior) $p(\theta \vert m)$. Then, a Variational Bayes treatment of $m$, also referred to as "approximate inference" or "variational inference", consists in

<br>
1) constructing an approximate [posterior distribution](/D/post)

$$ \label{eq:post-vb}
q(\theta) \approx p(\theta \vert y, m) \; ,
$$

<br>
2) evaluating the [variational free energy](/D/vblme)

$$ \label{eq:FE}
\mathrm{F}_m[q(\theta)] = \int_{\Theta} q(\theta) \log \frac{p(\theta \vert y, m)}{q(\theta)} \, \mathrm{d}\theta
$$

<br>
3) and maximizing this function with respect to $q(\theta)$

$$ \label{eq:VB}
\hat{q}(\theta) = \operatorname*{arg\,max}_{q} \mathrm{F}_m[q(\theta)]
$$

for [Bayesian inference](/P/bayes-th), i.e. obtaining the [posterior distribution](/D/post) (from eq. \eqref{eq:VB}) and approximating the [marginal likelihood](/D/ml) (by plugging eq. \eqref{eq:VB} into eq. \eqref{eq:FE}).