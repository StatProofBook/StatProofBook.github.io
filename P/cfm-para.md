---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-10-21 17:20:00

title: "Parameters of the corresponding forward model"
chapter: "Statistical Models"
section: "Multivariate normal data"
topic: "Inverse general linear model"
theorem: "Derivation of parameters"

sources:
  - authors: "Haufe S, Meinecke F, Görgen K, Dähne S, Haynes JD, Blankertz B, Bießmann F"
    year: 2014
    title: "On the interpretation of weight vectors of linear models in multivariate neuroimaging"
    in: "NeuroImage"
    pages: "vol. 87, pp. 96–110, Theorem 1"
    url: "https://www.sciencedirect.com/science/article/pii/S1053811913010914"
    doi: "10.1016/j.neuroimage.2013.10.067"

proof_id: "P269"
shortcut: "cfm-para"
username: "JoramSoch"
---


**Theorem:** Let there be observations $Y \in \mathbb{R}^{n \times v}$ and $X \in \mathbb{R}^{n \times p}$ and consider a weight matrix $W = f(Y,X) \in \mathbb{R}^{v \times p}$ predicting $X$ from $Y$:

$$ \label{eq:bda}
\hat{X} = Y W \; .
$$

Then, the parameter matrix of the [corresponding forward model](/D/cfm) is equal to

$$ \label{eq:cfm-para}
A = \Sigma_y W \Sigma_x^{-1}
$$

with the "[sample covariances](/D/cov-samp)"

$$ \label{eq:Sx-Sy}
\begin{split}
\Sigma_x &= \hat{X}^\mathrm{T} \hat{X} \\
\Sigma_y &= Y^\mathrm{T} Y \; .
\end{split}
$$


**Proof:** The [corresponding forward model](/D/cfm) is given by

$$ \label{eq:cfm}
Y = \hat{X} A^\mathrm{T} + E \; ,
$$

subject to the constraint that predicted $X$ and errors $E$ are uncorrelated:

$$ \label{eq:cfm-con}
\hat{X}^\mathrm{T} E = 0 \; .
$$

With that, we can directly derive the parameter matrix $A$:

$$ \label{eq:cfm-para-qed}
\begin{split}
Y &\overset{\eqref{eq:cfm}}{=} \hat{X} A^\mathrm{T} + E \\
\hat{X} A^\mathrm{T} &= Y - E \\
\hat{X}^\mathrm{T} \hat{X} A^\mathrm{T} &= \hat{X}^\mathrm{T} (Y - E) \\
\hat{X}^\mathrm{T} \hat{X} A^\mathrm{T} &= \hat{X}^\mathrm{T} Y - \hat{X}^\mathrm{T} E \\
\hat{X}^\mathrm{T} \hat{X} A^\mathrm{T} &\overset{\eqref{eq:cfm-con}}{=} \hat{X}^\mathrm{T} Y \\
\hat{X}^\mathrm{T} \hat{X} A^\mathrm{T} &\overset{\eqref{eq:bda}}{=} W^\mathrm{T} Y^\mathrm{T} Y \\
\Sigma_x A^\mathrm{T} &\overset{\eqref{eq:Sx-Sy}}{=} W^\mathrm{T} \Sigma_y \\
A^\mathrm{T} &= \Sigma_x^{-1} W^\mathrm{T} \Sigma_y \\
A &= \Sigma_y W \Sigma_x^{-1} \; .
\end{split}
$$