---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-10-21 15:03:00

title: "Distribution of the transformed general linear model"
chapter: "Statistical Models"
section: "Multivariate normal data"
topic: "Transformed general linear model"
theorem: "Derivation of the distribution"

sources:
  - authors: "Soch J, Allefeld C, Haynes JD"
    year: 2020
    title: "Inverse transformed encoding models – a solution to the problem of correlated trial-by-trial parameter estimates in fMRI decoding"
    in: "NeuroImage"
    pages: "vol. 209, art. 116449, Appendix A, Theorem 1"
    url: "https://www.sciencedirect.com/science/article/pii/S1053811919310407"
    doi: "10.1016/j.neuroimage.2019.116449"

proof_id: "P265"
shortcut: "tglm-dist"
username: "JoramSoch"
---


**Theorem:** Let there be two [general linear models](/D/glm) of measured data $Y$

$$ \label{eq:glm1}
Y = X B + E, \; E \sim \mathcal{MN}(0, V, \Sigma)
$$

$$ \label{eq:glm2}
Y = X_t \Gamma + E_t, \; E_t \sim \mathcal{MN}(0, V, \Sigma_t)
$$

and a matrix $T$ transforming $X_t$ into $X$:

$$ \label{eq:X-Xt-T}
X = X_t \, T \; .
$$

Then, the [transformed general linear model](/D/tglm) is given by

$$ \label{eq:tglm}
\hat{\Gamma} = T B + H, \; H \sim \mathcal{MN}(0, U, \Sigma)
$$

where the [covariance across rows](/D/matn) is $U = ( X_t^\mathrm{T} V^{-1} X_t )^{-1}$.


**Proof:** The [linear transformation theorem for the matrix-normal distribution](/P/matn-ltt) states:

$$ \label{eq:matn-ltt}
X \sim \mathcal{MN}(M, U, V) \quad \Rightarrow \quad Y = AXB + C \sim \mathcal{MN}(AMB+C, AUA^\mathrm{T}, B^\mathrm{T}VB) \; .
$$

The [weighted least squares parameter estimates](/P/glm-wls) for \eqref{eq:glm2} are given by

$$ \label{eq:glm2-wls}
\hat{\Gamma} = ( X_t^\mathrm{T} V^{-1} X_t )^{-1} X_t^\mathrm{T} V^{-1} Y \; .
$$

Using \eqref{eq:glm1} and \eqref{eq:matn-ltt}, the distribution of $Y$ is

$$ \label{eq:Y-dist}
Y \sim \mathcal{MN}(X B, V, \Sigma)
$$

Combining \eqref{eq:glm2-wls} with \eqref{eq:Y-dist}, the distribution of $\hat{\Gamma}$ is

$$ \label{eq:G-dist}
\begin{split}
\hat{\Gamma} &\sim \mathcal{MN}\left( \left[ ( X_t^\mathrm{T} V^{-1} X_t )^{-1} X_t^\mathrm{T} V^{-1} \right] X B, \left[ ( X_t^\mathrm{T} V^{-1} X_t )^{-1} X_t^\mathrm{T} V^{-1} \right] V \left[ V^{-1} X_t ( X_t^\mathrm{T} V^{-1} X_t )^{-1} \right], \Sigma \right) \\
&\sim \mathcal{MN}\left( ( X_t^\mathrm{T} V^{-1} X_t )^{-1} X_t^\mathrm{T} V^{-1} X_t \, T B, ( X_t^\mathrm{T} V^{-1} X_t )^{-1} X_t^\mathrm{T} V^{-1} X_t ( X_t^\mathrm{T} V^{-1} X_t )^{-1}, \Sigma \right) \\
&\sim \mathcal{MN}\left( T B, ( X_t^\mathrm{T} V^{-1} X_t )^{-1}, \Sigma \right) \; .
\end{split}
$$

This can also be written as

$$ \label{eq:tglm-qed}
\hat{\Gamma} = T B + H, \; H \sim \mathcal{MN}\left( 0, ( X_t^\mathrm{T} V^{-1} X_t )^{-1}, \Sigma \right)
$$

which is equivalent to \eqref{eq:tglm}.