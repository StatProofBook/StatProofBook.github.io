---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-06-06 05:08:00

title: "Precision matrix"
chapter: "General Theorems"
section: "Probability theory"
topic: "Covariance"
definition: "Precision matrix"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Precision (statistics)"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-06-06"
    url: "https://en.wikipedia.org/wiki/Precision_(statistics)"

def_id: "D74"
shortcut: "precmat"
username: "JoramSoch"
---


**Definition:** Let $X = [X_1, \ldots, X_n]^\mathrm{T}$ be a [random vector](/D/rvec). Then, the precision matrix of $X$ is defined as the inverse of the [covariance matrix](/D/covmat) of $X$:

$$ \label{eq:corrmat}
\Lambda_{XX} = \Sigma_{XX}^{-1} =
\begin{bmatrix}
\mathrm{Cov}(X_1,X_1) & \ldots & \mathrm{Cov}(X_1,X_n) \\
\vdots & \ddots & \vdots \\
\mathrm{Cov}(X_n,X_1) & \ldots & \mathrm{Cov}(X_n,X_n)
\end{bmatrix}^{-1} \; .
$$