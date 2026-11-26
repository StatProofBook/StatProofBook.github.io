---
layout: definition
mathjax: true

author: "Kenneth Petrykowski"
affiliation: "University of Warsaw"
e_mail: "kenneth.petrykowski@gmail.com"
date: 2026-11-11 19:47:17

title: "Sigma-algebra"
chapter: "General Theorems"
section: "Probability theory"
topic: "Random experiments"
definition: "Sigma-algebra"

sources:
  - authors: "Erhan Çınlar"
    year: 2011
    title: "Measurable Spaces"
    in: "Probability and Stochastics"
    pages: "Chapter I, Section 1, p. 2, conditions (1.3a-b)"
    doi: "10.1007/978-0-387-87859-1_1"

def_id: "D254"
shortcut: "sig-alg"
username: "kjpetrykowski"
---

**Definition:** Let $S$ be a set. A collection $\mathcal S$ of subsets of $S$ is called a $\sigma$-algebra (or $\sigma$-field) on $S$ if it has the following three properties:

1. The whole set $S$ belongs to $\mathcal S$.

2. If $A$ belongs to $\mathcal S$, then its complement $S\setminus A$ also belongs to $\mathcal S$.

3. If $A\_1,A\_2,\ldots$ belong to $\mathcal S$, then their union $\bigcup\_{n=1}^{\infty} A\_n$ also belongs to $\mathcal S$.

The sets in $\mathcal S$ are called measurable sets.
