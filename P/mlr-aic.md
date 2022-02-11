---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-02-11 06:26:00

title: "Akaike information criterion for multiple linear regression"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Multiple linear regression"
theorem: "Akaike information criterion"

sources:
  - authors: "Claeskens G, Hjort NL"
    year: 2008
    title: "Akaike's information criterion"
    in: "Model Selection and Model Averaging"
    pages: "ex. 2.2, p. 66"
    url: "https://www.cambridge.org/core/books/model-selection-and-model-averaging/E6F1EC77279D1223423BB64FC3A12C37"
    doi: "10.1017/CBO9780511790485"

proof_id: "P307"
shortcut: "mlr-aic"
username: "JoramSoch"
---


**Theorem:** Consider a [linear regression model](/D/mlr) $m$

$$ \label{eq:mlr}
m: \; y = X\beta + \varepsilon, \; \varepsilon \sim \mathcal{N}(0, \sigma^2 V) \; .
$$

Then, the [Akaike information criterion](/D/aic) for this model is

$$ \label{eq:mlr-aic}
\mathrm{AIC}(m) = n \log\left( \frac{\mathrm{wRSS}}{n} \right) + n \left[ 1 + \log(2\pi) \right] + \log|V| + 2 (p + 1)
$$

where $\mathrm{wRSS}$ is the weighted [residual sum of squares](/D/rss), $p$ is the [number of regressors](/D/mlr) in the design matrix $X$ and $n$ is the [number of observations](/D/mlr) in the data vector $y$.


**Proof:** The [Akaike information criterion](/D/aic) is defined as

$$ \label{eq:aic}
\mathrm{AIC}(m) = -2 \, \mathrm{MLL}(m) + 2 \, k
$$

where $\mathrm{MLL}(m)$ is the [maximum log-likelihood](/D/mll) is $k$ is the number of free parameters in $m$.

The [maximum log-likelihood for multiple linear regression](/P/mlr-mll) is given by

$$ \label{eq:mlr-mll}
\mathrm{MLL}(m) = - \frac{n}{2} \log\left( \frac{\mathrm{wRSS}}{n} \right) - \frac{n}{2} \left[ 1 + \log(2\pi) \right] - \frac{1}{2} \log|V|
$$

and the number of free paramters in [multiple linear regression](/D/mlr) is $k = p + 1$, i.e. one for each regressor in the [design matrix](/D/mlr) $X$, plus one for the [noise variance](/D/mlr) $\sigma^2$.

Thus, the AIC of $m$ follows from \eqref{eq:aic} and \eqref{eq:mlr-mll} as

$$ \label{eq:mlr-aic-qed}
\mathrm{AIC}(m) = n \log\left( \frac{\mathrm{wRSS}}{n} \right) + n \left[ 1 + \log(2\pi) \right] + \log|V| + 2 (p + 1) \; .
$$