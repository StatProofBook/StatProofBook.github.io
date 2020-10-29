---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-06-28 20:51:00

title: "Logistic regression"
chapter: "Statistical Models"
section: "Categorical data"
topic: "Logistic regression"
definition: "Definition"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Logistic regression"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-06-28"
    url: "https://en.wikipedia.org/wiki/Logistic_regression#Logistic_model"

def_id: "D76"
shortcut: "logreg"
username: "JoramSoch"
---


**Definition:** A logistic regression model is given by a set of binary observations $y_i \in \left\lbrace 0, 1 \right\rbrace, i = 1,\ldots,n$, a set of predictors $x_j \in \mathbb{R}^n, j = 1,\ldots,p$, a base $b$ and the assumption that the log-odds are a linear combination of the predictors:

$$ \label{eq:logreg}
l_i = x_i \beta + \varepsilon_i, \; i = 1,\ldots,n
$$

where $l_i$ are the log-odds that $y_i = 1$

$$ \label{eq:logodds}
l_i = \log_b \frac{\mathrm{Pr}(y_i = 1)}{\mathrm{Pr}(y_i = 0)}
$$

and $x_i$ is the $i$-th row of the $n \times p$ matrix

$$ \label{eq:X}
X = \left[ x_1, \ldots, x_p \right] \; .
$$

Within this model,

* $y$ are called "categorical observations" or "dependent variable";

* $X$ is called "design matrix" or "set of independent variables";

* $\beta$ are called "regression coefficients" or "weights";

* $\varepsilon_i$ is called "noise" or "error term";

* $n$ is the number of observations;

* $p$ is the number of predictors.