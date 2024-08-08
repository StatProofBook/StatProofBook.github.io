---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-02-11 07:07:00

title: "Corrected Akaike information criterion for multiple linear regression"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Multiple linear regression"
theorem: "Corrected Akaike information criterion"

sources:
  - authors: "Claeskens G, Hjort NL"
    year: 2008
    title: "Akaike's information criterion"
    in: "Model Selection and Model Averaging"
    pages: "ex. 2.5, p. 67"
    url: "https://www.cambridge.org/core/books/model-selection-and-model-averaging/E6F1EC77279D1223423BB64FC3A12C37"
    doi: "10.1017/CBO9780511790485"

proof_id: "P309"
shortcut: "mlr-aicc"
username: "JoramSoch"
---


**Theorem:** Consider a [linear regression model](/D/mlr) $m$

$$ \label{eq:mlr}
m: \; y = X\beta + \varepsilon, \; \varepsilon \sim \mathcal{N}(0, \sigma^2 V) \; .
$$

Then, the [corrected Akaike information criterion](/D/aicc) for this model is

$$ \label{eq:mlr-aicc}
\mathrm{AIC}_\mathrm{c}(m) = n \log\left( \frac{\mathrm{wRSS}}{n} \right) + n \left[ 1 + \log(2\pi) \right] + \log|V| + \frac{2 \, n \, (p+1)}{n-p-2}
$$

where $\mathrm{wRSS}$ is the weighted [residual sum of squares](/D/rss), $p$ is the [number of regressors](/D/mlr) in the design matrix $X$ and $n$ is the [number of observations](/D/mlr) in the data vector $y$.


**Proof:** The [corrected Akaike information criterion](/D/aicc) is defined as

$$ \label{eq:aicc}
\mathrm{AIC}_\mathrm{c}(m) = \mathrm{AIC}(m) + \frac{2k^2 + 2k}{n-k-1}
$$

where $\mathrm{AIC}(m)$ is the [Akaike information criterion](/D/aic), $k$ is the number of free parameters in $m$ and $n$ is the number of observations.

The [Akaike information criterion for multiple linear regression](/P/mlr-aic) is given by

$$ \label{eq:mlr-aic}
\mathrm{AIC}(m) = n \log\left( \frac{\mathrm{wRSS}}{n} \right) + n \left[ 1 + \log(2\pi) \right] + \log|V| + 2 (p + 1)
$$

and the number of free paramters in [multiple linear regression](/D/mlr) is $k = p + 1$, i.e. one for each regressor in the [design matrix](/D/mlr) $X$, plus one for the [noise variance](/D/mlr) $\sigma^2$.

Thus, the corrected AIC of $m$ follows from \eqref{eq:aicc} and \eqref{eq:mlr-aic} as

$$ \label{eq:mlr-aicc-qed}
\begin{split}
\mathrm{AIC}_\mathrm{c}(m) &= n \log\left( \frac{\mathrm{wRSS}}{n} \right) + n \left[ 1 + \log(2\pi) \right] + \log|V| + 2 \, k + \frac{2k^2 + 2k}{n-k-1} \\
&= n \log\left( \frac{\mathrm{wRSS}}{n} \right) + n \left[ 1 + \log(2\pi) \right] + \log|V| + \frac{2nk - 2k^2 - 2k}{n-k-1} + \frac{2k^2 + 2k}{n-k-1} \\ 
&= n \log\left( \frac{\mathrm{wRSS}}{n} \right) + n \left[ 1 + \log(2\pi) \right] + \log|V| + \frac{2nk}{n-k-1} \\ 
&= n \log\left( \frac{\mathrm{wRSS}}{n} \right) + n \left[ 1 + \log(2\pi) \right] + \log|V| + \frac{2 \, n \, (p+1)}{n-p-2} \\ \; .
\end{split}
$$