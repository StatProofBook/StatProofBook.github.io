---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-05-31 23:59:00

title: "Probability-generating function"
chapter: "General Theorems"
section: "Probability theory"
topic: "Other probability functions"
definition: "Probability-generating function"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Probability-generating function"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-05-31"
    url: "https://en.wikipedia.org/wiki/Probability-generating_function#Definition"

def_id: "D69"
shortcut: "pgf"
username: "JoramSoch"
---


**Definition:**

1) If $X$ is a [discrete](/D/rvar-disc) [random variable](/D/rvar) taking values in the non-negative integers $\left\lbrace 0, 1, \ldots \right\rbrace$, then the probability-generating function of $X$ is defined as

$$ \label{eq:pgf-var}
G_X(z) = \sum_{x=0}^{\infty} f_X(x) \, z^x
$$

where $z \in \mathbb{C}$ and $f_X(x)$ is the [probability mass function](/D/pmf) of $X$.

2) If $X$ is a [discrete](/D/rvar-disc) [random vector](/D/rvec) taking values in the $n$-dimensional integer lattice $x \in \left\lbrace 0, 1, \ldots \right\rbrace^n$, then the probability-generating function of $X$ is defined as

$$ \label{eq:cgf-vec}
G_X(z) = \sum_{x_1=0}^{\infty} \cdots \sum_{x_n=0}^{\infty} f_{X_1,\ldots,X_n}(x_1,\ldots,x_n) \, {z_1}^{x_1} \cdot \ldots \cdot {z_n}^{x_n}
$$

where $z \in \mathbb{C}^n$ and $f_{X_1,\ldots,X_n}(x_1,\ldots,x_n)$ is the [probability mass function](/D/pmf) of $X$.