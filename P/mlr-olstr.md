---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2023-10-06 12:48:11

title: "Ordinary least squares for multiple linear regression with two regressors"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Multiple linear regression"
theorem: "Ordinary least squares for two regressors"

sources:

proof_id: "P418"
shortcut: "mlr-olstr"
username: "JoramSoch"
---


**Theorem:** Consider a [linear regression model](/D/mlr) in which the [design matrix](/D/mlr) has two columns:

$$
 \label{eq:mlr-tr}
y = X\beta + \varepsilon \quad \text{where} \quad y \in \mathbb{R}^{n \times 1} \quad \text{and} \quad X = \left[ \begin{matrix} x_1 & x_2 \end{matrix} \right] \in \mathbb{R}^{n \times 2} \; .
$$

Then,

1) the [ordinary least squares](/P/mlr-ols) estimates for $\beta_1$ and $\beta_2$ are given by

$$ \label{eq:mlr-ols-tr}
\hat{\beta}_1 = \frac{x_2^\mathrm{T} x_2 x_1^\mathrm{T} y - x_1^\mathrm{T} x_2 x_2^\mathrm{T} y}{x_1^\mathrm{T} x_1 x_2^\mathrm{T} x_2 - x_1^\mathrm{T} x_2 x_2^\mathrm{T} x_1} \quad \text{and} \quad \hat{\beta}_2 = \frac{x_1^\mathrm{T} x_1 x_2^\mathrm{T} y - x_2^\mathrm{T} x_1 x_1^\mathrm{T} y}{x_1^\mathrm{T} x_1 x_2^\mathrm{T} x_2 - x_1^\mathrm{T} x_2 x_2^\mathrm{T} x_1}
$$

2) and, if the two regressors are orthogonal to each other, they simplify to

$$ \label{eq:mlr-ols-tr-orth}
\hat{\beta}_1 = \frac{x_1^\mathrm{T} y}{x_1^\mathrm{T} x_1} \quad \text{and} \quad \hat{\beta}_2 = \frac{x_2^\mathrm{T} y}{x_2^\mathrm{T} x_2}, \quad \text{if} \quad x_1 \perp x_2 \; .
$$


**Proof:** The model in \eqref{eq:mlr-tr} is a special case of [multiple linear regression](/D/mlr) and the [ordinary least squares solution for multiple linear regression](/P/mlr-ols) is:

$$ \label{eq:mlr-ols}
\hat{\beta} = (X^\mathrm{T} X)^{-1} X^\mathrm{T} y \; .
$$

1) Plugging $X = \left[ \begin{matrix} x_1 & x_2 \end{matrix} \right]$ into this equation, we obtain:

$$ \label{eq:mlr-ols-tr-s1}
\begin{split}
\hat{\beta} &= \left( \left[ \begin{matrix} x_1^\mathrm{T} \\ x_2^\mathrm{T} \end{matrix} \right] \left[ \begin{matrix} x_1 & x_2 \end{matrix} \right] \right)^{-1} \left[ \begin{matrix} x_1^\mathrm{T} \\ x_2^\mathrm{T} \end{matrix} \right] y \\
& = \left( \begin{matrix} x_1^\mathrm{T} x_1 & x_1^\mathrm{T} x_2 \\ x_2^\mathrm{T} x_1 & x_2^\mathrm{T} x_2 \end{matrix} \right)^{-1} \left( \begin{matrix} x_1^\mathrm{T} y \\ x_2^\mathrm{T} y \end{matrix} \right) \; .
\end{split}
$$

Using the inverse of of a $2 \times 2$ matrix

$$ \label{eq:inv-2x2}
\left[ \begin{matrix} a & b \\ c & d \end{matrix} \right]^{-1} = \frac{1}{a d - b c} \left[ \begin{matrix} d & -b \\ -c & a \end{matrix} \right] \; ,
$$

this can be further developped into

$$ \label{eq:mlr-ols-tr-s2}
\begin{split}
\hat{\beta} &= \frac{1}{x_1^\mathrm{T} x_1 x_2^\mathrm{T} x_2 - x_1^\mathrm{T} x_2 x_2^\mathrm{T} x_1} \left( \begin{matrix} x_2^\mathrm{T} x_2 & -x_1^\mathrm{T} x_2 \\ -x_2^\mathrm{T} x_1 & x_1^\mathrm{T} x_1 \end{matrix} \right) \left( \begin{matrix} x_1^\mathrm{T} y \\ x_2^\mathrm{T} y \end{matrix} \right) \\
&= \frac{1}{x_1^\mathrm{T} x_1 x_2^\mathrm{T} x_2 - x_1^\mathrm{T} x_2 x_2^\mathrm{T} x_1} \left( \begin{matrix} x_2^\mathrm{T} x_2 x_1^\mathrm{T} y - x_1^\mathrm{T} x_2 x_2^\mathrm{T} y \\ x_1^\mathrm{T} x_1 x_2^\mathrm{T} y - x_2^\mathrm{T} x_1 x_1^\mathrm{T} y \end{matrix} \right)
\end{split}
$$

which can also be written as

$$ \label{eq:mlr-ols-tr-qed}
\begin{split}
\hat{\beta}_1 &= \frac{x_2^\mathrm{T} x_2 x_1^\mathrm{T} y - x_1^\mathrm{T} x_2 x_2^\mathrm{T} y}{x_1^\mathrm{T} x_1 x_2^\mathrm{T} x_2 - x_1^\mathrm{T} x_2 x_2^\mathrm{T} x_1} \\
\hat{\beta}_2 &= \frac{x_1^\mathrm{T} x_1 x_2^\mathrm{T} y - x_2^\mathrm{T} x_1 x_1^\mathrm{T} y}{x_1^\mathrm{T} x_1 x_2^\mathrm{T} x_2 - x_1^\mathrm{T} x_2 x_2^\mathrm{T} x_1} \; .
\end{split}
$$

2) If two regressors are orthogonal to each other, this means that the inner product of the corresponding vectors is zero:

$$ \label{eq:reg-orth}
x_1 \perp x_2 \quad \Leftrightarrow \quad x_1^\mathrm{T} x_2 = x_2^\mathrm{T} x_1 = 0 \; .
$$

Applying this to equation \eqref{eq:mlr-ols-tr-qed}, we obtain:

$$ \label{eq:mlr-ols-tr-orth-qed}
\begin{split}
\hat{\beta}_1 &= \frac{x_2^\mathrm{T} x_2 x_1^\mathrm{T} y}{x_1^\mathrm{T} x_1 x_2^\mathrm{T} x_2} = \frac{x_1^\mathrm{T} y}{x_1^\mathrm{T} x_1} \\
\hat{\beta}_2 &= \frac{x_1^\mathrm{T} x_1 x_2^\mathrm{T} y}{x_1^\mathrm{T} x_1 x_2^\mathrm{T} x_2} = \frac{x_2^\mathrm{T} y}{x_2^\mathrm{T} x_2} \; .
\end{split}
$$