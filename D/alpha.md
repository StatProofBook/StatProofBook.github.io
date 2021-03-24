---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-03-19 14:50:00

title: "Significance level"
chapter: "General Theorems"
section: "Frequentist statistics"
topic: "Hypothesis testing"
definition: "Significance level"

sources:
  - authors: "Wikipedia"
    year: 2021
    title: "Statistical hypothesis testing"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-03-19"
    url: "https://en.wikipedia.org/wiki/Statistical_hypothesis_testing#Definition_of_terms"

def_id: "D133"
shortcut: "alpha"
username: "JoramSoch"
---


**Definition:** Let the [size](/D/size) of a [statistical hypothesis test](/D/test) be the probability of a false-positive result or making a type I error, i.e. the [probability](/D/prob) of rejecting the [null hypothesis](/D/h0) $H_0$, given that $H_0$ is actually true:

$$ \label{eq:size}
\mathrm{Pr}(\text{test rejects } H_0 \vert H_0) \; .
$$

Then, the test is said to have significance level $\alpha$, if the size is less than or equal to $\alpha$:

$$ \label{eq:alpha}
\mathrm{Pr}(\text{test rejects } H_0 \vert H_0) \leq \alpha \; .
$$