---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-06-06 06:28:00

title: "Relationship between precision matrix and correlation matrix"
chapter: "General Theorems"
section: "Probability theory"
topic: "Covariance"
theorem: "Precision matrix and correlation matrix"

sources:

proof_id: "P122"
shortcut: "precmat-corrmat"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random vector](/D/rvec). Then, the [precision matrix](/D/precmat) of $X$ can be expressed in terms of its [correlation matrix](/D/corrmat) as follows

$$ \label{eq:precmat-corrmat}
\Lambda_{XX} = \mathrm{D}_X^{-1} \cdot \mathrm{C}_{XX}^{-1} \cdot \mathrm{D}_X^{-1} \; ,
$$

where $\mathrm{D}_X^{-1}$ is a diagonal matrix with the inverse [standard deviations](/D/std) of $X_1, \ldots, X_n$ as entries on the diagonal:

$$ \label{eq:invdiagmat}
\mathrm{D}_X^{-1} = \mathrm{diag}(1/\sigma_{X_1},\ldots,1/\sigma_{X_n}) =
\begin{bmatrix}
\frac{1}{\sigma_{X_1}} & \ldots & 0 \\
\vdots & \ddots & \vdots \\
0 & \ldots & \frac{1}{\sigma_{X_n}}
\end{bmatrix} \; .
$$


**Proof:** The [precision matrix](/D/precmat) is defined as the inverse of the [covariance matrix](/D/covmat)

$$ \label{eq:precmat-covmat}
\Lambda_{XX} = \Sigma_{XX}^{-1}
$$

and the [relation between covariance matrix and correlation matrix](/P/covmat-corrmat) is given by

$$ \label{eq:covmat-corrmat}
\Sigma_{XX} = \mathrm{D}_X \cdot \mathrm{C}_{XX} \cdot \mathrm{D}_X
$$

where

$$ \label{eq:diagmat}
\mathrm{D}_X = \mathrm{diag}(\sigma_{X_1},\ldots,\sigma_{X_n}) =
\begin{bmatrix}
\sigma_{X_1} & \ldots & 0 \\
\vdots & \ddots & \vdots \\
0 & \ldots & \sigma_{X_n}
\end{bmatrix} \; .
$$

Using the matrix product property

$$ \label{eq:matprod-inv}
\left(A \cdot B \cdot C\right)^{-1} = C^{-1} \cdot B^{-1} \cdot A^{-1}
$$

and the diagonal matrix property

$$ \label{eq:diagmat-inv}
\mathrm{diag}(a_1,\ldots,a_n)^{-1} =
\begin{bmatrix}
a_1 & \ldots & 0 \\
\vdots & \ddots & \vdots \\
0 & \ldots & a_n
\end{bmatrix}^{-1} =
\begin{bmatrix}
\frac{1}{a_1} & \ldots & 0 \\
\vdots & \ddots & \vdots \\
0 & \ldots & \frac{1}{a_n}
\end{bmatrix} =
\mathrm{diag}(1/a_1,\ldots,1/a_n) \; ,
$$

we obtain

$$ \label{eq:precmat-corrmat-qed}
\begin{split}
\Lambda_{XX} &\overset{\eqref{eq:precmat-covmat}}{=} \Sigma_{XX}^{-1} \\
&\overset{\eqref{eq:covmat-corrmat}}{=} \left( \mathrm{D}_X \cdot \mathrm{C}_{XX} \cdot \mathrm{D}_X \right)^{-1} \\
&\overset{\eqref{eq:matprod-inv}}{=} \mathrm{D}_X^{-1} \cdot \mathrm{C}_{XX}^{-1} \cdot \mathrm{D}_X^{-1} \\
&\overset{\eqref{eq:diagmat-inv}}{=}
\begin{bmatrix}
\frac{1}{\sigma_{X_1}} & \ldots & 0 \\
\vdots & \ddots & \vdots \\
0 & \ldots & \frac{1}{\sigma_{X_n}}
\end{bmatrix} \cdot
\mathrm{C}_{XX}^{-1} \cdot
\begin{bmatrix}
\frac{1}{\sigma_{X_1}} & \ldots & 0 \\
\vdots & \ddots & \vdots \\
0 & \ldots & \frac{1}{\sigma_{X_n}}
\end{bmatrix}
\end{split}
$$

which conforms to equation \eqref{eq:precmat-corrmat}.