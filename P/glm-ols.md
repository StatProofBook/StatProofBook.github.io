---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-05-19 06:02:00

title: "Ordinary least squares for the general linear model"
chapter: "Statistical Models"
section: "Multivariate normal data"
topic: "General linear model"
theorem: "Ordinary least squares"

sources:

proof_id: "P106"
shortcut: "glm-ols"
username: "JoramSoch"
---


**Theorem:** Given a [general linear model](/D/glm) with independent observations

$$ \label{eq:GLM}
Y = X B + E, \; E \sim \mathcal{MN}(0, \sigma^2 I_n, \Sigma) \; ,
$$

the [ordinary least squares](/P/mlr-ols) parameters estimates are given by

$$ \label{eq:OLS}
\hat{B} = (X^\mathrm{T} X)^{-1} X^\mathrm{T} Y \; .
$$


**Proof:** Let $\hat{B}$ be the [ordinary least squares](/P/mlr-ols) (OLS) solution and let $\hat{E} = Y - X\hat{B}$ be the resulting matrix of residuals. According to the exogeneity assumption of OLS, the errors have conditional [mean](/D/mean) zero

$$ \label{eq:OLS-exo}
\mathrm{E}(E|X) = 0 \; ,
$$

a direct consequence of which is that the regressors are uncorrelated with the errors

$$ \label{eq:OLS-uncorr}
\mathrm{E}(X^\mathrm{T} E) = 0 \; ,
$$

which, in the finite sample, means that the residual matrix must be orthogonal to the design matrix:

$$ \label{eq:X-E-orth}
X^\mathrm{T} \hat{E} = 0 \; .
$$

From \eqref{eq:X-E-orth}, the OLS formula can be directly derived:

$$ \label{eq:OLS-qed}
\begin{split}
X^\mathrm{T} \hat{E} &= 0 \\
X^\mathrm{T} \left( Y - X\hat{B} \right) &= 0 \\
X^\mathrm{T} Y - X^\mathrm{T} X\hat{B} &= 0 \\
X^\mathrm{T} X\hat{B} &= X^\mathrm{T} Y \\
\hat{B} &= (X^\mathrm{T} X)^{-1} X^\mathrm{T} Y \; .
\end{split}
$$