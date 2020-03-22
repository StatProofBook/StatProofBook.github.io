---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-03-21 12:27:00

title: "Conditional differential entropy"
chapter: "General Theorems"
section: "Information theory"
topic: "Differential entropy"
definition: "Conditional differential entropy"

sources:

def_id: "D34"
shortcut: "dent-cond"
username: "JoramSoch"
---


**Definition:** Let $X$ and $Y$ be continuous [random variables](/D/rvar) with possible outcomes $\mathcal{X}$ and $\mathcal{Y}$ and [probability density functions](/D/pdf) $p(x)$ and $p(y)$. Then, the conditional differential entropy of $Y$ given $X$ or, differential entropy of $Y$ conditioned on $X$, is defined as

$$ \label{eq:dent-cond}
\mathrm{h}(Y|X) = \int_{x \in \mathcal{X}} p(x) \cdot \mathrm{h}(Y|X=x)
$$

where $\mathrm{h}(Y \vert X=x)$ is the [(marginal) differential entropy](/D/dent) of $Y$, evaluated at $x$.