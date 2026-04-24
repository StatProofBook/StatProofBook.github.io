---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2026-04-23 15:45:22

title: "Univariate von Mises"
chapter: "Statistical Models"
section: "Periodic data"
topic: "Univariate von Mises"
definition: "Definition"

sources:
  - authors: "Bishop CM"
    year: 2006
    title: "Periodic variables"
    in: "Pattern Recognition for Machine Learning"
    pages: "sect. 2.3.8, p. 108"
    url: "http://users.isr.ist.utl.pt/~wurmd/Livros/school/Bishop%20-%20Pattern%20Recognition%20And%20Machine%20Learning%20-%20Springer%20%202006.pdf"

def_id: "D232"
shortcut: "vm-data"
username: "JoramSoch"
---


**Definition:** A univariate von Mises data set is given by a set of real numbers $y = \left\lbrace y_1, \ldots, y_n \right\rbrace$ with $y_i \in [0, 2 \pi), \; i = 1,\ldots,n$, [independent and identically distributed](/D/iid) according to a [von Mises distribution](/D/vm) with unknown circular mean $\mu \in [0, 2 \pi)$ and unknown reciprocal dispersion $\kappa > 0$:

$$ \label{eq:vm}
y_i \sim \mathrm{vM}(\mu, \kappa), \quad i = 1, \ldots, n
$$