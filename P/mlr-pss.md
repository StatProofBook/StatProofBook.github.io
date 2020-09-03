---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-03-09 22:18:00

title: "Partition of sums of squares in ordinary least squares"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Multiple linear regression"
theorem: "Total, explained and residual sum of squares"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Partition of sums of squares"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-03-09"
    url: "https://en.wikipedia.org/wiki/Partition_of_sums_of_squares#Partitioning_the_sum_of_squares_in_linear_regression"

proof_id: "P76"
shortcut: "mlr-pss"
username: "JoramSoch"
---


**Theorem:** Assume a [linear regression model](/D/mlr) with independent observations

$$ \label{eq:mlr}
y = X\beta + \varepsilon, \; \varepsilon_i \overset{\mathrm{i.i.d.}}{\sim} \mathcal{N}(0, \sigma^2) \; ,
$$

and let $X$ contain a constant regressor $1_n$ modelling the intercept term. Then, it holds that

$$ \label{eq:pss}
\mathrm{TSS} = \mathrm{ESS} + \mathrm{RSS}
$$

where $\mathrm{TSS}$ is the [total sum of squares](/D/tss), $\mathrm{ESS}$ is the [explained sum of squares](/D/ess) and $\mathrm{RSS}$ is the [residual sum of squares](/D/rss).


**Proof:** The [total sum of squares](/D/tss) is given by

$$ \label{eq:TSS}
\mathrm{TSS} = \sum_{i=1}^{n} (y_i - \bar{y})^2
$$

where $\bar{y}$ is the mean across all $y_i$. The $\mathrm{TSS}$ can be rewritten as

$$ \label{eq:TSS-s1}
\begin{split}
\mathrm{TSS} &= \sum_{i=1}^{n} (y_i - \bar{y} + \hat{y}_i - \hat{y}_i)^2 \\
&= \sum_{i=1}^{n} \left( (\hat{y}_i - \bar{y}) + (y_i - \hat{y}_i) \right)^2 \\
&= \sum_{i=1}^{n} \left( (\hat{y}_i - \bar{y}) + \hat{\varepsilon}_i \right)^2 \\
&= \sum_{i=1}^{n} \left( (\hat{y}_i - \bar{y})^2 + 2 \, \hat{\varepsilon}_i (\hat{y}_i - \bar{y}) + \hat{\varepsilon}_i^2 \right) \\
&= \sum_{i=1}^{n} (\hat{y}_i - \bar{y})^2 + \sum_{i=1}^{n} \hat{\varepsilon}_i^2 + 2 \sum_{i=1}^{n} \hat{\varepsilon}_i (\hat{y}_i - \bar{y}) \\
&= \sum_{i=1}^{n} (\hat{y}_i - \bar{y})^2 + \sum_{i=1}^{n} \hat{\varepsilon}_i^2 + 2 \sum_{i=1}^{n} \hat{\varepsilon}_i (x_i \hat{\beta} - \bar{y}) \\
&= \sum_{i=1}^{n} (\hat{y}_i - \bar{y})^2 + \sum_{i=1}^{n} \hat{\varepsilon}_i^2 + 2 \sum_{i=1}^{n} \hat{\varepsilon}_i \left( \sum_{j=1}^{p} x_{ij} \hat{\beta}_j \right) - 2 \sum_{i=1}^{n} \hat{\varepsilon}_i \, \bar{y} \\
&= \sum_{i=1}^{n} (\hat{y}_i - \bar{y})^2 + \sum_{i=1}^{n} \hat{\varepsilon}_i^2 + 2 \sum_{j=1}^{p} \hat{\beta}_j \sum_{i=1}^{n} \hat{\varepsilon}_i x_{ij} - 2 \bar{y} \sum_{i=1}^{n} \hat{\varepsilon}_i \\
\end{split}
$$

The fact that the design matrix includes a constant regressor ensures that

$$ \label{eq:e-est-sum}
\sum_{i=1}^{n} \hat{\varepsilon}_i = \hat{\varepsilon}^\mathrm{T} 1_n = 0
$$

and because the [residuals are orthogonal to the design matrix](/P/mlr-ols), we have

$$ \label{eq:X-e-orth}
\sum_{i=1}^{n} \hat{\varepsilon}_i x_{ij} = \hat{\varepsilon}^\mathrm{T} x_j = 0 \; .
$$

Applying \eqref{eq:e-est-sum} and \eqref{eq:X-e-orth} to \eqref{eq:TSS-s1}, this becomes

$$ \label{eq:TSS-s2}
\mathrm{TSS} = \sum_{i=1}^{n} (\hat{y}_i - \bar{y})^2 + \sum_{i=1}^{n} \hat{\varepsilon}_i^2
$$

and, with the definitions of [explained](/D/ess) and [residual sum of squares](/D/rss), it is

$$ \label{eq:TSS-s3}
\mathrm{TSS} = \mathrm{ESS} + \mathrm{RSS} \; .
$$