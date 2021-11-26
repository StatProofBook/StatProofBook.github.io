---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-11-09 07:57:00

title: "Simple linear regression is a special case of multiple linear regression"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Simple linear regression"
theorem: "Special case of multiple linear regression"

sources:

proof_id: "P281"
shortcut: "slr-mlr"
username: "JoramSoch"
---


**Theorem:** [Simple linear regression](/D/slr) is a special case of [multiple linear regression](/D/mlr) with design matrix $X$ and regression coefficients $\beta$

$$ \label{eq:slr-mlr}
X = \left[ \begin{matrix} 1_n & x \end{matrix} \right] \quad \text{and} \quad \beta = \left[ \begin{matrix} \beta_0 \\ \beta_1 \end{matrix} \right]
$$

where $1_n$ is an $n \times 1$ vector of ones, $x$ is the $n \times 1$ single predictor variable, $\beta_0$ is the intercept and $\beta_1$ is the slope of the [regression line](/D/regline).


**Proof:** Without loss of generality, consider the [simple linear regression case with uncorrelated errors](/D/slr):

$$ \label{eq:slr}
y_i = \beta_0 + \beta_1 x_i + \varepsilon_i, \; \varepsilon_i \sim \mathcal{N}(0, \sigma^2), \; i = 1,\ldots,n \; .
$$

In matrix notation and using the [multivariate normal distribution](/D/mvn), this can also be written as

$$ \label{eq:slr-mlr-s1}
\begin{split}
y &= \beta_0 1_n + \beta_1 x + \varepsilon, \; \varepsilon \sim \mathcal{N}(0, I_n) \\
y &= \left[ \begin{matrix} 1_n & x \end{matrix} \right] \left[ \begin{matrix} \beta_0 \\ \beta_1 \end{matrix} \right] + \varepsilon, \; \varepsilon \sim \mathcal{N}(0, I_n) \; .
\end{split}
$$

Comparing with the [multiple linear regression equations for uncorrelated errors](/D/mlr), we finally note:

$$ \label{eq:slr-mlr-s3}
y = X\beta + \varepsilon \quad \text{with} \quad X = \left[ \begin{matrix} 1_n & x \end{matrix} \right] \quad \text{and} \quad \beta = \left[ \begin{matrix} \beta_0 \\ \beta_1 \end{matrix} \right] \; .
$$

In the [case of correlated observations](/D/slr), the [error distribution changes to](/D/mlr):

$$ \label{eq:mlr-noise}
\varepsilon \sim \mathcal{N}(0, \sigma^2 V) \; .
$$