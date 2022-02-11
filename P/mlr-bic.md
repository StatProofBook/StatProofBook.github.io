---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-02-11 06:43:00

title: "Bayesian information criterion for multiple linear regression"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Multiple linear regression"
theorem: "Bayesian information criterion"

sources:

proof_id: "P308"
shortcut: "mlr-bic"
username: "JoramSoch"
---


**Theorem:** Consider a [linear regression model](/D/mlr) $m$

$$ \label{eq:mlr}
m: \; y = X\beta + \varepsilon, \; \varepsilon \sim \mathcal{N}(0, \sigma^2 V) \; .
$$

Then, the [Bayesian information criterion](/D/bic) for this model is

$$ \label{eq:mlr-bic}
\mathrm{BIC}(m) = n \log\left( \frac{\mathrm{wRSS}}{n} \right) + n \left[ 1 + \log(2\pi) \right] + \log|V| + \log(n) \, (p + 1)
$$

where $\mathrm{wRSS}$ is the weighted [residual sum of squares](/D/rss), $p$ is the [number of regressors](/D/mlr) in the design matrix $X$ and $n$ is the [number of observations](/D/mlr) in the data vector $y$.


**Proof:** The [Bayesian information criterion](/D/bic) is defined as

$$ \label{eq:bic}
\mathrm{BIC}(m) = -2 \, \mathrm{MLL}(m) + k \log(n)
$$

where $\mathrm{MLL}(m)$ is the [maximum log-likelihood](/D/mll), $k$ is the number of free parameters in $m$ and $n$ is the number of observations.

The [maximum log-likelihood for multiple linear regression](/P/mlr-mll) is given by

$$ \label{eq:mlr-mll}
\mathrm{MLL}(m) = - \frac{n}{2} \log\left( \frac{\mathrm{wRSS}}{n} \right) - \frac{n}{2} \left[ 1 + \log(2\pi) \right] - \frac{1}{2} \log|V|
$$

and the number of free paramters in [multiple linear regression](/D/mlr) is $k = p + 1$, i.e. one for each regressor in the [design matrix](/D/mlr) $X$, plus one for the [noise variance](/D/mlr) $\sigma^2$.

Thus, the BIC of $m$ follows from \eqref{eq:bic} and \eqref{eq:mlr-mll} as

$$ \label{eq:mlr-bic-qed}
\mathrm{BIC}(m) = n \log\left( \frac{\mathrm{wRSS}}{n} \right) + n \left[ 1 + \log(2\pi) \right] + \log|V| + \log(n) \, (p + 1) \; .
$$