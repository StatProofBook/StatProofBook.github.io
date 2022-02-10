---
layout: proof
mathjax: true

author: "Maja Pavlovic"
affiliation: ""
e_mail: "mpavlovic@uw.co.uk"
date: 2022-02-07 22:33:00

title: "Median of the log-normal distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Log-normal distribution"
theorem: "Median"

sources:

proof_id: "P306"
shortcut: "lognorm-med"
username: "majapavlo"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [log-normal distribution](/D/lognorm):

$$ \label{eq:lognorm}
X \sim \ln \mathcal{N}(\mu, \sigma^2) \; .
$$

Then, the [median](/D/med) of $X$ is

$$ \label{eq:lognorm-med}
\mathrm{median}(X) = e^\mu \; .
$$


**Proof:** The [median](/D/med) is the value at which the cumulative distribution function is $1/2$:

$$ \label{eq:median}
F_X(\mathrm{median}(X)) = \frac{1}{2} \; .
$$

The [cumulative distribution function of the lognormal distribution](/P/lognorm-cdf) is

$$ \label{eq:lognorm-cdf}
F_X(x) = \frac{1}{2} \left[ 1 + \mathrm{erf} \left( \frac{\ln (x)-\mu}{\sigma \sqrt{2}} \right) \right]
$$

where $\mathrm{erf}(x)$ is the error function. Thus, the inverse CDF is

$$ \label{eq:lognorm-cdf-inv}
\begin{split}
\ln(x) &= \sigma \sqrt{2} \cdot \mathrm{erf}^{-1}(2p-1) + \mu \\
x &= \mathrm{exp} \left[ \sigma \sqrt{2} \cdot \mathrm{erf}^{-1}(2p-1) + \mu \right]
\end{split}
$$

where $\mathrm{erf}^{-1}(x)$ is the inverse error function. Setting $p = 1/2$, we obtain:

$$ \label{eq:lognorm-med-qed}
\begin{split}
\ln \left[ \mathrm{median}(X) \right] &= \mathrm{exp} \left[ \sigma \sqrt{2} \cdot \mathrm{erf}^{-1}(0) + \mu \right] \\
\mathrm{median}(X) &= e^\mu \; .
\end{split}
$$