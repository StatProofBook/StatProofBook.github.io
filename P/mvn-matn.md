---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-07-31 11:00:00

title: "Multivariate normal distribution is a special case of matrix-normal distribution"
chapter: "Probability Distributions"
section: "Multivariate continuous distributions"
topic: "Multivariate normal distribution"
theorem: "Special case of matrix-normal distribution"

sources:
  - authors: "Wikipedia"
    year: 2022
    title: "Matrix normal distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2022-07-31"
    url: "https://en.wikipedia.org/wiki/Matrix_normal_distribution#Definition"

proof_id: "P330"
shortcut: "mvn-matn"
username: "JoramSoch"
---


**Theorem:** The [multivariate normal distribution](/D/mvn) is a special case of the [matrix-normal distribution](/D/matn) with number of variables $p = 1$, i.e. [random matrix](/D/rvar) $X = x \in \mathbb{R}^{n \times 1}$, mean $M = \mu \in \mathbb{R}^{n \times 1}$, covariance across rows $U = \Sigma$ and covariance across columns $V = 1$.


**Proof:** The [probability density function of the matrix-normal distribution](/P/matn-pdf) is

$$ \label{eq:matn-pdf}
\mathcal{MN}(X; M, U, V) = \frac{1}{\sqrt{(2\pi)^{np} |V|^n |U|^p}} \cdot \exp\left[-\frac{1}{2} \mathrm{tr}\left( V^{-1} (X-M)^\mathrm{T} \, U^{-1} (X-M) \right) \right] \; .
$$

Setting $p = 1$, $X = x$, $M = \mu$, $U = \Sigma$ and $V = 1$, we obtain

$$ \label{eq:mvn-pdf}
\begin{split}
\mathcal{MN}(x; \mu, \Sigma, 1) &= \frac{1}{\sqrt{(2\pi)^{n} |1|^n |\Sigma|^1}} \cdot \exp\left[-\frac{1}{2} \mathrm{tr}\left( 1^{-1} (x-\mu)^\mathrm{T} \, \Sigma^{-1} (x-\mu) \right) \right] \\
&= \frac{1}{\sqrt{(2\pi)^{n} |\Sigma|}} \cdot \exp\left[-\frac{1}{2} (x-\mu)^\mathrm{T} \, \Sigma^{-1} (x-\mu) \right]
\end{split}
$$

which is equivalent to the [probability density function of the multivariate normal distribution](/P/mvn-pdf).