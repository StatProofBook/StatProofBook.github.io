---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2024-03-08 12:03:21

title: "Statistical significance test for the coefficient of determinantion based on an omnibus F-test"
chapter: "Model Selection"
section: "Goodness-of-fit measures"
topic: "R-squared"
theorem: "Statistical significance test for R²"

sources:
  - authors: "Alecos Papadopoulos"
    year: 2014
    title: "What is the distribution of R² in linear regression under the null hypothesis?"
    in: "StackExchange CrossValidated"
    pages: "retrieved on 2024-03-15"
    url: "https://stats.stackexchange.com/a/130082"

proof_id: "P441"
shortcut: "rsq-test"
username: "JoramSoch"
---


**Theorem:** Consider a [linear regression model](/D/mlr) with known design matrix $X$, known covariance structure $V$, unknown regression parameters $\beta$ and unknown noise variance $\sigma^2$:

$$ \label{eq:mlr}
y = X\beta + \varepsilon, \; \varepsilon \sim \mathcal{N}(0, \sigma^2 V) \; .
$$

Further assume that $X$ contains a [constant regressor](/D/mlr). Then, the [coefficient of determination](/D/rsq) can be used to calculate a [test statistic](/D/tstat)

$$ \label{eq:f-rsq}
F = \frac{R^2/(p-1)}{(1-R^2)/(n-p)}
$$

where $n$ and $p$ are the [dimensions of the design matrix](/D/mlr) $X$, and this test statistic follows an [F-distribution](/D/f)

$$ \label{eq:f-rsq-dist}
F \sim \mathrm{F}(p-1, n-p)
$$

under the [null hypothesis](/D/h0) that the true [coefficient of determination](/D/rsq) is zero:

$$ \label{eq:rsq-test-h0}
H_0: \; R^2 = 0 \; .
$$


**Proof:** Consider two [linear regression models](/D/mlr) for the same measured data $y$, with design matrices $X = X_0 \in \mathbb{R}^{n \times p_0}$ and $X = \left[ X_0, X_1 \right] \in \mathbb{R}^{n \times p}$ as well as regression coefficients $\beta = \beta_0 \in \mathbb{R}^{p_0 \times 1}$ and $\beta = \left[ \beta_0^\mathrm{T}, \beta_1^\mathrm{T} \right]^\mathrm{T} \in \mathbb{R}^{p \times 1}$.

Then, under the null hypothesis that all [regression coefficients](/D/mlr) $\beta_1$ associated with $X_1$ are zero

$$ \label{eq:mlr-fomnibus-h0}
H_0: \; \beta_1 = 0_{p-p_0} \quad \Leftrightarrow \quad \beta_i = 0 \quad \text{for all} \quad j = p_0+1,\ldots,p \; ,
$$

the [omnibus F-statistic follows an F-distribution](/P/mlr-fomnibus)

$$ \label{eq:mlr-fomnibus}
F = \frac{(\mathrm{RSS}_0-\mathrm{RSS})/(p-p_0)}{\mathrm{RSS}/(n-p)} \sim \mathrm{F}(p-p_0, n-p)
$$

where $\mathrm{RSS}_0$ and $\mathrm{RSS}$ are the [residual sums of squares](/D/rss) of the null model with $X_0$ and the full model with $X_0$ nested in $X$, after regression coefficients have been estimated with [weighted least squares](/P/mlr-wls) or [maximum likelihood](/P/mlr-mle).

<br>
Since by the requirements of our theorem, $X$ contains a constant regressor, we can assume the following design matrices without loss of generality:

$$ \label{eq:f-rsq-X}
X_0 = 1_n \in \mathbb{R}^{n \times 1} \quad \text{and} \quad X = \left[ 1_n, X_1 \right] \in \mathbb{R}^{n \times p} \; .
$$

Thus, since a single constant regressor estimates the mean and considering the definition of the [total sum of squares](/D/tss) $\mathrm{TSS}$, we in our case have:

$$ \label{eq:rss0-p0}
\mathrm{RSS}_0 = \mathrm{TSS} \quad \text{and} \quad p_0 = 1 \; .
$$

<br>
The [coefficient of determination is given by](/P/rsq-der)

$$ \label{eq:rsq-rss}
R^2 = 1 - \frac{\mathrm{RSS}}{\mathrm{TSS}}
$$

which [can also be written as](/P/mlr-pss)

$$ \label{eq:rsq-ess}
R^2 = \frac{\mathrm{ESS}}{\mathrm{TSS}} \; .
$$

If all regression coefficients $\beta_1$ associated with $X_1$ are zero, then the true $R^2$ is zero, because there is no variance explained beyond the constant regressor, the [explained sum of squares](/D/ess) $\mathrm{ESS}$ is zero and the [residual sum of squares](/D/rss) $\mathrm{RSS}$ is equal to the [total sum of squares](/D/tss) $\mathrm{TSS}$.

<br>
Then, by virtue of \eqref{eq:mlr-fomnibus}, we get the following F-statistic:

$$ \label{eq:f-rsq-qed}
\begin{split}
F &\overset{\eqref{eq:mlr-fomnibus}}{=} \frac{(\mathrm{RSS}_0-\mathrm{RSS})/(p-p_0)}{\mathrm{RSS}/(n-p)} \\
&\overset{\eqref{eq:rss0-p0}}{=} \frac{(\mathrm{TSS}-\mathrm{RSS})/(p-1)}{\mathrm{RSS}/(n-p)} \\
&= \frac{\frac{\mathrm{TSS}-\mathrm{RSS}}{\mathrm{TSS}}/(p-1)}{\frac{\mathrm{RSS}}{\mathrm{TSS}}/(n-p)} \\
&= \frac{\left( 1 - \frac{\mathrm{RSS}}{\mathrm{TSS}} \right)/(p-1)}{\left( 1 - \left( 1- \frac{\mathrm{RSS}}{\mathrm{TSS}} \right)\right)/(n-p)} \\
&\overset{\eqref{eq:rsq-rss}}{=} \frac{\left(R^2\right)/(p-1)}{\left(1-R^2\right)/(n-p)} \; .
\end{split}
$$

This means that the [null hypothesis](/D/h0) can be rejected when $F$ as a function of $R^2$ is as extreme or more extreme than the [critical value](/D/cval) obtained from the [F-distribution](/D/f) with $p-1$ denominator and $n-p$ numerator [degrees of freedom](/D/dof) using a [significance level](/D/alpha) $\alpha$.