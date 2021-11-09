---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-10-27 11:53:00

title: "Variance of parameter estimates for simple linear regression"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Simple linear regression"
theorem: "Variance of estimates"

sources:
  - authors: "Penny, William"
    year: 2006
    title: "Finding the uncertainty in estimating the slope"
    in: "Mathematics for Brain Imaging"
    pages: "ch. 1.2.4, pp. 18-20, eq. 1.37"
    url: "https://ueapsylabs.co.uk/sites/wpenny/mbi/mbi_course.pdf"
  - authors: "Wikipedia"
    year: 2021
    title: "Proofs involving ordinary least squares"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-10-27"
    url: "https://en.wikipedia.org/wiki/Proofs_involving_ordinary_least_squares#Unbiasedness_and_variance_of_%7F'%22%60UNIQ--postMath-00000037-QINU%60%22'%7F"

proof_id: "P273"
shortcut: "slr-olsvar"
username: "JoramSoch"
---


**Theorem:** Assume a [simple linear regression model](/D/slr) with independent observations

$$ \label{eq:slr}
y = \beta_0 + \beta_1 x + \varepsilon, \; \varepsilon_i \sim \mathcal{N}(0, \sigma^2), \; i = 1,\ldots,n
$$

and consider estimation using [ordinary least squares](/P/slr-ols). Then, the [variances](/D/var) of the estimated parameters are

$$ \label{eq:slr-ols-var}
\begin{split}
\mathrm{Var}(\hat{\beta}_0) &= \frac{x^\mathrm{T} x}{n} \cdot \frac{\sigma^2}{(n-1) s_x^2} \\
\mathrm{Var}(\hat{\beta}_1) &= \frac{\sigma^2}{(n-1) s_x^2}
\end{split}
$$

where $s_x^2$ is the [sample variance](/D/var-samp) of $x$ and $x^\mathrm{T} x$ is the sum of squared values of the covariate.


**Proof:** According to the simple linear regression model in \eqref{eq:slr}, the variance of a single data point is

$$ \label{eq:Var-yi}
\mathrm{Var}(y_i) = \mathrm{Var}(\varepsilon_i) = \sigma^2 \; .
$$

The [ordinary least squares estimates for simple linear regression](/P/slr-ols) are given by

$$ \label{eq:slr-ols}
\begin{split}
\hat{\beta}_0 &= \frac{1}{n} \sum_{i=1}^n y_i - \hat{\beta}_1 \cdot \frac{1}{n} \sum_{i=1}^n x_i \\
\hat{\beta}_1 &= \frac{\sum_{i=1}^n (x_i - \bar{x}) (y_i - \bar{y})}{\sum_{i=1}^n (x_i - \bar{x})^2} \; .
\end{split}
$$

If we define the following quantity

$$ \label{eq:ci}
c_i = \frac{x_i - \bar{x}}{\sum_{i=1}^n (x_i - \bar{x})^2} \; ,
$$

we note that

$$ \label{eq:sum-ci2}
\begin{split}
\sum_{i=1}^n c_i^2 &= \sum_{i=1}^n \left( \frac{x_i - \bar{x}}{\sum_{i=1}^n (x_i - \bar{x})^2} \right)^2 \\
&= \frac{\sum_{i=1}^n (x_i - \bar{x})^2}{\left[ \sum_{i=1}^n (x_i - \bar{x})^2 \right]^2} \\
&= \frac{1}{\sum_{i=1}^n (x_i - \bar{x})^2} \; .
\end{split}
$$

With \eqref{eq:ci}, the estimate for the slope from \eqref{eq:slr-ols} becomes

$$ \label{eq:slr-ols-sl}
\begin{split}
\hat{\beta}_1 &= \frac{\sum_{i=1}^n (x_i - \bar{x}) (y_i - \bar{y})}{\sum_{i=1}^n (x_i - \bar{x})^2} \\
&= \sum_{i=1}^n c_i (y_i - \bar{y}) \\
&= \sum_{i=1}^n c_i y_i - \bar{y} \sum_{i=1}^n c_i
\end{split}
$$

and with \eqref{eq:Var-yi} and \eqref{eq:sum-ci2} as well as [invariance](/P/var-inv), [scaling](/P/var-scal) and [additivity](/P/var-add) of the variance, the variance of $\hat{\beta}_1$ is:

$$ \label{eq:Var-b1}
\begin{split}
\mathrm{Var}(\hat{\beta}_1) &= \mathrm{Var}\left( \sum_{i=1}^n c_i y_i - \bar{y} \sum_{i=1}^n c_i \right) \\
&= \mathrm{Var}\left( \sum_{i=1}^n c_i y_i \right) \\
&= \sum_{i=1}^n c_i^2 \mathrm{Var}(y_i) \\
&= \sigma^2 \sum_{i=1}^n c_i^2 \\
&= \sigma^2 \frac{1}{\sum_{i=1}^n (x_i - \bar{x})^2} \\
&= \frac{\sigma^2}{(n-1) \frac{1}{n-1} \sum_{i=1}^n (x_i - \bar{x})^2} \\
&= \frac{\sigma^2}{(n-1) s_x^2} \; .
\end{split}
$$

Finally, with \eqref{eq:Var-yi} and \eqref{eq:Var-b1}, the variance of the intercept estimate from \eqref{eq:slr-ols} becomes:

$$ \label{eq:Var-b0-s1}
\begin{split}
\mathrm{Var}(\hat{\beta}_0) &= \mathrm{Var}\left( \frac{1}{n} \sum_{i=1}^n y_i - \hat{\beta}_1 \cdot \frac{1}{n} \sum_{i=1}^n x_i \right) \\
&= \mathrm{Var}\left( \frac{1}{n} \sum_{i=1}^n y_i \right) + \mathrm{Var}\left( \hat{\beta}_1 \cdot \bar{x} \right) \\
&= \left( \frac{1}{n} \right)^2 \sum_{i=1}^n \mathrm{Var}(y_i) + \bar{x}^2 \cdot \mathrm{Var}(\hat{\beta}_1) \\
&= \frac{1}{n^2} \sum_{i=1}^n \sigma^2 + \bar{x}^2 \frac{\sigma^2}{(n-1) s_x^2} \\
&= \frac{\sigma^2}{n} + \frac{\sigma^2 \bar{x}^2 }{(n-1) s_x^2} \; .
\end{split}
$$

Applying the formula for the [sample variance](/D/var-samp) $s_x^2$, we finally get:

$$ \label{eq:Var-b0-s2}
\begin{split}
\mathrm{Var}(\hat{\beta}_0) &= \sigma^2 \left( \frac{1}{n} + \frac{\bar{x}^2}{\sum_{i=1}^n (x_i - \bar{x})^2} \right) \\
&= \sigma^2 \left( \frac{\frac{1}{n}\sum_{i=1}^n (x_i - \bar{x})^2}{\sum_{i=1}^n (x_i - \bar{x})^2} + \frac{\bar{x}^2}{\sum_{i=1}^n (x_i - \bar{x})^2} \right) \\
&= \sigma^2 \left( \frac{\frac{1}{n}\sum_{i=1}^n \left( x_i^2 - 2 \bar{x} x_i + \bar{x}^2 \right) + \bar{x}^2}{\sum_{i=1}^n (x_i - \bar{x})^2} \right) \\
&= \sigma^2 \left( \frac{\left( \frac{1}{n}\sum_{i=1}^n x_i^2 - 2 \bar{x} \frac{1}{n}\sum_{i=1}^n x_i + \bar{x}^2 \right) + \bar{x}^2}{\sum_{i=1}^n (x_i - \bar{x})^2} \right) \\
&= \sigma^2 \left( \frac{\frac{1}{n}\sum_{i=1}^n x_i^2 - 2 \bar{x}^2 + 2 \bar{x}^2}{\sum_{i=1}^n (x_i - \bar{x})^2} \right) \\
&= \sigma^2 \left( \frac{\frac{1}{n}\sum_{i=1}^n x_i^2}{(n-1) \frac{1}{n-1} \sum_{i=1}^n (x_i - \bar{x})^2} \right) \\
&= \frac{x^\mathrm{T} x}{n} \cdot \frac{\sigma^2}{(n-1) s_x^2} \; .
\end{split}
$$