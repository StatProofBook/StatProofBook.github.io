---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2023-09-22 10:56:27

title: "Bivariate normal distribution"
chapter: "Probability Distributions"
section: "Multivariate continuous distributions"
topic: "Multivariate normal distribution"
definition: "Bivariate normal distribution"

sources:
  - authors: "Wikipedia"
    year: 2023
    title: "Multivariate normal distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2023-09-22"
    url: "https://en.wikipedia.org/wiki/Multivariate_normal_distribution#Bivariate_case"

def_id: "D189"
shortcut: "bvn"
username: "JoramSoch"
---


**Definition:** Let $X$ be an $2 \times 1$ [random vector](/D/rvec). Then, $X$ is said to have a bivariate normal distribution, if $X$ follows a [multivariate normal distribution](/D/mvn)

$$ \label{eq:mvn}
X \sim \mathcal{N}(\mu, \Sigma)
$$

with [means](/D/mean) $x_1$ and $x_2$, [variances](/D/var) $\sigma_1^2$ and $\sigma_2^2$ and [covariance](/D/cov) $\sigma_{12}$:

$$ \label{eq:bvn}
\mu = \left[ \begin{matrix} x_1 \\ x_2 \end{matrix} \right] \quad \text{and} \quad \Sigma = \left[ \begin{matrix} \sigma_1^2 & \sigma_{12} \\ \sigma_{12} & \sigma_2^2 \end{matrix} \right] \; .
$$
