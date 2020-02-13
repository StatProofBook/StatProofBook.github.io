---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-02-08 23:41:00

title: "Probability density function of the gamma distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Gamma distribution"
theorem: "Probability density function"

sources:

proof_id: "P45"
shortcut: "gam-pdf"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a positive [random variable](/D/rvar) following a [gamma distribution](/D/gam):

$$ \label{eq:gam}
X \sim \mathrm{Gam}(a, b) \; .
$$

Then, the [probability density function](/D/pdf) of $X$ is

$$ \label{eq:gam-pdf}
f_X(x) = \frac{b^a}{\Gamma(a)} x^{a-1} \exp[-b x] \; .
$$


**Proof:** This follows directly from the [definition of the gamma distribution](/D/gam).