---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-01-27 15:23:00

title: "Probability density function of the multivariate normal distribution"
chapter: "Probability Distributions"
section: "Multivariate continuous distributions"
topic: "Multivariate normal distribution"
theorem: "Probability density function"

sources:

proof_id: "P34"
shortcut: "mvn-pdf"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random vector](/D/rvec) following a [multivariate normal distribution](/D/mvn):

$$ \label{eq:mvn}
X \sim \mathcal{N}(\mu, \Sigma) \; .
$$

Then, the [probability density function](/D/pdf) of $X$ is

$$ \label{eq:mvn-pdf}
f_X(x) = \frac{1}{\sqrt{(2 \pi)^n |\Sigma|}} \cdot \exp \left[ -\frac{1}{2} (x-\mu)^\mathrm{T} \Sigma^{-1} (x-\mu) \right] \; .
$$


**Proof:** This follows directly from the [definition of the multivariate normal distribution](/D/mvn).