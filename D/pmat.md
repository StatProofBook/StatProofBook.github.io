---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-07-22 05:25:00

title: "Projection matrix"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Multiple linear regression"
definition: "Projection matrix"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Projection matrix"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-07-22"
    url: "https://en.wikipedia.org/wiki/Projection_matrix#Overview"

def_id: "D82"
shortcut: "pmat"
username: "JoramSoch"
---


**Definition:** In [multiple linear regression](/D/mlr), the projection matrix is the matrix $P$ that results in the fitted signal explained by [estimated parameters](/D/emat) when right-multiplied with the measured data:

$$ \label{eq:pm}
Py = \hat{y} = X \hat{\beta} \; .
$$