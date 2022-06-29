---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-05-14 23:06:00

title: "Normal-Wishart distribution"
chapter: "Probability Distributions"
section: "Matrix-variate continuous distributions"
topic: "Normal-Wishart distribution"
definition: "Definition"

sources:

def_id: "D175"
shortcut: "nw"
username: "JoramSoch"
---


**Definition:** Let $X$ be an $n \times p$ [random matrix](/D/rmat) and let $Y$ be a $p \times p$ positive-definite symmetric matrix. Then, $X$ and $Y$ are said to follow a normal-Wishart distribution

$$ \label{eq:nw}
X,Y \sim \mathrm{NW}(M, U, V, \nu) \; ,
$$

if the distribution of $X$ conditional on $Y$ is a [matrix-normal distribution](/D/matn) with mean $M$, covariance across rows $U$, covariance across columns $Y^{-1}$ and $Y$ follows a [Wishart distribution](/D/wish) with scale matrix $V$ and degrees of freedom $\nu$:

$$ \label{eq:matn-wish}
\begin{split}
X \vert Y &\sim \mathcal{MN}(M, U, Y^{-1}) \\
Y &\sim \mathcal{W}(V, \nu) \; .
\end{split}
$$

The $p \times p$ matrix $Y$ can be seen as the [precision matrix](/D/precmat) across the columns of the $n \times p$ matrix $X$.