---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-04-21 06:53:00

title: "Sample covariance"
chapter: "General Theorems"
section: "Probability theory"
topic: "Covariance"
definition: "Sample covariance"

sources:
  - authors: "Wikipedia"
    year: 2021
    title: "Sample mean and covariance"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-04-21"
    url: "https://en.wikipedia.org/wiki/Sample_mean_and_covariance#Definition_of_sample_covariance"

def_id: "D144"
shortcut: "cov-samp"
username: "JoramSoch"
---


**Definition:** Let $x = \left\lbrace x_1, \ldots, x_n \right\rbrace$ be a [sample](/D/samp) from a [random vector](/D/rvec) $X \in \mathbb{R}^{n \times 1}$. Then, the sample covariance matrix of $x$ is given by

$$ \label{eq:cov-samp}
\hat{\Sigma} = \frac{1}{n} \sum_{i=1}^{n} (x_i - \bar{x}) (x_i - \bar{x})^\mathrm{T}
$$

and the unbiased sample variance matrix of $x$ is given by

$$ \label{eq:cov-samp-unb}
S = \frac{1}{n} \sum_{i=1}^{n} (x_i - \bar{x}) (x_i - \bar{x})^\mathrm{T}
$$

where $\bar{x}$ is the [sample mean](/D/mean-samp).