---
layout: proof
mathjax: true

author: "Artemis Data Desk"
affiliation: ""
e_mail: ""
date: 2026-11-24 13:26:00

title: "Gauss-Markov theorem for ordinary least squares"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Multiple linear regression"
theorem: "Gauss-Markov theorem"

sources:
  - authors: "Freedman, David A."
    year: 2004
    title: "Notes on the Gauss-Markov theorem"
    in: "University of California, Berkeley"
    pages: "pp. 1-2"
    url: "https://www.stat.berkeley.edu/~freedman/GaussMar.pdf"

proof_id: "P572"
shortcut: "mlr-blue"
username: "theyounganimation-rgb"
---


**Theorem:** Consider the [linear regression model](/D/mlr) $y=X\beta+\varepsilon$, where $X\in\mathbb{R}^{n\times p}$ is fixed and has full column rank. Assume $\mathrm{E}(\varepsilon)=0$ and $\mathrm{Cov}(\varepsilon)=\sigma^2 I_n$ with $\sigma^2>0$. The [ordinary least squares](/P/mlr-ols) estimator $\hat\beta=(X^\mathrm{T}X)^{-1}X^\mathrm{T}y$ is the best linear unbiased estimator of $\beta$. In particular, for any matrix $A\in\mathbb{R}^{p\times n}$ such that $Ay$ is unbiased for every $\beta$, the covariance difference

$$ \label{eq:gm-order}
\mathrm{Cov}(Ay)-\mathrm{Cov}(\hat\beta)
$$

is positive semidefinite. Thus every linear contrast $c^\mathrm{T}\hat\beta$ has variance at most that of $c^\mathrm{T}Ay$.


**Proof:** Write $A_0=(X^\mathrm{T}X)^{-1}X^\mathrm{T}$. Since $\mathrm{E}(y)=X\beta$, unbiasedness of $Ay$ for every $\beta$ is equivalent to $AX=I_p$. In particular $A_0X=I_p$, so $\hat\beta=A_0y$ is unbiased. The difference $D=A-A_0$ therefore satisfies $DX=0$. This gives

$$ \label{eq:gm-cross}
D A_0^\mathrm{T}=D X(X^\mathrm{T}X)^{-1}=0
$$

and $A_0D^\mathrm{T}=0$ by transposition. Using $\mathrm{Cov}(y)=\sigma^2I_n$ and substituting $A=A_0+D$ yields

$$ \label{eq:gm-difference}
\begin{split}
\mathrm{Cov}(Ay)-\mathrm{Cov}(\hat\beta)
&=\sigma^2\left(AA^\mathrm{T}-A_0A_0^\mathrm{T}\right)\\
&=\sigma^2 DD^\mathrm{T}.
\end{split}
$$

For any $c\in\mathbb{R}^p$ the difference of the two contrast variances is consequently $\sigma^2\|D^\mathrm{T}c\|^2$. This proves the covariance order and shows that the variances agree for a given contrast exactly when $D^\mathrm{T}c=0$. They agree for every contrast exactly when $A=A_0$.
