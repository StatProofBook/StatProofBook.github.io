---
layout: definition
mathjax: true

author: "Kenneth Petrykowski"
affiliation: "University of Warsaw"
e_mail: "kenneth.petrykowski@gmail.com"
date: 2026-10-28 22:01:12

title: "Posterior expected loss"
chapter: "General Theorems"
section: "Bayesian statistics"
topic: "Probabilistic modeling"
definition: "Posterior expected loss"

sources:
  - authors: "George Casella, Roger L. Berger"
    year: 2002
    title: "Loss function optimality"
    in: "Statistical Inference"
    pages: "Second edition, Section 7.3.4, pp. 352-353"

def_id: "D244"
shortcut: "post-loss"
username: "kjpetrykowski"
---

**Definition:** Let $X$ denote the data, $x$ their observed value, and $\Theta$ the set of possible values of the parameter $\theta$. For an action $a$, suppose its [loss](/D/loss-fct) $L(a,\theta)$ is a random variable under the [posterior distribution](/D/post) of $\theta$ given $x$. The posterior expected loss of $a$ is

$$ \label{eq:posterior-expected-loss}
\rho(a\mid x)=\mathrm{E}[L(a,\theta)\mid X=x] \; .
$$

This expectation averages over $\theta$, with $a$ and $x$ fixed. If the posterior has density $p(\theta\mid x)$, then

$$ \label{eq:posterior-loss-integral}
\rho(a\mid x)=\int_\Theta L(a,\theta)p(\theta\mid x)\,\mathrm{d}\theta \; .
$$

For a discrete parameter, multiply each loss $L(a,\theta)$ by the posterior probability of $\theta$ and sum over $\Theta$. The expectation may be infinite. An action that minimizes posterior expected loss is called a Bayes action for $x$.
