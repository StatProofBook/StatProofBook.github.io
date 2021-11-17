---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-03-11 11:22:00

title: "Weighted least squares for multiple linear regression"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Multiple linear regression"
theorem: "Weighted least squares"

sources:
  - authors: "Stephan, Klaas Enno"
    year: 2010
    title: "The General Linear Model (GLM)"
    in: "Methods and models for fMRI data analysis in neuroeconomics"
    pages: "Lecture 3, Slides 20/23"
    url: "http://www.socialbehavior.uzh.ch/teaching/methodsspring10.html"
  - authors: "Wikipedia"
    year: 2021
    title: "Weighted least squares"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-11-17"
    url: "https://en.wikipedia.org/wiki/Weighted_least_squares#Motivation"

proof_id: "P77"
shortcut: "mlr-wls"
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

Since $V$ is a covariance matrix and thus symmetric, $W$ is also symmetric and can be expressed as the matrix square root of the inverse of $V$:

$$ \label{eq:W-V}
W V W = I_n \quad \Leftrightarrow \quad V = W^{-1} W^{-1} \quad \Leftrightarrow \quad V^{-1} = W W \quad \Leftrightarrow \quad W = V^{-1/2} \; .
$$

Left-multiplying the linear regression equation \eqref{eq:MLR} with $W$, the [linear transformation theorem](/P/mvn-ltt) implies that

$$ \label{eq:MLR-W}
Wy = WX\beta + W\varepsilon, \; W\varepsilon \sim \mathcal{N}(0, \sigma^2 W V W^T) \; .
$$

Applying \eqref{eq:W-def}, we see that \eqref{eq:MLR-W} is actually a [linear regression model](/D/mlr) with independent observations

$$ \label{eq:MLR-W-dev}
\tilde{y} = \tilde{X}\beta + \tilde{\varepsilon}, \; \tilde{\varepsilon} \sim \mathcal{N}(0, \sigma^2 I_n)
$$

where $\tilde{y} = Wy$, $\tilde{X} = WX$ and $\tilde{\varepsilon} = W\varepsilon$, such that we can apply the [ordinary least squares solution](/P/mlr-ols) giving

$$ \label{eq:WLS-qed}
\begin{split}
\hat{\beta} &= (\tilde{X}^\mathrm{T} \tilde{X})^{-1} \tilde{X}^\mathrm{T} \tilde{y} \\
&= \left( (WX)^\mathrm{T} WX \right)^{-1} (WX)^\mathrm{T} Wy \\
&= \left( X^\mathrm{T} W^\mathrm{T} W X \right)^{-1} X^\mathrm{T} W^\mathrm{T} W y \\
&= \left( X^\mathrm{T} W W X \right)^{-1} X^\mathrm{T} W W y \\
&\overset{\eqref{eq:W-V}}{=} \left( X^\mathrm{T} V^{-1} X \right)^{-1} X^\mathrm{T} V^{-1} y
\end{split}
$$

which corresponds to the weighted least squares solution \eqref{eq:WLS}.