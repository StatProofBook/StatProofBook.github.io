---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-07-23 16:32:00

title: "Mutual exclusivity"
chapter: "General Theorems"
section: "Probability theory"
topic: "Probability"
definition: "Mutual exclusivity"

sources:
  - authors: "Wikipedia"
    year: 2021
    title: "Mutual exclusivity"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-07-23"
    url: "https://en.wikipedia.org/wiki/Mutual_exclusivity#Probability"

def_id: "D156"
shortcut: "exc"
username: "JoramSoch"
---


**Definition:** Generally speaking, [random events](/D/reve) are mutually exclusive, if the [probability](/D/prob) of their disjunction can be expressed in terms of their [marginal probabilities](/D/prob-marg).

<br>
More precisely, a set of statements $A_1, \ldots, A_n$ is called mutually exclusive, if

$$ \label{eq:exc}
p(A_1 \vee \ldots \vee A_n) = \sum_{i=1}^n p(A_i)
$$

where $p(A_1, \ldots, A_n)$ is the [probability](/D/prob) of the disjunction of $A_1, \ldots, A_n$ and $p(A_i)$ is the [marginal probability](/D/prob-marg) of $A_i$, for all $i = 1, \ldots, n$.