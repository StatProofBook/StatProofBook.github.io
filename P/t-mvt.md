---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-08-25 12:38:00

title: "t-distribution is a special case of multivariate t-distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "t-distribution"
theorem: "Special case of multivariate t-distribution"

sources:
  - authors: "Wikipedia"
    year: 2022
    title: "Multivariate t-distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2022-08-25"
    url: "https://en.wikipedia.org/wiki/Multivariate_t-distribution#Derivation"

proof_id: "P332"
shortcut: "t-mvt"
username: "JoramSoch"
---


**Theorem:** The [t-distribution](/D/t) is a special case of the [multivariate t-distribution](/D/mvt) with number of variables $n = 1$, i.e. [random vector](/D/rvec) $x \in \mathbb{R}$, mean $\mu = 0$ and covariance matrix $\Sigma = 1$.


**Proof:** The [probability density function of the multivariate t-distribution](/P/mvt-pdf) is

$$ \label{eq:mvt-pdf}
t(x; \mu, \Sigma, \nu) = \sqrt{\frac{1}{(\nu \pi)^{n} |\Sigma|}} \, \frac{\Gamma([\nu+n]/2)}{\Gamma(\nu/2)} \, \left[ 1 + \frac{1}{\nu} (x-\mu)^\mathrm{T} \Sigma^{-1} (x-\mu) \right]^{-(\nu+n)/2} \; .
$$

Setting $n = 1$, such that $x \in \mathbb{R}$, as well as $\mu = 0$ and $\Sigma = 1$, we obtain

$$ \label{eq:t-pdf}
\begin{split}
t(x; 0, 1, \nu) &= \sqrt{\frac{1}{(\nu \pi)^{1} |1|}} \, \frac{\Gamma([\nu+1]/2)}{\Gamma(\nu/2)} \, \left[ 1 + \frac{1}{\nu} (x-0)^\mathrm{T} 1^{-1} (x-0) \right]^{-(\nu+1)/2} \\
&= \sqrt{\frac{1}{\nu \pi}} \, \frac{\Gamma([\nu+1]/2)}{\Gamma(\nu/2)} \, \left[ 1 + \frac{x^2}{\nu} \right]^{-(\nu+1)/2} \\
&= \frac{1}{\sqrt{\nu \pi}} \cdot \frac{\Gamma\left( \frac{\nu+1}{2} \right)}{\Gamma\left( \frac{\nu}{2} \right)} \cdot \left[ 1 + \frac{x^2}{\nu} \right]^{-\frac{\nu+1}{2}} \; .
\end{split}
$$

which is equivalent to the [probability density function of the t-distribution](/P/t-pdf).