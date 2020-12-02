---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-12-02 17:37:00

title: "Empirical and theoretical prior distribution"
chapter: "General Theorems"
section: "Bayesian statistics"
topic: "Prior distributions"
definition: "Empirical vs. non-empirical"

sources:
  - authors: "Soch J, Allefeld C, Haynes JD"
    year: 2016
    title: "How to avoid mismodelling in GLM-based fMRI data analysis: cross-validated Bayesian model selection"
    in: "NeuroImage"
    pages: "vol. 141, pp. 469-489, eq. 13, p. 473"
    url: "https://www.sciencedirect.com/science/article/pii/S1053811916303615"
    doi: "10.1016/j.neuroimage.2016.07.047"

def_id: "D119"
shortcut: "prior-emp"
username: "JoramSoch"
---


**Definition:** Let $p(\theta \vert m)$ be a [prior distribution](/D/prior) for the parameter $\theta$ of a [generative model](/D/gm) $m$. Then,

* the distribution is called an "empirical prior", if it has been [derived from empirical data](/P/post-jl);

* the distribution is called a "theoretical prior", if it was specified without regard to empirical data.