---
layout: proof
mathjax: true

author: "Thomas J. Faulkenberry"
affiliation: "Tarleton State University"
e_mail: "faulkenberry@tarleton.edu"
date: 2020-09-04 12:00:00

title: "Probability density function of the Wald distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Wald distribution"
theorem: "Probability density function"

sources:

proof_id: "P162"
shortcut: "wald-pdf"
username: "tomfaulkenberry"
---


**Theorem:** Let $X$ be a positive [random variable](/D/rvar) following a [Wald distribution](/D/wald):

$$ \label{eq:wald}
X \sim \mathrm{Wald}(\gamma, \alpha) \; .
$$

Then, the [probability density function](/D/pdf) of $X$ is

$$ \label{eq:wald-pdf}
f_X(x) = \frac{\alpha}{\sqrt{2\pi x^3}}\exp\left(-\frac{(\alpha-\gamma x)^2}{2x}\right) \; .
$$


**Proof:** This follows directly from the [definition of the Wald distribution](/D/wald).