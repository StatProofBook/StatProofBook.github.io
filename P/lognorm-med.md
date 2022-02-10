---
layout: proof
mathjax: true

author: "Maja Pavlovic"
affiliation: ""
e_mail: "mpavlovic@uw.co.uk"
date: 2022-02-07 22:33:00

title: "Median of the lognormal distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Lognormal distribution"
theorem: "Median"

sources:

proof_id: "P301"
shortcut: "lognorm-med"
username: "majapavlo"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [lognormal distribution](/D/lognorm):

$$ \label{eq:lognorm}
X \sim \ln \mathcal{N}(\mu, \sigma^2) \; .
$$

Then, the [median](/D/med) of $X$ is

$$ \label{eq:lognorm-median}
\mathrm{median}(X) = e^\mu \; .
$$


**Proof:** The [median](/D/med) is the value at which the cumulative distribution function is $1/2$:

$$ \label{eq:median}
F_X(\mathrm{median}(X)) = \frac{1}{2} \; .
$$

The cumulative distribution function of the lognormal distribution is

$$ \label{eq:lognorm-cdf}
F_X(x) = \frac{1}{2} \left[ 1 + \mathrm{erf} \left( \frac{\ln (x)-\mu}{\sigma \sqrt{2}} \right) \right]
$$

where $\mathrm{erf}(x)$ is the error function. Thus, the inverse CDF is

$$ \label{eq:lognorm-cdf-inv}
\ln (x) = \sigma \sqrt{2} \cdot \mathrm{erf}^{-1}(2p-1) + \mu
$$

where $\mathrm{erf}^{-1}(x)$ is the inverse error function. Setting $p = 1/2$, we obtain:

$$ \label{eq:lognorm-med-equ}
\ln (x) = \sigma \sqrt{2} \cdot \mathrm{erf}^{-1}(0) + \mu 
$$

$$ \label{eq:lognorm-med-ln}
\ln (x) = \mu 
$$

$$ \label{eq:lognorm-med}
\mathrm{median}(X) = e^\mu \; .
$$