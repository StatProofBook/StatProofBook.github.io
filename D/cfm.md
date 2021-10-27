---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-10-21 17:01:00

title: "Corresponding forward model"
chapter: "Statistical Models"
section: "Multivariate normal data"
topic: "Inverse general linear model"
definition: "Corresponding forward model"

sources:
  - authors: "Haufe S, Meinecke F, Görgen K, Dähne S, Haynes JD, Blankertz B, Bießmann F"
    year: 2014
    title: "On the interpretation of weight vectors of linear models in multivariate neuroimaging"
    in: "NeuroImage"
    pages: "vol. 87, pp. 96–110, eq. 3"
    url: "https://www.sciencedirect.com/science/article/pii/S1053811913010914"
    doi: "10.1016/j.neuroimage.2013.10.067"

def_id: "D162"
shortcut: "cfm"
username: "JoramSoch"
---


**Definition:** Let there be observations $Y \in \mathbb{R}^{n \times v}$ and $X \in \mathbb{R}^{n \times p}$ and consider a weight matrix $W = f(Y,X) \in \mathbb{R}^{v \times p}$ estimated from $Y$ and $X$, such that right-multiplying $Y$ with the weight matrix gives an estimate or prediction of $X$:

$$ \label{eq:bda}
\hat{X} = Y W \; .
$$

Given that the columns of $\hat{X}$ are linearly independent, then

$$ \label{eq:cfm}
Y = \hat{X} A^\mathrm{T} + E \quad \text{with} \quad \hat{X}^\mathrm{T} E = 0
$$

is called the corresponding forward model relative to the weight matrix $W$.