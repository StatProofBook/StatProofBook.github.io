---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-03-21 20:09:00

title: "Multiple linear regression"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Multiple linear regression"
definition: "Definition"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Linear regression"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-03-21"
    url: "https://en.wikipedia.org/wiki/Linear_regression#Simple_and_multiple_linear_regression"

def_id: "D36"
shortcut: "mlr"
username: "JoramSoch"
---


**Definition:** Let $y$ be an $n \times 1$ vector and let $X$ be an $n \times p$ matrix.

Then, a statement asserting a linear combination of $X$ into $y$

$$ \label{eq:mlr-model}
y = X\beta + \varepsilon \; ,
$$

together with a statement asserting a [normal distribution](/D/mvn) for $\varepsilon$

$$ \label{eq:mlr-noise}
\varepsilon \sim \mathcal{N}(0, \sigma^2 V)
$$

is called a univariate linear regression model or simply, "multiple linear regression".

* $y$ is called "measured data", "dependent variable" or "measurements";

* $X$ is called "design matrix", "set of independent variables" or "predictors";

* $V$ is called "covariance matrix" or "covariance structure";

* $\beta$ are called "regression coefficients" or "weights";

* $\varepsilon$ is called "noise", "errors" or "error terms";

* $\sigma^2$ is called "noise variance" or "error variance";

* $n$ is the number of observations;

* $p$ is the number of predictors.

Alternatively, the linear combination may also be written as

$$ \label{eq:mlr-model-sum}
y = \sum_{i=1}^{p} \beta_i x_i + \varepsilon
$$

or, when the model includes an intercept term, as

$$ \label{eq:mlr-model-sum-base}
y = \beta_0 + \sum_{i=1}^{p} \beta_i x_i + \varepsilon
$$

which is equivalent to adding a constant regressor $x_0 = 1_n$ to the design matrix $X$.

When the covariance structure $V$ is equal to the $n \times n$ identity matrix, this is called multiple linear regression with independent and identically distributed (i.i.d.) observations:

$$ \label{eq:mlr-noise-iid}
V = I_n \quad \Rightarrow \quad \varepsilon \sim \mathcal{N}(0, \sigma^2 I_n) \quad \Rightarrow \quad \varepsilon_i \overset{\text{i.i.d.}}{\sim} \mathcal{N}(0, \sigma^2) \; .
$$

Otherwise, it is called multiple linear regression with correlated observations.