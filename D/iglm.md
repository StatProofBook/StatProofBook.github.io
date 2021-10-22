---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-10-21 15:31:00

title: "Inverse general linear model"
chapter: "Statistical Models"
section: "Multivariate normal data"
topic: "Inverse general linear model"
definition: "Definition"

sources:
  - authors: "Soch J, Allefeld C, Haynes JD"
    year: 2020
    title: "Inverse transformed encoding models – a solution to the problem of correlated trial-by-trial parameter estimates in fMRI decoding"
    in: "NeuroImage"
    pages: "vol. 209, art. 116449, Appendix C"
    url: "https://www.sciencedirect.com/science/article/pii/S1053811919310407"
    doi: "10.1016/j.neuroimage.2019.116449"

def_id: "D161"
shortcut: "iglm"
username: "JoramSoch"
---


**Definition:** Let there be a [general linear model](/D/glm) of measured data $Y \in \mathbb{R}^{n \times v}$ in terms of the [design matrix](/D/glm) $X \in \mathbb{R}^{n \times p}$:

$$ \label{eq:glm}
Y = X B + E, \; E \sim \mathcal{MN}(0, V, \Sigma) \; .
$$

Then, a [linear model](/D/glm) of $X$ in terms of $Y$, under the assumption of \eqref{eq:glm}, is called an inverse general linear model.