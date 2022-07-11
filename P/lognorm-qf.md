---
layout: proof
mathjax: true

author: "Maja Pavlovic"
affiliation: ""
e_mail: "mpavlovic@uw.co.uk"
date: 2022-07-09 11:05:00

title: ""Quantile function of the log-normal distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Log-normal distribution"
theorem: "Quantile function"

sources:
  - authors: "Wikipedia"
    year: 2022
    title: "Log-normal distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2022-07-08"
    url: "https://en.wikipedia.org/wiki/Log-normal_distribution#Mode,_median,_quantiles"

proof_id: "P326"
shortcut: "lognorm-qf"
username: "majapavlo"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [log-normal distribution](/D/lognorm):

$$ \label{eq:lognorm}
X \sim \ln \mathcal{N}(\mu, \sigma^2) \; .
$$

Then, the [quantile function](/D/qf) of $X$ is

$$ \label{eq:lognorm-qf}
Q_X(p) = \exp( \mu + \sqrt{2} \sigma \cdot \mathrm{erf}^{-1}(2p-1) )
$$

where $\mathrm{erf}^{-1}(x)$ is the inverse error function.


**Proof:** The [cumulative distribution function of the log-normal distribution](/P/lognorm-cdf) is:

$$ \label{eq:lognorm-cdf}
F_X(x) = \frac{1}{2} \left[ 1 + \mathrm{erf}\left( \frac{\ln x-\mu}{\sqrt{2} \sigma} \right) \right] \; .
$$

From this point forward, the proof is similar to the derivation of the [quantile function for the normal distribution](/P/norm-qf). Because the cumulative distribution function (CDF) is strictly monotonically increasing the [quantile function is equal to the inverse of the CDF](/P/qf-cdf): 

$$ \label{eq:lognorm-qf-s1}
Q_X(p) = F_X^{-1}(x) \; .
$$

This can be derived by rearranging equation \eqref{eq:lognorm-cdf}:

$$ \label{eq:lognorm-qf-s2}
\begin{split}
p &= \frac{1}{2} \left[ 1 + \mathrm{erf}\left( \frac{\ln x-\mu}{\sqrt{2} \sigma} \right) \right] \\
2 p - 1 &= \mathrm{erf}\left( \frac{\ln x-\mu}{\sqrt{2} \sigma} \right) \\
\mathrm{erf}^{-1}(2p-1) &= \frac{\ln x-\mu}{\sqrt{2} \sigma} \\
x &= \exp(\mu + \sqrt{2}\sigma \cdot \mathrm{erf}^{-1}(2p-1) ) \; .
\end{split}
$$