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
theorem: "Maximum likelihood estimator is biased (p = 1)"

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


**Theorem:** Let $y = \left\lbrace y_1, \ldots, y_n \right\rbrace$ be a set of independent [normally distributed](/D/norm) observations with unknown [mean](/D/mean) $\mu$ and [variance](/D/var) $\sigma^2$:

$$ \label{eq:ug}
y_i \overset{\text{i.i.d.}}{\sim} \mathcal{N}(\mu, \sigma^2), \quad i = 1,\ldots,n \; .
$$

Then,

1) the [maximum likelihood estimator](/D/mle) of $\sigma^2$ is

$$ \label{eq:resvar-mle}
\hat{\sigma}^2 = \frac{1}{n} \sum_{i=1}^{n} \left( y_i - \bar{y} \right)^2
$$

where

$$ \label{eq:mean-mle}
\bar{y} = \frac{1}{n} \sum_{i=1}^{n} y_i
$$

2) and $\hat{\sigma}^2$ is a [biased estimator](/D/est-bias) of $\sigma^2$

$$ \label{eq:resvar-var}
\mathrm{E}\left[ \hat{\sigma}^2 \right] \neq \sigma^2 \; ,
$$

more precisely:

$$ \label{eq:resvar-bias}
\mathrm{E}\left[ \hat{\sigma}^2 \right] = \frac{n-1}{n} \sigma^2 \; .
$$


**Proof:**

1) This is equivalent to the [maximum likelihood estimator for the univariate Gaussian with unknown variance](/P/ug-mle) and a special case of the [maximum likelihood estimator for multiple linear regression](/P/mlr-mle) in which $X = 1_n$ and $\hat{\beta} = \bar{y}$:

$$ \label{eq:resvar-mle-qed}
\begin{split}
\hat{\sigma}^2 &= \frac{1}{n} (y-X\hat{\beta})^\mathrm{T} (y-X\hat{\beta}) \\
&= \frac{1}{n} (y - 1_n \bar{y})^\mathrm{T} (y - 1_n \bar{y}) \\
&= \frac{1}{n} \sum_{i=1}^{n} \left( y_i - \bar{y} \right)^2 \; .
\end{split}
$$

2) The [expectation](/D/mean) of the [maximum likelihood estimator](/D/mle) can be developed as follows:

$$ \label{eq:E-resvar-mle-s1}
\begin{split}
\mathrm{E}\left[ \hat{\sigma}^2 \right] &= \mathrm{E}\left[ \frac{1}{n} \sum_{i=1}^{n} \left( y_i - \bar{y} \right)^2 \right] \\
&= \frac{1}{n} \mathrm{E}\left[ \sum_{i=1}^{n} \left( y_i - \bar{y} \right)^2 \right] \\
&= \frac{1}{n} \mathrm{E}\left[ \sum_{i=1}^{n} \left( y_i^2 - 2 y_i \bar{y} + \bar{y}^2 \right) \right] \\
&= \frac{1}{n} \mathrm{E}\left[ \sum_{i=1}^{n} y_i^2 - 2 \sum_{i=1}^{n} y_i \bar{y} + \sum_{i=1}^{n} \bar{y}^2 \right] \\
&= \frac{1}{n} \mathrm{E}\left[ \sum_{i=1}^{n} y_i^2 - 2 n \bar{y}^2 + n \bar{y}^2 \right] \\
&= \frac{1}{n} \mathrm{E}\left[ \sum_{i=1}^{n} y_i^2 - n \bar{y}^2 \right] \\
&= \frac{1}{n} \left( \sum_{i=1}^{n} \mathrm{E} \left[ y_i^2 \right] - n \mathrm{E}\left[ \bar{y}^2 \right] \right) \\
&= \frac{1}{n} \sum_{i=1}^{n} \mathrm{E} \left[ y_i^2 \right] - \mathrm{E}\left[ \bar{y}^2 \right] \\
\end{split}
$$

Due to the [partition of variance into expected values](/P/var-mean)

$$ \label{eq:var-mean}
\mathrm{Var}(X) = \mathrm{E}(X^2) - \mathrm{E}(X)^2 \; ,
$$

we have

$$ \label{eq:Var-yi-yb}
\begin{split}
\mathrm{Var}(y_i) &= \mathrm{E}(y_i^2) - \mathrm{E}(y_i)^2 \\
\mathrm{Var}(\bar{y}) &= \mathrm{E}(\bar{y}^2) - \mathrm{E}(\bar{y})^2 \; ,
\end{split}
$$

such that \eqref{eq:E-resvar-mle-s1} becomes

$$ \label{eq:E-resvar-mle-s2}
\mathrm{E}\left[ \hat{\sigma}^2 \right] = \frac{1}{n} \sum_{i=1}^{n} \left( \mathrm{Var}(y_i) + \mathrm{E}(y_i)^2 \right) - \left( \mathrm{Var}(\bar{y}) + \mathrm{E}(\bar{y})^2 \right) \; .
$$

From \eqref{eq:ug}, it follows that

$$ \label{eq:E-Var-yi}
\mathrm{E}(y_i) = \mu \quad \text{and} \quad \mathrm{Var}(y_i) = \sigma^2 \; .
$$

The [expectation](/D/mean) of $\bar{y}$ given by \eqref{eq:mean-mle} is

$$ \label{eq:E-mean-mle}
\begin{split}
\mathrm{E}\left[ \bar{y} \right] &= \mathrm{E}\left[ \frac{1}{n} \sum_{i=1}^{n} y_i \right] = \frac{1}{n} \sum_{i=1}^{n} \mathrm{E}\left[ y_i \right] \\
&\overset{\eqref{eq:E-Var-yi}}{=} \frac{1}{n} \sum_{i=1}^{n} \mu = \frac{1}{n} \cdot n \cdot \mu \\
&= \mu \; .
\end{split}
$$

The variance of $\bar{y}$ given by \eqref{eq:mean-mle} is

$$ \label{eq:Var-mean-mle}
\begin{split}
\mathrm{Var}\left[ \bar{y} \right] &= \mathrm{Var}\left[ \frac{1}{n} \sum_{i=1}^{n} y_i \right] = \frac{1}{n^2} \sum_{i=1}^{n} \mathrm{Var}\left[ y_i \right] \\
&\overset{\eqref{eq:E-Var-yi}}{=} \frac{1}{n^2} \sum_{i=1}^{n} \sigma^2 = \frac{1}{n^2} \cdot n \cdot \sigma^2 \\
&= \frac{1}{n} \sigma^2 \; .
\end{split}
$$

Plugging \eqref{eq:E-Var-yi}, \eqref{eq:E-mean-mle} and \eqref{eq:Var-mean-mle} into \eqref{eq:E-resvar-mle-s2}, we have

$$ \label{eq:E-resvar-mle-s3}
\begin{split}
\mathrm{E}\left[ \hat{\sigma}^2 \right] &= \frac{1}{n} \sum_{i=1}^{n} \left( \sigma^2 + \mu^2 \right) - \left( \frac{1}{n} \sigma^2 + \mu^2 \right) \\
\mathrm{E}\left[ \hat{\sigma}^2 \right] &= \frac{1}{n} \cdot n \cdot \left( \sigma^2 + \mu^2 \right) - \left( \frac{1}{n} \sigma^2 + \mu^2 \right) \\
\mathrm{E}\left[ \hat{\sigma}^2 \right] &= \sigma^2 + \mu^2 - \frac{1}{n} \sigma^2 - \mu^2 \\
\mathrm{E}\left[ \hat{\sigma}^2 \right] &= \frac{n-1}{n} \sigma^2
\end{split}
$$

which proves the [bias](/D/est-bias) given by \eqref{eq:resvar-bias}.
