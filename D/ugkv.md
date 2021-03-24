---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-03-23 16:12:00

title: "Univariate Gaussian with known variance"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Univariate Gaussian with known variance"
definition: "Definition"

sources:
  - authors: "Bishop, Christopher M."
    year: 2006
    title: "Bayesian inference for the Gaussian"
    in: "Pattern Recognition for Machine Learning"
    pages: "ch. 2.3.6, p. 97, eq. 2.137"
    url: "http://users.isr.ist.utl.pt/~wurmd/Livros/school/Bishop%20-%20Pattern%20Recognition%20And%20Machine%20Learning%20-%20Springer%20%202006.pdf"

def_id: "D136"
shortcut: "ugkv"
username: "JoramSoch"
---


**Definition:** A univariate Gaussian data set with known variance is given by a set of real numbers $y = \left\lbrace y_1, \ldots, y_n \right\rbrace$, independent and identically distributed according to a [normal distribution](/D/norm) with unknown mean $\mu$ and known variance $\sigma^2$:

$$ \label{eq:ug}
y_i \sim \mathcal{N}(\mu, \sigma^2), \quad i = 1, \ldots, n \; .
$$