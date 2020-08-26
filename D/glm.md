---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-03-21 22:24:00

title: "General linear model"
chapter: "Statistical Models"
section: "Multivariate normal data"
topic: "General linear model"
definition: "Definition"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "General linear model"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-03-21"
    url: "https://en.wikipedia.org/wiki/General_linear_model"

def_id: "D40"
shortcut: "glm"
username: "JoramSoch"
---


**Definition:** Let $Y$ be an $n \times v$ matrix and let $X$ be an $n \times p$ matrix. Then, a statement asserting a linear mapping from $X$ to $Y$ with parameters $B$ and [matrix-normally distributed](/D/matn) errors $E$

$$ \label{eq:glm}
Y = X B + E, \; E \sim \mathcal{MN}(0, V, \Sigma)
$$

is called a multivariate linear regression model or simply, "general linear model".

* $Y$ is called "data matrix", "set of dependent variables" or "measurements";

* $X$ is called "design matrix", "set of independent variables" or "predictors";

* $B$ are called "regression coefficients" or "weights";

* $E$ is called "noise matrix" or "error terms";

* $V$ is called "covariance across rows";

* $\Sigma$ is called "covariance across columns";

* $n$ is the number of observations;

* $v$ is the number of measurements;

* $p$ is the number of predictors.

When rows of $Y$ correspond to units of time, e.g. subsequent measurements, $V$ is called "temporal covariance". When columns of $Y$ correspond to units of space, e.g. measurement channels, $\Sigma$ is called "spatial covariance".

When the covariance matrix $V$ is a scalar multiple of the $n \times n$ identity matrix, this is called a general linear model with independent and identically distributed (i.i.d.) observations:

$$ \label{eq:glm-iid}
V = \lambda I_n \quad \Rightarrow \quad E \sim \mathcal{MN}(0, \lambda I_n, \Sigma) \quad \Rightarrow \quad \varepsilon_i \overset{\text{i.i.d.}}{\sim} \mathcal{N}(0, \lambda \Sigma) \; .
$$

Otherwise, it is called a general linear model with correlated observations.