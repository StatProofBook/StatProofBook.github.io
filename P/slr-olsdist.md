---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-11-09 09:09:00

title: "Distribution of parameter estimates for simple linear regression"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Simple linear regression"
theorem: "Distribution of estimates"

sources:
  - authors: "Wikipedia"
    year: 2021
    title: "Proofs involving ordinary least squares"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-11-09"
    url: "https://en.wikipedia.org/wiki/Proofs_involving_ordinary_least_squares#Unbiasedness_and_variance_of_%7F'%22%60UNIQ--postMath-00000037-QINU%60%22'%7F"

proof_id: "P282"
shortcut: "slr-olsdist"
username: "JoramSoch"
---


**Theorem:** Assume a [simple linear regression model](/D/slr) with independent observations

$$ \label{eq:slr}
y = \beta_0 + \beta_1 x + \varepsilon, \; \varepsilon_i \sim \mathcal{N}(0, \sigma^2)
$$

and consider estimation using [ordinary least squares](/P/slr-ols). Then, the estimated parameters are [normally distributed](/D/mvn) as

$$ \label{eq:slr-olsdist}
\left[ \begin{matrix} \hat{\beta}_0 \\ \hat{\beta}_1 \end{matrix} \right] \sim \mathcal{N}\left( \left[ \begin{matrix} \beta_0 \\ \beta_1 \end{matrix} \right], \, \frac{\sigma^2}{(n-1) \, s_x^2} \cdot \left[ \begin{matrix} x^\mathrm{T}x/n & -\bar{x} \\ -\bar{x} & 1 \end{matrix} \right] \right)
$$

where $\bar{x}$ is the [sample mean](/D/mean-samp) and $s_x^2$ is the [sample variance](/D/var-samp) of $x$.


**Proof:** [Simple linear regression is a special case of multiple linear regression](/P/slr-mlr) with

$$ \label{eq:slr-mlr}
X = \left[ \begin{matrix} 1_n & x \end{matrix} \right] \quad \text{and} \quad \beta = \left[ \begin{matrix} \beta_0 \\ \beta_1 \end{matrix} \right] \; ,
$$

such that \eqref{eq:slr} can also be written as

$$ \label{eq:mlr}
y = X\beta + \varepsilon, \; \varepsilon \sim \mathcal{N}(0, \sigma^2 I_n)
$$

and [ordinary least sqaures estimates](/P/mlr-ols) are given by

$$ \label{eq:mlr-ols}
\hat{\beta} = (X^\mathrm{T} X)^{-1} X^\mathrm{T} y \; .
$$

From \eqref{eq:mlr} and the [linear transformation theorem for the multivariate normal distribution](/P/mvn-ltt), it follows that

$$ \label{eq:y-dist}
y \sim \mathcal{N}\left( X\beta, \, \sigma^2 I_n \right) \; .
$$

From \eqref{eq:mlr-ols}, in combination with \eqref{eq:y-dist} and the [transformation theorem](/P/mvn-ltt), it follows that

$$ \label{eq:b-est-dist}
\begin{split}
\hat{\beta} &\sim \mathcal{N}\left( (X^\mathrm{T} X)^{-1} X^\mathrm{T} X\beta, \, \sigma^2 (X^\mathrm{T} X)^{-1} X^\mathrm{T} I_n X (X^\mathrm{T} X)^{-1} \right) \\
&\sim \mathcal{N}\left( \beta, \, \sigma^2 (X^\mathrm{T} X)^{-1} \right) \; .
\end{split}
$$

Applying \eqref{eq:slr-mlr}, the [covariance matrix](/D/mvn) can be further developed as follows:

$$ \label{eq:b-est-cov}
\begin{split}
\sigma^2 (X^\mathrm{T} X)^{-1} &= \sigma^2 \left( \left[ \begin{matrix} 1_n^\mathrm{T} \\ x^\mathrm{T} \end{matrix} \right] \left[ \begin{matrix} 1_n & x \end{matrix} \right] \right)^{-1} \\
&= \sigma^2 \left( \left[ \begin{matrix} n & n\bar{x} \\ n\bar{x} & x^\mathrm{T} x \end{matrix} \right] \right)^{-1} \\
&= \frac{\sigma^2}{n x^\mathrm{T} x - (n\bar{x})^2} \left[ \begin{matrix} x^\mathrm{T} x & -n\bar{x} \\ -n\bar{x} & n \end{matrix} \right] \\
&= \frac{\sigma^2}{x^\mathrm{T} x - n\bar{x}^2} \left[ \begin{matrix} x^\mathrm{T} x/n & -\bar{x} \\ -\bar{x} & 1 \end{matrix} \right] \; .
\end{split}
$$

Note that the denominator in the first factor is equal to

$$ \label{eq:b-est-cov-den}
\begin{split}
x^\mathrm{T} x - n\bar{x}^2 &= x^\mathrm{T} x - 2 n\bar{x}^2 + n\bar{x}^2 \\
&= \sum_{i=1}^{n} x_i^2 - 2 n \bar{x} \frac{1}{n} \sum_{i=1}^{n} x_i + \sum_{i=1}^{n} \bar{x}^2 \\
&= \sum_{i=1}^{n} x_i^2 - 2 \sum_{i=1}^{n} x_i \bar{x} + \sum_{i=1}^{n} \bar{x}^2 \\
&= \sum_{i=1}^{n} \left( x_i^2 - 2 x_i \bar{x} + \bar{x}^2 \right) \\
&= \sum_{i=1}^{n} \left( x_i^2 - \bar{x} \right)^2 \\
&= (n-1) \, s_x^2 \; .
\end{split}
$$

Thus, combining \eqref{eq:b-est-dist}, \eqref{eq:b-est-cov} and \eqref{eq:b-est-cov-den}, we have

$$ \label{eq:slr-olsdist-qed}
\hat{\beta} \sim \mathcal{N}\left( \beta, \, \frac{\sigma^2}{(n-1) \, s_x^2} \cdot \left[ \begin{matrix} x^\mathrm{T}x/n & -\bar{x} \\ -\bar{x} & 1 \end{matrix} \right] \right)
$$

which is equivalent to equation \eqref{eq:slr-olsdist}.