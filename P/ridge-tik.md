---
layout: proof
mathjax: true

author: "Ljx000888"
affiliation: ""
e_mail: ""
date: 2026-11-25 10:06:00

title: "Tikhonov regularization for linear regression"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Ridge regression"
theorem: "Tikhonov regularization"

sources:
  - authors: "Hansen, Per Christian"
    year: 2008
    title: "Regularization Tools"
    pages: "Version 4.1, section 2.7.1"
    url: "https://www2.compute.dtu.dk/~pcha/Regutools/RTv4manual.pdf"
  - authors: "Hoerl, Arthur E. and Kennard, Robert W."
    year: 1970
    title: "Ridge regression: biased estimation for nonorthogonal problems"
    in: "Technometrics"
    pages: "12(1), 55–67"
    doi: "10.1080/00401706.1970.10488634"

proof_id: "P576"
shortcut: "ridge-tik"
username: "Ljx000888"
---

**Theorem:** Given a response vector $y\in\mathbb R^n$, a design matrix $X\in\mathbb R^{n\times p}$, a penalty matrix $L\in\mathbb R^{m\times p}$ and a scalar $\lambda>0$, consider the penalized [residual sum of squares](/D/rss)

$$ \label{eq:ridge-tik-objective}
Q(b)=\|y-Xb\|_2^2+\lambda\|Lb\|_2^2,\qquad b\in\mathbb R^p .
$$

A minimizer always exists. It is unique exactly when $\ker X\cap\ker L=\{0\}$, in which case it equals

$$ \label{eq:ridge-tik-solution}
\hat b=(X^\top X+\lambda L^\top L)^{-1}X^\top y .
$$

In particular, ordinary ridge regression ($L=I_p$) has a unique solution even if columns of $X$ are linearly dependent.

**Proof:** Write the objective as $\|z-Ab\|_2^2$ with

$$ \label{eq:ridge-tik-augmented}
A=\begin{bmatrix}X\\ \sqrt{\lambda}\,L\end{bmatrix},
\qquad
z=\begin{bmatrix}y\\0_m\end{bmatrix}.
$$

The orthogonal projection of $z$ onto the column space of $A$ exists and belongs to that space, so it equals $A\hat b$ for at least one coefficient vector $\hat b$. Its residual is orthogonal to every column of $A$. Thus $A^\top(z-A\hat b)=0$, or equivalently

$$ \label{eq:ridge-tik-normal}
(X^\top X+\lambda L^\top L)\hat b=X^\top y .
$$

For any displacement $h$, the two terms in $(z-A\hat b)-Ah$ are orthogonal. The Pythagorean identity therefore gives

$$ \label{eq:ridge-tik-difference}
Q(\hat b+h)-Q(\hat b)=\|Ah\|_2^2=\|Xh\|_2^2+\lambda\|Lh\|_2^2 .
$$

This proves minimality and identifies all minimizers: they are precisely $\hat b+h$ with $h\in\ker X\cap\ker L$. When the intersection is trivial, $h^\top A^\top Ah=\|Ah\|_2^2>0$ for every nonzero $h$, so the matrix in \eqref{eq:ridge-tik-normal} is invertible and \eqref{eq:ridge-tik-solution} follows. Choosing $L=I_p$ makes the intersection trivial for every $X$.
