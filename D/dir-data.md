---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-10-22 05:06:00

title: "Dirichlet-distributed data"
chapter: "Statistical Models"
section: "Probability data"
topic: "Dirichlet-distributed data"
definition: "Definition"

sources:

def_id: "D104"
shortcut: "dir-data"
username: "JoramSoch"
---


**Definition:** Dirichlet-distributed data are defined as a set of vectors of proportions $y = \left\lbrace y_1, \ldots, y_n \right\rbrace$ where

$$ \label{eq:dir-def}
\begin{split}
y_i &= [y_{i1}, \ldots, y_{ik}], \\
y_{ij} &\in [0,1] \quad \text{and} \\
\sum_{j=1}^k y_{ij} &= 1
\end{split}
$$

for all $i = 1,\ldots,n$ (and $j = 1,\ldots,k$) and each $y_i$ is independent and identically distributed according to a [Dirichlet distribution](/D/dir) with concentration parameters $\alpha = [\alpha_1, \ldots, \alpha_k]$:

$$ \label{eq:dir-data}
y_i \sim \mathrm{Dir}(\alpha), \quad i = 1, \ldots, n \; .
$$