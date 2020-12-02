---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-12-02 17:28:00

title: "Informative and non-informative prior distribution"
chapter: "General Theorems"
section: "Bayesian statistics"
topic: "Prior distributions"
definition: "Informative vs. non-informative"

sources:
  - authors: "Soch J, Allefeld C, Haynes JD"
    year: 2016
    title: "How to avoid mismodelling in GLM-based fMRI data analysis: cross-validated Bayesian model selection"
    in: "NeuroImage"
    pages: "vol. 141, pp. 469-489, eq. 15, p. 473"
    url: "https://www.sciencedirect.com/science/article/pii/S1053811916303615"
    doi: "10.1016/j.neuroimage.2016.07.047"

def_id: "D118"
shortcut: "prior-inf"
username: "JoramSoch"
---


**Definition:** Let $p(\theta \vert m)$ be a [prior distribution](/D/prior) for the parameter $\theta$ of a [generative model](/D/gm) $m$. Then,

* the distribution is called an "informative prior", if it biases the parameter towards particular values;

* the distribution is called a "weakly informative prior", if it mildly [influences the posterior distribution](/P/post-jl);

* the distribution is called a "non-informative prior", if it does not [influence](/P/post-jl) the [posterior hyperparameters](/D/post).