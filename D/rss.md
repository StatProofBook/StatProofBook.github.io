---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-03-21 22:03:00

title: "Residual sum of squares"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Multiple linear regression"
definition: "Residual sum of squares"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Residual sum of squares"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-03-21"
    url: "https://en.wikipedia.org/wiki/Residual_sum_of_squares"

def_id: "D39"
shortcut: "rss"
username: "JoramSoch"
---


**Definition:** Let there be a [multiple linear regression with independent observations](/D/mlr) using measured data $y$ and design matrix $X$:

$$ \label{eq:mlr}
y = X\beta + \varepsilon, \; \varepsilon_i \overset{\mathrm{i.i.d.}}{\sim} \mathcal{N}(0, \sigma^2) \; .
$$

Then, the residual sum of squares (RSS) is defined as the sum of squared deviations of the measured signal from the fitted signal:

$$ \label{eq:rss}
\mathrm{RSS} = \sum_{i=1}^n (y_i - \hat{y}_i)^2 \quad \text{where} \quad \hat{y} = X \hat{\beta}
$$

with estimated regression coefficients $\hat{\beta}$, e.g. obtained via [ordinary least squares](/P/mlr-ols).