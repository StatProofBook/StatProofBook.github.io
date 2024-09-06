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
  - authors: "Gelman A, Carlin JB, Stern HS, Dunson DB, Vehtari A, Rubin DB"
    year: 2014
    title: "Probability and inference"
    in: "Bayesian Data Analysis"
    pages: "ch. 1, p. 3"
    url: "http://www.stat.columbia.edu/~gelman/book/"

def_id: "D30"
shortcut: "fpm"
username: "JoramSoch"
---


**Definition:** Consider measured data $y$ and some unknown latent parameters $\theta$. The combination of a [generative model](/D/gm) for $y$ in terms of the parameters $\theta$ and a [prior distribution](/D/prior) on $\theta$ in terms of hyperparameters $\lambda$ is called a full probability model $m$:

$$ \label{eq:fpm}
m: \, y \sim \mathcal{D}_1(\theta), \, \theta \sim \mathcal{D}_1(\lambda) \; .
$$