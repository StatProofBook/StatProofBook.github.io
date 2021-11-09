---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-10-21 15:25:00

title: "Equivalence of parameter estimates from the transformed general linear model"
chapter: "Statistical Models"
section: "Multivariate normal data"
topic: "Transformed general linear model"
theorem: "Equivalence of parameter estimates"

sources:
  - authors: "Soch J, Allefeld C, Haynes JD"
    year: 2020
    title: "Inverse transformed encoding models – a solution to the problem of correlated trial-by-trial parameter estimates in fMRI decoding"
    in: "NeuroImage"
    pages: "vol. 209, art. 116449, Appendix A, Theorem 2"
    url: "https://www.sciencedirect.com/science/article/pii/S1053811919310407"
    doi: "10.1016/j.neuroimage.2019.116449"

proof_id: "P266"
shortcut: "tglm-para"
username: "JoramSoch"
---


**Theorem:** Let there be a [general linear model](/D/glm)

$$ \label{eq:glm1}
Y = X B + E, \; E \sim \mathcal{MN}(0, V, \Sigma)
$$

and the [transformed general linear model](/D/tglm)

$$ \label{eq:tglm}
\hat{\Gamma} = T B + H, \; H \sim \mathcal{MN}(0, U, \Sigma)
$$

which [are linked to each other](/P/tglm-dist) via

$$ \label{eq:glm2-wls}
\hat{\Gamma} = ( X_t^\mathrm{T} V^{-1} X_t )^{-1} X_t^\mathrm{T} V^{-1} Y
$$

and

$$ \label{eq:X-Xt-T}
X = X_t \, T \; .
$$

Then, the parameter estimates for $B$ from \eqref{eq:glm1} and \eqref{eq:tglm} are equivalent.


**Proof:** The [weighted least squares parameter estimates](/P/glm-wls) for \eqref{eq:glm1} are given by

$$ \label{eq:glm1-wls}
\hat{B} = (X^\mathrm{T} V^{-1} X)^{-1} X^\mathrm{T} V^{-1} Y
$$

and the [weighted least squares parameter estimates](/P/glm-wls) for \eqref{eq:tglm} are given by

$$ \label{eq:tglm-wls}
\hat{B} = (T^\mathrm{T} U^{-1} T)^{-1} T^\mathrm{T} U^{-1} \hat{\Gamma} \; .
$$

The [covariance across rows for the transformed general linear model](/P/tglm-dist) is equal to

$$ \label{eq:U}
U = ( X_t^\mathrm{T} V^{-1} X_t )^{-1} \; .
$$

Applying \eqref{eq:U}, \eqref{eq:X-Xt-T} and \eqref{eq:glm2-wls}, the estimates in \eqref{eq:tglm-wls} can be developed into

$$ \label{eq:tglm-wls-dev}
\begin{split}
\hat{B} \; &\overset{\eqref{eq:tglm-wls}}{=} ( T^\mathrm{T} \, U^{-1} \, T )^{-1} \, T^\mathrm{T} \, U^{-1} \, \hat{\Gamma} \\
&\overset{\eqref{eq:U}}{=} ( T^\mathrm{T} \left[ X_t^\mathrm{T} V^{-1} X_t \right] T )^{-1} \, T^\mathrm{T} \left[ X_t^\mathrm{T} V^{-1} X_t \right] \hat{\Gamma} \\
&\overset{\eqref{eq:X-Xt-T}}{=} ( X^\mathrm{T} V^{-1} X )^{-1} \, T^\mathrm{T} \, X_t^\mathrm{T} V^{-1} X_t \, \hat{\Gamma} \\
&\overset{\eqref{eq:glm2-wls}}{=} ( X^\mathrm{T} V^{-1} X )^{-1} \, T^\mathrm{T} \, X_t^\mathrm{T} V^{-1} X_t \left[ ( X_t^\mathrm{T} V^{-1} X_t )^{-1} X_t^\mathrm{T} V^{-1} Y \right] \\
&= ( X^\mathrm{T} V^{-1} X )^{-1} \, T^\mathrm{T} \, X_t^\mathrm{T} V^{-1} Y \\
&\overset{\eqref{eq:X-Xt-T}}{=} ( X^\mathrm{T} V^{-1} X )^{-1} X^\mathrm{T} V^{-1} Y
\end{split}
$$

which is equivalent to the estimates in \eqref{eq:glm1-wls}.