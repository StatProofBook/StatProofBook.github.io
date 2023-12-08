---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2023-12-01 14:32:38

title: "Maximum-a-posteriori estimation"
chapter: "General Theorems"
section: "Bayesian statistics"
topic: "Probabilistic modeling"
definition: "Maximum-a-posteriori estimation"

sources:
  - authors: "Wikipedia"
    year: 2023
    title: "Maximum a posteriori estimation"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2023-12-01"
    url: "https://en.wikipedia.org/wiki/Maximum_a_posteriori_estimation#Description"

def_id: "D191"
shortcut: "map"
username: "JoramSoch"
---


**Definition:** Consider a [posterior distribution](/D/post) of an unknown parameter $\theta$, given measured data $y$, parametrized by posterior hyperparameters $\phi$:

$$ \label{eq:post}
\theta|y \sim \mathcal{D}(\phi) \; .
$$

Then, the value of $\theta$ at which the [posterior density](/D/post) attains its maximum is called the "maximum-a-posteriori estimate", "MAP estimate" or "posterior mode" of $\theta$:

$$ \label{eq:prior-pdf}
\hat{\theta}_\mathrm{MAP} = \operatorname*{arg\,max}_\theta \mathcal{D}(\theta; \phi) \; .
$$