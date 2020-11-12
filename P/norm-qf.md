---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-03-20 04:47:00

title: "Quantile function of the normal distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Normal distribution"
theorem: "Quantile function"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Normal distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-03-20"
    url: "https://en.wikipedia.org/wiki/Normal_distribution#Quantile_function"

proof_id: "P87"
shortcut: "norm-qf"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [normal distributions](/D/norm):

$$ \label{eq:norm}
X \sim \mathcal{N}(\mu, \sigma^2) \; .
$$

Then, the [quantile function](/D/qf) of $X$ is

$$ \label{eq:norm-qf}
Q_X(p) = \sqrt{2}\sigma \cdot \mathrm{erf}^{-1}(2p-1) + \mu
$$

where $\mathrm{erf}^{-1}(x)$ is the inverse error function.


**Proof:** The [cumulative distribution function of the normal distribution](/P/norm-cdf) is:

$$ \label{eq:norm-cdf}
F_X(x) = \frac{1}{2} \left[ 1 + \mathrm{erf}\left( \frac{x-\mu}{\sqrt{2} \sigma} \right) \right] \; .
$$

Because the cumulative distribution function (CDF) is strictly monotonically increasing, the [quantile function is equal to the inverse of the CDF](/P/qf-cdf):

$$ \label{eq:norm-qf-s1}
Q_X(p) = F_X^{-1}(x) \; .
$$

This can be derived by rearranging equation \eqref{eq:norm-cdf}:

$$ \label{eq:norm-qf-s2}
\begin{split}
p &= \frac{1}{2} \left[ 1 + \mathrm{erf}\left( \frac{x-\mu}{\sqrt{2} \sigma} \right) \right] \\
2 p - 1 &= \mathrm{erf}\left( \frac{x-\mu}{\sqrt{2} \sigma} \right) \\
\mathrm{erf}^{-1}(2p-1) &= \frac{x-\mu}{\sqrt{2} \sigma} \\
x &= \sqrt{2}\sigma \cdot \mathrm{erf}^{-1}(2p-1) + \mu \; .
\end{split}
$$