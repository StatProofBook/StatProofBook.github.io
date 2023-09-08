---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-03-03 15:50:00

title: "Generative model"
chapter: "General Theorems"
section: "Bayesian statistics"
topic: "Probabilistic modeling"
definition: "Generative model"

sources:
  - authors: "Friston et al."
    year: 2008
    title: "Bayesian decoding of brain images"
    in: "NeuroImage"
    pages: "vol. 39, pp. 181-205"
    url: "https://www.sciencedirect.com/science/article/abs/pii/S1053811907007203"
    doi: "10.1016/j.neuroimage.2007.08.013"

def_id: "D27"
shortcut: "gm"
username: "JoramSoch"
---


**Definition:** Consider measured [data](/D/data) $y$ and some unknown latent [parameters](/D/para) $\theta$. A statement about the [distribution](/D/dist) of $y$ given $\theta$ is called a generative model $m$

$$ \label{eq:gm}
m: \, y \sim \mathcal{D}(\theta) \; ,
$$

where $\mathcal{D}$ denotes an arbitrary [probability distribution](/D/dist) and $\theta$ are the parameters of this distribution.