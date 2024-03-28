---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2024-03-28 10:34:17

title: "Relationship between F-statistic and maximum log-likelihood"
chapter: "Model Selection"
section: "Goodness-of-fit measures"
topic: "F-statistic"
theorem: "Relationship to maximum log-likelihood"

sources:

proof_id: "P443"
shortcut: "fstat-mll"
username: "JoramSoch"
---


**Theorem:** Given a [linear regression model](/D/mlr) with [independent](/D/ind) observations

$$ \label{eq:mlr}
y = X\beta + \varepsilon, \; \varepsilon_i \overset{\mathrm{i.i.d.}}{\sim} \mathcal{N}(0, \sigma^2) \; ;
$$

the [F-statistic](/D/fstat) can be expressed in terms of the [maximum log-likelihood](/D/mll) as

$$ \label{eq:F-MLL}
F = \left[ \left( \exp[\Delta\mathrm{MLL}] \right)^{2/n} - 1 \right] \cdot \frac{n-p}{p-1}
$$

where $n$ and $p$ are the dimensions of the design matrix $X$ in \eqref{eq:mlr} and $\Delta\mathrm{MLL}$ is the difference in maximum log-likelihood between the model given by \eqref{eq:mlr} and a linear regression model with only a constant regressor.


**Proof:** Under the conditions mentioned in the theorem, the [F-statistic can be expressed in terms of the coefficient of determination](/P/fstat-rsq) as

$$ \label{eq:F-R2}
F = \frac{R^2/(p-1)}{(1-R^2)/(n-p)}
$$

and [R-squared can be expressed in terms of maximum likelihood](/P/rsq-mll) as 

$$ \label{eq:R2-MLL}
R^2 = 1 - \left( \exp[\Delta\mathrm{MLL}] \right)^{-2/n} \; .
$$

Plugging \eqref{eq:R2-MLL} into \eqref{eq:F-R2}, we obtain:

$$ \label{eq:F-MLL-qed}
\begin{split}
F &= \frac{\left( 1 - \left( \exp[\Delta\mathrm{MLL}] \right)^{-2/n} \right)/(p-1)}{\left( \left( \exp[\Delta\mathrm{MLL}] \right)^{-2/n} \right)/(n-p)} \\
&= \left[ \frac{1}{\left( \exp[\Delta\mathrm{MLL}] \right)^{-2/n}} - \frac{\left( \exp[\Delta\mathrm{MLL}] \right)^{-2/n}}{\left( \exp[\Delta\mathrm{MLL}] \right)^{-2/n}} \right] \cdot \frac{n-p}{p-1} \\
&= \left[ \left( \exp[\Delta\mathrm{MLL}] \right)^{2/n} - 1 \right] \cdot \frac{n-p}{p-1} \; .
\end{split}
$$