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


**Definition:** Let $m$ be a [generative model](/D/gm) with model parameters $\theta$ implying the [likelihood function](/D/lf) $p(y \vert \theta, m)$ and [prior distribution](/D/prior) $p(\theta \vert m)$. Then, a Variational Bayes treatment of $m$, also referred to as "approximate inference" or "variational inference", consists in

<br>
1) constructing an approximate [posterior distribution](/D/post)

$$ \label{eq:post-vb}
q(\theta) \approx p(\theta \vert y, m) \; ,
$$

<br>
2) evaluating the [variational free energy](/D/vblme)

$$ \label{eq:FE}
F_q(m) = \int q(\theta) \log p(y|\theta,m) \, \mathrm{d}\theta - \int q(\theta) \frac{q(\theta)}{p(\theta|m)} \, \mathrm{d}\theta
$$

<br>
3) and maximizing this function with respect to $q(\theta)$

$$ \label{eq:VB}
\hat{q}(\theta) = \operatorname*{arg\,max}_{q} F_q(m) \; .
$$

for Bayesian inference, i.e. obtaining the posterior distribution (from eq. \eqref{eq:VB}) and approximating the marginal likelihood (by plugging eq. \eqref{eq:VB} into eq. \eqref{eq:FE}).