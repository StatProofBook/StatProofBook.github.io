---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2026-03-26 11:04:25

title: "Joint probability mass function"
chapter: "General Theorems"
section: "Probability theory"
topic: "Probability mass function"
definition: "Joint probability mass function"

sources:
  - authors: "Wikipedia"
    year: 2026
    title: "Joint probability distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2026-03-26"
    url: "https://en.wikipedia.org/wiki/Joint_probability_distribution#Joint_density_function_or_mass_function"

def_id: "D228"
shortcut: "pmf-joint"
username: "JoramSoch"
---


**Definition:** Let $X \in \mathcal{X} = \mathcal{X}_1 \times \ldots \times \mathcal{X}_n$ be a [discrete](/D/rvar-disc) [random vector](/D/rvec) where $\mathcal{X}_1, \ldots, \mathcal{X}_n$ are the sets of possible values of the entries $X_1, \ldots, X_n$. Then, a function $f_X(x): \mathcal{X} \to \mathbb{R}$ is the [joint](/D/dist-joint) [probability mass function](/D/pmf) of $X$, if

$$ \label{eq:pmf-joint-def-s0}
f_X(x) \in [0, 1]
$$

for all $x \in \mathcal{X}$,

$$ \label{eq:pmf-joint-def-s1}
\mathrm{Pr}(X_1 = x_1, \ldots, X_n = x_n) = f_X(x_1, \ldots, x_n)
$$

for all $(x_1, \ldots, x_n) \in \mathcal{X}$ and

$$ \label{eq:pmf-joint-def-s2}
\sum_{x_1 \in \mathcal{X}_1} \ldots \sum_{x_n \in \mathcal{X}_n} f_X(x_1, \ldots, x_n) = 1 \; .
$$