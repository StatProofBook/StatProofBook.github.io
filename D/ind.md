---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-06-06 07:16:00

title: "Statistical independence"
chapter: "General Theorems"
section: "Probability theory"
topic: "Probability"
definition: "Statistical independence"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Independence (probability theory)"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-06-06"
    url: "https://en.wikipedia.org/wiki/Independence_(probability_theory)#Definition"

def_id: "D75"
shortcut: "ind"
username: "JoramSoch"
---


**Definition:** Generally speaking, [random variables](/D/rvar) are statistically independent, if their [joint probability](/D/prob-joint) can be expressed in terms of their [marginal probabilities](/D/prob-marg).

<br>
1) A set of discrete [random variables](/D/rvar) $X_1, \ldots, X_n$ with possible values $\mathcal{X}_1, \ldots, \mathcal{X}_n$ is called statistically independent, if

$$ \label{eq:disc-ind}
p(X_1 = x_1, \ldots, X_n = x_n) = \prod_{i=1}^{n} p(X_i = x_i) \quad \text{for all} \; x_i \in \mathcal{X}_i, \; i = 1, \ldots, n
$$

where $p(x_1, \ldots, x_n)$ are the [joint probabilities](/D/prob-joint) of $X_1, \ldots, X_n$ and $p(x_i)$ are the [marginal probabilities](/D/prob-marg) of $X_i$.

<br>
2) A set of continuous [random variables](/D/rvar) $X_1, \ldots, X_n$ defined on the domains $\mathcal{X}_1, \ldots, \mathcal{X}_n$ is called statistically independent, if

$$ \label{eq:cont-ind-F}
F_{X_1,\ldots,X_n}(x_1,\ldots,x_n) = \prod_{i=1}^{n} F_{X_i}(x_i) \quad \text{for all} \; x_i \in \mathcal{X}_i, \; i = 1, \ldots, n
$$

or equivalently, if the [probability densities](/D/pdf) exist, if

$$ \label{eq:cont-ind-f}
f_{X_1,\ldots,X_n}(x_1,\ldots,x_n) = \prod_{i=1}^{n} f_{X_i}(x_i) \quad \text{for all} \; x_i \in \mathcal{X}_i, \; i = 1, \ldots, n
$$

where $F$ are the [joint](/D/dist-joint) or [marginal](/D/dist-marg) [cumulative distribution functions](/D/cdf) and $f$ are the respective [probability density functions](/D/pdf).