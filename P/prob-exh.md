---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-08-08 04:10:00

title: "Probability of exhaustive events"
chapter: "General Theorems"
section: "Probability theory"
topic: "Probability axioms"
theorem: "Probability of exhaustive events"

sources:
  - authors: "Alan Stuart & J. Keith Ord"
    year: 1994
    title: "Probability and Statistical Inference"
    in: "Kendall's Advanced Theory of Statistics, Vol. 1: Distribution Theory"
    pages: "pp. 288-289"
    url: "https://www.wiley.com/en-us/Kendall%27s+Advanced+Theory+of+Statistics%2C+3+Volumes%2C+Set%2C+6th+Edition-p-9780470669549"
  - authors: "Wikipedia"
    year: 2021
    title: "Probability axioms"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-08-08"
    url: "https://en.wikipedia.org/wiki/Probability_axioms#Axioms"

proof_id: "P249"
shortcut: "prob-exh"
username: "JoramSoch"
---


**Theorem:** Let $B_1, \ldots, B_n$ be mutually exclusive and collectively exhaustive subsets of a [sample space](/D/samp-spc) $\Omega$. Then, their [total probability](/P/prob-tot) is one:

$$ \label{eq:prob-exh}
\sum_i P(B_i) = 1 \; .
$$


**Proof:** Because all $B_i$ are mutually exclusive, we have:

$$ \label{eq:B-exclusive}
B_i \cap B_j = \emptyset \quad \text{for all} \quad i \neq j \; .
$$

Because the $B_i$ are collectively exhaustive, we have:

$$ \label{eq:B-exhaustive}
\cup_i \, B_i = \Omega \; .
$$

Thus, the [third axiom of probability](/D/prob-ax) implies that

$$ \label{eq:prob-exh-s1}
\sum_i P(B_i) = P(\Omega) \; .
$$

and the [second axiom of probability](/D/prob-ax) implies that

$$ \label{eq:prob-exh-s2}
\sum_i P(B_i) = 1 \; .
$$