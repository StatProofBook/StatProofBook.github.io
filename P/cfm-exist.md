---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-10-21 17:43:00

title: "Existence of a corresponding forward model"
chapter: "Statistical Models"
section: "Multivariate normal data"
topic: "Inverse general linear model"
theorem: "Proof of existence"

sources:
  - authors: "Haufe S, Meinecke F, Görgen K, Dähne S, Haynes JD, Blankertz B, Bießmann F"
    year: 2014
    title: "On the interpretation of weight vectors of linear models in multivariate neuroimaging"
    in: "NeuroImage"
    pages: "vol. 87, pp. 96–110, Appendix B"
    url: "https://www.sciencedirect.com/science/article/pii/S1053811913010914"
    doi: "10.1016/j.neuroimage.2013.10.067"

proof_id: "P270"
shortcut: "cfm-exist"
username: "JoramSoch"
---


**Theorem:** Let there be observations $Y \in \mathbb{R}^{n \times v}$ and $X \in \mathbb{R}^{n \times p}$ and consider a weight matrix $W = f(Y,X) \in \mathbb{R}^{v \times p}$ predicting $X$ from $Y$:

$$ \label{eq:bda}
\hat{X} = Y W \; .
$$

Then, there exists a [corresponding forward model](/D/cfm).


**Proof:** The [corresponding forward model](/D/cfm) is defined as

$$ \label{eq:cfm}
Y = \hat{X} A^\mathrm{T} + E \quad \text{with} \quad \hat{X}^\mathrm{T} E = 0
$$

and the [parameters of the corresponding forward model](/P/cfm-para) are equal to

$$ \label{eq:cfm-para}
A = \Sigma_y W \Sigma_x^{-1} \quad \text{where} \quad \Sigma_x = \hat{X}^\mathrm{T} \hat{X} \quad \text{and} \quad \Sigma_y = Y^\mathrm{T} Y \; .
$$

<br>
1) Because the columns of $\hat{X}$ are assumed to be linearly independent [by definition of the corresponding forward model](/D/cfm), the matrix $\Sigma_x = \hat{X}^\mathrm{T} \hat{X}$ is invertible, such that $A$ in \eqref{eq:cfm-para} is well-defined.

<br>
2) Moreover, the solution for the matrix $A$ satisfies the [constraint of the corresponding forward model](/D/cfm) for predicted $X$ and errors $E$ to be uncorrelated which can be shown as follows:

$$ \label{eq:X-E-0}
\begin{split}
\hat{X}^\mathrm{T} E &\overset{\eqref{eq:cfm}}{=} \hat{X}^\mathrm{T} \left( Y - \hat{X} A^\mathrm{T} \right) \\
&\overset{\eqref{eq:cfm-para}}{=} \hat{X}^\mathrm{T} \left( Y - \hat{X} \, \Sigma_x^{-1} W^\mathrm{T} \Sigma_y \right) \\
&= \hat{X}^\mathrm{T} Y - \hat{X}^\mathrm{T} \hat{X} \, \Sigma_x^{-1} W^\mathrm{T} \Sigma_y \\
&\overset{\eqref{eq:cfm-para}}{=} \hat{X}^\mathrm{T} Y - \hat{X}^\mathrm{T} \hat{X} \left( \hat{X}^\mathrm{T} \hat{X} \right)^{-1} W^\mathrm{T} \left( Y^\mathrm{T} Y \right) \\
% &= \hat{X}^\mathrm{T} Y - W^\mathrm{T} \left( Y^\mathrm{T} Y \right) \\
&\overset{\eqref{eq:bda}}{=} (Y W)^\mathrm{T} Y - W^\mathrm{T} \left( Y^\mathrm{T} Y \right) \\
&= W^\mathrm{T} Y^\mathrm{T} Y - W^\mathrm{T} Y^\mathrm{T} Y \\
&= 0 \; .
\end{split}
$$

This completes the proof.