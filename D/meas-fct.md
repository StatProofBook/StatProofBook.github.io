---
layout: definition
mathjax: true

author: "Kenneth Petrykowski"
affiliation: "University of Warsaw"
e_mail: "kenneth.petrykowski@gmail.com"
date: 2026-11-11 19:15:24

title: "Measurable function"
chapter: "General Theorems"
section: "Probability theory"
topic: "Random variables"
definition: "Measurable function"

sources:
  - authors: "Erhan Çınlar"
    year: 2011
    title: "Measurable Functions"
    in: "Probability and Stochastics"
    pages: "Chapter I, Section 2, pp. 6-7, especially Proposition 2.6"
    doi: "10.1007/978-0-387-87859-1_1"

def_id: "D253"
shortcut: "meas-fct"
username: "kjpetrykowski"
---

**Definition:** Let $S$ and $T$ be sets, with [$\sigma$-algebras](/D/sig-alg) $\mathcal S$ and $\mathcal T$ specifying their measurable subsets. A function $f:S\to T$ is measurable if, for every measurable set $B$ of output values, the inputs mapped into $B$ form a measurable set. This set of inputs is called the inverse image of $B$.

$$ \label{eq:measurable-preimage}
f^{-1}(B)=\{s\in S:f(s)\in B\}\in\mathcal S
\qquad\text{for every }B\in\mathcal T \; .
$$

For a real-valued function, take the usual measurable sets on the real line, called Borel sets. Then $f$ is measurable if and only if the following condition holds for every real cutoff $c$:

$$ \label{eq:measurable-cutoff}
\{s\in S:f(s)\leq c\}\in\mathcal S \; .
$$

On a [probability space](/D/prob-spc), this set is the event that the value of $f$ is at most $c$.
