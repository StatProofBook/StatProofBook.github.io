---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-01-08 04:46:00

title: "Relationship between R² and maximum log-likelihood"
chapter: "Model Selection"
section: "Goodness-of-fit measures"
topic: "R-squared"
theorem: "Relationship to maximum log-likelihood"

sources:

proof_id: "P14"
shortcut: "rsq-mll"
username: "JoramSoch"
---


**Theorem:** Given a [linear regression model](/D/mlr) with independent observations

$$ \label{eq:MLR}
y = X\beta + \varepsilon, \; \varepsilon_i \overset{\mathrm{i.i.d.}}{\sim} \mathcal{N}(0, \sigma^2) \; ,
$$

the [coefficient of determination](/D/rsq) can be expressed in terms of the [maximum log-likelihood](/D/mll) as

$$ \label{eq:R2-MLL}
R^2 = 1 - \left( \exp[\Delta\mathrm{MLL}] \right)^{-2/n}
$$

where $n$ is the number of observations and $\Delta\mathrm{MLL}$ is the difference in maximum log-likelihood between the model given by \eqref{eq:MLR} and a linear regression model with only a constant regressor.


**Proof:** First, we express the [maximum log-likelihood](/D/mll) (MLL) of a linear regression model in terms of its [residual sum of squares](/D/rss) (RSS). The model in \eqref{eq:MLR} implies the following [log-likelihood function](/D/llf)

$$ \label{eq:MLR-LL}
\mathrm{LL}(\beta,\sigma^2) = \log p(y|\beta,\sigma^2) = - \frac{n}{2} \log(2\pi\sigma^2) - \frac{1}{2\sigma^2} (y - X\beta)^\mathrm{T} (y - X\beta) \; ,
$$

such that [maximum likelihood estimates are](/P/mlr-mle)

$$ \label{eq:MLR-MLE-beta}
\hat{\beta} = (X^\mathrm{T} X)^{-1} X^\mathrm{T} y
$$

$$ \label{eq:MLR-MLE-sigma2}
\hat{\sigma}^2 = \frac{1}{n} (y - X\hat{\beta})^\mathrm{T} (y - X\hat{\beta})
$$

and the [residual sum of squares](/D/rss) is

$$ \label{eq:RSS}
\mathrm{RSS} = \sum_{i=1}^n \hat{\varepsilon}_i = \hat{\varepsilon}^\mathrm{T} \hat{\varepsilon} = (y - X\hat{\beta})^\mathrm{T} (y - X\hat{\beta}) = n \cdot \hat{\sigma}^2 \; .
$$

Since $\hat{\beta}$ and $\hat{\sigma}^2$ are [maximum likelihood estimates](/D/mle), plugging them into the log-likelihood function gives the maximum log-likelihood:

$$ \label{eq:MLR-MLL}
\mathrm{MLL} = \mathrm{LL}(\hat{\beta},\hat{\sigma}^2) = - \frac{n}{2} \log(2\pi\hat{\sigma}^2) - \frac{1}{2\hat{\sigma}^2} (y - X\hat{\beta})^\mathrm{T} (y - X\hat{\beta}) \; .
$$

With \eqref{eq:RSS} for the first $\hat{\sigma}^2$ and \eqref{eq:MLR-MLE-sigma2} for the second $\hat{\sigma}^2$, the MLL becomes

$$ \label{eq:MLR-MLL-RSS}
\mathrm{MLL} = - \frac{n}{2} \log(\mathrm{RSS}) - \frac{n}{2} \log \left( \frac{2\pi}{n} \right) - \frac{n}{2} \; .
$$

Second, we establish the relationship between maximum log-likelihood (MLL) and coefficient of determination (R²). Consider the two models

$$ \label{eq:m0-m1}
\begin{split}
m_0: \; X_0 &= 1_n \\
m_1: \; X_1 &= X
\end{split}
$$

For $m_1$, the residual sum of squares is given by \eqref{eq:RSS}; and for $m_0$, the residual sum of squares is equal to the [total sum of squares](/D/tss):

$$ \label{eq:TSS}
\mathrm{TSS} = \sum_{i=1}^n (y_i - \bar{y})^2 \; .
$$

Using \eqref{eq:MLR-MLL-RSS}, we can therefore write

$$ \label{eq:MLR-DMLL}
\Delta\mathrm{MLL} = \mathrm{MLL}(m_1) - \mathrm{MLL}(m_0) = - \frac{n}{2} \log(\mathrm{RSS}) + \frac{n}{2} \log(\mathrm{TSS}) \; .
$$

Exponentiating both sides of the equation, we have:

$$ \label{eq:MLR-DMLL-RTSS}
\begin{split}
\exp[\Delta\mathrm{MLL}] &= \exp\left[ - \frac{n}{2} \log(\mathrm{RSS}) + \frac{n}{2} \log(\mathrm{TSS}) \right] \\
&= \left( \exp\left[ \log(\mathrm{RSS}) - \log(\mathrm{TSS}) \right] \right)^{-n/2} \\
&= \left( \frac{\exp[\log(\mathrm{RSS})]}{\exp[\log(\mathrm{TSS})]} \right)^{-n/2} \\
&= \left( \frac{\mathrm{RSS}}{\mathrm{TSS}} \right)^{-n/2} \; .
\end{split}
$$

Taking both sides to the power of $-2/n$ and subtracting from 1, we have

$$ \label{eq:MLR-DMLL-R2}
\begin{split}
\left( \exp[\Delta\mathrm{MLL}] \right)^{-2/n} &= \frac{\mathrm{RSS}}{\mathrm{TSS}} \\
1 - \left( \exp[\Delta\mathrm{MLL}] \right)^{-2/n} &= 1 - \frac{\mathrm{RSS}}{\mathrm{TSS}} = R^2
\end{split}
$$

which proves the identity given above.