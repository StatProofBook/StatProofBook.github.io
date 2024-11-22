---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2024-11-22 11:39:58

title: "The geometric mean of independent log-normal random variables is a log-normal random variable"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Log-normal distribution"
theorem: "Geometric mean of independent log-normals "

sources:
  - authors: "Probability Fact"
    year: 2022
    title: "The geometric mean of independent log-normal random variables has a log-normal distribution"
    in: "X"
    pages: "retrieved on 2024-11-22"
    url: "https://x.com/ProbFact/status/1592989704646848512"

proof_id: "P480"
shortcut: "lognorm-geomind"
username: "JoramSoch"
---


**Theorem:** Let $X_1, \ldots, X_n$ be [independent](/D/ind) [random variables](/D/rvar) following [log-normal distributions](/D/lognorm):

$$ \label{eq:X-lognorm}
X_i \sim \ln \mathcal{N}(\mu_i, \sigma_i^2), \; i = 1, \ldots, n \; .
$$

Then, the [geometric mean](/D/mean-geom) of these random variables also follows a [log-normal distribution](/D/lognorm):

$$ \label{eq:Z-lognorm}
Z = \sqrt[n]{\prod_{i=1}^n X_i} \sim \mathcal{N}(\mu, \sigma^2)
$$

where the [log-normal](/D/lognorm) parameters are given by

$$ \label{eq:Z-lognorm-para}
\mu      = \frac{1}{n} \sum_{i=1}^n \mu_i
\quad \text{and} \quad
\sigma^2 = \frac{1}{n^2} \sum_{i=1}^n \sigma_i^2 \; .
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
= \ln \left( \sqrt[n]{\prod_{i=1}^n X_i} \right)
= \frac{1}{n} \sum_{i=1}^n \ln X_i
= \frac{1}{n} \sum_{i=1}^n Y_i \; .
$$

This means that the logarithm of the geometric mean of independent [log-normal](/D/lognorm) random variables is the arithmetic mean of independent [normal](/D/norm) random variables. This average, like any [linear combination of independent normal random variables, is again normally distributed](/P/norm-lincomb). Thus, combining \eqref{eq:ln-Z} and \eqref{eq:Y-norm}, we have:

$$ \label{eq:ln-Z-norm}
     \ln Z
=    \frac{1}{n} \sum_{i=1}^n Y_i
\sim \mathcal{N}\left( \frac{1}{n} \sum_{i=1}^n \mu_i, \, \frac{1}{n^2} \sum_{i=1}^n \sigma_i^2 \right) \; .
$$

If a random variable [follows a normal distribution, then its exponential follows a log-normal distribution with the same parameters]:

$$ \label{eq:norm-lognorm}
Y \sim \mathcal{N}(\mu, \sigma^2)
\quad \Leftrightarrow \quad
\exp(Y) \sim \ln \mathcal{N}(\mu, \sigma^2) \; .
$$

Thus, from \eqref{eq:ln-Z-norm}, we have

$$ \label{eq:Z-lognorm-qed}
     Z
=    \exp(\ln Z)
\sim \ln \mathcal{N}\left( \frac{1}{n} \sum_{i=1}^n \mu_i, \, \frac{1}{n^2} \sum_{i=1}^n \sigma_i^2 \right)
$$

which is equivalent to \eqref{eq:Z-lognorm} and \eqref{eq:Z-lognorm-para}.