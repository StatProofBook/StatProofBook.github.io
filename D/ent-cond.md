---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-02-19 18:08:00

title: "Conditional entropy"
chapter: "General Theorems"
section: "Information theory"
topic: "Shannon entropy"
definition: "Conditional entropy"

sources:
  - authors: "Cover TM, Thomas JA"
    year: 1991
    title: "Joint Entropy and Conditional Entropy"
    in: "Elements of Information Theory"
    pages: "ch. 2.2, p. 15"
    url: "https://www.wiley.com/en-us/Elements+of+Information+Theory%2C+2nd+Edition-p-9780471241959"

def_id: "D17"
shortcut: "ent-cond"
username: "JoramSoch"
---


**Definition:** Let $X$ and $Y$ be discrete [random variables](/D/rvar) with possible outcomes $\mathcal{X}$ and $\mathcal{Y}$ and [probability mass functions](/D/pmf) $p(x)$ and $p(y)$. Then, the conditional entropy of $Y$ given $X$ or, entropy of $Y$ conditioned on $X$, is defined as

$$ \label{eq:ent-cond}
\mathrm{H}(Y|X) = \sum_{x \in \mathcal{X}} p(x) \cdot \mathrm{H}(Y|X=x)
$$

where $\mathrm{H}(Y \vert X=x)$ is the [(marginal) entropy](/D/ent) of $Y$, evaluated at $x$.