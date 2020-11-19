---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-02-13 19:09:00

title: "Probability mass function"
chapter: "General Theorems"
section: "Probability theory"
topic: "Probability functions"
definition: "Probability mass function"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Probability mass function"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-02-13"
    url: "https://en.wikipedia.org/wiki/Probability_mass_function"

def_id: "D9"
shortcut: "pmf"
username: "JoramSoch"
---


**Definition:** Let $X$ be a [discrete](/D/rvar-disc) [random variable](/D/rvar) with possible outcomes $\mathcal{X}$. Then, $f_X(x): \mathbb{R} \to [0,1]$ is the probability mass function (PMF) of $X$, if

$$ \label{eq:pmf-def-s0}
f_X(x) = 0
$$

for all $x \notin \mathcal{X}$,

$$ \label{eq:pmf-def-s1}
\mathrm{Pr}(X = x) = f_X(x)
$$

for all $x \in \mathcal{X}$ and

$$ \label{eq:pmf-def-s2}
\sum_{x \in \mathcal{X}} f_X(x) = 1 \; .
$$