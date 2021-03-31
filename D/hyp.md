---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-03-19 14:18:00

title: "Statistical hypothesis"
chapter: "General Theorems"
section: "Frequentist statistics"
topic: "Statistical hypotheses"
definition: "Statistical hypothesis"

sources:
  - authors: "Wikipedia"
    year: 2021
    title: "Statistical hypothesis testing"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-03-19"
    url: "https://en.wikipedia.org/wiki/Statistical_hypothesis_testing#Definition_of_terms"

def_id: "D127"
shortcut: "hyp"
username: "JoramSoch"
---


**Definition:** A statistical hypothesis is a statement about the parameters of a distribution describing a population from which observations can be sampled as [measured data](/D/data).

More precisely, let $m$ be a [generative model](/D/gm) describing measured data $y$ in terms of a distribution $\mathcal{D}(\theta)$ with model parameters $\theta \in \Theta$. Then, a statistical hypothesis is formally specified as

$$ \label{eq:hyp}
H: \; \theta \in \Theta^{*} \quad \text{where} \quad \Theta^{*} \subset \Theta \; .
$$