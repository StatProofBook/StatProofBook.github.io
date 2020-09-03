---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-07-22 06:48:00

title: "Weighted least squares for multiple linear regression"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Multiple linear regression"
theorem: "Weighted least squares"

sources:

proof_id: "P136"
shortcut: "mlr-wls2"
username: "JoramSoch"
---


**Theorem:** Given a [linear regression model](/D/mlr) with correlated observations

$$ \label{eq:MLR}
y = X\beta + \varepsilon, \; \varepsilon \sim \mathcal{N}(0, \sigma^2 V) \; ,
$$

the parameters minimizing the weighted [residual sum of squares](/D/rss) are given by

$$ \label{eq:WLS}
\hat{\beta} = (X^\mathrm{T} V^{-1} X)^{-1} X^\mathrm{T} V^{-1} y \; .
$$


**Proof:** Let there be an $n \times n$ square matrix $W$, such that

$$ \label{eq:W-def}
W V W^\mathrm{T} = I_n \; .
$$

Since $V$ is a covariance matrix and thus symmetric, $W$ is also symmetric and can be expressed the matrix square root of the inverse of $V$:

$$ \label{eq:W-V}
W V W = I_n \quad \Leftrightarrow \quad V = W^{-1} W^{-1} \quad \Leftrightarrow \quad V^{-1} = W W \quad \Leftrightarrow \quad W = V^{-1/2} \; .
$$

Left-multiplying the linear regression equation \eqref{eq:MLR} with $W$, the [linear transformation theorem](/P/mvn-ltt) implies that

$$ \label{eq:MLR-W}
Wy = WX\beta + W\varepsilon, \; W\varepsilon \sim \mathcal{N}(0, \sigma^2 W V W^T) \; .
$$

Applying \eqref{eq:W-def}, we see that \eqref{eq:MLR-W} is actually a [linear regression model](/D/mlr) with independent observations

$$ \label{eq:MLR-W-dev}
Wy = WX\beta + W\varepsilon, \; W\varepsilon \sim \mathcal{N}(0, \sigma^2 I_n) \; .
$$

With this, we can express the weighted [residual sum of squares](/D/rss) as

$$ \label{eq:wRSS}
\mathrm{wRSS}(\beta) = \sum_{i=1}^n (W \varepsilon)_i = (W \varepsilon)^\mathrm{T} (W \varepsilon) = (Wy-WX\beta)^\mathrm{T} (Wy-WX\beta)
$$

which can be developed into

$$ \label{eq:wRSS-dev}
\begin{split}
\mathrm{wRSS}(\beta) &= y^\mathrm{T} W^\mathrm{T} W y - y^\mathrm{T} W^\mathrm{T} W X \beta - \beta^\mathrm{T} X^\mathrm{T} W^\mathrm{T} W y + \beta^\mathrm{T} X^\mathrm{T} W^\mathrm{T} W X \beta \\
&= y^\mathrm{T} W W y - 2 \beta^\mathrm{T} X^\mathrm{T} W W y + \beta^\mathrm{T} X^\mathrm{T} W W X \beta \\
&\overset{\eqref{eq:W-V}}{=} y^\mathrm{T} V^{-1} y - 2 \beta^\mathrm{T} X^\mathrm{T} V^{-1} y + \beta^\mathrm{T} X^\mathrm{T} V^{-1} X \beta \; .
\end{split}
$$

The derivative of $\mathrm{wRSS}(\beta)$ with respect to $\beta$ is

$$ \label{eq:wRSS-der}
\frac{\mathrm{d}\mathrm{wRSS}(\beta)}{\mathrm{d}\beta} = - 2 X^\mathrm{T} V^{-1} y + 2 X^\mathrm{T} V^{-1} X \beta
$$

and setting this deriative to zero, we obtain:

$$ \label{eq:WLS-qed}
\begin{split}
\frac{\mathrm{d}\mathrm{wRSS}(\hat{\beta})}{\mathrm{d}\beta} &= 0 \\
0 &= - 2 X^\mathrm{T} V^{-1} y + 2 X^\mathrm{T} V^{-1} X \hat{\beta} \\
X^\mathrm{T} V^{-1} X \hat{\beta} &= X^\mathrm{T} V^{-1} y \\
\hat{\beta} &= (X^\mathrm{T} V^{-1} X)^{-1} X^\mathrm{T} V^{-1} y \; .
\end{split}
$$

Since the quadratic form $y^\mathrm{T} V^{-1} y$ in \eqref{eq:wRSS-dev} is positive, $\hat{\beta}$ minimizes $\mathrm{wRSS}(\beta)$.