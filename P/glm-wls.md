---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-05-19 06:27:00

title: "Weighted least squares for the general linear model"
chapter: "Statistical Models"
section: "Multivariate normal data"
topic: "General linear model"
theorem: "Weighted least squares"

sources:

proof_id: "P107"
shortcut: "glm-wls"
username: "JoramSoch"
---


**Theorem:** Given a [general linear model](/D/glm) with correlated observations

$$ \label{eq:GLM}
Y = X B + E, \; E \sim \mathcal{MN}(0, V, \Sigma) \; ,
$$

the [weighted least sqaures](/P/mlr-wls) parameter estimates are given by

$$ \label{eq:WLS}
\hat{B} = (X^\mathrm{T} V^{-1} X)^{-1} X^\mathrm{T} V^{-1} Y \; .
$$


**Proof:** Let there be an $n \times n$ square matrix $W$, such that

$$ \label{eq:W-def}
W V W^\mathrm{T} = I_n \; .
$$

Since $V$ is a covariance matrix and thus symmetric, $W$ is also symmetric and can be expressed as the matrix square root of the inverse of $V$:

$$ \label{eq:W-V}
W W = V^{-1} \quad \Leftrightarrow \quad W = V^{-1/2} \; .
$$

Left-multiplying the linear regression equation \eqref{eq:GLM} with $W$, the [linear transformation theorem](/P/matn-ltt) implies that

$$ \label{eq:GLM-W}
WY = WXB + WE, \; WE \sim \mathcal{MN}(0, W V W^\mathrm{T}, \Sigma) \; .
$$

Applying \eqref{eq:W-def}, we see that \eqref{eq:GLM-W} is actually a [general linear model](/D/glm) with independent observations

$$ \label{eq:GLM-W-dev}
\tilde{Y} = \tilde{X}B + \tilde{E}, \; \tilde{E} \sim \mathcal{N}(0, I_n, \Sigma)
$$

where $\tilde{Y} = WY$, $\tilde{X} = WX$ and $\tilde{E} = WE$, such that we can apply the [ordinary least squares solution](/P/glm-ols) giving

$$ \label{eq:WLS-qed}
\begin{split}
\hat{B} &= (\tilde{X}^\mathrm{T} \tilde{X})^{-1} \tilde{X}^\mathrm{T} \tilde{Y} \\
&= \left( (WX)^\mathrm{T} WX \right)^{-1} (WX)^\mathrm{T} WY \\
&= \left( X^\mathrm{T} W^\mathrm{T} W X \right)^{-1} X^\mathrm{T} W^\mathrm{T} W Y \\
&= \left( X^\mathrm{T} W W X \right)^{-1} X^\mathrm{T} W W Y \\
&\overset{\eqref{eq:W-V}}{=} \left( X^\mathrm{T} V^{-1} X \right)^{-1} X^\mathrm{T} V^{-1} Y
\end{split}
$$

which corresponds to the weighted least squares solution \eqref{eq:WLS}.