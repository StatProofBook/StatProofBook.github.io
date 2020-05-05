---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-05-05 21:03:00

title: "Probability density function of the beta distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Beta distribution"
theorem: "Probability density function"

sources:

proof_id: "P94"
shortcut: "beta-pdf"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [beta distribution](/D/beta):

$$ \label{eq:beta}
X \sim \mathrm{Bet}(\alpha, \beta) \; .
$$

Then, the [probability density function](/D/pdf) of $X$ is

$$ \label{eq:beta-pdf}
f_X(x) = \frac{1}{\mathrm{B}(\alpha, \beta)} \, x^{\alpha-1} \, (1-x)^{\beta-1} \; .
$$


**Proof:** This follows directly from the [definition of the beta distribution](/D/beta).