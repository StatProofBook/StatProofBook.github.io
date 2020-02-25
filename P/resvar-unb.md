---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-02-25 15:38:00

title: "Construction of unbiased estimator for variance"
chapter: "Model Selection"
section: "Goodness-of-fit measures"
topic: "Residual variance"
theorem: "Construction of unbiased estimator"

sources:
  - authors: "Liang, Dawen"
    year: "????"
    title: "Maximum Likelihood Estimator for Variance is Biased: Proof"
    pages: "retrieved on 2020-02-25"
    url: "https://dawenl.github.io/files/mle_biased.pdf"

proof_id: "P62"
shortcut: "resvar-unb"
username: "JoramSoch"
---


**Theorem:** Let $x = \left\lbrace x_1, \ldots, x_n \right\rbrace$ be a set of independent [normally distributed](/D/norm) observations with unknown [mean](/D/mean) $\mu$ and [variance](/D/var) $\sigma^2$:

$$ \label{eq:ug}
x_i \overset{\text{i.i.d.}}{\sim} \mathcal{N}(\mu, \sigma^2), \quad i = 1,\ldots,n \; .
$$

An [unbiased estimator](/D/est-unb) of $\sigma^2$ is given by

$$ \label{eq:resvar-unb}
\hat{\sigma}^2_{\mathrm{unb}} = \frac{1}{n-1} \sum_{i=1}^{n} \left( x_i - \bar{x} \right)^2 \; .
$$


**Proof:** [It can be shown that](/P/resvar-bias) the [maximum likelihood estimator](/D/mle) of $\sigma^2$

$$ \label{eq:resvar-mle}
\hat{\sigma}^2_{\mathrm{MLE}} = \frac{1}{n} \sum_{i=1}^{n} \left( x_i - \bar{x} \right)^2
$$

is a [biased estimator](/D/est-unb) in the sense that

$$ \label{eq:resvar-bias}
\mathbb{E}\left[ \hat{\sigma}^2_{\mathrm{MLE}} \right] = \frac{n-1}{n} \sigma^2 \; .
$$

From \eqref{eq:resvar-bias}, it follows that

$$ \label{eq:resvar-bias-adj}
\begin{split}
\mathbb{E}\left[ \frac{n}{n-1} \hat{\sigma}^2_{\mathrm{MLE}} \right] &= \frac{n}{n-1} \mathbb{E}\left[ \hat{\sigma}^2_{\mathrm{MLE}} \right] \\
&\overset{\eqref{eq:resvar-bias}}{=} \frac{n}{n-1} \cdot \frac{n-1}{n} \sigma^2 \\
&= \sigma^2 \; ,
\end{split}
$$

such that an [unbiased estimator](/D/est-unb) can be constructed as

$$ \label{eq:resvar-unb-qed}
\begin{split}
\hat{\sigma}^2_{\mathrm{unb}} &= \frac{n}{n-1} \hat{\sigma}^2_{\mathrm{MLE}} \\
&\overset{\eqref{eq:resvar-mle}}{=} \frac{n}{n-1} \cdot \frac{1}{n} \sum_{i=1}^{n} \left( x_i - \bar{x} \right)^2 \\
&= \frac{1}{n-1} \sum_{i=1}^{n} \left( x_i - \bar{x} \right)^2 \; .
\end{split}
$$