---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-06-06 04:56:00

title: "Correlation matrix"
chapter: "General Theorems"
section: "Probability theory"
topic: "Correlation"
definition: "Correlation matrix"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Correlation and dependence"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-06-06"
    url: "https://en.wikipedia.org/wiki/Correlation_and_dependence#Correlation_matrices"

def_id: "D73"
shortcut: "corrmat"
username: "JoramSoch"
---


**Definition:** Let $X = [X_1, \ldots, X_n]^\mathrm{T}$ be a [random vector](/D/rvec). Then, the correlation matrix of $X$ is defined as the $n \times n$ matrix in which the entry $(i,j)$ is the [correlation](/D/corr) of $X_i$ and $X_j$:

$$ \label{eq:corrmat}
\mathrm{C}_{XX} =
\begin{bmatrix}
\mathrm{Corr}(X_1,X_1) & \ldots & \mathrm{Corr}(X_1,X_n) \\
\vdots & \ddots & \vdots \\
\mathrm{Corr}(X_n,X_1) & \ldots & \mathrm{Corr}(X_n,X_n)
\end{bmatrix} =
\begin{bmatrix}
\frac{\mathrm{E}\left[(X_1-\mathrm{E}[X_1]) (X_1-\mathrm{E}[X_1])\right]}{\sigma_{X_1} \, \sigma_{X_1}} & \ldots & \frac{\mathrm{E}\left[(X_1-\mathrm{E}[X_1]) (X_n-\mathrm{E}[X_n])\right]}{\sigma_{X_1} \, \sigma_{X_n}} \\
\vdots & \ddots & \vdots \\
\frac{\mathrm{E}\left[(X_n-\mathrm{E}[X_n]) (X_1-\mathrm{E}[X_1])\right]}{\sigma_{X_n} \, \sigma_{X_1}} & \ldots & \frac{\mathrm{E}\left[(X_n-\mathrm{E}[X_n]) (X_n-\mathrm{E}[X_n])\right]}{\sigma_{X_n} \, \sigma_{X_n}}
\end{bmatrix} \; .
$$