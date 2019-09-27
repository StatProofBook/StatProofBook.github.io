---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2019-05-02 15:50:00 +0000

title: "Ordinary least squares for multiple linear regression"
chapter: "Statistical Models"
section: "Normal data"
topic: "Multiple linear regression"
theorem: "Ordinary least squares"

proof_id: "P2"
shortcut: "mlr-ols"
username: "JoramSoch"
---


**Theorem:** Given a linear regression model with independent observations

\begin{equation} \label{eq:MLR}
y = X\beta + \varepsilon, \; \varepsilon_i \overset{\mathrm{i.i.d.}}{\sim} \mathcal{N}(0, \sigma^2) \; ,
\end{equation}

the parameters minimizing the residual sum of squares are given by

\begin{equation} \label{eq:OLS}
\hat{\beta} = (X^\mathrm{T} X)^{-1} X^\mathrm{T} y \; .
\end{equation}


**Proof:** Let $\hat{\beta}$ be the ordinary least squares (OLS) solution and let $\hat{\varepsilon} = y - X\hat{\beta}$ be the resulting vector of residuals. Then, this vector must be orthogonal to the design matrix,

\begin{equation} \label{eq:X-e-orth}
X^\mathrm{T} \hat{\varepsilon} = 0 \; ,
\end{equation}

because if it wasn't, there would be another solution $\tilde{\beta}$ giving another vector $\tilde{\varepsilon}$ with a smaller residual sum of squares. From (\ref{eq:X-e-orth}), the OLS formula can be directly derived:

\begin{equation} \label{eq:OLS-proof}
\begin{split}
X^\mathrm{T} \hat{\varepsilon} &= 0 \\
X^\mathrm{T} \left( y - X\hat{\beta} \right) &= 0 \\
X^\mathrm{T} y - X^\mathrm{T} X\hat{\beta} &= 0 \\
X^\mathrm{T} X\hat{\beta} &= X^\mathrm{T} y \\
\hat{\beta} &= (X^\mathrm{T} X)^{-1} X^\mathrm{T} y \; .
\end{split}
\end{equation}

$$\tag*{$\blacksquare$}$$


**Source:**
- Stephen, Klaas Enno (2010): "The General Linear Model (GLM)"; in: *Methods and models for fMRI data analysis in neuroeconomics*; URL: <http://www.socialbehavior.uzh.ch/teaching/methodsspring10.html>.