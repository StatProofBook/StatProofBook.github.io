---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-11-09 15:19:00

title: "Transformation matrices for simple linear regression"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Simple linear regression"
theorem: "Transformation matrices"

sources:

proof_id: "P285"
shortcut: "slr-mat"
username: "JoramSoch"
---


**Theorem:** Under [ordinary least squares](/P/slr-ols) for [simple linear regression](/D/slr), [estimation](/D/emat), [projection](/D/pmat) and [residual-forming](/D/rfmat) matrices are given by

$$ \label{eq:slr-mat}
\begin{split}
E &= \frac{1}{(n-1)\,s_x^2} \left[ \begin{matrix} (x^\mathrm{T} x/n) \, 1_n^\mathrm{T} - \bar{x} \, x^\mathrm{T} \\ - \bar{x} \, 1_n^\mathrm{T} + x^\mathrm{T} \end{matrix} \right] \\
P &= \frac{1}{(n-1)\,s_x^2} \left[ \begin{matrix} (x^\mathrm{T} x/n) - 2 \bar{x} x_1 + x_1^2 & \cdots & (x^\mathrm{T} x/n) - \bar{x} (x_1 + x_n) + x_1 x_n \\ \vdots & \ddots & \vdots \\ (x^\mathrm{T} x/n) - \bar{x} (x_1 + x_n) + x_1 x_n & \cdots & (x^\mathrm{T} x/n) - 2 \bar{x} x_n + x_n^2 \end{matrix} \right] \\
R &= \frac{1}{(n-1)\,s_x^2} \left[ \begin{matrix} (n-1) (x^\mathrm{T} x/n) + \bar{x} (2 x_1 - n\bar{x}) - x_1^2 & \cdots & -(x^\mathrm{T} x/n) + \bar{x} (x_1 + x_n) - x_1 x_n \\ \vdots & \ddots & \vdots \\ -(x^\mathrm{T} x/n) + \bar{x} (x_1 + x_n) - x_1 x_n & \cdots &  (n-1) (x^\mathrm{T} x/n) + \bar{x} (2 x_n - n\bar{x}) - x_n^2 \end{matrix} \right]
\end{split}
$$

where $1_n$ is an $n \times 1$ vector of ones, $x$ is the $n \times 1$ single predictor variable, $\bar{x}$ is the [sample mean](/D/mean-samp) of $x$ and $s_x^2$ is the [sample variance](/D/var-samp) of $x$.


**Proof:** [Simple linear regression is a special case of multiple linear regression](/P/slr-mlr) with

$$ \label{eq:slr-mlr}
X = \left[ \begin{matrix} 1_n & x \end{matrix} \right] \quad \text{and} \quad \beta = \left[ \begin{matrix} \beta_0 \\ \beta_1 \end{matrix} \right] \; ,
$$

such that the simple linear regression model can also be written as

$$ \label{eq:mlr}
y = X\beta + \varepsilon, \; \varepsilon \sim \mathcal{N}(0, \sigma^2 I_n) \; .
$$

Moreover, we [note the following equality](/P/slr-olsdist):

$$ \label{eq:b-est-cov-den}
x^\mathrm{T} x - n\bar{x}^2 = (n-1) \, s_x^2 \; .
$$

<br>
1) The [estimation matrix is given by](/P/mlr-mat)

$$ \label{eq:E}
E = (X^\mathrm{T} X)^{-1} X^\mathrm{T}
$$

which is a $2 \times n$ matrix and can be reformulated as follows:

$$ \label{eq:E-qed}
\begin{split}
E &= (X^\mathrm{T} X)^{-1} X^\mathrm{T} \\
&= \left( \left[ \begin{matrix} 1_n^\mathrm{T} \\ x^\mathrm{T} \end{matrix} \right] \left[ \begin{matrix} 1_n & x \end{matrix} \right] \right)^{-1} \left[ \begin{matrix} 1_n^\mathrm{T} \\ x^\mathrm{T} \end{matrix} \right] \\
&= \left( \left[ \begin{matrix} n & n\bar{x} \\ n\bar{x} & x^\mathrm{T} x \end{matrix} \right] \right)^{-1} \left[ \begin{matrix} 1_n^\mathrm{T} \\ x^\mathrm{T} \end{matrix} \right] \\
&= \frac{1}{n x^\mathrm{T} x - (n\bar{x})^2} \left[ \begin{matrix} x^\mathrm{T} x & -n\bar{x} \\ -n\bar{x} & n \end{matrix} \right] \left[ \begin{matrix} 1_n^\mathrm{T} \\ x^\mathrm{T} \end{matrix} \right] \\
&= \frac{1}{x^\mathrm{T} x - n\bar{x}^2} \left[ \begin{matrix} x^\mathrm{T} x/n & -\bar{x} \\ -\bar{x} & 1 \end{matrix} \right] \left[ \begin{matrix} 1_n^\mathrm{T} \\ x^\mathrm{T} \end{matrix} \right] \\
&\overset{\eqref{eq:b-est-cov-den}}{=} \frac{1}{(n-1)\,s_x^2} \left[ \begin{matrix} (x^\mathrm{T} x/n) \, 1_n^\mathrm{T} - \bar{x} \, x^\mathrm{T} \\ - \bar{x} \, 1_n^\mathrm{T} + x^\mathrm{T} \end{matrix} \right] \; .
\end{split}
$$

<br>
2) The [projection matrix is given by](/P/mlr-mat)

$$ \label{eq:P}
P = X (X^\mathrm{T} X)^{-1} X^\mathrm{T} = X \, E
$$

which is an $n \times n$ matrix and can be reformulated as follows:

$$ \label{eq:P-qed}
\begin{split}
P &= X \, E = \left[ \begin{matrix} 1_n & x \end{matrix} \right] \left[ \begin{matrix} e_1 \\ e_2 \end{matrix} \right] \\
&= \frac{1}{(n-1)\,s_x^2} \left[ \begin{matrix} 1 & x_1 \\ \vdots & \vdots \\ 1 & x_n \end{matrix} \right] \left[ \begin{matrix} (x^\mathrm{T} x/n) - \bar{x} x_1 & \cdots & (x^\mathrm{T} x/n) - \bar{x} x_n \\ -\bar{x} + x_1 & \cdots & -\bar{x} + x_n \end{matrix} \right] \\
&= \frac{1}{(n-1)\,s_x^2} \left[ \begin{matrix} (x^\mathrm{T} x/n) - 2 \bar{x} x_1 + x_1^2 & \cdots & (x^\mathrm{T} x/n) - \bar{x} (x_1 + x_n) + x_1 x_n \\ \vdots & \ddots & \vdots \\ (x^\mathrm{T} x/n) - \bar{x} (x_1 + x_n) + x_1 x_n & \cdots & (x^\mathrm{T} x/n) - 2 \bar{x} x_n + x_n^2 \end{matrix} \right] \; .
\end{split}
$$

<br>
3) The [residual-forming matrix is given by](/P/mlr-mat)

$$ \label{eq:R}
R = I_n - X (X^\mathrm{T} X)^{-1} X^\mathrm{T} = I_n - P
$$

which also is an $n \times n$ matrix and can be reformulated as follows:

$$ \label{eq:R-qed}
\begin{split}
R &= I_n - P = \left[ \begin{matrix} 1 & \cdots & 0 \\ \vdots & \ddots & \vdots \\ 0 & \cdots & 1 \end{matrix} \right] - \left[ \begin{matrix} p_{11} & \cdots & p_{1n} \\ \vdots & \ddots & \vdots \\ p_{n1} & \cdots & p_{nn} \end{matrix} \right] \\
&\overset{\eqref{eq:b-est-cov-den}}{=} \frac{1}{(n-1)\,s_x^2} \left[ \begin{matrix} x^\mathrm{T} x - n\bar{x}^2 & \cdots & 0 \\ \vdots & \ddots & \vdots \\ 0 & \cdots & x^\mathrm{T} x - n\bar{x}^2 \end{matrix} \right] \\
&- \frac{1}{(n-1)\,s_x^2} \left[ \begin{matrix} (x^\mathrm{T} x/n) - 2 \bar{x} x_1 + x_1^2 & \cdots & (x^\mathrm{T} x/n) - \bar{x} (x_1 + x_n) + x_1 x_n \\ \vdots & \ddots & \vdots \\ (x^\mathrm{T} x/n) - \bar{x} (x_1 + x_n) + x_1 x_n & \cdots & (x^\mathrm{T} x/n) - 2 \bar{x} x_n + x_n^2 \end{matrix} \right] \\
&= \frac{1}{(n-1)\,s_x^2} \left[ \begin{matrix} (n-1) (x^\mathrm{T} x/n) + \bar{x} (2 x_1 - n\bar{x}) - x_1^2 & \cdots & -(x^\mathrm{T} x/n) + \bar{x} (x_1 + x_n) - x_1 x_n \\ \vdots & \ddots & \vdots \\ -(x^\mathrm{T} x/n) + \bar{x} (x_1 + x_n) - x_1 x_n & \cdots &  (n-1) (x^\mathrm{T} x/n) + \bar{x} (2 x_n - n\bar{x}) - x_n^2 \end{matrix} \right] \; .
\end{split}
$$