---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-02-19 17:36:00

title: "Shannon entropy"
chapter: "General Theorems"
section: "Information theory"
topic: "Shannon entropy"
definition: "Definition"

sources:
  - authors: "Shannon CE"
    year: 1948
    title: "A Mathematical Theory of Communication"
    in: "Bell System Technical Journal"
    pages: "vol. 27, iss. 3, pp. 379-423"
    url: "https://ieeexplore.ieee.org/document/6773024"
    doi: "10.1002/j.1538-7305.1948.tb01338.x"

def_id: "D15"
shortcut: "ent"
username: "JoramSoch"
---


**Definition:** Let $X$ be a discrete [random variable](/D/rvar) with possible outcomes $\mathcal{X}$ and the (observed or assumed) [probability mass function](/D/pmf) $p(x) = f_X(x)$. Then, the entropy (also referred to as "Shannon entropy") of $X$ is defined as

$$ \label{eq:ent}
\mathrm{H}(X) = - \sum_{x \in \mathcal{X}} p(x) \cdot \log_b p(x)
$$

where $b$ is the base of the logarithm specifying in which unit the entropy is determined.