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


**Theorem:** Let $x$ be an $n \times 1$ [random vector](/D/rvec) following a [multivariate normal distribution](/D/mvn) with [zero mean](/D/mean-rvec) and arbitrary [covariance matrix](/P/mvn-cov) $\Sigma$:

$$ \label{eq:mvn}
x \sim \mathcal{N}(0, \Sigma) \; .
$$

Then, the quadratic form of $x$, weighted by $\Sigma$, follows a [chi-squared distribution](/D/chi2) with $n$ [degrees of freedom](/D/dof):

$$ \label{eq:mvn-chi2}
y = x^\mathrm{T} \Sigma^{-1} x \sim \chi^2(n) \; .
$$


**Proof:** Define a new [random vector](/D/rvec) $z$ as

$$ \label{eq:z}
z = \Sigma^{-1/2} x \; .
$$

where $\Sigma^{-1/2}$ is the matrix square root of $\Sigma$. This matrix must exist, because $\Sigma$ is a [covariance matrix](/D/covmat) and [thus positive semi-definite](/P/covmat-psd). Due to the [linear transformation theorem](/P/mvn-ltt), $z$ is distributed as

$$ \label{eq:z-dist}
\begin{split}
z &\sim \mathcal{N}\left( \Sigma^{-1/2} 0, \, \Sigma^{-1/2} \Sigma \, {\Sigma^{-1/2}}^\mathrm{T} \right) \\
&\sim \mathcal{N}\left( \Sigma^{-1/2} 0, \, \Sigma^{-1/2} \Sigma^{1/2} \Sigma^{1/2} \Sigma^{-1/2} \right) \\
&\sim \mathcal{N}(0, I_n) \; ,
\end{split}
$$

i.e. [each entry of this vector follows](/P/mvn-marg) a [standard normal distribution](/D/snorm):

$$ \label{eq:zi-dist}
z_i \sim \mathcal{N}(0, 1) \quad \text{for all} \quad i = 1, \ldots, n \; .
$$

We further observe that $y$ can be represented in terms of $z$

$$ \label{eq:y-z}
y = x^\mathrm{T} \Sigma^{-1} x = \left( x^\mathrm{T} \Sigma^{-1/2} \right) \left( \Sigma^{-1/2} x \right) = z^\mathrm{T} z \; ,
$$

thus $z$ is a sum of $n$ standard normally distributed [random variables](/D/rvar)

$$ \label{eq:y-z-sum}
y = \sum_{i=1}^{n} z_i \quad \text{where all} \quad z_i \sim \mathcal{N}(0, 1)
$$

which, [by definition, is chi-squared distributed](/D/chi2) with $n$ degrees of freedom:

$$ \label{eq:mvn-chi2-qed}
y \sim \chi^2(n) \; .
$$