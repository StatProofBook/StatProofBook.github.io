---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2025-02-06 16:36:07

title: "Joint probability density function"
chapter: "General Theorems"
section: "Probability theory"
topic: "Probability density function"
definition: "Joint probability density function"

sources:
  - authors: "Wikipedia"
    year: 2025
    title: "Probability density function"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2025-02-06"
    url: "https://en.wikipedia.org/wiki/Probability_density_function#Densities_associated_with_multiple_variables"

def_id: "D216"
shortcut: "pdf-joint"
username: "JoramSoch"
---


**Definition:** Let $X \in \mathbb{R}^{n}$ be a [continuous](/D/rvar-disc) [random vector](/D/rvec). Then, a function $f_X(x): \mathbb{R}^n \to \mathbb{R}$ is the [joint](/D/dist-joint) [probability density function](/D/pdf) of $X$, if

$$ \label{eq:pdf-joint-def-s0}
f_X(x) \geq 0
$$

for all $x \in \mathbb{R}^n$,

$$ \label{eq:pdf-joint-def-s1}
\mathrm{Pr}(X \in A) = \int_{A} f_X(x) \, \mathrm{d}x
$$

for any $A \subset \mathbb{R}^n$ and

$$ \label{eq:pdf-joint-def-s2}
\int_{\mathbb{R}^n} f_X(x) \, \mathrm{d}x = 1 \; .
$$