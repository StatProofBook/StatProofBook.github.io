---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-02-19 18:18:00

title: "Joint entropy"
chapter: "General Theorems"
section: "Information theory"
topic: "Shannon entropy"
definition: "Joint entropy"

sources:
  - authors: "Cover TM, Thomas JA"
    year: 1991
    title: "Joint Entropy and Conditional Entropy"
    in: "Elements of Information Theory"
    pages: "ch. 2.2, p. 16"
    url: "https://www.wiley.com/en-us/Elements+of+Information+Theory%2C+2nd+Edition-p-9780471241959"

def_id: "D18"
shortcut: "ent-joint"
username: "JoramSoch"
---


**Definition:** Let $X$ and $Y$ be discrete [random variables](/D/rvar) with possible outcomes $\mathcal{X}$ and $\mathcal{Y}$ and [joint probability](/D/prob-joint) [mass function](/D/pmf) $p(x,y)$. Then, the joint entropy of $X$ and $Y$ is defined as

$$ \label{eq:ent-joint}
\mathrm{H}(X,Y) = - \sum_{x \in \mathcal{X}} \sum_{y \in \mathcal{Y}} p(x,y) \cdot \log_b p(x,y)
$$

where $b$ is the base of the logarithm specifying in which unit the entropy is determined.