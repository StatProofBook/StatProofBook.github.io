---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-11-16 11:53:00

title: "Maximum likelihood estimation for simple linear regression"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Simple linear regression"
theorem: "Maximum likelihood estimation"

sources:

proof_id: "P290"
shortcut: "slr-mle2"
username: "JoramSoch"
---


**Theorem:** Given a [simple linear regression model](/D/mlr) with independent observations

$$ \label{eq:slr}
y_i = \beta_0 + \beta_1 x_i + \varepsilon_i, \; \varepsilon_i \sim \mathcal{N}(0, \sigma^2), \; i = 1,\ldots,n \; ,
$$

the [maximum likelihood estimates](/D/mle) of $\beta_0$, $\beta_1$ and $\sigma^2$ are given by

$$ \label{eq:slr-mle}
\begin{split}
\hat{\beta}_0 &= \bar{y} - \hat{\beta}_1 \bar{x} \\
\hat{\beta}_1 &= \frac{s_{xy}}{s_x^2} \\
\hat{\sigma}^2 &= \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{\beta}_0 - \hat{\beta}_1 x_i)^2
\end{split}
$$

where $\bar{x}$ and $\bar{y}$ are the [sample means](/D/mean-samp), $s_x^2$ is the [sample variance](/D/var-samp) of $x$ and $s_{xy}$ is the [sample covariance](/D/cov-samp) between $x$ and $y$.


**Proof:** [Simple linear regression is a special case of multiple linear regression](/P/slr-mlr) with

$$ \label{eq:slr-mlr}
X = \left[ \begin{matrix} 1_n & x \end{matrix} \right] \quad \text{and} \quad \beta = \left[ \begin{matrix} \beta_0 \\ \beta_1 \end{matrix} \right]
$$

and [weighted least sqaures estimates](/P/mlr-mle) are given by

$$ \label{eq:mlr-mle}
\begin{split}
\hat{\beta} &= (X^\mathrm{T} V^{-1} X)^{-1} X^\mathrm{T} V^{-1} y \\
\hat{\sigma}^2 &= \frac{1}{n} (y-X\hat{\beta})^\mathrm{T} V^{-1} (y-X\hat{\beta}) \; .
\end{split}
$$

Under independent observations, the covariance matrix is

$$ \label{eq:mlr-ind}
V = I_n, \quad \text{such that} \quad V^{-1} = I_n \; .
$$

Thus, we can write out the estimate of $\beta$

$$ \label{eq:slr-mle-b}
\begin{split}
\hat{\beta} &= \left( \left[ \begin{matrix} 1_n^\mathrm{T} \\ x^\mathrm{T} \end{matrix} \right] V^{-1} \left[ \begin{matrix} 1_n & x \end{matrix} \right] \right)^{-1} \left[ \begin{matrix} 1_n^\mathrm{T} \\ x^\mathrm{T} \end{matrix} \right] V^{-1} y \\
&= \left( \left[ \begin{matrix} 1_n^\mathrm{T} \\ x^\mathrm{T} \end{matrix} \right] \left[ \begin{matrix} 1_n & x \end{matrix} \right] \right)^{-1} \left[ \begin{matrix} 1_n^\mathrm{T} \\ x^\mathrm{T} \end{matrix} \right] y
\end{split}
$$

which [is equal to the ordinary least squares solution for simple linear regression](/P/slr-ols2):

$$ \label{eq:slr-mle-b-qed}
\begin{split}
\hat{\beta}_0 &= \bar{y} - \hat{\beta}_1 \bar{x} \\
\hat{\beta}_1 &= \frac{s_{xy}}{s_x^2} \; .
\end{split}
$$

Additionally, we can write out the estimate of $\sigma^2$:

$$ \label{eq:slr-mle-s2}
\begin{split}
\hat{\sigma}^2 &= \frac{1}{n} (y-X\hat{\beta})^\mathrm{T} V^{-1} (y-X\hat{\beta}) \\
&= \frac{1}{n} \left( y - \left[ \begin{matrix} 1_n & x \end{matrix} \right] \left[ \begin{matrix} \hat{\beta}_0 \\ \hat{\beta}_1 \end{matrix} \right] \right)^\mathrm{T} \left( y - \left[ \begin{matrix} 1_n & x \end{matrix} \right] \left[ \begin{matrix} \hat{\beta}_0 \\ \hat{\beta}_1 \end{matrix} \right] \right) \\
&= \frac{1}{n} \left( y - \hat{\beta}_0 - \hat{\beta}_1 x \right)^\mathrm{T} \left( y - \hat{\beta}_0 - \hat{\beta}_1 x \right) \\
&= \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{\beta}_0 - \hat{\beta}_1 x_i)^2 \; .
\end{split}
$$