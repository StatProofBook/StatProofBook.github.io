---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-07-30 11:37:00

title: "Monotonicity of probability"
chapter: "General Theorems"
section: "Probability theory"
topic: "Probability axioms"
theorem: "Monotonicity of probability"

sources:
  - authors: "A.N. Kolmogorov"
    year: 1950
    title: "Elementary Theory of Probability"
    in: "Foundations of the Theory of Probability"
    pages: "p. 6"
    url: "https://archive.org/details/foundationsofthe00kolm/page/6/mode/2up"
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
    pages: "retrieved on 2021-07-30"
    url: "https://en.wikipedia.org/wiki/Probability_axioms#Monotonicity"

proof_id: "P243"
shortcut: "prob-mon"
username: "JoramSoch"
---


**Theorem:** [Probability](/D/prob) is monotonic, i.e. if $A$ is a subset of or equal to  $B$, then the probability of $A$ is smaller than or equal to $B$:

$$ \label{eq:prob-mon}
A \subseteq B \quad \Rightarrow \quad P(A) \leq P(B) \; .
$$


**Proof:** Set $E_1 = A$, $E_2 = B \setminus A$ and $E_i = \emptyset$ for $i \geq 3$. Then, the sets $E_i$ are pairwise disjoint and $E_1 \cup E_2 \cup \ldots = B$, because $A \subseteq B$. Thus, from the [third axiom of probability](/D/prob-ax), we have:

$$ \label{eq:pB}
P(B) = P(A) + P(B \setminus A) + \sum_{i=3}^\infty P(E_i) \; .
$$

Since, by the [first axiom of probability](/D/prob-ax), the right-hand side is a series of non-negative numbers converging to $P(B)$ on the left-hand side, it follows that

$$ \label{eq:prob-mon-qed}
P(A) \leq P(B) \; .
$$