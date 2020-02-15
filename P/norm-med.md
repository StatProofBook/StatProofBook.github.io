---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-01-09 15:33:00

title: "Median of the normal distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Normal distribution"
theorem: "Median"

sources:

proof_id: "P16"
shortcut: "norm-med"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [normal distribution](/D/norm):

$$ \label{eq:norm}
X \sim \mathcal{N}(\mu, \sigma^2) \; .
$$

Then, the [median](/D/med) of $X$ is

$$ \label{eq:norm-median}
\mathrm{median}(X) = \mu \; .
$$


**Proof:** The [median](/D/med) is the value at which the [cumulative distribution function](/D/cdf) is $1/2$:

$$ \label{eq:median}
F_X(\mathrm{median}(X)) = \frac{1}{2} \; .
$$

The [cumulative distribution function of the normal distribution](/P/norm-cdf) is

$$ \label{eq:norm-cdf}
F_X(x) = \frac{1}{2} \left[ 1 + \mathrm{erf} \left( \frac{x-\mu}{\sqrt{2}\sigma} \right) \right]
$$

where $\mathrm{erf}(x)$ is the error function. Thus, the inverse CDF is

$$ \label{eq:norm-cdf-inv}
x = \sqrt{2}\sigma \cdot \mathrm{erf}^{-1}(2p-1) + \mu
$$

where $\mathrm{erf}^{-1}(x)$ is the inverse error function. Setting $p = 1/2$, we obtain:

$$ \label{eq:norm-med-qed}
\mathrm{median}(X) = \sqrt{2}\sigma \cdot \mathrm{erf}^{-1}(0) + \mu = \mu \; .
$$