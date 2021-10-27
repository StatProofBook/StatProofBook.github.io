---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-10-21 16:46:00

title: "Best linear unbiased estimator for the inverse general linear model"
chapter: "Statistical Models"
section: "Multivariate normal data"
topic: "Inverse general linear model"
theorem: "Best linear unbiased estimator"

sources:
  - authors: "Soch J, Allefeld C, Haynes JD"
    year: 2020
    title: "Inverse transformed encoding models – a solution to the problem of correlated trial-by-trial parameter estimates in fMRI decoding"
    in: "NeuroImage"
    pages: "vol. 209, art. 116449, Appendix C, Theorem 5"
    url: "https://www.sciencedirect.com/science/article/pii/S1053811919310407"
    doi: "10.1016/j.neuroimage.2019.116449"

proof_id: "P268"
shortcut: "iglm-blue"
username: "JoramSoch"
---


**Theorem:** Let there be a [general linear model](/D/glm) of $Y \in \mathbb{R}^{n \times v}$

$$ \label{eq:glm}
Y = X B + E, \; E \sim \mathcal{MN}(0, V, \Sigma)
$$

[implying the inverse general linear model](/P/iglm-dist) of $X \in \mathbb{R}^{n \times p}$

$$ \label{eq:iglm}
X = Y W + N, \; N \sim \mathcal{MN}(0, V, \Sigma_x) \; .
$$

where 

$$ \label{eq:BW-Sx}
B \, W = I_p \quad \text{and} \quad \Sigma_x = W^\mathrm{T} \Sigma W \; .
$$

Then, the [weighted least squares solution](/P/glm-wls) for $W$ is the [best linear unbiased estimator](/D/blue) of $W$.


**Proof:** The [linear transformation theorem for the matrix-normal distribution](/P/matn-ltt) states:

$$ \label{eq:matn-ltt}
X \sim \mathcal{MN}(M, U, V) \quad \Rightarrow \quad Y = AXB + C \sim \mathcal{MN}(AMB+C, AUA^\mathrm{T}, B^\mathrm{T}VB) \; .
$$

The [weighted least squares parameter estimates](/P/glm-wls) for \eqref{eq:iglm} are given by

$$ \label{eq:iglm-wls}
\hat{W} = (Y^\mathrm{T} V^{-1} Y)^{-1} Y^\mathrm{T} V^{-1} X \; .
$$

The [best linear unbiased estimator](/D/blue) $\hat{\theta}$ of a certain quantity $\theta$ estimated from [measured data](/D/data) $y$ is 1) an estimator resulting from a linear operation $f(y)$, 2) whose expected value is equal to $\theta$ and 3) which has, among those satisfying 1) and 2), the minimum [variance](/D/var).

<br>
1) First, $\hat{W}$ is a linear estimator, because it is of the form $\tilde{W} = M \hat{X}$ where $M$ is an arbitrary $v \times n$ matrix.

<br>
2) Second, $\hat{W}$ is an unbiased estimator, if $\left\langle \hat{W} \right\rangle = W$. By applying \eqref{eq:matn-ltt} to \eqref{eq:iglm}, the distribution of $\tilde{W}$ is

$$ \label{eq:W-hat-dist}
\tilde{W} = M X \sim \mathcal{MN}(M Y W, M V M^T, \Sigma_x) \;
$$

[which requires](/P/matn-mean) that $M Y = I_v$. This is fulfilled by any matrix

$$ \label{eq:M-D}
M = (Y^\mathrm{T} V^{-1} Y)^{-1} Y^\mathrm{T} V^{-1} + D
$$

where $D$ is a $v \times n$ matrix which satisfies $D Y = 0$.

<br>
3) Third, the [best linear unbiased estimator](/D/blue) is the one with minimum [variance](/D/var), i.e. the one that minimizes the expected Frobenius norm

$$ \label{eq:Var-W}
\mathrm{Var}\left( \tilde{W} \right) = \left\langle \mathrm{tr}\left[ (\tilde{W} - W)^\mathrm{T} (\tilde{W} - W) \right] \right\rangle \; .
$$

Using the [matrix-normal distribution](/D/matn) of $\tilde{W}$ from \eqref{eq:W-hat-dist}

$$ \label{eq:W-hat-W-dist}
\left( \tilde{W} - W \right) \sim \mathcal{MN}(0, M V M^\mathrm{T}, \Sigma_x)
$$

and the property of the [Wishart distribution](/D/wish)

$$ \label{eq:E-XX}
X \sim \mathcal{MN}(0, U, V) \quad \Rightarrow \quad \left\langle X X^\mathrm{T} \right\rangle = \mathrm{tr}(V) \, U \; ,
$$

this [variance](/D/var) can be evaluated as a function of $M$:

$$ \label{eq:Var-M}
\begin{split}
\mathrm{Var}\left[ \tilde{W}(M) \right] &\overset{\eqref{eq:Var-W}}{=} \left\langle \mathrm{tr}\left[ (\tilde{W} - W)^\mathrm{T} (\tilde{W} - W) \right] \right\rangle \\
&= \left\langle \mathrm{tr}\left[ (\tilde{W} - W) (\tilde{W} - W)^\mathrm{T} \right] \right\rangle \\
&= \mathrm{tr}\left[ \left\langle (\tilde{W} - W) (\tilde{W} - W)^\mathrm{T} \right\rangle \right] \\
&\overset{\eqref{eq:E-XX}}{=} \mathrm{tr}\left[ \mathrm{tr}(\Sigma_x) \, M V M^\mathrm{T} \right] \\
&= \mathrm{tr}(\Sigma_x) \; \mathrm{tr}(M V M^\mathrm{T}) \; .
\end{split}
$$

As a function of $D$ and using $D Y = 0$, it becomes:

$$ \label{eq:Var-D}
\begin{split}
\mathrm{Var}\left[ \tilde{W}(D) \right] &\overset{\eqref{eq:M-D}}{=} \mathrm{tr}(\Sigma_x) \; \mathrm{tr}\!\left[ \left( (Y^\mathrm{T} V^{-1} Y)^{-1} Y^\mathrm{T} V^{-1} + D \right) V \left( (Y^\mathrm{T} V^{-1} Y)^{-1} Y^\mathrm{T} V^{-1} + D \right)^\mathrm{T} \right] \\
&= \mathrm{tr}(\Sigma_x) \; \mathrm{tr}\!\left[ (Y^\mathrm{T} V^{-1} Y)^{-1} \, Y^\mathrm{T} V^{-1} V V^{-1} Y \; (Y^\mathrm{T} V^{-1} Y)^{-1} + \right. \\
&\hphantom{=\mathrm{tr}(\Sigma_x) \; \mathrm{tr}\!\left[\right.} \left. \, (Y^\mathrm{T} V^{-1} Y)^{-1} Y^\mathrm{T} V^{-1} V D^\mathrm{T} + D V V^{-1} Y (Y^\mathrm{T} V^{-1} Y)^{-1} + D V D^\mathrm{T} \right] \\
&= \mathrm{tr}(\Sigma_x) \left[ \mathrm{tr}\!\left( (Y^\mathrm{T} V^{-1} Y)^{-1} \right) + \mathrm{tr}\!\left( D V D^\mathrm{T} \right) \right] \; .
\end{split}
$$

Since $D V D^\mathrm{T}$ is a positive-semidefinite matrix, all its eigenvalues are non-negative. Because the trace of a square matrix is the sum of its eigenvalues, the mimimum variance is achieved by $D = 0$, thus producing $\hat{W}$ as in \eqref{eq:iglm-wls}.