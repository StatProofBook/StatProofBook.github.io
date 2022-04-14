---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-04-14 17:17:00

title: "Parameter estimates for simple linear regression are uncorrelated after mean-centering"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Simple linear regression"
theorem: "Correlation of estimates"

sources:

proof_id: "P320"
shortcut: "slr-olscorr"
username: "JoramSoch"
---


**Theorem:** In [simple linear regression](/D/slr), when the independent variable $x$ is [mean-centered](/D/mean), the [ordinary least squares](/P/slr-ols) estimates for slope and intercept are [uncorrelated](/D/corr).


**Proof:** The [parameter estimates for simple linear regression are bivariate normally distributed under ordinary least squares](/P/slr-olsdist):

$$ \label{eq:slr-olsdist}
\left[ \begin{matrix} \hat{\beta}_0 \\ \hat{\beta}_1 \end{matrix} \right] \sim \mathcal{N}\left( \left[ \begin{matrix} \beta_0 \\ \beta_1 \end{matrix} \right], \, \frac{\sigma^2}{(n-1) \, s_x^2} \cdot \left[ \begin{matrix} x^\mathrm{T}x/n & -\bar{x} \\ -\bar{x} & 1 \end{matrix} \right] \right)
$$

Because the [covariance matrix](/D/covmat) of the [multivariate normal distribution](/D/mvn) contains the pairwise covariances of the [random variables](/D/rvar), we can deduce that the [covariance](/D/cov) of $\hat{\beta}_0$ and $\hat{\beta}_1$ is:

$$ \label{eq:slr-olscov}
\mathrm{Cov}\left( \hat{\beta}_0, \hat{\beta}_1 \right) = -\frac{\sigma^2 \, \bar{x}}{(n-1) \, s_x^2}
$$

where $\sigma^2$ is the [noise variance](/D/slr), $s_x^2$ is the [sample variance](/D/var-samp) of $x$ and $n$ is the number of observations. When $x$ is mean-centered, we have $\bar{x} = 0$, such that:

$$ \label{eq:slr-olscov-meancent}
\mathrm{Cov}\left( \hat{\beta}_0, \hat{\beta}_1 \right) = 0 \; .
$$

Because [correlation is equal to covariance divided by standard deviations](/D/corr), we can conclude that the correlation of $\hat{\beta}_0$ and $\hat{\beta}_1$ is also zero:

$$ \label{eq:slr-olscorr-qed}
\mathrm{Corr}\left( \hat{\beta}_0, \hat{\beta}_1 \right) = 0 \; .
$$