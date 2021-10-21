---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-07-30 11:58:00

title: "Probability of the empty set"
chapter: "General Theorems"
section: "Probability theory"
topic: "Probability axioms"
theorem: "Probability of the empty set"

sources:
  - authors: "A.N. Kolmogorov"
    year: 1950
    title: "Elementary Theory of Probability"
    in: "Foundations of the Theory of Probability"
    pages: "p. 6, eq. 3"
    url: "https://archive.org/details/foundationsofthe00kolm/page/6/mode/2up"
  - authors: "Alan Stuart & J. Keith Ord"
    year: 1994
    title: "Probability and Statistical Inference"
    in: "Kendall's Advanced Theory of Statistics, Vol. 1: Distribution Theory"
    pages: "ch. 8.6, p. 288, eq. (b)"
    url: "https://www.wiley.com/en-us/Kendall%27s+Advanced+Theory+of+Statistics%2C+3+Volumes%2C+Set%2C+6th+Edition-p-9780470669549"
  - authors: "Wikipedia"
    year: 2021
    title: "Probability axioms"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-07-30"
    url: "https://en.wikipedia.org/wiki/Probability_axioms#The_probability_of_the_empty_set"

proof_id: "P244"
shortcut: "prob-emp"
username: "JoramSoch"
---


**Theorem:** The [probability](/D/prob) of the empty set is zero:

$$ \label{eq:prob-emp}
P(\emptyset) = 0 \; .
$$


**Proof:** Assume that the probability of the empty set is not zero, i.e. $P(\emptyset) > 0$. Then, in an [equation derived when proving that probability is monotonic](/P/prob-mon),

$$ \label{eq:pB}
P(B) = P(A) + P(B \setminus A) + \sum_{i=3}^\infty P(E_i) \quad \text{where} \quad E_i = \emptyset \quad \text{for} \quad i \geq 3 \; ,
$$

the right-hand side would be infinite. However, by the [first axiom of probability](/D/prob-ax), the left-hand side must be finite. This is a contradiction. Therefore, $P(\emptyset) = 0$.