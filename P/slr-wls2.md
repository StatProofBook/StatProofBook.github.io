---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-11-16 11:20:00

title: "Weighted least squares for simple linear regression"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Simple linear regression"
theorem: "Weighted least squares"

sources:

proof_id: "P289"
shortcut: "slr-wls2"
username: "JoramSoch"
---


**Theorem:** Given a [simple linear regression model](/D/slr) with correlated observations

$$ \label{eq:slr}
y = \beta_0 + \beta_1 x + \varepsilon, \; \varepsilon \sim \mathcal{N}(0, \sigma^2 V) \; ,
$$

the parameters minimizing the weighted [residual sum of squares](/D/rss) are given by

$$ \label{eq:slr-wls}
\begin{split}
\hat{\beta}_0 &= \frac{x^\mathrm{T} V^{-1} x \, 1_n^\mathrm{T} V^{-1} y - 1_n^\mathrm{T} V^{-1} x \, x^\mathrm{T} V^{-1} y}{x^\mathrm{T} V^{-1} x \, 1_n^\mathrm{T} V^{-1} 1_n - 1_n^\mathrm{T} V^{-1} x \, x^\mathrm{T} V^{-1} 1_n} \\
\hat{\beta}_1 &= \frac{1_n^\mathrm{T} V^{-1} 1_n \, x^\mathrm{T} V^{-1} y - x^\mathrm{T} V^{-1} 1_n \, 1_n^\mathrm{T} V^{-1} y}{1_n^\mathrm{T} V^{-1} 1_n \, x^\mathrm{T} V^{-1} x - x^\mathrm{T} V^{-1} 1_n \, 1_n^\mathrm{T} V^{-1} x}
\end{split}
$$

where $1_n$ is an $n \times 1$ vector of ones.


**Proof:** [Simple linear regression is a special case of multiple linear regression](/P/slr-mlr) with

$$ \label{eq:slr-mlr}
X = \left[ \begin{matrix} 1_n & x \end{matrix} \right] \quad \text{and} \quad \beta = \left[ \begin{matrix} \beta_0 \\ \beta_1 \end{matrix} \right]
$$

and [weighted least sqaures estimates](/P/mlr-wls) are given by

$$ \label{eq:mlr-wls}
\hat{\beta} = (X^\mathrm{T} V^{-1} X)^{-1} X^\mathrm{T} V^{-1} y \; .
$$

Writing out equation \eqref{eq:mlr-wls}, we have

$$ \label{eq:slr-wls-b}
\begin{split}
\hat{\beta} &= \left( \left[ \begin{matrix} 1_n^\mathrm{T} \\ x^\mathrm{T} \end{matrix} \right] V^{-1} \left[ \begin{matrix} 1_n & x \end{matrix} \right] \right)^{-1} \left[ \begin{matrix} 1_n^\mathrm{T} \\ x^\mathrm{T} \end{matrix} \right] V^{-1} y \\
&= \left[ \begin{matrix} 1_n^\mathrm{T} V^{-1} 1_n & 1_n^\mathrm{T} V^{-1} x \\ x^\mathrm{T} V^{-1} 1_n & x^\mathrm{T} V^{-1} x \end{matrix} \right]^{-1} \left[ \begin{matrix} 1_n^\mathrm{T} V^{-1} y \\ x^\mathrm{T} V^{-1} y \end{matrix} \right] \\
&= \frac{1}{x^\mathrm{T} V^{-1} x \, 1_n^\mathrm{T} V^{-1} 1_n - 1_n^\mathrm{T} V^{-1} x \, x^\mathrm{T} V^{-1} 1_n} \left[ \begin{matrix} x^\mathrm{T} V^{-1} x & -1_n^\mathrm{T} V^{-1} x \\ -x^\mathrm{T} V^{-1} 1_n & 1_n^\mathrm{T} V^{-1} 1_n \end{matrix} \right] \left[ \begin{matrix} 1_n^\mathrm{T} V^{-1} y \\ x^\mathrm{T} V^{-1} y \end{matrix} \right] \\
&= \frac{1}{x^\mathrm{T} V^{-1} x \, 1_n^\mathrm{T} V^{-1} 1_n - 1_n^\mathrm{T} V^{-1} x \, x^\mathrm{T} V^{-1} 1_n} \left[ \begin{matrix} x^\mathrm{T} V^{-1} x \, 1_n^\mathrm{T} V^{-1} y - 1_n^\mathrm{T} V^{-1} x \, x^\mathrm{T} V^{-1} y \\ 1_n^\mathrm{T} V^{-1} 1_n \, x^\mathrm{T} V^{-1} y - x^\mathrm{T} V^{-1} 1_n \, 1_n^\mathrm{T} V^{-1} y \end{matrix} \right] \; .
\end{split}
$$

Thus, the first entry of $\hat{\beta}$ is equal to:

$$ \label{eq:slr-wls-b1}
\hat{\beta}_0 = \frac{x^\mathrm{T} V^{-1} x \, 1_n^\mathrm{T} V^{-1} y - 1_n^\mathrm{T} V^{-1} x \, x^\mathrm{T} V^{-1} y}{x^\mathrm{T} V^{-1} x \, 1_n^\mathrm{T} V^{-1} 1_n - 1_n^\mathrm{T} V^{-1} x \, x^\mathrm{T} V^{-1} 1_n} \; .
$$

Moreover, the second entry of $\hat{\beta}$ [is equal to](/P/slr-wls):

$$ \label{eq:slr-wls-b2}
\hat{\beta}_1 = \frac{1_n^\mathrm{T} V^{-1} 1_n \, x^\mathrm{T} V^{-1} y - x^\mathrm{T} V^{-1} 1_n \, 1_n^\mathrm{T} V^{-1} y}{1_n^\mathrm{T} V^{-1} 1_n \, x^\mathrm{T} V^{-1} x - x^\mathrm{T} V^{-1} 1_n \, 1_n^\mathrm{T} V^{-1} x} \; .
$$