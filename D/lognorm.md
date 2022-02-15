---
layout: definition
mathjax: true

author: "Maja Pavlovic"
affiliation: ""
e_mail: "mpavlovic@uw.co.uk"
date: 2022-02-12 19:30:00

title: "Log-normal distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Log-normal distribution"
definition: "Definition"

sources:
  - authors: "Wikipedia"
    year: 2022
    title: "Log-normal distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2022-02-07"
    url: "https://en.wikipedia.org/wiki/Log-normal_distribution"

def_id: "D170"
shortcut: "lognorm"
username: "majapavlo"
---


**Definition:** Let $\ln X$ be a [random variable](/D/rvar) following a [normal distribution](/D/norm) with mean $\mu$ and variance $\sigma^2$ (or, standard deviation $\sigma$):

$$ \label{eq:norm}
Y = \ln (X) \sim \mathcal{N}(\mu, \sigma^2) \; .
$$

Then, the exponential function of $Y$ is said to have a log-normal distribution with location parameter $\mu$ and scale parameter $\sigma$

$$ \label{eq:lognorm}
\begin{split} 
X = \mathrm{exp}(Y) \sim \ln \mathcal{N}(\mu, \sigma^2)
\end{split}
$$

where $\mu \in \mathbb{R}$ and $\sigma^2 > 0$.