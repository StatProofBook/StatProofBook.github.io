---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2026-04-20 15:18:30

title: "Circular random variable"
chapter: "General Theorems"
section: "Probability theory"
topic: "Random variables"
definition: "Circular random variable"

sources:
  - authors: "Wikipedia"
    year: 2026
    title: "Circular distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2026-04-20"
    url: "https://en.wikipedia.org/wiki/Circular_distribution#Examples"

def_id: "D229"
shortcut: "rvar-circ"
username: "JoramSoch"
---


**Definition:** Let $X$ be a [random variable](/D/rvar) with possible outcomes $\mathcal{X}$. Then, $X$ is called a circular random variable, if $\mathcal{X} = [0, 2 \pi)$ and if the [probability density function](/D/pdf) of $X$ satisfies

$$ \label{eq:pdf-circ}
f_X(x + 2 \pi k) = f_X(x)
\quad \text{for all} \quad
k \in \mathbb{Z} \; .
$$