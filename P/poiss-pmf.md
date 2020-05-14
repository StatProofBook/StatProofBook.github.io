---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-05-14 20:39:00

title: "Probability mass function of the Poisson distribution"
chapter: "Probability Distributions"
section: "Univariate discrete distributions"
topic: "Poisson distribution"
theorem: "Probability mass function"

sources:

proof_id: "P102"
shortcut: "poiss-pmf"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [Poisson distribution](/D/poiss):

$$ \label{eq:Poiss}
X \sim \mathrm{Poiss}(\lambda) \; .
$$

Then, the [probability mass function](/D/pmf) of $X$ is

$$ \label{eq:Poiss-pmf}
f_X(x) = \frac{\lambda^x \, e^{-\lambda}}{x!}, \; x \in \mathbb{N}_0 \; .
$$


**Proof:** This follows directly from the [definition of the Poisson distribution](/D/poiss).