---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2025-06-20 14:46:00

title: "Multivariate normally distributed data"
chapter: "Statistical Models"
section: "Multivariate normal data"
topic: "Multivariate Gaussian"
definition: "Multivariate normally distributed data"

sources:

def_id: "D223"
shortcut: "mvn-data"
username: "JoramSoch"
---


**Definition:** Multivariate normally distributed data are defined as a set of $p$-dimensional vectors $y = \left\lbrace y_1, \ldots, y_n \right\rbrace$ with $y_i \in \mathbb{R}^p, \; i = 1,\ldots,n$, [independent and identically distributed](/D/iid) according to a [multivariate normal distribution](/D/mvn) with mean vector $\mu \in \mathbb{R}^p$ and covariance matrix $\Sigma \in \mathbb{R}^{p \times p}$

$$ \label{eq:mvn}
y_i \sim \mathcal{N}(\mu, \Sigma), \quad i = 1, \ldots, n
$$

where $\mu$ is a $p$-dimensional real vector and $\Sigma$ is a $p \times p$ positive-definite matrix.