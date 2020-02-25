---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-02-25 11:21:00

title: "Residual variance"
chapter: "Model Selection"
section: "Goodness-of-fit measures"
topic: "Residual variance"
definition: "Definition"

sources:

def_id: "D20"
shortcut: "resvar"
username: "JoramSoch"
---


**Definition:** Let there be a [linear regression model](/D/mlr)

$$ \label{eq:mlr}
y = X\beta + \varepsilon, \; \varepsilon \sim \mathcal{N}(0, \sigma^2 V)
$$

with measured data $y$, known design matrix $X$ and covariance structure $V$ as well as unknown regression coefficients $\beta$ and noise variance $\sigma^2$.

Then, an estimate of the noise variance $\sigma^2$ is called the "residual variance" $\hat{\sigma}^2$, e.g. obtained via [maximum likelihood estimation](/D/mle).