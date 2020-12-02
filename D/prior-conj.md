---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-12-02 17:55:00

title: "Conjugate and non-conjugate prior distribution"
chapter: "General Theorems"
section: "Bayesian statistics"
topic: "Prior distributions"
definition: "Conjugate vs. non-conjugate"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Conjugate prior"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-12-02"
    url: "https://en.wikipedia.org/wiki/Conjugate_prior"

def_id: "D120"
shortcut: "prior-conj"
username: "JoramSoch"
---


**Definition:** Let $m$ be a [generative model](/D/gm) with [likelihood function](/D/lf) $p(y \vert \theta, m)$ and [prior distribution](/D/prior) $p(\theta \vert m)$. Then,

* the [prior distribution](/D/prior) is called "conjugate", if it, when combined with the [likelihood function](/D/lf), leads to a [posterior distribution](/D/post) that belongs to the same family of [probability distributions](/D/dist);

* the prior distribution is called "non-conjugate", if this is not the case.