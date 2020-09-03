---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-03-03 16:43:00

title: "Posterior distribution"
chapter: "General Theorems"
section: "Bayesian statistics"
topic: "Probabilistic modeling"
definition: "Posterior distribution"

sources:

def_id: "D32"
shortcut: "post"
username: "JoramSoch"
---


**Definition:** Consider measured data $y$ and some unknown latent parameters $\theta$. The distribution of $\theta$ conditional on $y$ is called the posterior distribution:

$$ \label{eq:post}
\theta|y \sim \mathcal{D}(\phi) \; .
$$

The parameters $\phi$ of this distribution are called the posterior hyperparameters and the [probability density function](/D/pdf) is called the posterior density:

$$ \label{eq:prior-pdf}
p(\theta|y,m) = \mathcal{D}(\theta; \phi) \; .
$$