---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-03-03 16:09:00

title: "Prior distribution"
chapter: "General Theorems"
section: "Bayesian statistics"
topic: "Probabilistic modeling"
definition: "Prior distribution"

sources:

def_id: "D29"
shortcut: "prior"
username: "JoramSoch"
---


**Definition:** Consider measured data $y$ and some unknown latent parameters $\theta$. A distribution of $\theta$ unconditional on $y$ is called a prior distribution:

$$ \label{eq:prior}
\theta \sim \mathcal{D}(\lambda) \; .
$$

The parameters $\lambda$ of this distribution are called the prior hyperparameters and the [probability density function](/D/pdf) is called the prior density:

$$ \label{eq:prior-pdf}
p(\theta|m) = \mathcal{D}(\theta; \lambda) \; .
$$