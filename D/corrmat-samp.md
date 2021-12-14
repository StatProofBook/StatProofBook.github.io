---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-12-14 07:45:00

title: "Sample correlation matrix"
chapter: "General Theorems"
section: "Probability theory"
topic: "Correlation"
definition: "Sample correlation matrix"

sources:

def_id: "D169"
shortcut: "corrmat-samp"
username: "JoramSoch"
---


**Definition:** Let $x = \left\lbrace x_1, \ldots, x_n \right\rbrace$ be a [sample](/D/samp) from a [random vector](/D/rvec) $X \in \mathbb{R}^{p \times 1}$. Then, the sample correlation matrix of $x$ is the matrix whose entries are the [sample correlation coefficients](/D/corr-samp) between pairs of entries of $x_1, \ldots, x_n$:

$$ \label{eq:corrmat-samp-v1}
\mathrm{R}_{xx} =
\begin{bmatrix}
r_{x^{(1)},x^{(1)}} & \ldots & r_{x^{(1)},x^{(n)}} \\
\vdots & \ddots & \vdots \\
r_{x^{(n)},x^{(1)}} & \ldots & r_{x^{(n)},x^{(n)}}
\end{bmatrix}
$$

where the $r_{x^{(j)},x^{(k)}}$ is the [sample correlation](/D/corr-samp) between the $j$-th and the $k$-th entry of $X$ given by

$$ \label{eq:corrmat-samp-v2}
r_{x^{(j)},x^{(k)}} = \frac{\sum_{i=1}^n (x_{ij}-\bar{x}^{(j)}) (x_{ik}-\bar{x}^{(k)})}{\sqrt{\sum_{i=1}^n (x_{ij}-\bar{x}^{(j)})^2} \sqrt{\sum_{i=1}^n (x_{ik}-\bar{x}^{(k)})^2}}
$$

in which $\bar{x}^{(j)}$ and $\bar{x}^{(k)}$ are the [sample means](/D/mean-samp)

$$ \label{eq:mean-samp}
\begin{split}
\bar{x}^{(j)} &= \frac{1}{n} \sum_{i=1}^n x_{ij} \\
\bar{x}^{(k)} &= \frac{1}{n} \sum_{i=1}^n x_{ik} \; .
\end{split}
$$