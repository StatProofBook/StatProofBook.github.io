---
layout: definition
mathjax: true

author: "Kenneth Petrykowski"
affiliation: "University of Warsaw"
e_mail: "kenneth.petrykowski@gmail.com"
date: 2026-11-07 12:51:16

title: "Convergence in probability"
chapter: "General Theorems"
section: "Probability theory"
topic: "Random variables"
definition: "Convergence in probability"

sources:
  - authors: "George Casella, Roger L. Berger"
    year: 2002
    title: "Convergence in probability"
    in: "Statistical Inference"
    pages: "Second edition, Definition 5.5.1, p. 232"

def_id: "D249"
shortcut: "conv-prob"
username: "kjpetrykowski"
---

**Definition:** Let $Z\_1,Z\_2,\ldots$ and $Z$ be random variables on the same [probability space](/D/prob-spc). The sequence converges in probability to $Z$ if, for every $\varepsilon>0$,

$$ \label{eq:convergence-in-probability}
\lim_{n\to\infty}\mathrm{Pr}(|Z_n-Z|\geq\varepsilon)=0 \; .
$$

The limit $Z$ may be a constant. For any positive tolerance $\varepsilon$, the probability that $Z\_n$ differs from $Z$ by at least $\varepsilon$ tends to zero. For random functions $F\_n$ and a fixed function $F$, pointwise convergence in probability means that $F\_n(t)$ converges in probability to $F(t)$ for each fixed $t$.
