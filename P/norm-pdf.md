---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-01-27 15:15:00

title: "Probability density function of the normal distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Normal distribution"
theorem: "Probability density function"

sources:

proof_id: "P33"
shortcut: "norm-pdf"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [normal distribution](/D/norm):

$$ \label{eq:norm}
X \sim \mathcal{N}(\mu, \sigma^2) \; .
$$

Then, the [probability density function](/D/pdf) of $X$ is

$$ \label{eq:norm-pdf}
f_X(x) = \frac{1}{\sqrt{2 \pi} \sigma} \cdot \exp \left[ -\frac{1}{2} \left( \frac{x-\mu}{\sigma} \right)^2 \right] \; .
$$


**Proof:** This follows directly from the [definition of the normal distribution](/D/norm).