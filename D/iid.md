---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2024-08-08 11:37:05

title: "independent and identically distributed"
chapter: "General Theorems"
section: "Probability theory"
topic: "Random variables"
definition: "independent and identically distributed"

sources:
  - authors: "Wikipedia"
    year: 2024
    title: "Independent and identically distributed random variables"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2024-08-08"
    url: "https://en.wikipedia.org/wiki/Independent_and_identically_distributed_random_variables#Introduction"

def_id: "D200"
shortcut: "iid"
username: "JoramSoch"
---


**Definition:** Let $X_i$ for $i = 1,\ldots,n$ be [random variables](/D/rvar). Then, $X_1, \ldots, X_n$ are called independent and identically distributed (i.i.d.), if (i) they are [statistically independent](/D/ind) and (ii) they follow the same [probability distribution](/D/dist) $\mathcal{D}$ with the same parameters $\theta$:

$$ \label{eq:iid}
X_i \overset{\mathrm{i.i.d.}}{\sim} \mathcal{D}(\theta), \; i = 1,\ldots,n \; .
$$

Often, especially in [linear regression models, error terms](/D/mlr) are independent and identically distributed according to a [normal distribution](/D/norm) with mean zero and unknown variance:

$$ \label{eq:iid-mlr}
\varepsilon_i \overset{\mathrm{i.i.d.}}{\sim} \mathcal{N}(0,\sigma^2), \; i = 1,\ldots,n \; .
$$