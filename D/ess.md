---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-03-21 21:57:00

title: "Explained sum of squares"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Multiple linear regression"
definition: "Explained sum of squares"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Explained sum of squares"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-03-21"
    url: "https://en.wikipedia.org/wiki/Explained_sum_of_squares"

def_id: "D38"
shortcut: "ess"
username: "JoramSoch"
---


**Definition:** Let there be a [multiple linear regression with independent observations](/D/mlr) using measured data $y$ and design matrix $X$:

$$ \label{eq:mlr}
y = X\beta + \varepsilon, \; \varepsilon_i \overset{\mathrm{i.i.d.}}{\sim} \mathcal{N}(0, \sigma^2) \; .
$$

Then, the explained sum of squares (ESS) is defined as the sum of squared deviations of the fitted signal from the average signal:

$$ \label{eq:ess}
\mathrm{ESS} = \sum_{i=1}^n (\hat{y}_i - \bar{y})^2 \quad \text{where} \quad \hat{y} = X \hat{\beta} \quad \text{and} \quad \bar{y} = \frac{1}{n} \sum_{i=1}^n y_i
$$

with estimated regression coefficients $\hat{\beta}$, e.g. obtained via [ordinary least squares](/P/mlr-ols).