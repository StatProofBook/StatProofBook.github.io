---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-11-16 07:16:00

title: "Weighted least squares for simple linear regression"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Simple linear regression"
theorem: "Weighted least squares"

sources:

proof_id: "P286"
shortcut: "slr-wls"
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


**Proof:** Let there be an $n \times n$ square matrix $W$, such that

$$ \label{eq:W-def}
W V W^\mathrm{T} = I_n \; .
$$

Since $V$ is a covariance matrix and thus symmetric, $W$ is also symmetric and can be expressed as the matrix square root of the inverse of $V$:

$$ \label{eq:W-V}
W V W = I_n \quad \Leftrightarrow \quad V = W^{-1} W^{-1} \quad \Leftrightarrow \quad V^{-1} = W W \quad \Leftrightarrow \quad W = V^{-1/2} \; .
$$

Because $\beta_0$ is a scalar, \eqref{eq:slr} may also be written as

$$ \label{eq:slr-s1}
y = \beta_0 1_n + \beta_1 x + \varepsilon, \; \varepsilon \sim \mathcal{N}(0, \sigma^2 V) \; ,
$$

Left-multiplying \eqref{eq:slr-s1} with $W$, the [linear transformation theorem](/P/mvn-ltt) implies that

$$ \label{eq:slr-s2}
W y = \beta_0 W 1_n + \beta_1 W x + W \varepsilon, \; W \varepsilon \sim \mathcal{N}(0, \sigma^2 W V W^\mathrm{T}) \; .
$$

Applying \eqref{eq:W-def}, we see that \eqref{eq:slr-s2} is actually a [linear regression model](/D/mlr) with independent observations

$$ \label{eq:slr-s3}
\tilde{y} = \left[ \begin{matrix} \tilde{x}_0 & \tilde{x} \end{matrix} \right] \left[ \begin{matrix} \beta_0 \\ \beta_1 \end{matrix} \right] + \tilde{\varepsilon}, \; \tilde{\varepsilon} \sim \mathcal{N}(0, \sigma^2 I_n)
$$

where $\tilde{y} = Wy$, $\tilde{x}_0 = W 1_n$, $\tilde{x} = W x$ and $\tilde{\varepsilon} = W\varepsilon$, such that we can apply the [ordinary least squares solution](/P/mlr-ols) giving:

$$ \label{eq:slr-wls-s1}
\begin{split}
\hat{\beta} &= (\tilde{X}^\mathrm{T} \tilde{X})^{-1} \tilde{X}^\mathrm{T} \tilde{y} \\
&= \left( \left[ \begin{matrix} \tilde{x}_0^\mathrm{T} \\ \tilde{x}^\mathrm{T} \end{matrix} \right] \left[ \begin{matrix} \tilde{x}_0 & \tilde{x} \end{matrix} \right] \right)^{-1} \left[ \begin{matrix} \tilde{x}_0^\mathrm{T} \\ \tilde{x}^\mathrm{T} \end{matrix} \right] \tilde{y} \\
&= \left[ \begin{matrix} \tilde{x}_0^\mathrm{T} \tilde{x}_0 & \tilde{x}_0^\mathrm{T} \tilde{x} \\ \tilde{x}^\mathrm{T} \tilde{x}_0 & \tilde{x}^\mathrm{T} \tilde{x} \end{matrix} \right]^{-1} \left[ \begin{matrix} \tilde{x}_0^\mathrm{T} \\ \tilde{x}^\mathrm{T} \end{matrix} \right] \tilde{y} \; .
\end{split}
$$

Applying the inverse of a $2 \times 2$ matrix, this reformulates to:

$$ \label{eq:slr-wls-s2}
\begin{split}
\hat{\beta} &= \frac{1}{\tilde{x}_0^\mathrm{T} \tilde{x}_0 \, \tilde{x}^\mathrm{T} \tilde{x} - \tilde{x}_0^\mathrm{T} \tilde{x} \, \tilde{x}^\mathrm{T} \tilde{x}_0} \left[ \begin{matrix} \tilde{x}^\mathrm{T} \tilde{x} & -\tilde{x}_0^\mathrm{T} \tilde{x} \\ -\tilde{x}^\mathrm{T} \tilde{x}_0 & \tilde{x}_0^\mathrm{T} \tilde{x}_0 \end{matrix} \right]^{-1} \left[ \begin{matrix} \tilde{x}_0^\mathrm{T} \\ \tilde{x}^\mathrm{T} \end{matrix} \right] \tilde{y} \\
&= \frac{1}{\tilde{x}_0^\mathrm{T} \tilde{x}_0 \, \tilde{x}^\mathrm{T} \tilde{x} - \tilde{x}_0^\mathrm{T} \tilde{x} \, \tilde{x}^\mathrm{T} \tilde{x}_0} \left[ \begin{matrix} \tilde{x}^\mathrm{T} \tilde{x} \, \tilde{x}_0^\mathrm{T} - \tilde{x}_0^\mathrm{T} \tilde{x} \, \tilde{x}^\mathrm{T} \\ \tilde{x}_0^\mathrm{T} \tilde{x}_0 \, \tilde{x}^\mathrm{T} - \tilde{x}^\mathrm{T} \tilde{x}_0 \, \tilde{x}_0^\mathrm{T} \end{matrix} \right] \tilde{y} \\
&= \frac{1}{\tilde{x}_0^\mathrm{T} \tilde{x}_0 \, \tilde{x}^\mathrm{T} \tilde{x} - \tilde{x}_0^\mathrm{T} \tilde{x} \, \tilde{x}^\mathrm{T} \tilde{x}_0} \left[ \begin{matrix} \tilde{x}^\mathrm{T} \tilde{x} \, \tilde{x}_0^\mathrm{T} \tilde{y} - \tilde{x}_0^\mathrm{T} \tilde{x} \, \tilde{x}^\mathrm{T} \tilde{y} \\ \tilde{x}_0^\mathrm{T} \tilde{x}_0 \, \tilde{x}^\mathrm{T} \tilde{y} - \tilde{x}^\mathrm{T} \tilde{x}_0 \, \tilde{x}_0^\mathrm{T} \tilde{y} \end{matrix} \right] \; .
\end{split}
$$

Applying $\tilde{x}_0 = W 1_n$, $\tilde{x} = W x$ and $W^\mathrm{T} W = W W = V^{-1}$, we finally have

$$ \label{eq:slr-wls-s3}
\begin{split}
\hat{\beta} &= \frac{1}{1_n^\mathrm{T} W^\mathrm{T} W 1_n \, x^\mathrm{T} W^\mathrm{T} W x - 1_n^\mathrm{T} W^\mathrm{T} W x \, x^\mathrm{T} W^\mathrm{T} W 1_n} \left[ \begin{matrix} x^\mathrm{T} W^\mathrm{T} W x \, 1_n^\mathrm{T} W^\mathrm{T} W y - 1_n^\mathrm{T} W^\mathrm{T} W x \, x^\mathrm{T} W^\mathrm{T} W y \\ 1_n^\mathrm{T} W^\mathrm{T} W 1_n \, x^\mathrm{T} W^\mathrm{T} W y - x^\mathrm{T} W^\mathrm{T} W 1_n \, 1_n^\mathrm{T} W^\mathrm{T} W y \end{matrix} \right] \\
&= \frac{1}{x^\mathrm{T} V^{-1} x \, 1_n^\mathrm{T} V^{-1} 1_n - 1_n^\mathrm{T} V^{-1} x \, x^\mathrm{T} V^{-1} 1_n} \left[ \begin{matrix} x^\mathrm{T} V^{-1} x \, 1_n^\mathrm{T} V^{-1} y - 1_n^\mathrm{T} V^{-1} x \, x^\mathrm{T} V^{-1} y \\ 1_n^\mathrm{T} V^{-1} 1_n \, x^\mathrm{T} V^{-1} y - x^\mathrm{T} V^{-1} 1_n \, 1_n^\mathrm{T} V^{-1} y \end{matrix} \right] \\
&= \left[ \begin{matrix} \frac{x^\mathrm{T} V^{-1} x \, 1_n^\mathrm{T} V^{-1} y - 1_n^\mathrm{T} V^{-1} x \, x^\mathrm{T} V^{-1} y}{x^\mathrm{T} V^{-1} x \, 1_n^\mathrm{T} V^{-1} 1_n - 1_n^\mathrm{T} V^{-1} x \, x^\mathrm{T} V^{-1} 1_n} \\ 
\frac{1_n^\mathrm{T} V^{-1} 1_n \, x^\mathrm{T} V^{-1} y - x^\mathrm{T} V^{-1} 1_n \, 1_n^\mathrm{T} V^{-1} y}{1_n^\mathrm{T} V^{-1} 1_n \, x^\mathrm{T} V^{-1} x - x^\mathrm{T} V^{-1} 1_n \, 1_n^\mathrm{T} V^{-1} x} \end{matrix} \right]
\end{split}
$$

which corresponds to the weighted least squares solution \eqref{eq:slr-wls}.