---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-06-06 04:24:00

title: "Covariance matrix"
chapter: "General Theorems"
section: "Probability theory"
topic: "Covariance"
definition: "Covariance matrix"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Covariance matrix"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-06-06"
    url: "https://en.wikipedia.org/wiki/Covariance_matrix#Definition"

def_id: "D72"
shortcut: "covmat"
username: "JoramSoch"
---


**Definition:** Let $X = [X_1, \ldots, X_n]^\mathrm{T}$ be a [random vector](/D/rvec). Then, the covariance matrix of $X$ is defined as the $n \times n$ matrix in which the entry $(i,j)$ is the [covariance](/D/cov) of $X_i$ and $X_j$:

$$ \label{eq:covmat}
\Sigma_{XX} =
\begin{bmatrix}
\mathrm{Cov}(X_1,X_1) & \ldots & \mathrm{Cov}(X_1,X_n) \\
\vdots & \ddots & \vdots \\
\mathrm{Cov}(X_n,X_1) & \ldots & \mathrm{Cov}(X_n,X_n)
\end{bmatrix} =
\begin{bmatrix}
\mathrm{E}\left[ (X_1-\mathrm{E}[X_1]) (X_1-\mathrm{E}[X_1]) \right] & \ldots & \mathrm{E}\left[ (X_1-\mathrm{E}[X_1]) (X_n-\mathrm{E}[X_n]) \right] \\
\vdots & \ddots & \vdots \\
\mathrm{E}\left[ (X_n-\mathrm{E}[X_n]) (X_1-\mathrm{E}[X_1]) \right] & \ldots & \mathrm{E}\left[ (X_n-\mathrm{E}[X_n]) (X_n-\mathrm{E}[X_n]) \right]
\end{bmatrix} \; .
$$