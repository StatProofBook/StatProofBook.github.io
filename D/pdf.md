---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-02-13 19:26:00

title: "Probability density function"
chapter: "General Theorems"
section: "Probability theory"
topic: "Probability functions"
definition: "Probability density function"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Probability density function"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-02-13"
    url: "https://en.wikipedia.org/wiki/Probability_density_function"

def_id: "D10"
shortcut: "pdf"
username: "JoramSoch"
---


**Definition:** Let $X$ be a [continuous](/D/rvar-disc) [random variable](/D/rvar) with possible outcomes $\mathcal{X}$. Then, $f_X(x): \mathbb{R} \to \mathbb{R}$ is the probability density function (PDF) of $X$, if

$$ \label{eq:pdf-def-s0}
f_X(x) \geq 0
$$

for all $x \in \mathbb{R}$,

$$ \label{eq:pdf-def-s1}
\mathrm{Pr}(X \in A) = \int_{A} f_X(x) \, \mathrm{d}x
$$

for any $A \subset \mathcal{X}$ and

$$ \label{eq:pdf-def-s2}
\int_{\mathcal{X}} f_X(x) \, \mathrm{d}x = 1 \; .
$$