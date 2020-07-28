---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-07-28 03:03:00

title: "Differential cross-entropy"
chapter: "General Theorems"
section: "Information theory"
topic: "Differential entropy"
definition: "Differential cross-entropy"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Cross entropy"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-07-28"
    url: "https://en.wikipedia.org/wiki/Cross_entropy#Definition"

def_id: "D86"
shortcut: "dent-cross"
username: "JoramSoch"
---


**Definition:** Let $X$ be a continuous [random variable](/D/rvar) with possible outcomes $\mathcal{X}$ and let $P$ and $Q$ be two [probability distributions](/D/dist) on $X$ with the [probability density functions](/D/pdf) $p(x)$ and $q(x)$. Then, the differential cross-entropy of $Q$ relative to $P$ is defined as

$$ \label{eq:dent-cross}
\mathrm{h}(P,Q) = - \int_{\mathcal{X}} p(x) \log_b q(x) \, \mathrm{d}x
$$

where $b$ is the base of the logarithm specifying in which unit the differential cross-entropy is determined.