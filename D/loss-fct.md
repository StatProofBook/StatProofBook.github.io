---
layout: definition
mathjax: true

author: "Kenneth Petrykowski"
affiliation: "University of Warsaw"
e_mail: "kenneth.petrykowski@gmail.com"
date: 2026-11-07 13:29:43

title: "Loss function"
chapter: "General Theorems"
section: "Estimation theory"
topic: "Basic concepts of estimation"
definition: "Loss function"

sources:
  - authors: "George Casella, Roger L. Berger"
    year: 2002
    title: "Loss function optimality"
    in: "Statistical Inference"
    pages: "Second edition, Section 7.3.4, pp. 348-349"

def_id: "D252"
shortcut: "loss-fct"
username: "kjpetrykowski"
---

**Definition:** Let $\mathcal A$ be the set of allowed decisions (actions) and $\Theta$ the set of possible states or [parameter](/D/para) values. A loss function gives the nonnegative cost $L(a,\theta)$ of taking action $a$ when the true state is $\theta$:

$$ \label{eq:loss-function}
L:\mathcal A\times\Theta\longrightarrow[0,\infty),
\qquad(a,\theta)\longmapsto L(a,\theta) \; .
$$

For a given state, an action with smaller loss is preferable. For example, when $a$ is an estimate of a real parameter $\theta$, squared error loss is

$$ \label{eq:squared-error-loss}
L(a,\theta)=(a-\theta)^2 \; .
$$
