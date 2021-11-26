---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-11-16 09:36:00

title: "Ordinary least squares for simple linear regression"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Simple linear regression"
theorem: "Ordinary least squares"

sources:

proof_id: "P288"
shortcut: "slr-ols2"
username: "JoramSoch"
---


**Theorem:** Given a [simple linear regression model](/D/slr) with independent observations

$$ \label{eq:slr}
y_i = \beta_0 + \beta_1 x_i + \varepsilon_i, \; \varepsilon_i \sim \mathcal{N}(0, \sigma^2), \; i = 1,\ldots,n \; ,
$$

the parameters minimizing the [residual sum of squares](/D/rss) are given by

$$ \label{eq:slr-ols}
\begin{split}
\hat{\beta}_0 &= \bar{y} - \hat{\beta}_1 \bar{x} \\
\hat{\beta}_1 &= \frac{s_{xy}}{s_x^2}
\end{split}
$$

where $\bar{x}$ and $\bar{y}$ are the [sample means](/D/mean-samp), $s_x^2$ is the [sample variance](/D/var-samp) of $x$ and $s_{xy}$ is the [sample covariance](/D/cov-samp) between $x$ and $y$.


**Proof:** [Simple linear regression is a special case of multiple linear regression](/P/slr-mlr) with

$$ \label{eq:slr-mlr}
X = \left[ \begin{matrix} 1_n & x \end{matrix} \right] \quad \text{and} \quad \beta = \left[ \begin{matrix} \beta_0 \\ \beta_1 \end{matrix} \right]
$$

and [ordinary least sqaures estimates](/P/mlr-ols) are given by

$$ \label{eq:mlr-ols}
\hat{\beta} = (X^\mathrm{T} X)^{-1} X^\mathrm{T} y \; .
$$

Writing out equation \eqref{eq:mlr-ols}, we have

$$ \label{eq:slr-ols-b}
\begin{split}
\hat{\beta} &= \left( \left[ \begin{matrix} 1_n^\mathrm{T} \\ x^\mathrm{T} \end{matrix} \right] \left[ \begin{matrix} 1_n & x \end{matrix} \right] \right)^{-1} \left[ \begin{matrix} 1_n^\mathrm{T} \\ x^\mathrm{T} \end{matrix} \right] y \\
&= \left( \left[ \begin{matrix} n & n\bar{x} \\ n\bar{x} & x^\mathrm{T} x \end{matrix} \right] \right)^{-1} \left[ \begin{matrix} n \bar{y} \\ x^\mathrm{T} y \end{matrix} \right] \\
&= \frac{1}{n x^\mathrm{T} x - (n\bar{x})^2} \left[ \begin{matrix} x^\mathrm{T} x & -n\bar{x} \\ -n\bar{x} & n \end{matrix} \right]  \left[ \begin{matrix} n \bar{y} \\ x^\mathrm{T} y \end{matrix} \right] \\
&= \frac{1}{n x^\mathrm{T} x - (n\bar{x})^2} \left[ \begin{matrix} n \bar{y} \, x^\mathrm{T} x - n \bar{x} \, x^\mathrm{T} y \\ n \, x^\mathrm{T} y - (n \bar{x})(n \bar{y}) \end{matrix} \right] \; .
\end{split}
$$

Thus, the second entry of $\hat{\beta}$ [is equal to](/P/slr-ols):

$$ \label{eq:slr-ols-b1}
\begin{split}
\hat{\beta}_1 &= \frac{n \, x^\mathrm{T} y - (n \bar{x})(n \bar{y})}{n x^\mathrm{T} x - (n\bar{x})^2} \\
&= \frac{x^\mathrm{T} y - n \bar{x} \bar{y}}{x^\mathrm{T} x - n \bar{x}^2} \\
&= \frac{\sum_{i=1}^n x_i y_i - \sum_{i=1}^n \bar{x} \bar{y}}{\sum_{i=1}^n x_i^2 - \sum_{i=1}^n \bar{x}^2} \\
&= \frac{\sum_{i=1}^n (x_i - \bar{x}) (y_i - \bar{y})}{\sum_{i=1}^n (x_i - \bar{x})^2} \\
&= \frac{s_{xy}}{s_x^2} \; .
\end{split}
$$

Moreover, the first entry of $\hat{\beta}$ is equal to:

$$ \label{eq:slr-ols-b2}
\begin{split}
\hat{\beta}_0 &= \frac{n \bar{y} \, x^\mathrm{T} x - n \bar{x} \, x^\mathrm{T} y}{n x^\mathrm{T} x - (n\bar{x})^2} \\
&= \frac{\bar{y} \, x^\mathrm{T} x - \bar{x} \, x^\mathrm{T} y}{x^\mathrm{T} x - n \bar{x}^2} \\
&= \frac{\bar{y} \, x^\mathrm{T} x - \bar{x} \, x^\mathrm{T} y + n \bar{x}^2 \bar{y} - n \bar{x}^2 \bar{y}}{x^\mathrm{T} x - n \bar{x}^2} \\
&= \frac{\bar{y} (x^\mathrm{T} x - n \bar{x}^2) - \bar{x} (x^\mathrm{T} y - n \bar{x} \bar{y})}{x^\mathrm{T} x - n \bar{x}^2} \\
&= \frac{\bar{y} (x^\mathrm{T} x - n \bar{x}^2)}{x^\mathrm{T} x - n \bar{x}^2} - \frac{\bar{x} (x^\mathrm{T} y - n \bar{x} \bar{y})}{x^\mathrm{T} x - n \bar{x}^2} \\
&= \bar{y} - \bar{x} \, \frac{\sum_{i=1}^n x_i y_i - \sum_{i=1}^n \bar{x} \bar{y}}{\sum_{i=1}^n x_i^2 - \sum_{i=1}^n \bar{x}^2} \\
&= \bar{y} - \hat{\beta}_1 \bar{x} \; .
\end{split}
$$