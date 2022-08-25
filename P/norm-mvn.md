---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-08-19 19:41:00

title: "Normal distribution is a special case of multivariate normal distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Normal distribution"
theorem: "Special case of multivariate normal distribution"

sources:
  - authors: "Wikipedia"
    year: 2022
    title: "Multivariate normal distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2022-08-19"
    url: "https://en.wikipedia.org/wiki/Multivariate_normal_distribution"

proof_id: "P331"
shortcut: "norm-snorm"
username: "JoramSoch"
---


**Theorem:** The [normal distribution](/D/norm) is a special case of the [multivariate normal distribution](/D/mvn) with number of variables $n = 1$, i.e. [random vector](/D/rvec) $x \in \mathbb{R}$, mean $\mu \in \mathbb{R}$ and covariance matrix $\Sigma = \sigma^2$.


**Proof:** The [probability density function of the multivariate normal distribution](/P/mvn-pdf) is

$$ \label{eq:mvn-pdf}
\mathcal{N}(x; \mu, \Sigma) = \frac{1}{\sqrt{(2 \pi)^n |\Sigma|}} \cdot \exp \left[ -\frac{1}{2} (x-\mu)^\mathrm{T} \Sigma^{-1} (x-\mu) \right] \; .
$$

Setting $n = 1$, such that $x, \mu \in \mathbb{R}$, and $\Sigma = \sigma^2$, we obtain

$$ \label{eq:norm-pdf}
\begin{split}
\mathcal{N}(x; \mu, \sigma^2) &= \frac{1}{\sqrt{(2 \pi)^1 |\sigma^2|}} \cdot \exp \left[ -\frac{1}{2} (x-\mu)^\mathrm{T} (\sigma^2)^{-1} (x-\mu) \right] \\
&= \frac{1}{\sqrt{(2\pi) \sigma^2}} \cdot \exp\left[-\frac{1}{2 \sigma^2} (x-\mu)^2 \right] \\
&= \frac{1}{\sqrt{2\pi} \sigma} \cdot \exp \left[ -\frac{1}{2} \left( \frac{x-\mu}{\sigma} \right)^2 \right]
\end{split}
$$

which is equivalent to the [probability density function of the normal distribution](/P/norm-pdf).