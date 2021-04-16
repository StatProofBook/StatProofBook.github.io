---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-04-16 12:04:00

title: "Sample variance"
chapter: "General Theorems"
section: "Probability theory"
topic: "Variance"
definition: "Sample variance"

sources:
  - authors: "Wikipedia"
    year: 2021
    title: "Variance"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-04-16"
    url: "https://en.wikipedia.org/wiki/Variance#Sample_variance"

def_id: "D143"
shortcut: "var-samp"
username: "JoramSoch"
---


**Definition:** Let $x = \left\lbrace x_1, \ldots, x_n \right\rbrace$ be a [sample](/D/samp) from a [random variable](/D/rvar) $X$. Then, the sample variance of $x$ is given by

$$ \label{eq:var-samp}
\hat{\sigma}^2 = \frac{1}{n} \sum_{i=1}^{n} (x_i - \bar{x})^2
$$

and the unbiased sample variance of $x$ is given by

$$ \label{eq:var-samp-unb}
s^2 = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2
$$

where $\bar{x}$ is the [sample mean](/D/mean-samp).