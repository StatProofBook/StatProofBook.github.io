---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-11-26 14:30:00

title: "Probability space"
chapter: "General Theorems"
section: "Probability theory"
topic: "Random experiments"
definition: "Probability space"

sources:
  - authors: "Wikipedia"
    year: 2021
    title: "Probability space"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-11-26"
    url: "https://en.wikipedia.org/wiki/Probability_space#Definition"

def_id: "D167"
shortcut: "prob-spc"
username: "JoramSoch"
---


**Definition:** Given a [random experiment](/D/rexp), a probability space $(\Omega, \mathcal{E}, P)$ is a triple consisting of

* the [sample space](/D/samp-spc) $\Omega$, i.e. the set of all possible outcomes from this experiment;

* an [event space](/D/eve-spc) $\mathcal{E} \subseteq 2^\Omega$, i.e. a set of subsets from the sample space, called [events](/D/reve);

* a [probability measure](/D/prob-meas) $P: \; \mathcal{E} \rightarrow [0,1]$, i.e. a function mapping from the [event space](/D/eve-spc) to the real numbers, observing the [axioms of probability](/D/prob-ax).