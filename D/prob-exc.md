---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-10-22 04:36:00

title: "Exceedance probability"
chapter: "General Theorems"
section: "Probability theory"
topic: "Probability"
definition: "Exceedance probability"

sources:
  - authors: "Stephan KE, Penny WD, Daunizeau J, Moran RJ, Friston KJ"
    year: 2009
    title: "Bayesian model selection for group studies"
    in: "NeuroImage"
    pages: "vol. 46, pp. 1004–1017, eq. 16"
    url: "https://www.sciencedirect.com/science/article/abs/pii/S1053811909002638"
    doi: "10.1016/j.neuroimage.2009.03.025"
  - authors: "Soch J, Allefeld C"
    year: 2016
    title: "Exceedance Probabilities for the Dirichlet Distribution"
    in: "arXiv stat.AP"
    pages: "1611.01439"
    url: "https://arxiv.org/abs/1611.01439"

def_id: "D103"
shortcut: "prob-exc"
username: "JoramSoch"
---


**Definition:** Let $X = \left\lbrace X_1, \ldots, X_n \right\rbrace$ be a set of $n$ [random variables](/D/rvar) which the [joint probability distribution](/D/dist-joint) $p(X) = p(X_1, \ldots, X_n)$. Then, the exceedance probability for random variable $X_i$ is the [probability](/D/prob) that $X_i$ is larger than all other random variables $X_j, \; j \neq i$:

$$ \label{eq:EP}
\begin{split}
\varphi(X_i) &= \mathrm{Pr}\left( \forall j \in \left\lbrace 1, \ldots, n | j \neq i \right\rbrace: \, X_i > X_j \right) \\
&= \mathrm{Pr}\left( \bigwedge_{j \neq i} X_i > X_j \right) \\
&= \mathrm{Pr}\left( X_i = \mathrm{max}(\left\lbrace X_1, \ldots, X_n \right\rbrace) \right) \\
&= \int_{X_i = \mathrm{max}(X)} p(X) \, \mathrm{d}X \; .
\end{split}
$$