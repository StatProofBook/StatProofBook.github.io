---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-05-05 04:59:00

title: "Marginal likelihood is a definite integral of joint likelihood"
chapter: "General Theorems"
section: "Bayesian statistics"
topic: "Probabilistic modeling"
theorem: "Marginal likelihood is integral of joint likelihood"

sources:

proof_id: "P91"
shortcut: "ml-jl"
username: "JoramSoch"
---


**Theorem:** In a [full probability model](/D/fpm) $m$ describing measured data $y$ using model parameters $\theta$, the [marginal likelihood](/D/ml) is the integral of the [joint likelihood](/D/jl) across the parameter space $\Theta$:

$$ \label{eq:ml}
p(y|m) = \int_{\Theta} p(y,\theta|m) \, \mathrm{d}\theta \; .
$$


**Proof:** In a [full probability model](/D/fpm), the [marginal likelihood](/D/ml) is defined as the [marginal probability](/D/prob-marg) of the data $y$, given only the model $m$:

$$ \label{eq:ml-def}
p(y|m) \; .
$$

Using the [law of marginal probabililty](/D/prob-marg), this can be obtained by integrating the [joint likelihood](/D/jl) function over the entire parameter space:

$$ \label{eq:ml-qed}
p(y|m) = \int_{\Theta} p(y,\theta|m) \, \mathrm{d}\theta \; .
$$

Applying the [law of conditional probability](/D/prob-cond), the integrand can also be written as the product of [likelihood function](/D/lf) and [prior density](/D/prior):

$$ \label{eq:ml-int}
p(y|m) = \int_{\Theta} p(y|\theta,m) \, p(\theta|m) \, \mathrm{d}\theta \; .
$$
