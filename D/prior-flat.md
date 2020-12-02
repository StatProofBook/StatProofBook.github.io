---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-12-02 17:04:00

title: "Flat, hard and soft prior distribution"
chapter: "General Theorems"
section: "Bayesian statistics"
topic: "Prior distributions"
definition: "Flat vs. hard vs. soft"

sources:
  - authors: "Friston et al."
    year: 2002
    title: "Classical and Bayesian Inference in Neuroimaging: Theory"
    in: "NeuroImage"
    pages: "vol. 16, iss. 2, pp. 465-483, fn. 1"
    url: "https://www.sciencedirect.com/science/article/pii/S1053811902910906"
    doi: "10.1006/nimg.2002.1090"
  - authors: "Friston et al."
    year: 2002
    title: "Classical and Bayesian Inference in Neuroimaging: Applications"
    in: "NeuroImage"
    pages: "vol. 16, iss. 2, pp. 484-512, fn. 10"
    url: "https://www.sciencedirect.com/science/article/pii/S1053811902910918"
    doi: "10.1006/nimg.2002.1091"

def_id: "D116"
shortcut: "prior-flat"
username: "JoramSoch"
---


**Definition:** Let $p(\theta \vert m)$ be a [prior distribution](/D/prior) for the parameter $\theta$ of a [generative model](/D/gm) $m$. Then,

* the distribution is called a "flat prior", if its [precision](/D/prec) is zero or [variance](/D/var) is infinite;

* the distribution is called a "hard prior", if its [precision](/D/prec) is infinite or [variance](/D/var) is zero;

* the distribution is called a "soft prior", if its [precision](/D/prec) and [variance](/D/var) are non-zero and finite.