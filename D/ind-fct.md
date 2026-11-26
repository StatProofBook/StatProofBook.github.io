---
layout: definition
mathjax: true

author: "Kenneth Petrykowski"
affiliation: "University of Warsaw"
e_mail: "kenneth.petrykowski@gmail.com"
date: 2026-10-28 23:38:29

title: "Indicator function and indicator random variable"
chapter: "General Theorems"
section: "Probability theory"
topic: "Random variables"
definition: "Indicator function and indicator random variable"

sources:
  - authors: "George Casella, Roger L. Berger"
    year: 2002
    title: "Exponential families"
    in: "Statistical Inference"
    pages: "Second edition, Definition 3.4.5, p. 113"

def_id: "D247"
shortcut: "ind-fct"
username: "kjpetrykowski"
---

**Definition:** For a point $z$, the indicator function of a set $A$ is given by

$$ \label{eq:indicator-function}
\mathbf{1}_A(z)=
\begin{cases}
1,&z\in A,\\
0,&z\notin A \; .
\end{cases}
$$

If $E$ is an event in a [probability space](/D/prob-spc), its indicator random variable $\mathbf{1}\_E$ is 1 when $E$ occurs and 0 otherwise. For a real random variable $X$ and a threshold $x$, $\mathbf{1}\_{\lbrace X\leq x\rbrace}$ indicates whether $X$ is at most $x$.
