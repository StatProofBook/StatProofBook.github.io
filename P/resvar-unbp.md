---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2024-03-08 10:09:24

title: "Construction of unbiased estimator for variance in multiple linear regression"
chapter: "Model Selection"
section: "Goodness-of-fit measures"
topic: "Residual variance"
theorem: "Construction of unbiased estimator (p > 1)"

sources:

proof_id: "P439"
shortcut: "resvar-unbp"
username: "JoramSoch"
---


**Theorem:** Consider a [linear regression model](/D/mlr) with known design matrix $X$, known covariance structure $V$, unknown regression parameters $\beta$ and unknown noise variance $\sigma^2$:

$$ \label{eq:mlr}
y = X\beta + \varepsilon, \; \varepsilon \sim \mathcal{N}(0, \sigma^2 V) \; .
$$

An [unbiased estimator](/D/est-unb) of $\sigma^2$ is given by

$$ \label{eq:sigma-unb}
\hat{\sigma}^2 = \frac{1}{n-p} (y-X\hat{\beta})^\mathrm{T} V^{-1} (y-X\hat{\beta})
$$

where

$$ \label{eq:beta-mle}
\hat{\beta} = (X^\mathrm{T} V^{-1} X)^{-1} X^\mathrm{T} V^{-1} y \; .
$$


**Proof:** [It can be shown that](/P/resvar-biasp) the [maximum likelihood estimator](/D/mle) of $\sigma^2$

$$ \label{eq:resvar-mle}
\hat{\sigma}^2_{\mathrm{MLE}} = \frac{1}{n} (y-X\hat{\beta})^\mathrm{T} V^{-1} (y-X\hat{\beta})
$$

is a [biased estimator](/D/est-unb) in the sense that

$$ \label{eq:resvar-bias}
\mathbb{E}\left[ \hat{\sigma}^2_{\mathrm{MLE}} \right] = \frac{n-p}{n} \sigma^2 \; .
$$

From \eqref{eq:resvar-bias}, it follows that

$$ \label{eq:resvar-bias-adj}
\begin{split}
\mathbb{E}\left[ \frac{n}{n-p} \hat{\sigma}^2_{\mathrm{MLE}} \right] &= \frac{n}{n-p} \mathbb{E}\left[ \hat{\sigma}^2_{\mathrm{MLE}} \right] \\
&\overset{\eqref{eq:resvar-bias}}{=} \frac{n}{n-p} \cdot \frac{n-p}{n} \sigma^2 \\
&= \sigma^2 \; ,
\end{split}
$$

such that an [unbiased estimator](/D/est-unb) can be constructed as

$$ \label{eq:resvar-unb-qed}
\begin{split}
\hat{\sigma}^2_{\mathrm{unb}} &= \frac{n}{n-p} \hat{\sigma}^2_{\mathrm{MLE}} \\
&\overset{\eqref{eq:resvar-mle}}{=} \frac{n}{n-p} \cdot \frac{1}{n} (y-X\hat{\beta})^\mathrm{T} V^{-1} (y-X\hat{\beta}) \\
&= \frac{1}{n-p} (y-X\hat{\beta})^\mathrm{T} V^{-1} (y-X\hat{\beta}) \; .
\end{split}
$$