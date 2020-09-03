---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-05-17 22:52:00

title: "Log-likelihood function"
chapter: "General Theorems"
section: "Frequentist statistics"
topic: "Likelihood theory"
definition: "Log-likelihood function"

sources:

def_id: "D59"
shortcut: "llf"
username: "JoramSoch"
---


**Definition:** Let there be a [generative model](/D/gm) $m$ describing measured data $y$ using model parameters $\theta$. Then, the logarithm of the [probability density function](/D/pdf) of the distribution of $y$ given $\theta$ is called the log-[likelihood function](/D/lf) of $m$:

$$ \label{eq:llf}
\mathrm{LL}_m(\theta) = \log p(y|\theta,m) = \log \mathcal{D}(y; \theta) \; .
$$