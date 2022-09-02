---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-09-02 11:50:00

title: "Probability density function of the multivariate t-distribution"
chapter: "Probability Distributions"
section: "Multivariate continuous distributions"
topic: "Multivariate t-distribution"
theorem: "Probability density function"

sources:

proof_id: "P333"
shortcut: "mvt-pdf"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random vector](/D/rvec) following a [multivariate t-distribution](/D/mvt):

$$ \label{eq:mvt}
X \sim t(\mu, \Sigma, \nu) \; .
$$

Then, the [probability density function](/D/pdf) of $X$ is

$$ \label{eq:mvt-pdf}
f_X(x) = \sqrt{\frac{1}{(\nu \pi)^{n} |\Sigma|}} \, \frac{\Gamma([\nu+n]/2)}{\Gamma(\nu/2)} \, \left[ 1 + \frac{1}{\nu} (x-\mu)^\mathrm{T} \Sigma^{-1} (x-\mu) \right]^{-(\nu+n)/2} \; .
$$


**Proof:** This follows directly from the [definition of the multivariate t-distribution](/D/mvt).