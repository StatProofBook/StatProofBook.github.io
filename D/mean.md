---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-02-13 19:38:00

title: "Expected value"
chapter: "General Theorems"
section: "Probability theory"
topic: "Expected value"
definition: "Definition"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Expected value"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-02-13"
    url: "https://en.wikipedia.org/wiki/Expected_value#Definition"

def_id: "D11"
shortcut: "mean"
username: "JoramSoch"
---


**Definition:**

1) The expected value (or, mean) of a discrete [random variable](/D/rvar) $X$ with domain $\mathcal{X}$ is

$$ \label{eq:mean-disc}
\mathrm{E}(X) = \sum_{x \in \mathcal{X}} x \cdot f_X(x)
$$

where $f_X(x)$ is the [probability mass function](/D/pmf) of $X$.

<br>
2) The expected value (or, mean) of a continuous [random variable](/D/rvar) $X$ with domain $\mathcal{X}$ is

$$ \label{eq:mean-cont}
\mathrm{E}(X) = \int_{\mathcal{X}} x \cdot f_X(x) \, \mathrm{d}x
$$

where $f_X(x)$ is the [probability density function](/D/pdf) of $X$.