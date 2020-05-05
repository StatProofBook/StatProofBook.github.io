---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-05-05 04:46:00

title: "Posterior density is proportional to joint likelihood"
chapter: "General Theorems"
section: "Bayesian statistics"
topic: "Probabilistic modeling"
theorem: "Posterior density is proportional to joint likelihood"

sources:

proof_id: "P90"
shortcut: "post-jl"
username: "JoramSoch"
---


**Theorem:** In a [full probability model](/D/fpm) $m$ describing measured data $y$ using model parameters $\theta$, the [posterior density](/D/post) over the model parameters is proportional to the [joint likelihood](/D/jl):

$$ \label{eq:post}
p(\theta|y,m) \propto p(y,\theta|m) \; .
$$


**Proof:** In a [full probability model](/D/fpm), the [posterior distribution](/D/post) can be expressed using [Bayes' theorem](/P/bayes-th):

$$ \label{eq:post-s1}
p(\theta|y,m) = \frac{p(y|\theta,m) \, p(\theta|m)}{p(y|m)} \; .
$$

Applying the [law of conditional probability](/D/prob-cond) to the numerator, we have:

$$ \label{eq:post-s2}
p(\theta|y,m) = \frac{p(y,\theta|m)}{p(y|m)} \; .
$$

Because the denominator does not depend on $\theta$, it is constant in $\theta$ and thus acts a proportionality factor between the posterior distribution and the joint likelihood:

$$ \label{eq:post-qed}
p(\theta|y,m) \propto p(y,\theta|m) \; .
$$