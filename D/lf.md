---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-03-03 15:50:00

title: "Likelihood function"
chapter: "General Theorems"
section: "Frequentist statistics"
topic: "Likelihood theory"
definition: "Likelihood function"

sources:

def_id: "D28"
shortcut: "lf"
username: "JoramSoch"
---


**Definition:** Let there be a [generative model](/D/gm) $m$ describing measured data $y$ using model parameters $\theta$. Then, the [probability density function](/D/pdf) of the distribution of $y$ given $\theta$ is called the likelihood function of $m$:

$$ \label{eq:lf}
\mathcal{L}_m(\theta) = p(y|\theta,m) = \mathcal{D}(y; \theta) \; .
$$