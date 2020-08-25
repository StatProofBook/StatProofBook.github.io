---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-05-15 23:05:00

title: "Maximum likelihood estimation"
chapter: "General Theorems"
section: "Frequentist statistics"
topic: "Likelihood theory"
definition: "Maximum likelihood estimation"

sources:

def_id: "D60"
shortcut: "mle"
username: "JoramSoch"
---


**Definition:** Let there be a [generative model](/D/gm) $m$ describing measured data $y$ using model parameters $\theta$. Then, the parameter values maximizing the [likelihood function](/D/lf) or [log-likelihood function](/D/llf) are called maximum likelihood estimates of $\theta$:

$$ \label{eq:mle}
\hat{\theta} = \operatorname*{arg\,max}_\theta \mathcal{L}_m(\theta) = \operatorname*{arg\,max}_\theta \mathrm{LL}_m(\theta) \; .
$$

The process of calculating $\hat{\theta}$ is called "maximum likelihood estimation" and the functional form leading from $y$ to $\hat{\theta}$ given $m$ is called "maximum likelihood estimator". Maximum likelihood estimation, estimator and estimates may all be abbreviated as "MLE".