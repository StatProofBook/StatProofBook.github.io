---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-06-02 08:24:00

title: "Linear combination of independent normal random variables"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Normal distribution"
theorem: "Linear combination"

sources:

proof_id: "P235"
shortcut: "norm-lincomb"
username: "JoramSoch"
---


**Theorem:** Let $X_1, \ldots, X_n$ be [independent](/D/ind) [normally distributed](/D/norm) [random variables](/D/rvar) with [means](/D/mean) $\mu_1, \ldots, \mu_n$ and [variances](/D/var) $\sigma^2_1, \ldots, \sigma^2_n$:

$$ \label{eq:norm}
X_i \sim \mathcal{N}(\mu_i, \sigma^2_i) \quad \text{for} \quad i = 1, \ldots, n \; .
$$

Then, any linear combination of those random variables

$$ \label{eq:lincomb}
Y = \sum_{i=1}^{n} a_i X_i \quad \text{where} \quad a_1, \ldots, a_n \in \mathbb{R}
$$

also follows a normal distribution

$$ \label{eq:norm-lincomb}
Y \sim \mathcal{N}\left( \sum_{i=1}^{n} a_i \mu_i, \; \sum_{i=1}^{n} a_i^2 \sigma^2_i \right)
$$

with mean and variance which are functions of the individual means and variances.


**Proof:** A set of $n$ independent normal random variables $X_1, \ldots, X_n$ [is equivalent](/P/mvn-ind) to an $n \times 1$ [random vector](/D/rvec) $x$ following a [multivariate normal distribution](/D/mvn) with a diagonal [covariance matrix](/D/covmat). Therefore, we can write

$$ \label{eq:norm-mvn}
X_i \sim \mathcal{N}(\mu_i, \sigma^2_i), \; i = 1, \ldots, n \quad \Rightarrow \quad x = \left[ \begin{array}{c} X_1 \\ \vdots \\ X_n \end{array} \right] \sim \mathcal{N}(\mu, \Sigma)
$$

with mean vector and covariance matrix

$$ \label{eq:mu-Sigma}
\mu = \left[ \begin{array}{c} \mu_1 \\ \vdots \\ \mu_n \end{array} \right] \quad \text{and} \quad \Sigma = \left[ \begin{array}{ccc} \sigma^2_1 & \cdots & 0 \\ \vdots & \ddots & \vdots \\ 0 & \cdots & \sigma^2_n \end{array} \right] = \mathrm{diag}\left( \left[ \sigma^2_1, \ldots, \sigma^2_n \right] \right) \; .
$$

Thus, we can apply the [linear transformation theorem for the multivariate normal distribution](/P/mvn-ltt)

$$ \label{eq:mvn-ltt}
x \sim \mathcal{N}(\mu, \Sigma) \quad \Rightarrow \quad y = Ax + b \sim \mathcal{N}(A\mu + b, A \Sigma A^\mathrm{T})
$$

with the constant matrix and vector

$$ \label{eq:A-b}
A = \left[ a_1, \ldots, a_n \right] \quad \text{and} \quad b = 0 \; .
$$

This implies the following distribution the linear combination given by equation \eqref{eq:lincomb}:

$$ \label{eq:norm-lincomb-p1}
Y = Ax + b \sim \mathcal{N}(A\mu, A \Sigma A^\mathrm{T}) \; .
$$

Finally, we note that

$$ \label{eq:A-b-mu-Sigma}
\begin{split}
A \mu &= \left[ a_1, \ldots, a_n \right] \left[ \begin{array}{c} \mu_1 \\ \vdots \\ \mu_n \end{array} \right] = \sum_{i=1}^{n} a_i \mu_i \quad \text{and} \quad \\
A \Sigma A^\mathrm{T} &= \left[ a_1, \ldots, a_n \right] \left[ \begin{array}{ccc} \sigma^2_1 & \cdots & 0 \\ \vdots & \ddots & \vdots \\ 0 & \cdots & \sigma^2_n \end{array} \right] \left[ \begin{array}{c} a_1 \\ \vdots \\ a_n \end{array} \right] = \sum_{i=1}^{n} a_i^2 \sigma^2_i \; .
\end{split}
$$