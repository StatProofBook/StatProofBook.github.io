---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-11-19 05:40:00

title: "Conditional independence"
chapter: "General Theorems"
section: "Probability theory"
topic: "Probability"
definition: "Conditional independence"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Conditional independence"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-11-19"
    url: "https://en.wikipedia.org/wiki/Conditional_independence#Conditional_independence_of_random_variables"

def_id: "D112"
shortcut: "ind-cond"
username: "JoramSoch"
---


**Definition:** Generally speaking, [random variables](/D/rvar) are conditionally independent given another random variable, if they are [statistically independent](/D/ind) in their [conditional probability distributions](/D/dist-cond) given this random variable.

<br>
1) A set of [discrete random variables](/D/rvar-disc) $X_1, \ldots, X_n$ with possible values $\mathcal{X}_1, \ldots, \mathcal{X}_n$ is called conditionally independent given the random variable $Y$ with possible values $\mathcal{Y}$, if

$$ \label{eq:disc-ind}
p(X_1 = x_1, \ldots, X_n = x_n|Y = y) = \prod_{i=1}^{n} p(X_i = x_i|Y = y) \quad \text{for all} \; x_i \in \mathcal{X}_i \quad \text{and all} \; y \in \mathcal{Y}
$$

where $p(x_1, \ldots, x_n \vert y)$ are the [joint (conditional) probabilities](/D/prob-joint) of $X_1, \ldots, X_n$ given $Y$ and $p(x_i)$ are the [marginal (conditional) probabilities](/D/prob-marg) of $X_i$ given $Y$.

<br>
2) A set of [continuous random variables](/D/rvar-disc) $X_1, \ldots, X_n$ with possible values $\mathcal{X}_1, \ldots, \mathcal{X}_n$ is called conditionally independent given the random variable $Y$ with possible values $\mathcal{Y}$, if

$$ \label{eq:cond-ind-F}
F_{X_1,\ldots,X_n|Y=y}(x_1,\ldots,x_n) = \prod_{i=1}^{n} F_{X_i|Y=y}(x_i) \quad \text{for all} \; x_i \in \mathcal{X}_i \quad \text{and all} \; y \in \mathcal{Y}
$$

or equivalently, if the [probability densities](/D/pdf) exist, if

$$ \label{eq:cont-ind-f}
f_{X_1,\ldots,X_n|Y=y}(x_1,\ldots,x_n) = \prod_{i=1}^{n} f_{X_i|Y=y}(x_i) \quad \text{for all} \; x_i \in \mathcal{X}_i \quad \text{and all} \; y \in \mathcal{Y}
$$

where $F$ are the [joint (conditional)](/D/dist-joint) or [marginal (conditional)](/D/dist-marg) [cumulative distribution functions](/D/cdf) and $f$ are the respective [probability density functions](/D/pdf).