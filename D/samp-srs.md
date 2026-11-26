---
layout: definition
mathjax: true

author: "Kenneth Petrykowski"
affiliation: "University of Warsaw"
e_mail: "kenneth.petrykowski@gmail.com"
date: 2026-11-07 13:02:39

title: "Simple random sampling without replacement"
chapter: "General Theorems"
section: "Probability theory"
topic: "Random experiments"
definition: "Simple random sampling without replacement"

sources:
  - authors: "John A. Rice"
    year: 2007
    title: "Simple random sampling"
    in: "Mathematical Statistics and Data Analysis"
    pages: "Third edition, Section 7.3, p. 202"

def_id: "D250"
shortcut: "samp-srs"
username: "kjpetrykowski"
---

**Definition:** Consider a finite population with $N$ distinct labels $1,\ldots,N$ and fix $1\leq n\leq N$. A simple random sample without replacement is a random subset $S$ of $n$ labels such that, for every subset $s$ of that size,

$$ \label{eq:simple-random-sample}
\mathrm{Pr}(S=s)=\frac{1}{\binom{N}{n}} \; .
$$

Thus all subsets of size $n$ are equally likely, and no label appears more than once. Different labels may carry the same observed value.
