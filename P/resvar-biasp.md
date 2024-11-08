---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-12-21 14:15:00

title: "Maximum likelihood estimator of variance in multiple linear regression is biased"
chapter: "Model Selection"
section: "Goodness-of-fit measures"
topic: "Residual variance"
theorem: "Maximum likelihood estimator is biased (p > 1)"

sources:
  - authors: "ocram"
    year: 2022
    title: "Why is RSS distributed chi square times n-p?"
    in: "StackExchange CrossValidated"
    pages: "retrieved on 2022-12-21"
    url: "https://stats.stackexchange.com/a/20230"

proof_id: "P398"
shortcut: "resvar-biasp"
username: "JoramSoch"
---


**Theorem:** Consider a [linear regression model](/D/mlr) with known design matrix $X$, known covariance structure $V$, unknown regression parameters $\beta$ and unknown noise variance $\sigma^2$:

$$ \label{eq:mlr}
y = X\beta + \varepsilon, \; \varepsilon \sim \mathcal{N}(0, \sigma^2 V) \; .
$$

Then,

1) the [maximum likelihood estimator](/D/mle) of $\sigma^2$ is

$$ \label{eq:sigma-mle}
\hat{\sigma}^2 = \frac{1}{n} (y-X\hat{\beta})^\mathrm{T} V^{-1} (y-X\hat{\beta})
$$

where

$$ \label{eq:beta-mle}
\hat{\beta} = (X^\mathrm{T} V^{-1} X)^{-1} X^\mathrm{T} V^{-1} y
$$

2) and $\hat{\sigma}^2$ is a [biased estimator](/D/est-bias) of $\sigma^2$

$$ \label{eq:resvar-var}
\mathrm{E}\left[ \hat{\sigma}^2 \right] \neq \sigma^2 \; ,
$$

more precisely:

$$ \label{eq:resvar-biasp}
\mathrm{E}\left[ \hat{\sigma}^2 \right] = \frac{n-p}{n} \sigma^2 \; .
$$


**Proof:** 

1) This follows from [maximum likelihood estimation for multiple linear regression](/P/mlr-mle) and [is a special case](/P/mlr-glm) of [maximum likelihood estimation for the general linear model](/P/glm-mle) in which $Y = y$, $B = \beta$ and $\Sigma = \sigma^2$:

$$ \label{eq:sigma-mle-qed}
\begin{split}
\hat{\sigma}^2 &= \frac{1}{n} (Y-X\hat{B})^\mathrm{T} V^{-1} (Y-X\hat{B}) \\
&= \frac{1}{n} (y-X\hat{\beta})^\mathrm{T} V^{-1} (y-X\hat{\beta}) \; .
\end{split}
$$

2) We know that [the residual sum of squares, divided by the true noise variance, is following a chi-squared distribution](/P/mlr-rssdist):

$$ \label{eq:rss-dist}
\begin{split}
\frac{\hat{\varepsilon}^\mathrm{T} \hat{\varepsilon}}{\sigma^2} &\sim \chi^2(n-p) \\
\text{where} \quad \hat{\varepsilon}^\mathrm{T} \hat{\varepsilon} &= (y-X\hat{\beta})^\mathrm{T} V^{-1} (y-X\hat{\beta}) \; .
\end{split}
$$

Thus, combining \eqref{eq:rss-dist} and \eqref{eq:sigma-mle-qed}, we have:

$$ \label{eq:resvar-bias-s1}
\frac{n \hat{\sigma}^2}{\sigma^2} \sim \chi^2(n-p) \; .
$$

Using the [relationship between chi-squared distribution and gamma distribution](/P/chi2-gam)

$$ \label{eq:chi2-gam}
X \sim \chi^2(k) \quad \Rightarrow \quad cX \sim \mathrm{Gam}\left( \frac{k}{2}, \frac{1}{2c} \right) \; ,
$$

we can deduce from \eqref{eq:resvar-bias-s1} that

$$ \label{eq:resvar-bias-s2}
\hat{\sigma}^2 = \frac{\sigma^2}{n} \cdot \frac{n \hat{\sigma}^2}{\sigma^2} \sim \mathrm{Gam}\left( \frac{n-p}{2}, \frac{n}{2\sigma^2} \right) \; .
$$

Using the [expected value of the gamma distribution](/P/gam-mean)

$$ \label{eq:gam-mean}
X \sim \mathrm{Gam}(a,b) \quad \Rightarrow \quad \mathrm{E}(X) = \frac{a}{b} \; ,
$$

we can deduce from \eqref{eq:resvar-bias-s2} that

$$ \label{eq:resvar-bias-s3}
\mathrm{E}\left[ \hat{\sigma}^2 \right] = \frac{\frac{n-p}{2}}{\frac{n}{2\sigma^2}} = \frac{n-p}{n} \sigma^2
$$

which proves the relationship given by \eqref{eq:resvar-biasp}.