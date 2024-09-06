---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-07-21 08:28:00

title: "Multiple linear regression is a special case of the general linear model"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Multiple linear regression"
theorem: "Special case of general linear model"

sources:
  - authors: "Wikipedia"
    year: 2022
    title: "General linear model"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2022-07-21"
    url: "https://en.wikipedia.org/wiki/General_linear_model#Comparison_to_multiple_linear_regression"

proof_id: "P329"
shortcut: "mlr-glm"
username: "JoramSoch"
---


**Theorem:** [Multiple linear regression](/D/mlr) is a special case of the [general linear model](/D/glm) with number of measurements $v = 1$, such that data matrix $Y$, regression coefficients $B$, noise matrix $E$ and noise covariance $\Sigma$ equate as

$$ \label{eq:mlr-glm}
Y = y, \quad B = \beta, \quad E = \varepsilon \quad \text{and} \quad \Sigma = \sigma^2
$$

where $y$, $\beta$, $\varepsilon$ and $\sigma^2$ are the data vector, regression coefficients, noise vector and noise variance from [multiple linear regression](/D/mlr).


**Proof:** The [linear regression model with correlated errors](/D/mlr) is given by:

$$ \label{eq:mlr}
y = X\beta + \varepsilon, \; \varepsilon \sim \mathcal{N}(0, \sigma^2 V) \; .
$$

Because $\varepsilon$ is an $n \times 1$ vector and $\sigma^2$ is scalar, we have the following identities:

$$
\begin{split}
\mathrm{vec}(\varepsilon) &= \varepsilon \\
\sigma^2 \otimes V &= \sigma^2 V \; .
\end{split}
$$

Thus, using the [relationship between multivariate normal and matrix normal distribution](/P/matn-mvn), equation \eqref{eq:mlr} can also be written as

$$ \label{eq:mlr-dev}
y = X\beta + \varepsilon, \; \varepsilon \sim \mathcal{MN}(0, V, \sigma^2) \; .
$$

Comparing with the [general linear model with correlated observations](/D/glm)

$$ \label{eq:glm}
Y = X B + E, \; E \sim \mathcal{MN}(0, V, \Sigma) \; ,
$$

we finally note the equivalences given in equation \eqref{eq:mlr-glm}.