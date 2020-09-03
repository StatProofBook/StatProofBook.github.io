---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-03-03 16:16:00

title: "Full probability model"
chapter: "General Theorems"
section: "Bayesian statistics"
topic: "Probabilistic modeling"
definition: "Full probability model"

sources:

def_id: "D30"
shortcut: "fpm"
username: "JoramSoch"
---


**Definition:** Consider measured data $y$ and some unknown latent parameters $\theta$. The combination of a [generative model](/D/gm) for $y$ and a [prior distribution](/D/prior) on $\theta$ is called a full probability model $m$:

$$ \label{eq:fpm}
m: \, y \sim \mathcal{D}(\theta), \, \theta \sim \mathcal{D}(\lambda) \; .
$$