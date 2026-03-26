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


**Theorem:** In [simple linear regression](/D/slr), the [residuals](/D/rss) and the [covariate](/D/slr) are [uncorrelated](/D/corr-samp) when [estimated using ordinary least squares](/P/slr-ols).


**Proof:** [Signal and covariate in simple linear regression](/D/slr) are given as

$$ \label{eq:slr-y-x}
y = \left[ \begin{matrix} y_1 \\ \vdots \\ y_n \end{matrix} \right]
\quad \mathrm{and} \quad
x = \left[ \begin{matrix} x_1 \\ \vdots \\ x_n \end{matrix} \right] \; .
$$

The [residuals](/D/rss) are defined as the [estimated](/D/est) [error terms](/D/slr)

$$ \label{eq:slr-res}
\hat{\varepsilon}_i = y_i - \hat{\beta}_0 - \hat{\beta}_1 x_i
$$

where $\hat{\beta}_0$ and $\hat{\beta}_1$ are parameter estimates [obtained using ordinary least squares](/P/slr-ols):

$$ \label{eq:slr-ols}
\hat{\beta}_0 = \bar{y} - \hat{\beta}_1 \bar{x} \quad \text{and} \quad \hat{\beta}_1 = \frac{s_{xy}}{s_x^2} \; .
$$

The [sample correlation coefficient](/D/corr-samp) of covariate and residuals is defined as:

$$ \label{eq:r-xe}
  r_{x\hat{\varepsilon}}
= \mathrm{Corr}(x,\hat{\varepsilon})
= \frac{\sum_{i=1}^n (x_i-\bar{x}) (\hat{\varepsilon}_i-\bar{\hat{\varepsilon}})}{\sqrt{\sum_{i=1}^n (x_i-\bar{x})^2} \sqrt{\sum_{i=1}^n (\hat{\varepsilon}_i-\bar{\hat{\varepsilon}})^2}} \; .
$$

The [sum of residuals in simple linear regression is zero](/P/slr-ressum):

$$ \label{eq:slr-ressum}
\sum_{i=1}^n \hat{\varepsilon}_i = 0 \; .
$$

From that, it follows that the residual mean is zero

$$ \label{eq:slr-resmean}
\bar{\hat{\varepsilon}} = \frac{1}{n} \sum_{i=1}^n \hat{\varepsilon}_i = 0
$$

and that the following covariate-residual term is also zero

$$ \label{eq:sum-xe}
\sum_{i=1}^n \bar{x} \hat{\varepsilon}_i = \bar{x} \sum_{i=1}^n \hat{\varepsilon}_i = 0 \; .
$$

With that, the numerator of the sample correlation becomes:

$$ \label{eq:slr-rescov}
\begin{split}
   \sum_{i=1}^n (x_i-\bar{x}) (\hat{\varepsilon}_i-\bar{\hat{\varepsilon}})
&= \sum_{i=1}^n \left( x_i \hat{\varepsilon}_i - x_i \bar{\hat{\varepsilon}} - \bar{x} \hat{\varepsilon}_i + \bar{x} \bar{\hat{\varepsilon}} \right) \\
&= \sum_{i=1}^n x_i \hat{\varepsilon}_i
 - \sum_{i=1}^n x_i \bar{\hat{\varepsilon}}
 - \sum_{i=1}^n \bar{x} \hat{\varepsilon}_i
 + \sum_{i=1}^n \bar{x} \bar{\hat{\varepsilon}} \\
&= \sum_{i=1}^n x_i \hat{\varepsilon}_i
 - \bar{\hat{\varepsilon}} \sum_{i=1}^n x_i
 - \bar{x} \sum_{i=1}^n \hat{\varepsilon}_i
 + n \bar{x} \bar{\hat{\varepsilon}} \\
&= \sum_{i=1}^n x_i \hat{\varepsilon}_i \; .
\end{split}
$$

Thus, we only need to calculate the inner product of covariate and residuals vector:

$$ \label{eq:slr-rescorr-s1}
\begin{split}
   \sum_{i=1}^n x_i \hat{\varepsilon}_i
&= \sum_{i=1}^n x_i (y_i - \hat{\beta}_0 - \hat{\beta}_1 x_i) \\
&= \sum_{i=1}^n \left( x_i y_i - \hat{\beta}_0 x_i - \hat{\beta}_1 x_i^2 \right) \\
&= \sum_{i=1}^n \left( x_i y_i - x_i (\bar{y} - \hat{\beta}_1 \bar{x}) - \hat{\beta}_1 x_i^2 \right) \\
&= \sum_{i=1}^n \left( x_i (y_i - \bar{y}) + \hat{\beta}_1 (\bar{x} x_i - x_i^2) \right) \\
&= \sum_{i=1}^n x_i y_i - \bar{y} \sum_{i=1}^n x_i - \hat{\beta}_1 \left( \sum_{i=1}^n x_i^2 - \bar{x} \sum_{i=1}^n x_i \right) \\
&= \left( \sum_{i=1}^n x_i y_i - n \bar{x} \bar{y} - n \bar{x} \bar{y} + n \bar{x} \bar{y} \right) - \hat{\beta}_1 \left( \sum_{i=1}^n x_i^2 - 2 n \bar{x} \bar{x} + n \bar{x}^2 \right) \\
&= \left( \sum_{i=1}^n x_i y_i - \bar{y} \sum_{i=1}^n x_i - \bar{x} \sum_{i=1}^n y_i + n \bar{x} \bar{y} \right) - \hat{\beta}_1 \left( \sum_{i=1}^n x_i^2 - 2 \bar{x} \sum_{i=1}^n x_i + n \bar{x}^2 \right) \\
&= \sum_{i=1}^n \left( x_i y_i - \bar{y} x_i - \bar{x} y_i + \bar{x} \bar{y} \right) - \hat{\beta}_1 \sum_{i=1}^n \left( x_i^2 - 2 \bar{x} x_i + \bar{x}^2 \right) \\
&= \sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y}) - \hat{\beta}_1 \sum_{i=1}^n (x_i - \bar{x})^2 \; .
\end{split}
$$

With \eqref{eq:slr-ols} and with the definitions of [sample variance](/D/var-samp) and [sample covariance](/D/cov-samp), we get:

$$ \label{eq:slr-rescorr-s2}
\begin{split}
   \sum_{i=1}^n x_i \hat{\varepsilon}_i
&= (n-1) s_{xy} - \frac{s_{xy}}{s_x^2} (n-1) s_x^2 \\
&= (n-1) s_{xy} - (n-1) s_{xy} \\
&= 0 \; .
\end{split}
$$

Thus, the inner product of $x$ and $\hat{\varepsilon}$ is zero, and with \eqref{eq:slr-rescov}, it follows that $\mathrm{Corr}(x,\hat{\varepsilon})$ in \eqref{eq:r-xe} is zero. This demonstrates that [residuals](/D/rss) and [covariate](/D/slr) values are uncorrelated [under ordinary least squares](/P/slr-ols).