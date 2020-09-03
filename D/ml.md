---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-03-03 16:49:00

title: "Marginal likelihood"
chapter: "General Theorems"
section: "Bayesian statistics"
topic: "Probabilistic modeling"
definition: "Marginal likelihood"

sources:

def_id: "D33"
shortcut: "ml"
username: "JoramSoch"
---


**Definition:** Let there be a [generative model](/D/gm) $m$ describing measured data $y$ using model parameters $\theta$ and a [prior distribution](/D/prior) on $\theta$. Then, the [marginal probability](/D/prob-marg) [density function](/D/pdf) of $y$ across the parameter space $\Theta$ is called the marginal likelihood:

$$ \label{eq:ml}
p(y|m) = \int_{\Theta} p(y|\theta,m) \, p(\theta|m) \, \mathrm{d}\theta \; .
$$