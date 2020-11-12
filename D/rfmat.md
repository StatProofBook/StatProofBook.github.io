---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-07-22 05:35:00

title: "Residual-forming matrix"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Multiple linear regression"
definition: "Residual-forming matrix"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Projection matrix"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-07-22"
    url: "https://en.wikipedia.org/wiki/Projection_matrix#Properties"

def_id: "D83"
shortcut: "rfmat"
username: "JoramSoch"
---


**Definition:** In [multiple linear regression](/D/mlr), the residual-forming matrix is the matrix $R$ that results in the vector of residuals left over by [estimated parameters](/D/emat) when right-multiplied with the measured data:

$$ \label{eq:pm}
Ry = \hat{\varepsilon} = y - \hat{y} = y - X \hat{\beta} \; .
$$