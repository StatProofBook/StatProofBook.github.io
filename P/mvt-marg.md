---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2026-01-23 14:04:00

title: "Marginal distributions of the multivariate t-distribution"
chapter: "Probability Distributions"
section: "Multivariate continuous distributions"
topic: "Multivariate t-distribution"
theorem: "Marginal distributions"

sources:
  - authors: "Wikipedia"
    year: 2026
    title: "Multivariate t-distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2026-01-23"
    url: "https://en.wikipedia.org/wiki/Multivariate_t-distribution#Marginal_Distributions"

proof_id: "P525"
shortcut: "mvt-marg"
username: "JoramSoch"
---


**Theorem:** Let $X$ be an $n$-dimensional [random vector](/D/rvec) following a [multivariate t-distribution](/D/mvt):

$$ \label{eq:mvt}
X \sim t(\mu, \Sigma, \nu) \; .
$$

Then, the [marginal distribution](/D/dist-marg) of any $m$-dimensional subset vector $X_s$ is also a multivariate t-distribution

$$ \label{eq:mvt-marg}
X_s \sim t(\mu_s, \Sigma_s, \nu)
$$

where $\mu_s$ drops the irrelevant variables (the ones not in the subset, i.e. marginalized out) from the mean vector $\mu$ and $\Sigma_s$ drops the corresponding rows and columns from the covariance matrix $\Sigma$.


**Proof:** Define an $m \times n$ subset matrix $S$ such that $s_{ij} = 1$, if the $j$-th element in $X_s$ corresponds to the $i$-th element in $X$, and $s_{ij} = 0$ otherwise. Then,

$$ \label{eq:Xs}
X_s = S X
$$

and we can apply the [linear transformation theorem](/P/mvt-ltt) to give

$$ \label{eq:mvt-marg-qed}
X_s \sim t(S \mu, S \Sigma S^\mathrm{T}, \nu) \; .
$$

Finally, we see that $S \mu = \mu_s$ and $S \Sigma S^\mathrm{T} = \Sigma_s$.