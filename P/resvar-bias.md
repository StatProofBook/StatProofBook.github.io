---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-02-24 23:44:00

title: "Maximum likelihood estimator of variance is biased"
chapter: "Model Selection"
section: "Goodness-of-fit measures"
topic: "Residual variance"
theorem: "Maximum likelihood estimator is biased"

sources:
  - authors: "Liang, Dawen"
    year: "????"
    title: "Maximum Likelihood Estimator for Variance is Biased: Proof"
    pages: "retrieved on 2020-02-24"
    url: "https://dawenl.github.io/files/mle_biased.pdf"

proof_id: "P61"
shortcut: "resvar-bias"
username: "JoramSoch"
---


**Theorem:** Let $x = \left\lbrace x_1, \ldots, x_n \right\rbrace$ be a set of independent [normally distributed](/D/norm) observations with unknown [mean](/D/mean) $\mu$ and [variance](/D/var) $\sigma^2$:

$$ \label{eq:ug}
x_i \overset{\text{i.i.d.}}{\sim} \mathcal{N}(\mu, \sigma^2), \quad i = 1,\ldots,n \; .
$$

Then,

1) the [maximum likelihood estimator](/D/mle) of $\sigma^2$ is

$$ \label{eq:resvar-mle}
\hat{\sigma}^2 = \frac{1}{n} \sum_{i=1}^{n} \left( x_i - \bar{x} \right)^2
$$

where

$$ \label{eq:mean-mle}
\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i
$$

2) and $\hat{\sigma}^2$ is a [biased estimator](/D/est-unb) of $\sigma^2$

$$ \label{eq:resvar-var}
\mathbb{E}\left[ \hat{\sigma}^2 \right] \neq \sigma^2 \; ,
$$

more precisely:

$$ \label{eq:resvar-bias}
\mathbb{E}\left[ \hat{\sigma}^2 \right] = \frac{n-1}{n} \sigma^2 \; .
$$


**Proof:**

1) This is equivalent to the [maximum likelihood estimator for the univariate Gaussian with unknown variance](/P/ug-mle) and a special case of the [maximum likelihood estimator for multiple linear regression](/P/mlr-mle) in which $y = x$, $X = 1_n$ and $\hat{\beta} = \bar{x}$:

$$ \label{eq:resvar-mle-qed}
\begin{split}
\hat{\sigma}^2 &= \frac{1}{n} (y-X\hat{\beta})^\mathrm{T} (y-X\hat{\beta}) \\
&= \frac{1}{n} (x - 1_n \bar{x})^\mathrm{T} (x - 1_n \bar{x}) \\
&= \frac{1}{n} \sum_{i=1}^{n} \left( x_i - \bar{x} \right)^2 \; .
\end{split}
$$

2) The [expectation](/D/mean) of the [maximum likelihood estimator](/D/mle) can be developed as follows:

$$ \label{eq:E-resvar-mle-s1}
\begin{split}
\mathbb{E}\left[ \hat{\sigma}^2 \right] &= \mathbb{E}\left[ \frac{1}{n} \sum_{i=1}^{n} \left( x_i - \bar{x} \right)^2 \right] \\
&= \frac{1}{n} \mathbb{E}\left[ \sum_{i=1}^{n} \left( x_i - \bar{x} \right)^2 \right] \\
&= \frac{1}{n} \mathbb{E}\left[ \sum_{i=1}^{n} \left( x_i^2 - 2 x_i \bar{x} + \bar{x}^2 \right) \right] \\
&= \frac{1}{n} \mathbb{E}\left[ \sum_{i=1}^{n} x_i^2 - 2 \sum_{i=1}^{n} x_i \bar{x} + \sum_{i=1}^{n} \bar{x}^2 \right] \\
&= \frac{1}{n} \mathbb{E}\left[ \sum_{i=1}^{n} x_i^2 - 2 n \bar{x}^2 + n \bar{x}^2 \right] \\
&= \frac{1}{n} \mathbb{E}\left[ \sum_{i=1}^{n} x_i^2 - n \bar{x}^2 \right] \\
&= \frac{1}{n} \left( \sum_{i=1}^{n} \mathbb{E} \left[ x_i^2 \right] - n \mathbb{E}\left[ \bar{x}^2 \right] \right) \\
&= \frac{1}{n} \sum_{i=1}^{n} \mathbb{E} \left[ x_i^2 \right] - \mathbb{E}\left[ \bar{x}^2 \right] \\
\end{split}
$$

Due to the [partition of variance into expected values](/P/var-mean)

$$ \label{eq:var-mean}
\mathrm{Var}(X) = \mathbb{E}(X^2) - \mathbb{E}(X)^2 \; ,
$$

we have

$$ \label{eq:Var-xi-xb}
\begin{split}
\mathrm{Var}(x_i) &= \mathbb{E}(x_i^2) - \mathbb{E}(x_i)^2 \\
\mathrm{Var}(\bar{x}) &= \mathbb{E}(\bar{x}^2) - \mathbb{E}(\bar{x})^2 \; ,
\end{split}
$$

such that \eqref{eq:E-resvar-mle-s1} becomes

$$ \label{eq:E-resvar-mle-s2}
\mathbb{E}\left[ \hat{\sigma}^2 \right] = \frac{1}{n} \sum_{i=1}^{n} \left( \mathrm{Var}(x_i) + \mathbb{E}(x_i)^2 \right) - \left( \mathrm{Var}(\bar{x}) + \mathbb{E}(\bar{x})^2 \right) \; .
$$

From \eqref{eq:ug}, it follows that

$$ \label{eq:E-Var-xi}
\mathbb{E}(x_i) = \mu \quad \text{and} \quad \mathrm{Var}(x_i) = \sigma^2 \; .
$$

The [expectation](/D/mean) of $\bar{x}$ given by \eqref{eq:mean-mle} is

$$ \label{eq:E-mean-mle}
\begin{split}
\mathbb{E}\left[ \bar{x} \right] &= \mathbb{E}\left[ \frac{1}{n} \sum_{i=1}^{n} x_i \right] = \frac{1}{n} \sum_{i=1}^{n} \mathbb{E}\left[ x_i \right] \\
&\overset{\eqref{eq:E-Var-xi}}{=} \frac{1}{n} \sum_{i=1}^{n} \mu = \frac{1}{n} \cdot n \cdot \mu \\
&= \mu \; .
\end{split}
$$

The variance of $\bar{x}$ given by \eqref{eq:mean-mle} is

$$ \label{eq:Var-mean-mle}
\begin{split}
\mathrm{Var}\left[ \bar{x} \right] &= \mathrm{Var}\left[ \frac{1}{n} \sum_{i=1}^{n} x_i \right] = \frac{1}{n^2} \sum_{i=1}^{n} \mathrm{Var}\left[ x_i \right] \\
&\overset{\eqref{eq:E-Var-xi}}{=} \frac{1}{n^2} \sum_{i=1}^{n} \sigma^2 = \frac{1}{n^2} \cdot n \cdot \sigma^2 \\
&= \frac{1}{n} \sigma^2 \; .
\end{split}
$$

Plugging \eqref{eq:E-Var-xi}, \eqref{eq:E-mean-mle} and \eqref{eq:Var-mean-mle} into \eqref{eq:E-resvar-mle-s2}, we have

$$ \label{eq:E-resvar-mle-s3}
\begin{split}
\mathbb{E}\left[ \hat{\sigma}^2 \right] &= \frac{1}{n} \sum_{i=1}^{n} \left( \sigma^2 + \mu^2 \right) - \left( \frac{1}{n} \sigma^2 + \mu^2 \right) \\
\mathbb{E}\left[ \hat{\sigma}^2 \right] &= \frac{1}{n} \cdot n \cdot \left( \sigma^2 + \mu^2 \right) - \left( \frac{1}{n} \sigma^2 + \mu^2 \right) \\
\mathbb{E}\left[ \hat{\sigma}^2 \right] &= \sigma^2 + \mu^2 - \frac{1}{n} \sigma^2 - \mu^2 \\
\mathbb{E}\left[ \hat{\sigma}^2 \right] &= \frac{n-1}{n} \sigma^2
\end{split}
$$

which proves the [bias](/D/est-unb) given by \eqref{eq:resvar-bias}.
