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