---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-03-19 14:46:00

title: "Size of a statistical test"
chapter: "General Theorems"
section: "Frequentist statistics"
topic: "Hypothesis testing"
definition: "Size of a test"

sources:
  - authors: "Wikipedia"
    year: 2021
    title: "Size (statistics)"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-03-19"
    url: "https://en.wikipedia.org/wiki/Size_(statistics)"

def_id: "D132"
shortcut: "size"
username: "JoramSoch"
---


**Definition:** Let there be a [statistical hypothesis test](/D/test) with [null hypothesis](/D/h0) $H_0$. Then, the size of the test is the probability of a false-positive result or making a type I error, i.e. the [probability](/D/prob) of rejecting the [null hypothesis](/D/h0) $H_0$, given that $H_0$ is actually true.

For a [simple null hypothesis](/D/hyp-simp), the size is determined by the following [conditional probability](/D/prob-cond):

$$ \label{eq:size-h0-simp}
\mathrm{Pr}(\text{test rejects } H_0 \vert H_0) \; .
$$

For a [composite null hypothesis](/D/hyp-simp), the size is the supremum over all possible realizations of the [null hypothesis](/D/h0):

$$ \label{eq:size-h0-comp}
\operatorname*{sup}_{h \in H_0} \mathrm{Pr}(\text{test rejects } H_0 \vert h) \; .
$$