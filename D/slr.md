---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-10-27 07:07:00

title: "Simple linear regression"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Simple linear regression"
definition: "Definition"

sources:
  - authors: "Wikipedia"
    year: 2021
    title: "Simple linear regression"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-10-27"
    url: "https://en.wikipedia.org/wiki/Simple_linear_regression#Fitting_the_regression_line"

def_id: "D163"
shortcut: "slr"
username: "JoramSoch"
---


**Definition:** Let $y$ and $x$ be two $n \times 1$ vectors.

Then, a statement asserting a linear relationship between $x$ and $y$

$$ \label{eq:slr-model}
y = \beta_0 + \beta_1 x + \varepsilon \; ,
$$

together with a statement asserting a [normal distribution](/D/mvn) for $\varepsilon$

$$ \label{eq:slr-noise}
\varepsilon \sim \mathcal{N}(0, \sigma^2 V)
$$

is called a univariate simple regression model or simply, "simple linear regression".

* $y$ is called "dependent variable", "measured data" or "signal";

* $x$ is called "independent variable", "predictor" or "covariate";

* $V$ is called "covariance matrix" or "covariance structure";

* $\beta_1$ is called "slope of the [regression line](/D/regline)";

* $\beta_0$ is called "intercept of the [regression line](/D/regline)";

* $\varepsilon$ is called "noise", "errors" or "error terms";

* $\sigma^2$ is called "noise variance" or "error variance";

* $n$ is the number of observations.

When the covariance structure $V$ is equal to the $n \times n$ identity matrix, this is called simple linear regression with independent and identically distributed (i.i.d.) observations:

$$ \label{eq:mlr-noise-iid}
V = I_n \quad \Rightarrow \quad \varepsilon \sim \mathcal{N}(0, \sigma^2 I_n) \quad \Rightarrow \quad \varepsilon_i \overset{\text{i.i.d.}}{\sim} \mathcal{N}(0, \sigma^2) \; .
$$

In this case, the linear regression model can also be written as

$$ \label{eq:slr-model-sum}
y_i = \beta_0 + \beta_1 x_i + \varepsilon_i, \; \varepsilon_i \sim \mathcal{N}(0, \sigma^2) \; .
$$

Otherwise, it is called simple linear regression with correlated observations.