---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-07-28 02:51:00

title: "Cross-entropy"
chapter: "General Theorems"
section: "Information theory"
topic: "Shannon entropy"
definition: "Cross-entropy"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Cross entropy"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-07-28"
    url: "https://en.wikipedia.org/wiki/Cross_entropy#Definition"

def_id: "D85"
shortcut: "ent-cross"
username: "JoramSoch"
---


**Definition:** Let $X$ be a discrete [random variable](/D/rvar) with possible outcomes $\mathcal{X}$ and let $P$ and $Q$ be two [probability distributions](/D/dist) on $X$ with the [probability mass functions](/D/pmf) $p(x)$ and $q(x)$. Then, the cross-entropy of $Q$ relative to $P$ is defined as

$$ \label{eq:ent-cross}
\mathrm{H}(P,Q) = - \sum_{x \in \mathcal{X}} p(x) \cdot \log_b q(x)
$$

where $b$ is the base of the logarithm specifying in which unit the cross-entropy is determined.