---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2025-07-04 11:47:00

title: "Distribution of the coefficient of determination under the null hypothesis"
chapter: "Model Selection"
section: "Goodness-of-fit measures"
topic: "R-squared"
theorem: "Distribution under null hypothesis"

sources:
  - authors: "Alecos Papadopoulos"
    year: 2014
    title: "What is the distribution of R² in linear regression under the null hypothesis?"
    in: "StackExchange CrossValidated"
    pages: "retrieved on 2024-03-15"
    url: "https://stats.stackexchange.com/a/130082"

proof_id: "P507"
shortcut: "rsq-dist"
username: "JoramSoch"
---


**Theorem:** Consider a [linear regression model](/D/mlr) with known design matrix $X$, known covariance structure $V$, unknown regression parameters $\beta$ and unknown noise variance $\sigma^2$:

$$ \label{eq:mlr}
y = X\beta + \varepsilon, \; \varepsilon \sim \mathcal{N}(0, \sigma^2 V) \; .
$$

Further assume that $X$ contains a [constant regressor](/D/mlr), i.e. it is of the following form:

$$ \label{eq:X-X0}
X = \left[ 1_n, \; X_1 \right] \in \mathbb{R}^{n \times p} \; .
$$

Then, the [coefficient of determination](/D/rsq) follows a [beta distribution](/D/beta)

$$ \label{eq:rsq-dist}
R^2 \sim \mathrm{Bet}\left( \frac{p-1}{2}, \frac{n-p}{2} \right)
$$

under the [null hypothesis](/D/h0) that the true [coefficient of determination](/D/rsq) is zero:

$$ \label{eq:rsq-dist-h0}
H_0: \; R^2 = 0 \; .
$$


**Proof:** We know that the [F-statistic is related to R-squared as](/P/fstat-rsq)

$$ \label{eq:fstat-rsq}
F = \frac{R^2/(p-1)}{(1-R^2)/(n-p)}
$$

and that the [F-statistic follows an F-distribution](/P/rsq-test) under $H_0$:

$$ \label{eq:fstat-dist}
F \sim \mathrm{F}(p-1, n-p), \quad \text{if} \quad R^2 = 0 \; .
$$

Rearranging equation \eqref{eq:fstat-rsq} gives [R-squared as a function of the F-statistic](/P/fstat-rsq)

$$ \label{eq:rsq-fstat-v1}
R^2 = \frac{F \cdot \frac{p-1}{n-p}}{1 + F \cdot \frac{p-1}{n-p}}
$$

which, when expanding with $(n-p)$, can also be written as:

$$ \label{eq:rsq-fstat-v2}
R^2 = \frac{(p-1) F}{(n-p) + (p-1) F} \; .
$$

Using the [relationship between F-distribution and beta distribution](/P/beta-f)

$$ \label{eq:beta-f}
X \sim F(d_1, d_2)
\quad \Rightarrow \quad
Y = \frac{d_1 X}{d_2 + d_1 X} \sim \mathrm{Bet}\left( \frac{d_1}{2}, \frac{d_2}{2} \right) \; ,
$$

i.e. combining \eqref{eq:fstat-dist} and \eqref{eq:rsq-fstat-v2}, it follows that

$$ \label{eq:rsq-dist-qed}
R^2 \sim \mathrm{Bet}\left( \frac{p-1}{2}, \frac{n-p}{2} \right)
$$

under the null hypothesis that $R^2 = 0$.