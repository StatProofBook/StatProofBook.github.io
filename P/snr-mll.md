---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2024-03-28 10:55:29

title: "Relationship between signal-to-noise ratio and maximum log-likelihood"
chapter: "Model Selection"
section: "Goodness-of-fit measures"
topic: "Signal-to-noise ratio"
theorem: "Relationship to maximum log-likelihood"

sources:

proof_id: "P444"
shortcut: "snr-mll"
username: "JoramSoch"
---


**Theorem:** Given a [linear regression model](/D/mlr) with [independent](/D/ind) observations

$$ \label{eq:mlr}
y = X\beta + \varepsilon, \; \varepsilon_i \overset{\mathrm{i.i.d.}}{\sim} \mathcal{N}(0, \sigma^2) \; ;
$$

the [signal-to-noise ratio](/D/snr) can be expressed in terms of the [maximum log-likelihood](/D/mll) as

$$ \label{eq:SNR-MLL}
\mathrm{SNR} = \left( \exp[\Delta\mathrm{MLL}] \right)^{2/n} - 1 \; ,
$$

where $n$ is the number of observations and $\Delta\mathrm{MLL}$ is the difference in maximum log-likelihood between the model given by \eqref{eq:mlr} and a linear regression model with only a constant regressor.

This holds, if the predicted signal mean is equal to the actual signal mean

$$ \label{eq:y-hat-mean-y-mean}
\bar{\hat{y}} = \frac{1}{n} \sum_{i=1}^{n} (X\hat{\beta})_i = \frac{1}{n} \sum_{i=1}^{n} y_i = \bar{y}
$$

where $X$ is the $n \times p$ design matrix and $\hat{\beta}$ are the [ordinary least squares](/P/mlr-ols) estimates.


**Proof:** Under the conditions mentioned in the theorem, the [signal-to-noise ratio can be expressed in terms of the coefficient of determination](/P/snr-rsq) as

$$ \label{eq:SNR-R2}
\mathrm{SNR} = \frac{R^2}{\mathrm{1-R^2}}
$$

and [R-squared can be expressed in terms of maximum likelihood](/P/rsq-mll) as 

$$ \label{eq:R2-MLL}
R^2 = 1 - \left( \exp[\Delta\mathrm{MLL}] \right)^{-2/n} \; .
$$

Plugging \eqref{eq:R2-MLL} into \eqref{eq:SNR-R2}, we obtain:

$$ \label{eq:SNR-MLL-qed}
\begin{split}
\mathrm{SNR} &= \frac{1 - \left( \exp[\Delta\mathrm{MLL}] \right)^{-2/n}}{\mathrm{\left( \exp[\Delta\mathrm{MLL}] \right)^{-2/n}}} \\
&= \frac{1}{\left( \exp[\Delta\mathrm{MLL}] \right)^{-2/n}} - \frac{\left( \exp[\Delta\mathrm{MLL}] \right)^{-2/n}}{\mathrm{\left( \exp[\Delta\mathrm{MLL}] \right)^{-2/n}}} \\
&= \left( \exp[\Delta\mathrm{MLL}] \right)^{2/n} - 1 \; .
\end{split}
$$