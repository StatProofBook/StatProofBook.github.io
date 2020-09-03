---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-03-03 16:36:00

title: "Joint likelihood"
chapter: "General Theorems"
section: "Bayesian statistics"
topic: "Probabilistic modeling"
definition: "Joint likelihood"

sources:

def_id: "D31"
shortcut: "jl"
username: "JoramSoch"
---


**Definition:** Let there be a [generative model](/D/gm) $m$ describing measured data $y$ using model parameters $\theta$ and a [prior distribution](/D/prior) on $\theta$. Then, the [joint probability](/D/prob-joint) [density function](/D/pdf) of $y$ and $\theta$ is called the joint likelihood:

$$ \label{eq:jl}
p(y,\theta|m) = p(y|\theta,m) \, p(\theta|m) \; .
$$