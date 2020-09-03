---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2019-09-27 07:18:00

title: "Ordinary least squares for multiple linear regression"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Multiple linear regression"
theorem: "Ordinary least squares"

sources:
  - authors: "Stephan, Klaas Enno"
    year: 2010
    title: "The General Linear Model (GLM)"
    in: "Methods and models for fMRI data analysis in neuroeconomics"
    pages: "Lecture 3, Slides 10/11"
    url: "http://www.socialbehavior.uzh.ch/teaching/methodsspring10.html"

proof_id: "P2"
shortcut: "mlr-ols"
username: "JoramSoch"
---


**Theorem:** Given a [linear regression model](/D/mlr) with independent observations

$$ \label{eq:MLR}
y = X\beta + \varepsilon, \; \varepsilon_i \overset{\mathrm{i.i.d.}}{\sim} \mathcal{N}(0, \sigma^2) \; ,
$$

the parameters minimizing the [residual sum of squares](/D/rss) are given by

$$ \label{eq:OLS}
\hat{\beta} = (X^\mathrm{T} X)^{-1} X^\mathrm{T} y \; .
$$


**Proof:** Let $\hat{\beta}$ be the ordinary least squares (OLS) solution and let $\hat{\varepsilon} = y - X\hat{\beta}$ be the resulting vector of residuals. Then, this vector must be orthogonal to the design matrix,

$$ \label{eq:X-e-orth}
X^\mathrm{T} \hat{\varepsilon} = 0 \; ,
$$

because if it wasn't, there would be another solution $\tilde{\beta}$ giving another vector $\tilde{\varepsilon}$ with a smaller residual sum of squares. From \eqref{eq:X-e-orth}, the OLS formula can be directly derived:

$$ \label{eq:OLS-qed}
\begin{split}
X^\mathrm{T} \hat{\varepsilon} &= 0 \\
X^\mathrm{T} \left( y - X\hat{\beta} \right) &= 0 \\
X^\mathrm{T} y - X^\mathrm{T} X\hat{\beta} &= 0 \\
X^\mathrm{T} X\hat{\beta} &= X^\mathrm{T} y \\
\hat{\beta} &= (X^\mathrm{T} X)^{-1} X^\mathrm{T} y \; .
\end{split}
$$