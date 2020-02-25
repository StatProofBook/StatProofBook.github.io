---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-02-25 11:41:00

title: "Coefficient of determination"
chapter: "Model Selection"
section: "Goodness-of-fit measures"
topic: "R-squared"
definition: "Definition"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Coefficient of determination"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-02-25"
    url: "https://en.wikipedia.org/wiki/Mean_squared_error#Proof_of_variance_and_bias_relationship"

def_id: "D21"
shortcut: "rsq"
username: "JoramSoch"
---


**Definition:** Let there be a [linear regression model](/D/mlr) with [independent](/D/ind) observations

$$ \label{eq:mlr}
y = X\beta + \varepsilon, \; \varepsilon_i \overset{\mathrm{i.i.d.}}{\sim} \mathcal{N}(0, \sigma^2)
$$

with measured data $y$, known design matrix $X$ as well as unknown regression coefficients $\beta$ and noise variance $\sigma^2$.

Then, the proportion of the variance of the dependent variable $y$ ("[total variance](/D/tss)") that can be predicted from the independent variables $X$ ("[explained variance](/D/ess)") is called "coefficient of determination", "R-squared" or $R^2$.