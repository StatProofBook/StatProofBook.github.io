---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2026-06-29 17:48:00

title: "Likeliest model frequency"
chapter: "Model Selection"
section: "Bayesian model selection"
topic: "Random-effects Bayesian model selection"
definition: "Likeliest frequencies"

sources:
  - authors: "Soch J, Allefeld C, Haynes JD"
    year: 2016
    title: "How to avoid mismodelling in GLM-based fMRI data analysis: cross-validated Bayesian model selection"
    in: "NeuroImage"
    pages: "vol. 141, pp. 469-489, p. 474"
    url: "https://www.sciencedirect.com/science/article/pii/S1053811916303615"
    doi: "10.1016/j.neuroimage.2016.07.047"

def_id: "D237"
shortcut: "likfreq"
username: "JoramSoch"
---


**Definition:** Let $p(y,m,r)$ with data sets $y = \left\lbrace y_1, \ldots, y_N \right\rbrace$, generative models $m \in \left\lbrace 0, 1 \right\rbrace^{N \times K}$ and model frequencies $r \in [0, 1]^K$ be the [joint likelihood function](/D/jl) of the [model](/D/fpm) specified by [random-effects Bayesian model selection](/D/bmsrfx) and let $p(r \vert y)$ be the [posterior distribution](/D/post) resulting from estimation of this model.

Then, the [posterior mode](/D/mode) of the $j$-th model frequency $r_j$ is called the likeliest frequency of model $j$:

$$ \label{eq:likfreq}
\mathrm{LF}_j = \mathrm{mode}_{p(r|y)}(r_j) \; .
$$