---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2024-11-08 10:53:01

title: "Biased vs. unbiased estimator"
chapter: "General Theorems"
section: "Estimation theory"
topic: "Basic concepts of estimation"
definition: "Biased vs. unbiased"

sources:
  - authors: "Wikipedia"
    year: 2024
    title: "Estimator"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2024-11-08"
    url: "https://en.wikipedia.org/wiki/Estimator#Bias"

def_id: "D209"
shortcut: "est-bias"
username: "JoramSoch"
---


**Definition:** Let $\hat{\theta}: \mathcal{Y} \rightarrow \Theta$ be an [estimator](/D/est) of a [parameter](/D/para) $\theta \in \Theta$ from [data](/D/data) $y \in \mathcal{Y}$. Then,

* $\hat{\theta}$ is called an unbiased estimator when its [expected value](/D/mean) is equal to the parameter that it is estimating: $\mathrm{E}_{\hat{\theta}}(\hat{\theta}) = \theta$, where the expectation is calculated over all possible samples $y$ leading to values of $\hat{\theta}$.

* $\hat{\theta}$ is called a biased estimator otherwise, i.e. when $\mathrm{E}_{\hat{\theta}}(\hat{\theta}) \neq \theta$.