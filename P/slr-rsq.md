---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-10-27 15:31:00

title: "Relationship between coefficient of determination and correlation coefficient in simple linear regression"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Simple linear regression"
theorem: "Coefficient of determination in terms of correlation coefficient"

sources:
  - authors: "Wikipedia"
    year: 2021
    title: "Simple linear regression"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-10-27"
    url: "https://en.wikipedia.org/wiki/Simple_linear_regression#Fitting_the_regression_line"
  - authors: "Wikipedia"
    year: 2021
    title: "Coefficient of determination"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-10-27"
    url: "https://en.wikipedia.org/wiki/Coefficient_of_determination#As_squared_correlation_coefficient"
  - authors: "Wikipedia"
    year: 2021
    title: "Correlation"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-10-27"
    url: "https://en.wikipedia.org/wiki/Correlation#Sample_correlation_coefficient"

proof_id: "P280"
shortcut: "slr-rsq"
username: "JoramSoch"
---


**Theorem:** Assume a [simple linear regression model](/D/slr) with independent observations

$$ \label{eq:slr}
y = \beta_0 + \beta_1 x + \varepsilon, \; \varepsilon_i \sim \mathcal{N}(0, \sigma^2), \; i = 1,\ldots,n
$$

and consider estimation using [ordinary least squares](/P/slr-ols). Then, the [coefficient of determination](/D/rsq) is equal to the squared [correlation coefficient](/D/corr) between $x$ and $y$:

$$ \label{eq:slr-R2}
R^2 = r_{xy}^2 \; .
$$


**Proof:** The [ordinary least squares estimates for simple linear regression](/P/slr-ols) are

$$ \label{eq:slr-ols}
\begin{split}
\hat{\beta}_0 &= \bar{y} - \hat{\beta}_1 \bar{x} \\
\hat{\beta}_1 &= \frac{s_{xy}}{s_x^2} \; .
\end{split}
$$

The [coefficient of determination](/D/rsq) $R^2$ is defined as the proportion of the variance explained by the independent variables, relative to the total variance in the data. This can be quantified as the ratio of [explained sum of squares](/D/ess) to [total sum of squares](/D/tss):

$$ \label{eq:slr-R2-s1}
R^2 = \frac{\mathrm{ESS}}{\mathrm{TSS}} \; .
$$

Using the [explained and total sum of squares for simple linear regression](/P/slr-sss), we have:

$$ \label{eq:slr-R2-s2}
\begin{split}
R^2 &= \frac{\sum_{i=1}^{n} (\hat{y}_i - \bar{y})^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2} \\
&= \frac{\sum_{i=1}^{n} (\hat{\beta}_0 + \hat{\beta}_1 x_i - \bar{y})^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2} \; .
\end{split}
$$

By applying \eqref{eq:slr-ols}, we can further develop the coefficient of determination:

$$ \label{eq:slr-R2-s3}
\begin{split}
R^2 &= \frac{\sum_{i=1}^{n} (\bar{y} - \hat{\beta}_1 \bar{x} + \hat{\beta}_1 x_i - \bar{y})^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2} \\
&= \frac{\sum_{i=1}^{n} \left( \hat{\beta}_1 (x_i - \bar{x}) \right)^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2} \\
&= \hat{\beta}_1^2 \, \frac{\frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2}{\frac{1}{n-1} \sum_{i=1}^{n} (y_i - \bar{y})^2} \\
&= \hat{\beta}_1^2 \, \frac{s_x^2}{s_y^2} \\ 
&= \left( \frac{s_x}{s_y} \, \hat{\beta}_1 \right)^2 \; .
\end{split}
$$

Using the [relationship between correlation coefficient and slope estimate](/P/slr-corr), we conclude:

$$ \label{eq:slr-R2-qed}
R^2 = \left( \frac{s_x}{s_y} \, \hat{\beta}_1 \right)^2 = r_{xy}^2 \; .
$$