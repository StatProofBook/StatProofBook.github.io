---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2025-05-21 13:24:00

title: "Expectation of a quadratic form for the multivariate normal distribution"
chapter: "Probability Distributions"
section: "Multivariate continuous distributions"
topic: "Multivariate normal distribution"
theorem: "Expectation of a quadratic form"

sources:

proof_id: "P499"
shortcut: "mvn-meanqf"
username: "JoramSoch"
---


**Theorem:** Let $X$ follow a [multivariate normal distribution](/D/mvn):

$$ \label{eq:mvn}
X \sim \mathcal{N}(\mu, \Sigma) \; .
$$

Then, the [expectation](/D/mean) of the quadratic form $X^\mathrm{T} A X$ is

$$ \label{eq:mvn-meanqf}
\mathrm{E}\left[ X^\mathrm{T} A X \right] = \mu^\mathrm{T} A \mu + \mathrm{tr}(A \Sigma)
$$

where $A$ is an $n \times n$ matrix.


**Proof:** For any [random vector](/D/rvec) $X \in \mathbb{R}^n$, [this expectation is a function of mean and covariance](/P/mean-qf):

$$ \label{eq:mean-qf}
\mathrm{E}\left[ X^\mathrm{T} A X \right] = \mathrm{E}(X)^\mathrm{T} A \mathrm{X} + \mathrm{tr}(A \, \mathrm{Cov}(X)) \; .
$$

For a [multivariate normal random vector](/D/mvn) $X \sim \mathcal{N}(\mu, \Sigma)$, [mean](/P/mvn-mean) and [covariance](/P/mvn-cov) are

$$ \label{eq:mvn-mean-cov}
\begin{split}
  \mathrm{E}(X) &= \mu \\
\mathrm{Cov}(X) &= \Sigma \; .
\end{split}
$$

Combing \eqref{eq:mean-qf} with \eqref{eq:mvn-mean-cov}, we have:

$$ \label{eq:mvn-meanqf-qed}
\mathrm{E}\left[ X^\mathrm{T} A X \right] = \mu^\mathrm{T} A \mu + \mathrm{tr}(A \Sigma)
$$