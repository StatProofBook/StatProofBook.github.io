---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-07-30 12:14:00

title: "Probability of the complement"
chapter: "General Theorems"
section: "Probability theory"
topic: "Probability axioms"
theorem: "Probability of the complement"

sources:
  - authors: "A.N. Kolmogorov"
    year: 1950
    title: "Elementary Theory of Probability"
    in: "Foundations of the Theory of Probability"
    pages: "p. 6, eq. 2"
    url: "https://archive.org/details/foundationsofthe00kolm/page/6/mode/2up"
  - authors: "Alan Stuart & J. Keith Ord"
    year: 1994
    title: "Probability and Statistical Inference"
    in: "Kendall's Advanced Theory of Statistics, Vol. 1: Distribution Theory"
    pages: "ch. 8.6, p. 288, eq. (c)"
    url: "https://www.wiley.com/en-us/Kendall%27s+Advanced+Theory+of+Statistics%2C+3+Volumes%2C+Set%2C+6th+Edition-p-9780470669549"
  - authors: "Wikipedia"
    year: 2021
    title: "Probability axioms"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-07-30"
    url: "https://en.wikipedia.org/wiki/Probability_axioms#The_complement_rule"

proof_id: "P245"
shortcut: "prob-comp"
username: "JoramSoch"
---


**Theorem:** The [probability](/D/prob) of a complement of a set is one minus the probability of this set:

$$ \label{eq:prob-comp}
P(A^\mathrm{c}) = 1 - P(A)
$$

where $A^\mathrm{c} = \Omega \setminus A$ and $\Omega$ is the [sample space](/D/samp-spc).


**Proof:** Since $A$ and $A^\mathrm{c}$ are [mutually exclusive](/D/exc) and $A \cup A^\mathrm{c} = \Omega$, the [third axiom of probability](/D/prob-ax) implies:

$$ \label{eq:pAAc}
\begin{split}
P(A \cup A^\mathrm{c}) &= P(A) + P(A^\mathrm{c}) \\
P(\Omega) &= P(A) + P(A^\mathrm{c}) \\
P(A^\mathrm{c}) &= P(\Omega) - P(A) \; .
\end{split}
$$

The [second axiom of probability](/D/prob-ax) states that $P(\Omega) =1$, such that we obtain:

$$ \label{eq:prob-comp-qed}
P(A^\mathrm{c}) = 1 - P(A) \; .
$$