---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-09-26 10:54:00

title: "Symmetry of the covariance matrix"
chapter: "General Theorems"
section: "Probability theory"
topic: "Covariance matrix"
theorem: "Symmetry"

sources:
  - authors: "Wikipedia"
    year: 2022
    title: "Covariance matrix"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2022-09-26"
    url: "https://en.wikipedia.org/wiki/Covariance_matrix#Basic_properties"

proof_id: "P350"
shortcut: "covmat-symm"
username: "JoramSoch"
---


**Theorem:** Each [covariance matrix](/D/covmat) is symmetric:

$$ \label{eq:covmat-symm}
\Sigma_{XX}^\mathrm{T} = \Sigma_{XX} \; .
$$


**Proof:** The [covariance matrix](/D/covmat) of a [random vector](/D/rvec) $X$ is defined as

$$ \label{eq:covmat}
\Sigma_{XX} =
\begin{bmatrix}
\mathrm{Cov}(X_1,X_1) & \ldots & \mathrm{Cov}(X_1,X_n) \\
\vdots & \ddots & \vdots \\
\mathrm{Cov}(X_n,X_1) & \ldots & \mathrm{Cov}(X_n,X_n)
\end{bmatrix} \; .
$$

A symmetric matrix is a matrix whose transpose is equal to itself. The transpose of $\Sigma_{XX}$ is 

$$ \label{eq:covmat-trans}
\Sigma_{XX}^\mathrm{T} =
\begin{bmatrix}
\mathrm{Cov}(X_1,X_1) & \ldots & \mathrm{Cov}(X_n,X_1) \\
\vdots & \ddots & \vdots \\
\mathrm{Cov}(X_1,X_n) & \ldots & \mathrm{Cov}(X_n,X_n)
\end{bmatrix} \; .
$$

Because the [covariance is a symmetric function](/P/cov-symm), i.e. $\mathrm{Cov}(X,Y) = \mathrm{Cov}(Y,X)$, this matrix is equal to

$$ \label{eq:covmat-symm-qed}
\Sigma_{XX}^\mathrm{T} =
\begin{bmatrix}
\mathrm{Cov}(X_1,X_1) & \ldots & \mathrm{Cov}(X_1,X_n) \\
\vdots & \ddots & \vdots \\
\mathrm{Cov}(X_n,X_1) & \ldots & \mathrm{Cov}(X_n,X_n)
\end{bmatrix}
$$

which is equivalent to our original definition in \eqref{eq:covmat}.