---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2024-11-15 11:52:45

title: "The product of independent log-normal random variables is a log-normal random variable"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Log-normal distribution"
theorem: "Product of independent log-normals"

sources:
  - authors: "drhab"
    year: 2018
    title: "If Xi is a log-normal r.v., show product of all Xi is also a log-normal r.v."
    in: "StackExchange Mathematics"
    pages: "retrieved on 2024-11-15"
    url: "https://math.stackexchange.com/a/2838307/480910"

proof_id: "P479"
shortcut: "lognorm-prodind"
username: "JoramSoch"
---


**Theorem:** Let $X_1, \ldots, X_n$ be [independent](/D/ind) [random variables](/D/rvar) following [log-normal distributions](/D/lognorm):

$$ \label{eq:X-lognorm}
X_i \sim \ln \mathcal{N}(\mu_i, \sigma_i^2), \; i = 1, \ldots, n \; .
$$

Then, the product of these random variables also follows a [log-normal distribution](/D/lognorm)

$$ \label{eq:Z-lognorm}
Z = \prod_{i=1}^n X_i \sim \mathcal{N}(\mu, \sigma^2)
$$

where the [log-normal](/D/lognorm) parameters are given by

$$ \label{eq:Z-lognorm-para}
\mu      = \sum_{i=1}^n \mu_i
\quad \text{and} \quad
\sigma^2 = \sum_{i=1}^n \sigma_i^2 \; .
$$


**Proof:** A random variable [follows a log-normal distribution, if and only if its natural logarithm follows a normal distribution](/D/lognorm):

$$ \label{eq:lognorm-norm}
X \sim \ln \mathcal{N}(\mu, \sigma^2)
\quad \Leftrightarrow \quad
\ln X \sim \mathcal{N}(\mu, \sigma^2) \; .
$$

Thus, from \eqref{eq:X-lognorm}, we have

$$ \label{eq:Y-norm}
Y_i = \ln X_i \sim \mathcal{N}(\mu_i, \sigma_i^2)
$$

and from \eqref{eq:Z-lognorm}, we have

$$ \label{eq:ln-Z}
  \ln Z
= \ln \left( \prod_{i=1}^n X_i \right)
= \sum_{i=1}^n \ln X_i
= \sum_{i=1}^n Y_i \; .
$$

This means that the logarithm of the product of independent [log-normal](/D/lognorm) random variables is a sum of independent [normal](/D/norm) random variables. Because [any linear combination of independent normal random variables is again normally distributed](/P/norm-lincomb), this sum follows a normal distribution. Combining this with \eqref{eq:ln-Z} and \eqref{eq:Y-norm}, we have:

$$ \label{eq:ln-Z-norm}
     \ln Z
=    \sum_{i=1}^n Y_i
\sim \mathcal{N}\left( \sum_{i=1}^n \mu_i, \, \sum_{i=1}^n \sigma_i^2 \right) \; .
$$

If a random variable [follows a normal distribution, then its exponential follows a log-normal distribution with the same parameters](/D/lognorm):

$$ \label{eq:norm-lognorm}
Y \sim \mathcal{N}(\mu, \sigma^2)
\quad \Leftrightarrow \quad
\exp(Y) \sim \ln \mathcal{N}(\mu, \sigma^2) \; .
$$

Thus, from \eqref{eq:ln-Z-norm}, we have

$$ \label{eq:Z-lognorm-qed}
     Z
=    \exp(\ln Z) 
\sim \ln \mathcal{N}\left( \sum_{i=1}^n \mu_i, \, \sum_{i=1}^n \sigma_i^2 \right)
$$

which is equivalent to \eqref{eq:Z-lognorm} and \eqref{eq:Z-lognorm-para}.