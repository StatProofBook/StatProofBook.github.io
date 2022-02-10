---
layout: definition
mathjax: true

author: "Maja Pavlovic"
affiliation: ""
e_mail: "mpavlovic@uw.co.uk"
date: 2022-02-07 22:33:00

title: "Lognormal distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Lognormal distribution"
definition: "Definition"

sources:
  - authors: "Wikipedia"
    year: 2022
    title: "Lognormal distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2022-02-07"
    url: "https://en.wikipedia.org/wiki/Log-normal_distribution"

def_id: "D170"
shortcut: "lognorm"
username: "majapavlo"
---


**Definition:** Let $X$ be a [random variable](/D/rvar). Then, $X$ is said to have a log normal distribution with location parameter $\mu$ and scale parameter $\sigma$

$$ \label{eq:lognorm}
X \sim \ln \mathcal{N}(\mu, \sigma^2) \; ,
$$

if and only if its [probability density function](/D/pdf) is given by

$$ \label{eq:lognorm-pdf}
f_X(x) = \frac{1}{x \sigma \sqrt{2 \pi} \sigma} \cdot \exp \left[ -\frac{\left( \ln x -\mu \right)^2}{2 \sigma^2} \right]
$$

where $\mu \in \mathbb{R}$ and $\sigma^2 > 0$.
