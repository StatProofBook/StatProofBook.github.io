---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-10-27 13:07:00

title: "The sum of residuals is zero in simple linear regression"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Simple linear regression"
theorem: "Sum of residuals is zero"

sources:
  - authors: "Wikipedia"
    year: 2021
    title: "Simple linear regression"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-10-27"
    url: "https://en.wikipedia.org/wiki/Simple_linear_regression#Numerical_properties"

proof_id: "P276"
shortcut: "slr-ressum"
username: "JoramSoch"
---


**Theorem:** In [simple linear regression](/D/slr), the sum of the [residuals](/D/rss) is zero when estimated using [ordinary least squares](/P/slr-ols).

**Proof:** The residuals are defined as the estimated [error terms](/D/slr)

$$ \label{eq:slr-res}
\hat{\varepsilon}_i = y_i - \hat{\beta}_0 - \hat{\beta}_1 x_i
$$

where $\hat{\beta}_0$ and $\hat{\beta}_1$ are parameter estimates obtained using [ordinary least squares](/P/slr-ols):

$$ \label{eq:slr-ols}
\hat{\beta}_0 = \bar{y} - \hat{\beta}_1 \bar{x} \quad \text{and} \quad \hat{\beta}_1 = \frac{s_{xy}}{s_x^2} \; .
$$

With that, we can calculate the sum of the residuals:

$$ \label{eq:slr-ressum}
\begin{split}
\sum_{i=1}^n \hat{\varepsilon}_i &= \sum_{i=1}^n (y_i - \hat{\beta}_0 - \hat{\beta}_1 x_i) \\
&= \sum_{i=1}^n (y_i - \bar{y} + \hat{\beta}_1 \bar{x} - \hat{\beta}_1 x_i) \\
&= \sum_{i=1}^n y_i - n \bar{y} + \hat{\beta}_1 n \bar{x} - \hat{\beta}_1 \sum_{i=1}^n x_i \\
&= n \bar{y} - n \bar{y} + \hat{\beta}_1 n \bar{x} - \hat{\beta}_1 n \bar{x} \\
&= 0 \; .
\end{split}
$$

Thus, the sum of the [residuals](/D/rss) is zero under [ordinary least squares](/P/slr-ols), if [the model](/D/slr) includes an intercept term $\beta_0$.