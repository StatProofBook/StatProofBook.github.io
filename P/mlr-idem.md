---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-07-22 06:28:00

title: "Projection matrix and residual-forming matrix are idempotent"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Multiple linear regression"
theorem: "Idempotence of projection and residual-forming matrix"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Projection matrix"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-07-22"
    url: "https://en.wikipedia.org/wiki/Projection_matrix#Properties"

proof_id: "P135"
shortcut: "mlr-idem"
username: "JoramSoch"
---


**Theorem:** The [projection matrix](/D/pmat) and the [residual-forming matrix](/D/rfmat) are idempotent:

$$ \label{eq:P^2-R^2}
\begin{split}
P^2 &= P \\
R^2 &= R \; .
\end{split}
$$


**Proof:**

1) The [projection matrix for ordinary least squares is given by](/P/mlr-mat)

$$ \label{eq:P}
P = X (X^\mathrm{T} X)^{-1} X^\mathrm{T} \; ,
$$

such that

$$ \label{eq:P^2}
\begin{split}
P^2 &= X (X^\mathrm{T} X)^{-1} X^\mathrm{T} X (X^\mathrm{T} X)^{-1} X^\mathrm{T} \\
&= X (X^\mathrm{T} X)^{-1} X^\mathrm{T} \\
&\overset{\eqref{eq:P}}{=} P \; .
\end{split}
$$

<br>
2) The [residual-forming matrix for ordinary least squares is given by](/P/mlr-mat)

$$ \label{eq:R}
R = I_n - X (X^\mathrm{T} X)^{-1} X^\mathrm{T} = I_n - P \; ,
$$

such that

$$ \label{eq:R^2}
\begin{split}
R^2 &= (I_n - P) (I_n - P) \\
&= I_n - P - P + P^2 \\
&\overset{\eqref{eq:P^2}}{=} I_n - 2 P + P \\
&= I_n - P \\
&\overset{\eqref{eq:R}}{=} R \; .
\end{split}
$$