---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-02-03 18:43:00

title: "Ordinary least squares for multiple linear regression"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Multiple linear regression"
theorem: "Ordinary least squares"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Proofs involving ordinary least squares"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-02-03"
    url: "https://en.wikipedia.org/wiki/Proofs_involving_ordinary_least_squares#Least_squares_estimator_for_%CE%B2"
  - authors: "ad"
    year: 2015
    title: "Derivation of the Least Squares Estimator for Beta in Matrix Notation"
    in: "Economic Theory Blog"
    pages: "retrieved on 2021-05-27"
    url: "https://economictheoryblog.com/2015/02/19/ols_estimator/"

proof_id: "P40"
shortcut: "mlr-ols2"
username: "JoramSoch"
---


**Theorem:** Given a [linear regression model](/D/mlr) with independent observations

$$ \label{eq:MLR}
y = X\beta + \varepsilon, \; \varepsilon_i \overset{\mathrm{i.i.d.}}{\sim} \mathcal{N}(0, \sigma^2) \; ,
$$

the parameters minimizing the [residual sum of squares](/D/rss) are given by

$$ \label{eq:OLS}
\hat{\beta} = (X^\mathrm{T} X)^{-1} X^\mathrm{T} y \; .
$$


**Proof:** The [residual sum of squares](/D/rss) is defined as

$$ \label{eq:RSS}
\mathrm{RSS}(\beta) = \sum_{i=1}^n \varepsilon_i^2 = \varepsilon^\mathrm{T} \varepsilon = (y-X\beta)^\mathrm{T} (y-X\beta)
$$

which can be developed into

$$ \label{eq:RSS-dev}
\begin{split}
\mathrm{RSS}(\beta) &= y^\mathrm{T} y - y^\mathrm{T} X \beta - \beta^\mathrm{T} X^\mathrm{T} y + \beta^\mathrm{T} X^\mathrm{T} X \beta \\
&= y^\mathrm{T} y - 2 \beta^\mathrm{T} X^\mathrm{T} y + \beta^\mathrm{T} X^\mathrm{T} X \beta \; .
\end{split}
$$

The derivative of $\mathrm{RSS}(\beta)$ with respect to $\beta$ is

$$ \label{eq:RSS-der}
\frac{\mathrm{d}\mathrm{RSS}(\beta)}{\mathrm{d}\beta} = - 2 X^\mathrm{T} y + 2 X^\mathrm{T} X \beta
$$

and setting this deriative to zero, we obtain:

$$ \label{eq:OLS-qed}
\begin{split}
\frac{\mathrm{d}\mathrm{RSS}(\hat{\beta})}{\mathrm{d}\beta} &= 0 \\
0 &= - 2 X^\mathrm{T} y + 2 X^\mathrm{T} X \hat{\beta} \\
X^\mathrm{T} X \hat{\beta} &= X^\mathrm{T} y \\
\hat{\beta} &= (X^\mathrm{T} X)^{-1} X^\mathrm{T} y \; .
\end{split}
$$

Since the quadratic form $y^\mathrm{T} y$ in \eqref{eq:RSS-dev} is positive, $\hat{\beta}$ minimizes $\mathrm{RSS}(\beta)$.