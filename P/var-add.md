---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-07-07 06:52:00

title: "Additivity of the variance for independent random variables"
chapter: "General Theorems"
section: "Probability theory"
topic: "Variance"
theorem: "Additivity under independence"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Variance"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-07-07"
    url: "https://en.wikipedia.org/wiki/Variance#Basic_properties"

proof_id: "P130"
shortcut: "var-add"
username: "JoramSoch"
---


**Theorem:** The [variance](/D/var) is additive for [independent](/D/ind) [random variables](/D/rvar):

$$ \label{eq:var-add}
p(X,Y) = p(X) \, p(Y) \quad \Rightarrow \quad \mathrm{Var}(X+Y) = \mathrm{Var}(X) + \mathrm{Var}(Y) \; .
$$


**Proof:** The [variance of the sum of two random variables](/P/var-sum) is given by

$$ \label{eq:var-sum}
\mathrm{Var}(X+Y) = \mathrm{Var}(X) + \mathrm{Var}(Y) + 2 \, \mathrm{Cov}(X,Y) \; .
$$

The [covariance of independent random variables](/P/cov-ind) is zero:

$$ \label{eq:cov-ind}
p(X,Y) = p(X) \, p(Y) \quad \Rightarrow \quad \mathrm{Cov}(X,Y) = 0 \; .
$$

Combining \eqref{eq:var-sum} and \eqref{eq:cov-ind}, we have:

$$ \label{eq:var-add-qed}
\mathrm{Var}(X+Y) = \mathrm{Var}(X) + \mathrm{Var}(Y) \; .
$$