---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-01-27 14:15:00

title: "Normal distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Normal distribution"
definition: "Definition"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Normal distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-01-27"
    url: "https://en.wikipedia.org/wiki/Normal_distribution"

def_id: "D4"
shortcut: "norm"
username: "JoramSoch"
---


**Definition:** Let $X$ be a [random variable](/D/rvar). Then, $X$ is said to be normally distributed with mean $\mu$ and variance $\sigma^2$ (or, standard deviation $\sigma$)

$$ \label{eq:norm}
X \sim \mathcal{N}(\mu, \sigma^2) \; ,
$$

if and only if its [probability density function](/D/pdf) is given by

$$ \label{eq:norm-pdf}
\mathcal{N}(x; \mu, \sigma^2) = \frac{1}{\sqrt{2 \pi} \sigma} \cdot \exp \left[ -\frac{1}{2} \left( \frac{x-\mu}{\sigma} \right)^2 \right]
$$

where $\mu \in \mathbb{R}$ and $\sigma^2 > 0$.