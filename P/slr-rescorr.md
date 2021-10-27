---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-10-27 13:07:00

title: "The residuals and the covariate are uncorrelated in simple linear regression"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Simple linear regression"
theorem: "Correlation with covariate is zero"

sources:
  - authors: "Wikipedia"
    year: 2021
    title: "Simple linear regression"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-10-27"
    url: "https://en.wikipedia.org/wiki/Simple_linear_regression#Numerical_properties"

proof_id: "P277"
shortcut: "slr-rescorr"
username: "JoramSoch"
---


**Theorem:** In [simple linear regression](/D/slr), the [residuals](/D/rss) and the [covariate](/D/slr) are [uncorrelated](/D/corr) when estimated using [ordinary least squares](/P/slr-ols).

**Proof:** The residuals are defined as the estimated [error terms](/D/slr)

$$ \label{eq:slr-res}
\hat{\varepsilon}_i = y_i - \hat{\beta}_0 - \hat{\beta}_1 x_i
$$

where $\hat{\beta}_0$ and $\hat{\beta}_1$ are parameter estimates obtained using [ordinary least squares](/P/slr-ols):

$$ \label{eq:slr-ols}
\hat{\beta}_0 = \bar{y} - \hat{\beta}_1 \bar{x} \quad \text{and} \quad \hat{\beta}_1 = \frac{s_{xy}}{s_x^2} \; .
$$

With that, we can calculate the inner product of the covariate and the residuals vector:

$$ \label{eq:slr-rescorr}
\begin{split}
\sum_{i=1}^n x_i \hat{\varepsilon}_i &= \sum_{i=1}^n x_i (y_i - \hat{\beta}_0 - \hat{\beta}_1 x_i) \\
&= \sum_{i=1}^n \left( x_i y_i - \hat{\beta}_0 x_i - \hat{\beta}_1 x_i^2 \right) \\
&= \sum_{i=1}^n \left( x_i y_i - x_i (\bar{y} - \hat{\beta}_1 \bar{x}) - \hat{\beta}_1 x_i^2 \right) \\
&= \sum_{i=1}^n \left( x_i (y_i - \bar{y}) + \hat{\beta}_1 (\bar{x} x_i - x_i^2 \right) \\
&= \sum_{i=1}^n x_i y_i - \bar{y} \sum_{i=1}^n x_i - \hat{\beta}_1 \left( \sum_{i=1}^n x_i^2 - \bar{x} \sum_{i=1}^n x_i \right) \\
&= \left( \sum_{i=1}^n x_i y_i - n \bar{x} \bar{y} - n \bar{x} \bar{y} + n \bar{x} \bar{y} \right) - \hat{\beta}_1 \left( \sum_{i=1}^n x_i^2 - 2 n \bar{x} \bar{x} + n \bar{x}^2 \right) \\
&= \left( \sum_{i=1}^n x_i y_i - \bar{y} \sum_{i=1}^n x_i - \bar{x} \sum_{i=1}^n y_i + n \bar{x} \bar{y} \right) - \hat{\beta}_1 \left( \sum_{i=1}^n x_i^2 - 2 \bar{x} \sum_{i=1}^n x_i + n \bar{x}^2 \right) \\
&= \sum_{i=1}^n \left( x_i y_i - \bar{y} x_i - \bar{x} y_i + \bar{x} \bar{y} \right) - \hat{\beta}_1 \sum_{i=1}^n \left( x_i^2 - 2 \bar{x} x_i + \bar{x}^2 \right) \\
&= \sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y}) - \hat{\beta}_1 \sum_{i=1}^n (x_i - \bar{x})^2 \\
&= (n-1) s_{xy} - \frac{s_{xy}}{s_x^2} (n-1) s_x^2 \\
&= (n-1) s_{xy} - (n-1) s_{xy} \\
&= 0 \; .
\end{split}
$$

Because an inner product of zero also implies zero [correlation](/D/corr), this demonstrates that [residuals](/D/rss) and [covariate](/D/slr) values are uncorrelated under [ordinary least squares](/P/slr-ols).