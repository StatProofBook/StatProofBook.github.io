---
layout: definition
mathjax: true

author: "Thomas J. Faulkenberry"
affiliation: "Tarleton State University"
e_mail: "faulkenberry@tarleton.edu"
date: 2020-09-02 12:00:00

title: "Encompassing model"
chapter: "Model Selection"
section: "Bayesian model selection"
topic: "Bayes factor"
definition: "Encompassing model"

sources:
  - authors: "Klugkist, I., Kato, B., and Hoijtink, H."
    year: 2005
    title: "Bayesian model selection using encompassing priors"
    in: "Statistica Neerlandica"
    pages: "vol. 59, no. 1, pp. 57-69"
    url: "https://dx.doi.org/10.1111/j.1467-9574.2005.00279.x"
    doi: "10.1111/j.1467-9574.2005.00279.x"

def_id: "D93"
shortcut: "encm"
username: "tomfaulkenberry"
---


**Definition:** Consider a family $f$ of [generative models](/D/gm) $m$ on data $y$, where each $m \in f$ is defined by placing an inequality constraint on model parameter(s) $\theta$ (e.g., $m:\theta>0$). Then the encompassing model $m_e$ is constructed such that each $m$ is nested within $m_e$ and all inequality constraints on the parameter(s) $\theta$ are removed.
