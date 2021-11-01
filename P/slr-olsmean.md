---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-10-27 09:54:00

title: "Expectation of parameter estimates for simple linear regression"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Simple linear regression"
theorem: "Expectation of estimates"

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

proof_id: "P272"
shortcut: "slr-olsmean"
username: "JoramSoch"
---


**Theorem:** Assume a [simple linear regression model](/D/slr) with independent observations

$$ \label{eq:slr}
y = \beta_0 + \beta_1 x + \varepsilon, \; \varepsilon_i \sim \mathcal{N}(0, \sigma^2), \; i = 1,\ldots,n
$$

and consider estimation using [ordinary least squares](/P/slr-ols). Then, the [expected values](/D/mean) of the estimated parameters are

$$ \label{eq:slr-ols-mean}
\begin{split}
\mathrm{E}(\hat{\beta}_0) &= \beta_0 \\
\mathrm{E}(\hat{\beta}_1) &= \beta_1
\end{split}
$$

which means that the [ordinary least squares solution](/P/slr-ols) produces [unbiased estimators](/D/est-unb).


**Proof:** According to the simple linear regression model in \eqref{eq:slr}, the expectation of a single data point is

$$ \label{eq:E-yi}
\mathrm{E}(y_i) = \beta_0 + \beta_1 x_i \; .
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

$$ \label{eq:sum-ci}
\begin{split}
\sum_{i=1}^n c_i &= \frac{\sum_{i=1}^n (x_i - \bar{x})}{\sum_{i=1}^n (x_i - \bar{x})^2} = \frac{\sum_{i=1}^n x_i - n \bar{x}}{\sum_{i=1}^n (x_i - \bar{x})^2} \\
&= \frac{n \bar{x} - n \bar{x}}{\sum_{i=1}^n (x_i - \bar{x})^2} = 0 \; , \\
\end{split}
$$

and

$$ \label{eq:sum-ci-xi}
\begin{split}
\sum_{i=1}^n c_i x_i &= \frac{\sum_{i=1}^n (x_i - \bar{x}) x_i}{\sum_{i=1}^n (x_i - \bar{x})^2} = \frac{\sum_{i=1}^n \left( x_i^2 - \bar{x} x_i \right)}{\sum_{i=1}^n (x_i - \bar{x})^2} \\
&= \frac{\sum_{i=1}^n x_i^2 - 2 n \bar{x} \bar{x} + n \bar{x}^2}{\sum_{i=1}^n (x_i - \bar{x})^2} = \frac{\sum_{i=1}^n \left( x_i^2 - 2 \bar{x} x_i + \bar{x}^2 \right)}{\sum_{i=1}^n (x_i - \bar{x})^2} \\
&= \frac{\sum_{i=1}^n (x_i - \bar{x})^2}{\sum_{i=1}^n (x_i - \bar{x})^2} = 1 \; .
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

and with \eqref{eq:E-yi}, \eqref{eq:sum-ci} and \eqref{eq:sum-ci-xi}, its expectation becomes:

$$ \label{eq:E-b1}
\begin{split}
\mathrm{E}(\hat{\beta}_1) &= \mathrm{E}\left( \sum_{i=1}^n c_i y_i - \bar{y} \sum_{i=1}^n c_i \right) \\
&= \sum_{i=1}^n c_i \mathrm{E}(y_i) - \bar{y} \sum_{i=1}^n c_i \\
&= \beta_1 \sum_{i=1}^n c_i x_i + \beta_0 \sum_{i=1}^n c_i - \bar{y} \sum_{i=1}^n c_i \\
&= \beta_1 \; .
\end{split}
$$

Finally, with \eqref{eq:E-yi} and \eqref{eq:E-b1}, the expectation of the intercept estimate from \eqref{eq:slr-ols} becomes

$$ \label{eq:E-b0}
\begin{split}
\mathrm{E}(\hat{\beta}_0) &= \mathrm{E}\left( \frac{1}{n} \sum_{i=1}^n y_i - \hat{\beta}_1 \cdot \frac{1}{n} \sum_{i=1}^n x_i \right) \\
&= \frac{1}{n} \sum_{i=1}^n \mathrm{E}(y_i) - \mathrm{E}(\hat{\beta}_1) \cdot \bar{x} \\
&= \frac{1}{n} \sum_{i=1}^n (\beta_0 + \beta_1 x_i) - \beta_1 \cdot \bar{x} \\
&= \beta_0 + \beta_1 \bar{x} - \beta_1 \bar{x} \\
&= \beta_0 \; .
\end{split}
$$