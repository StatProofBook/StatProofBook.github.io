---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-12-22 13:17:00

title: "Projection matrix and residual-forming matrix are symmetric"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Multiple linear regression"
theorem: "Symmetry of projection and residual-forming matrix"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Projection matrix"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2022-12-22"
    url: "https://en.wikipedia.org/wiki/Projection_matrix#Properties"

proof_id: "P399"
shortcut: "mlr-symm"
username: "JoramSoch"
---


**Theorem:** The [projection matrix](/D/pmat) and the [residual-forming matrix](/D/rfmat) are symmetric:

$$ \label{eq:P-R-symm}
\begin{split}
P^\mathrm{T} &= P \\
R^\mathrm{T} &= R \; .
\end{split}
$$


**Proof:** Let $X$ be the [design matrix from the linear regression model](/D/mlr). Then, the matrix $X^\mathrm{T} X$ is symmetric, because 

$$ \label{eq:XTX-symm}
(X^\mathrm{T} X)^\mathrm{T} = X^\mathrm{T} {X^\mathrm{T}}^\mathrm{T} = X^\mathrm{T} X \; .
$$

Thus, the inverse of $X^\mathrm{T} X$ is also symmetric, i.e.

$$ \label{eq:XTX-inv-symm}
\left((X^\mathrm{T} X)^{-1}\right)^\mathrm{T} = (X^\mathrm{T} X)^{-1} \; .
$$

1) The [projection matrix for ordinary least squares is given by](/P/mlr-mat)

$$ \label{eq:P}
P = X (X^\mathrm{T} X)^{-1} X^\mathrm{T} \; ,
$$

such that

$$ \label{eq:P-symm}
\begin{split}
P^\mathrm{T} &= \left( X (X^\mathrm{T} X)^{-1} X^\mathrm{T} \right)^\mathrm{T} \\
&= {X^\mathrm{T}}^\mathrm{T} \left((X^\mathrm{T} X)^{-1}\right)^\mathrm{T} X^\mathrm{T} \\
&= X (X^\mathrm{T} X)^{-1} X^\mathrm{T} \\
&\overset{\eqref{eq:P}}{=} P \; .
\end{split}
$$

2) The [residual-forming matrix for ordinary least squares is given by](/P/mlr-mat)

$$ \label{eq:R}
R = I_n - X (X^\mathrm{T} X)^{-1} X^\mathrm{T} = I_n - P \; ,
$$

such that

$$ \label{eq:R-symm}
\begin{split}
R^\mathrm{T} &= (I_n - P)^\mathrm{T} \\
&= I_n^\mathrm{T} - P^\mathrm{T} \\
&\overset{\eqref{eq:P-symm}}{=} I_n - P \\
&\overset{\eqref{eq:R}}{=} R \; .
\end{split}
$$