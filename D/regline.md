---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-10-27 07:30:00

title: "Regression line"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Simple linear regression"
definition: "Regression line"

sources:
  - authors: "Wikipedia"
    year: 2021
    title: "Simple linear regression"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-10-27"
    url: "https://en.wikipedia.org/wiki/Simple_linear_regression#Fitting_the_regression_line"

def_id: "D164"
shortcut: "regline"
username: "JoramSoch"
---


**Definition:** Let there be a [simple linear regression with independent observations](/D/slr) using dependent variable $y$ and independent variable $x$:

$$ \label{eq:slr}
y_i = \beta_0 + \beta_1 x_i + \varepsilon_i, \; \varepsilon_i \sim \mathcal{N}(0, \sigma^2) \; .
$$

Then, given some parameters $\beta_0, \beta_1 \in \mathbb{R}$, the set

$$ \label{eq:regline}
L(\beta_0, \beta_1) = \left\lbrace (x,y) \in \mathbb{R}^2 \mid y = \beta_0 + \beta_1 x \right\rbrace
$$

is called a "regression line" and the set

$$ \label{eq:regline-ols}
L(\hat{\beta}_0, \hat{\beta}_1)
$$

is called the "fitted regression line", with estimated regression coefficients $\hat{\beta}_0, \hat{\beta}_1$, e.g. obtained via [ordinary least squares](/P/slr-ols).