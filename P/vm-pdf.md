---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2026-04-21 15:08:40

title: "Probability density function of the von Mises distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "von Mises distribution"
theorem: "Probability density function"

sources:

proof_id: "P534"
shortcut: "vm-pdf"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [von Mises distribution](/D/vm):

$$ \label{eq:vm}
X \sim \mathrm{vM}(\mu, \kappa) \; .
$$

Then, the [probability density function](/D/pdf) of $X$ is

$$ \label{eq:norm-pdf}
f_X(x) = \frac{1}{2 \pi I_0(\kappa)} \cdot \exp \left[ \kappa \cos(x-\mu) \right] \; .
$$


**Proof:** This follows directly from the [definition of the von Mises distribution](/D/vm).