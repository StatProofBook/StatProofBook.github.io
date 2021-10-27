---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-10-27 08:56:00

title: "Ordinary least squares for simple linear regression"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Simple linear regression"
theorem: "Ordinary least squares"

sources:
  - authors: "Penny, William"
    year: 2006
    title: "Linear regression"
    in: "Mathematics for Brain Imaging"
    pages: "ch. 1.2.2, pp. 14-16, eqs. 1.24/1.25"
    url: "https://ueapsylabs.co.uk/sites/wpenny/mbi/mbi_course.pdf"
  - authors: "Wikipedia"
    year: 2021
    title: "Proofs involving ordinary least squares"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-10-27"
    url: "https://en.wikipedia.org/wiki/Proofs_involving_ordinary_least_squares#Derivation_of_simple_linear_regression_estimators"

proof_id: "P271"
shortcut: "slr-ols"
username: "JoramSoch"
---


**Theorem:** Given a [simple linear regression model](/D/slr) with independent observations

$$ \label{eq:slr}
y = \beta_0 + \beta_1 x + \varepsilon, \; \varepsilon_i \sim \mathcal{N}(0, \sigma^2), \; i = 1,\ldots,n \; ,
$$

the parameters minimizing the [residual sum of squares](/D/rss) are given by

$$ \label{eq:slr-ols}
\begin{split}
\hat{\beta}_0 &= \bar{y} - \hat{\beta}_1 \bar{x} \\
\hat{\beta}_1 &= \frac{s_{xy}}{s_x^2}
\end{split}
$$

where $\bar{x}$ and $\bar{y}$ are the [sample means](/D/mean-samp), $s_x^2$ is the [sample variance](/D/var-samp) of $x$ and $s_{xy}$ is the [sample covariance](/D/cov-samp) between $x$ and $y$.


**Proof:** The [residual sum of squares](/D/rss) is defined as

$$ \label{eq:rss}
\mathrm{RSS}(\beta_0,\beta_1) = \sum_{i=1}^n \varepsilon_i^2 = \sum_{i=1}^n (y_i - \beta_0 - \beta_1 x_i)^2 \; .
$$

The derivatives of $\mathrm{RSS}(\beta_0,\beta_1)$ with respect to $\beta_0$ and $\beta_1$ are

$$ \label{eq:rss-der}
\begin{split}
\frac{\mathrm{d}\mathrm{RSS}(\beta_0,\beta_1)}{\mathrm{d}\beta_0} &= \sum_{i=1}^n 2 (y_i - \beta_0 - \beta_1 x_i) (-1) \\
&= -2 \sum_{i=1}^n (y_i - \beta_0 - \beta_1 x_i) \\
\frac{\mathrm{d}\mathrm{RSS}(\beta_0,\beta_1)}{\mathrm{d}\beta_1} &= \sum_{i=1}^n 2 (y_i - \beta_0 - \beta_1 x_i) (-x_i) \\
&= -2 \sum_{i=1}^n (x_i y_i - \beta_0 x_i - \beta_1 x_i^2)
\end{split}
$$

and setting these derivatives to zero

$$ \label{eq:rss-der-zero}
\begin{split}
0 &= -2 \sum_{i=1}^n (y_i - \hat{\beta}_0 - \hat{\beta}_1 x_i) \\
0 &= -2 \sum_{i=1}^n (x_i y_i - \hat{\beta}_0 x_i - \hat{\beta}_1 x_i^2)
\end{split}
$$

yields the following equations:

$$ \label{eq:slr-norm-eq}
\begin{split}
\hat{\beta}_1 \sum_{i=1}^n x_i + \hat{\beta}_0 \cdot n &= \sum_{i=1}^n y_i \\
\hat{\beta}_1 \sum_{i=1}^n x_i^2 + \hat{\beta}_0 \sum_{i=1}^n x_i &= \sum_{i=1}^n x_i y_i \; .
\end{split}
$$

From the first equation, we can derive the estimate for the intercept:

$$ \label{eq:slr-ols-int}
\begin{split}
\hat{\beta}_0 &= \frac{1}{n} \sum_{i=1}^n y_i - \hat{\beta}_1 \cdot \frac{1}{n} \sum_{i=1}^n x_i \\
&= \bar{y} - \hat{\beta}_1 \bar{x} \; .
\end{split}
$$

From the second equation, we can derive the estimate for the slope:

$$ \label{eq:slr-ols-sl}
\begin{split}
\hat{\beta}_1 \sum_{i=1}^n x_i^2 + \hat{\beta}_0 \sum_{i=1}^n x_i &= \sum_{i=1}^n x_i y_i \\
\hat{\beta}_1 \sum_{i=1}^n x_i^2 + \left( \bar{y} - \hat{\beta}_1 \bar{x} \right) \sum_{i=1}^n x_i &\overset{\eqref{eq:slr-ols-int}}{=} \sum_{i=1}^n x_i y_i \\
\hat{\beta}_1 \left( \sum_{i=1}^n x_i^2 - \bar{x} \sum_{i=1}^n x_i \right) &= \sum_{i=1}^n x_i y_i - \bar{y} \sum_{i=1}^n x_i \\
\hat{\beta}_1 &= \frac{\sum_{i=1}^n x_i y_i - \bar{y} \sum_{i=1}^n x_i}{\sum_{i=1}^n x_i^2 - \bar{x} \sum_{i=1}^n x_i} \; .
\end{split}
$$

Note that the numerator can be rewritten as

$$ \label{eq:slr-ols-sl-num}
\begin{split}
\sum_{i=1}^n x_i y_i - \bar{y} \sum_{i=1}^n x_i &= \sum_{i=1}^n x_i y_i - n \bar{x} \bar{y} \\
&= \sum_{i=1}^n x_i y_i - n \bar{x} \bar{y} - n \bar{x} \bar{y} + n \bar{x} \bar{y} \\
&= \sum_{i=1}^n x_i y_i - \bar{y} \sum_{i=1}^n x_i - \bar{x} \sum_{i=1}^n y_i + \sum_{i=1}^n \bar{x} \bar{y} \\
&= \sum_{i=1}^n \left( x_i y_i - x_i \bar{y} - \bar{x} y_i + \bar{x} \bar{y} \right) \\
&= \sum_{i=1}^n (x_i - \bar{x}) (y_i - \bar{y})
\end{split}
$$

and that the denominator can be rewritten as

$$ \label{eq:slr-ols-sl-den}
\begin{split}
\sum_{i=1}^n x_i^2 - \bar{x} \sum_{i=1}^n x_i &= \sum_{i=1}^n x_i^2 - n \bar{x}^2 \\
&= \sum_{i=1}^n x_i^2 - 2 n \bar{x} \bar{x} + n \bar{x}^2 \\
&= \sum_{i=1}^n x_i^2 - 2 \bar{x} \sum_{i=1}^n x_i - \sum_{i=1}^n \bar{x}^2 \\
&= \sum_{i=1}^n \left( x_i^2 - 2 \bar{x} x_i + \bar{x}^2 \right) \\
&= \sum_{i=1}^n (x_i - \bar{x})^2 \; .
\end{split}
$$

With \eqref{eq:slr-ols-sl-num} and \eqref{eq:slr-ols-sl-den}, the estimate from \eqref{eq:slr-ols-sl} can be simplified as follows:

$$ \label{eq:slr-ols-sl-qed}
\begin{split}
\hat{\beta}_1 &= \frac{\sum_{i=1}^n x_i y_i - \bar{y} \sum_{i=1}^n x_i}{\sum_{i=1}^n x_i^2 - \bar{x} \sum_{i=1}^n x_i} \\
&= \frac{\sum_{i=1}^n (x_i - \bar{x}) (y_i - \bar{y})}{\sum_{i=1}^n (x_i - \bar{x})^2} \\
&= \frac{\frac{1}{n-1} \sum_{i=1}^n (x_i - \bar{x}) (y_i - \bar{y})}{\frac{1}{n-1} \sum_{i=1}^n (x_i - \bar{x})^2} \\
&= \frac{s_{xy}}{s_x^2} \; .
\end{split}
$$

Together, \eqref{eq:slr-ols-int} and \eqref{eq:slr-ols-sl-qed} constitute the ordinary least squares parameter estimates for simple linear regression.