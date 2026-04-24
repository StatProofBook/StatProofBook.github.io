---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-12-20 16:27:00

title: "Relationship between multivariate normal distribution and chi-squared distribution"
chapter: "Probability Distributions"
section: "Multivariate continuous distributions"
topic: "Multivariate normal distribution"
theorem: "Relationship to chi-squared distribution"

sources:
  - authors: "Koch KR"
    year: 2007
    title: "Chi-Squared Distribution"
    in: "Introduction to Bayesian Statistics"
    pages: "ch. 2.4.5, pp. 48-49, eq. 2.180"
    url: "https://www.springer.com/gp/book/9783540727231"
    doi: "10.1007/978-3-540-72726-2"

proof_id: "P395"
shortcut: "mvn-chi2"
username: "JoramSoch"
---


**Theorem:** Let $X$ be an $n$-dimensional [random vector](/D/rvec) following a [multivariate normal distribution](/D/mvn) with [zero mean](/D/mean-rvec) and arbitrary [covariance matrix](/P/mvn-cov) $\Sigma$:

$$ \label{eq:mvn}
X \sim \mathcal{N}(0, \Sigma) \; .
$$

Then, the quadratic form of $X$, weighted by $\Sigma$, follows a [chi-squared distribution](/D/chi2) with $n$ [degrees of freedom](/D/dof):

$$ \label{eq:mvn-chi2}
Y = X^\mathrm{T} \Sigma^{-1} X \sim \chi^2(n) \; .
$$


**Proof:** Define a new [random vector](/D/rvec) $Z$ as

$$ \label{eq:Z}
Z = \Sigma^{-1/2} X \; .
$$

where $\Sigma^{-1/2}$ is the matrix square root of $\Sigma$. This matrix must exist, because $\Sigma$ is a [covariance matrix](/D/covmat) and [thus positive semi-definite](/P/covmat-psd). Due to the [linear transformation theorem](/P/mvn-ltt), $Z$ is distributed as

$$ \label{eq:Z-dist}
\begin{split}
Z &\sim \mathcal{N}\left( \Sigma^{-1/2} 0, \, \Sigma^{-1/2} \Sigma \, {\Sigma^{-1/2}}^\mathrm{T} \right) \\
  &\sim \mathcal{N}\left( \Sigma^{-1/2} 0, \, \Sigma^{-1/2} \Sigma^{1/2} \Sigma^{1/2} \Sigma^{-1/2} \right) \\
  &\sim \mathcal{N}(0, I_n) \; ,
\end{split}
$$

i.e. [each entry of this vector follows](/P/mvn-marg) a [standard normal distribution](/D/snorm):

$$ \label{eq:Zi-dist}
Z_i \sim \mathcal{N}(0, 1) \quad \text{for all} \quad i = 1, \ldots, n \; .
$$

We further observe that $Y$ can be represented in terms of $Z$

$$ \label{eq:y-z}
Y = X^\mathrm{T} \Sigma^{-1} X = \left( X^\mathrm{T} \Sigma^{-1/2} \right) \left( \Sigma^{-1/2} X \right) = Z^\mathrm{T} Z \; ,
$$

thus $Z$ is a sum of $n$ squared [standard normally distributed](/D/snorm) [random variables](/D/rvar)

$$ \label{eq:y-z-sum}
Y = \sum_{i=1}^{n} Z_i^2 \quad \text{where all} \quad Z_i \sim \mathcal{N}(0, 1)
$$

which, [by definition, is chi-squared distributed](/D/chi2) with $n$ degrees of freedom:

$$ \label{eq:mvn-chi2-qed}
Y \sim \chi^2(n) \; .
$$