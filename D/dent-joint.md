---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-03-21 12:37:00

title: "Joint differential entropy"
chapter: "General Theorems"
section: "Information theory"
topic: "Differential entropy"
definition: "Joint differential entropy"

sources:

def_id: "D35"
shortcut: "dent-joint"
username: "JoramSoch"
---


**Definition:** Let $X$ and $Y$ be continuous [random variables](/D/rvar) with possible outcomes $\mathcal{X}$ and $\mathcal{Y}$ and [joint probability](/D/prob-joint) [density function](/D/pdf) $p(x,y)$. Then, the joint differential entropy of $X$ and $Y$ is defined as

$$ \label{eq:dent-joint}
\mathrm{h}(X,Y) = - \int_{x \in \mathcal{X}} \int_{y \in \mathcal{Y}} p(x,y) \cdot \log_b p(x,y) \, \mathrm{d}y \, \mathrm{d}x
$$

where $b$ is the base of the logarithm specifying in which unit the differential entropy is determined.