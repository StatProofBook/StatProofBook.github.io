---
layout: definition
mathjax: true

author: "Kenneth Petrykowski"
affiliation: "University of Warsaw"
e_mail: "kenneth.petrykowski@gmail.com"
date: 2026-11-07 12:31:59

title: "Empirical cumulative distribution function"
chapter: "General Theorems"
section: "Probability theory"
topic: "Cumulative distribution function"
definition: "Empirical cumulative distribution function"

sources:
  - authors: "John A. Rice"
    year: 2007
    title: "The empirical cumulative distribution function"
    in: "Mathematical Statistics and Data Analysis"
    pages: "Third edition, Section 10.2.1, p. 378"

def_id: "D248"
shortcut: "ecdf"
username: "kjpetrykowski"
---

**Definition:** Let $x\_1,\ldots,x\_n$ be real observations, with $n\geq1$. At a threshold $t$, the empirical cumulative distribution function $F\_n(t)$ is the fraction of observations less than or equal to $t$. Using [indicators](/D/ind-fct), this fraction is

$$ \label{eq:ecdf}
F_n(t)=\frac{1}{n}\sum_{i=1}^n\mathbf{1}_{\lbrace x_i\leq t\rbrace},
\qquad t\in\mathbb{R} \; .
$$

Each indicator contributes 1 if $x\_i\leq t$ and 0 otherwise. For random observations, replacing each $x\_i$ by $X\_i$ gives a random function $F\_n$. The observations may be dependent or have different distributions.
