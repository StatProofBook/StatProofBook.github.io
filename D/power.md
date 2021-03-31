---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-03-31 09:01:00

title: "Power of a statistical test"
chapter: "General Theorems"
section: "Frequentist statistics"
topic: "Hypothesis testing"
definition: "Power of a test"

sources:
  - authors: "Wikipedia"
    year: 2021
    title: "Power of a test"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-03-31"
    url: "https://en.wikipedia.org/wiki/Power_of_a_test#Description"

def_id: "D137"
shortcut: "power"
username: "JoramSoch"
---


**Definition:** Let there be a [statistical hypothesis test](/D/test) with [null hypothesis](/D/h0) $H_0$ and [alternative hypothesis](/D/h1) $H_1$. Then, the power of the test is the probability of a true-positive result or not making a type II error, i.e. the [probability](/D/prob) of rejecting $H_0$, given that $H_1$ is actually true.

For given [null](/D/h0) and [alternative](/D/h1) [hypothesis](/D/hyp), the size is determined by the following [conditional probability](/D/prob-cond):

$$ \label{eq:power}
\mathrm{Pr}(\text{test rejects } H_0 \vert H_1) \; .
$$