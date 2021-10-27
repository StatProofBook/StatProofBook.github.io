---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-10-21 14:43:00

title: "Transformed general linear model"
chapter: "Statistical Models"
section: "Multivariate normal data"
topic: "Transformed general linear model"
definition: "Definition"

sources:
  - authors: "Soch J, Allefeld C, Haynes JD"
    year: 2020
    title: "Inverse transformed encoding models – a solution to the problem of correlated trial-by-trial parameter estimates in fMRI decoding"
    in: "NeuroImage"
    pages: "vol. 209, art. 116449, Appendix A"
    url: "https://www.sciencedirect.com/science/article/pii/S1053811919310407"
    doi: "10.1016/j.neuroimage.2019.116449"

def_id: "D160"
shortcut: "tglm"
username: "JoramSoch"
---


**Definition:** Let there be two [general linear models](/D/glm) of measured data $Y \in \mathbb{R}^{n \times v}$ using [design matrices](/D/glm) $X \in \mathbb{R}^{n \times p}$ and $X_t \in \mathbb{R}^{n \times t}$

$$ \label{eq:glm1}
Y = X B + E, \; E \sim \mathcal{MN}(0, V, \Sigma)
$$

$$ \label{eq:glm2}
Y = X_t \Gamma + E_t, \; E_t \sim \mathcal{MN}(0, V, \Sigma_t)
$$

and assume that $X_t$ can be transformed into $X$ using a transformation matrix $T \in \mathbb{R}^{t \times p}$

$$ \label{eq:X-Xt-T}
X = X_t \, T
$$

where $p < t$ and $X$, $X_t$ and $T$ have full ranks $\mathrm{rk}(X) = p$, $\mathrm{rk}(X_t) = t$ and $\mathrm{rk}(T) = p$.

Then, a [linear model](/D/glm) of the parameter estimates from \eqref{eq:glm2}, under the assumption of \eqref{eq:glm1}, is called a transformed general linear model.