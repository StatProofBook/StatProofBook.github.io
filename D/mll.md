---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-05-15 23:13:00

title: "Maximum log-likelihood"
chapter: "General Theorems"
section: "Frequentist statistics"
topic: "Likelihood theory"
definition: "Maximum log-likelihood"

sources:

def_id: "D61"
shortcut: "mll"
username: "JoramSoch"
---


**Definition:** Let there be a [generative model](/D/gm) $m$ describing measured data $y$ using model parameters $\theta$. Then, the maximum log-likelihood (MLL) of $m$ is the maximal value of the [log-likelihood function](/D/llf) of this model:

$$ \label{eq:mll}
\mathrm{MLL}(m) = \operatorname*{max}_\theta \mathrm{LL}_m(\theta) \; .
$$

The maximum log-likelihood can be obtained by plugging the [maximum likelihood estimates](/D/mle) into the [log-likelihood function](/D/llf).