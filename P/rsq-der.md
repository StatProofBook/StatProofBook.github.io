---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2019-12-06 11:19:00

title: "Derivation of R² and adjusted R²"
chapter: "Model Selection"
section: "Goodness-of-fit measures"
topic: "R-squared"
theorem: "Derivation of R² and adjusted R²"

sources:
  - authors: "Wikipedia"
    year: 2019
    title: "Coefficient of determination"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2019-12-06"
    url: "https://en.wikipedia.org/wiki/Coefficient_of_determination#Adjusted_R2"

proof_id: "P8"
shortcut: "rsq-der"
username: "JoramSoch"
---


**Theorem:** Given a [linear regression model](/D/mlr)

$$ \label{eq:rsq-mlr}
y = X\beta + \varepsilon, \; \varepsilon_i \overset{\mathrm{i.i.d.}}{\sim} \mathcal{N}(0, \sigma^2)
$$

with $n$ independent observations and $p$ independent variables,

1) the [coefficient of determination](/D/rsq) is given by

$$ \label{eq:R2}
R^2 = 1 - \frac{\mathrm{RSS}}{\mathrm{TSS}}
$$

2) the adjusted coefficient of determination is

$$ \label{eq:R2-adj}
R^2_{\mathrm{adj}} = 1 - \frac{\mathrm{RSS}/(n-p)}{\mathrm{TSS}/(n-1)}
$$

where the [residual](/D/rss) and [total sum of squares](/D/tss) are

$$ \label{eq:SS}
\begin{split}
\mathrm{RSS} &= \sum_{i=1}^{n} (y_i - \hat{y}_i)^2, \quad \hat{y} = X\hat{\beta} \\
\mathrm{TSS} &= \sum_{i=1}^{n} (y_i - \bar{y})^2\;, \quad \bar{y} = \frac{1}{n} \sum_{i=1}^n y_i \\
\end{split}
$$

where $X$ is the $n \times p$ design matrix and $\hat{\beta}$ are the [ordinary least squares](/P/mlr-ols) estimates.


**Proof:** The coefficient of determination $R^2$ [is defined as](/D/rsq) the proportion of the variance explained by the independent variables, relative to the total variance in the data.

<br>
1) If we define the [explained sum of squares](/D/ess) as

$$ \label{eq:ESS}
\mathrm{ESS} = \sum_{i=1}^{n} (\hat{y}_i - \bar{y})^2 \; ,
$$

then $R^2$ is given by

$$ \label{eq:R2-s1}
R^2 = \frac{\mathrm{ESS}}{\mathrm{TSS}} \; .
$$

which is equal to

$$ \label{eq:R2-s2}
R^2 = \frac{\mathrm{TSS}-\mathrm{RSS}}{\mathrm{TSS}} = 1 - \frac{\mathrm{RSS}}{\mathrm{TSS}} \; ,
$$

[because](/P/mlr-pss) $\mathrm{TSS} = \mathrm{ESS} + \mathrm{RSS}$.

<br>
2) Using \eqref{eq:SS}, the coefficient of determination can be also written as:

$$ \label{eq:R2'}
R^2 = 1 - \frac{\sum_{i=1}^{n} (y_i - \hat{y}_i)^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2} = 1 - \frac{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}{\frac{1}{n} \sum_{i=1}^{n} (y_i - \bar{y})^2} \; .
$$

If we replace the variance estimates by their [unbiased estimators](/P/resvar-unb), we obtain

$$ \label{eq:R2-adj'}
R^2_{\mathrm{adj}} = 1 - \frac{\frac{1}{n-p} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}{\frac{1}{n-1} \sum_{i=1}^{n} (y_i - \bar{y})^2} = 1 - \frac{\mathrm{RSS}/\mathrm{df}_r}{\mathrm{TSS}/\mathrm{df}_t}
$$

where $\mathrm{df}_r = n-p$ and $\mathrm{df}_t = n-1$ are the residual and total [degrees of freedom](/D/dof).

<br>
This gives the adjusted $R^2$ which adjusts $R^2$ for the number of explanatory variables.