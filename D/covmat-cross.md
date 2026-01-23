---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-09-26 09:45:00

title: "Cross-covariance matrix"
chapter: "General Theorems"
section: "Probability theory"
topic: "Covariance matrix"
definition: "Cross-covariance matrix"

sources:
  - authors: "Wikipedia"
    year: 2022
    title: "Cross-covariance matrix"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2022-09-26"
    url: "https://en.wikipedia.org/wiki/Cross-covariance_matrix#Definition"

def_id: "D176"
shortcut: "covmat-cross"
username: "JoramSoch"
---


**Definition:** Let $X = [X_1, \ldots, X_n]^\mathrm{T}$ and $Y = [Y_1, \ldots, Y_m]^\mathrm{T}$ be two [random vectors](/D/rvec) that can or cannot be of equal size. Then, the cross-covariance matrix of $X$ and $Y$ is defined as the $n \times m$ matrix in which the entry $(i,j)$ is the [covariance](/D/cov) of $X_i$ and $Y_j$:

$$ \label{eq:covmat-cross}
\Sigma_{XY} =
\begin{bmatrix}
\mathrm{Cov}(X_1,Y_1) & \ldots & \mathrm{Cov}(X_1,Y_m) \\
\vdots & \ddots & \vdots \\
\mathrm{Cov}(X_n,Y_1) & \ldots & \mathrm{Cov}(X_n,Y_m)
\end{bmatrix} =
\begin{bmatrix}
\mathrm{E}\left[ (X_1-\mathrm{E}[X_1]) (Y_1-\mathrm{E}[Y_1]) \right] & \ldots & \mathrm{E}\left[ (X_1-\mathrm{E}[X_1]) (Y_m-\mathrm{E}[Y_m]) \right] \\
\vdots & \ddots & \vdots \\
\mathrm{E}\left[ (X_n-\mathrm{E}[X_n]) (Y_1-\mathrm{E}[Y_1]) \right] & \ldots & \mathrm{E}\left[ (X_n-\mathrm{E}[X_n]) (Y_m-\mathrm{E}[Y_m]) \right]
\end{bmatrix} \; .
$$