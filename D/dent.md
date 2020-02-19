---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-02-19 17:53:00

title: "Differential entropy"
chapter: "General Theorems"
section: "Information theory"
topic: "Differential entropy"
definition: "Definition"

sources:
  - authors: "Cover TM, Thomas JA"
    year: 1991
    title: "Differential Entropy"
    in: "Elements of Information Theory"
    pages: "ch. 8.1, p. 243"
    url: "https://www.wiley.com/en-us/Elements+of+Information+Theory%2C+2nd+Edition-p-9780471241959"

def_id: "D16"
shortcut: "dent"
username: "JoramSoch"
---


**Definition:** Let $X$ be a continuous [random variable](/D/rvar) with possible outcomes $\mathcal{X}$ and the (estimated or assumed) [probability density function](/D/pdf) $p(x) = f_X(x)$. Then, the differential entropy (also referred to as "continuous entropy") of $X$ is defined as

$$ \label{eq:dent}
\mathrm{h}(X) = - \int_{\mathcal{X}} p(x) \log_b p(x) \, \mathrm{d}x
$$

where $b$ is the base of the logarithm specifying in which unit the entropy is determined.