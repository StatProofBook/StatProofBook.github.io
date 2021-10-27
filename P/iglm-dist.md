---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-10-21 16:03:00

title: "Distribution of the inverse general linear model"
chapter: "Statistical Models"
section: "Multivariate normal data"
topic: "Inverse general linear model"
theorem: "Derivation of the distribution"

sources:
  - authors: "Soch J, Allefeld C, Haynes JD"
    year: 2020
    title: "Inverse transformed encoding models – a solution to the problem of correlated trial-by-trial parameter estimates in fMRI decoding"
    in: "NeuroImage"
    pages: "vol. 209, art. 116449, Appendix C, Theorem 4"
    url: "https://www.sciencedirect.com/science/article/pii/S1053811919310407"
    doi: "10.1016/j.neuroimage.2019.116449"

proof_id: "P267"
shortcut: "iglm-dist"
username: "JoramSoch"
---


**Theorem:** Let there be a [general linear model](/D/glm) of $Y \in \mathbb{R}^{n \times v}$

$$ \label{eq:glm}
Y = X B + E, \; E \sim \mathcal{MN}(0, V, \Sigma) \; .
$$

Then, the [inverse general linear model](/D/iglm) of $X \in \mathbb{R}^{n \times p}$ is given by

$$ \label{eq:iglm}
X = Y W + N, \; N \sim \mathcal{MN}(0, V, \Sigma_x)
$$

where $W \in \mathbb{R}^{v \times p}$ is a matrix, such that $B \, W = I_p$, and the [covariance across columns](/D/matn) is $\Sigma_x = W^\mathrm{T} \Sigma W$.


**Proof:** The [linear transformation theorem for the matrix-normal distribution](/P/matn-ltt) states:

$$ \label{eq:matn-ltt}
X \sim \mathcal{MN}(M, U, V) \quad \Rightarrow \quad Y = AXB + C \sim \mathcal{MN}(AMB+C, AUA^\mathrm{T}, B^\mathrm{T}VB) \; .
$$

The matrix $W$ exists, if the rows of $B \in \mathbb{R}^{p \times v}$ are linearly independent, such that $\mathrm{rk}(B) = p$. Then, right-multiplying the model \eqref{eq:glm} with $W$ and applying \eqref{eq:matn-ltt} yields

$$ \label{eq:iglm-s1}
Y W = X B W + E W, \; E W \sim \mathcal{MN}(0, V, W^\mathrm{T} \Sigma W) \; .
$$

Employing $B \, W = I_p$ and rearranging, we have

$$ \label{eq:iglm-s2}
X = Y W - E W, \; E W \sim \mathcal{MN}(0, V, W^\mathrm{T} \Sigma W) \; .
$$

Substituting $N = - E W$, we get

$$ \label{eq:iglm-s3}
X = Y W + N, \; N \sim \mathcal{MN}(0, V, W^\mathrm{T} \Sigma W)
$$

which is equivalent to \eqref{eq:iglm}.