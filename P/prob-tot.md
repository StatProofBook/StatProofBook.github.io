---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-08-08 03:56:00

title: "Law of total probability"
chapter: "General Theorems"
section: "Probability theory"
topic: "Probability axioms"
theorem: "Law of total probability"

sources:
  - authors: "Alan Stuart & J. Keith Ord"
    year: 1994
    title: "Probability and Statistical Inference"
    in: "Kendall's Advanced Theory of Statistics, Vol. 1: Distribution Theory"
    pages: "p. 288, eq. (d); p. 289, eq. 8.7"
    url: "https://www.wiley.com/en-us/Kendall%27s+Advanced+Theory+of+Statistics%2C+3+Volumes%2C+Set%2C+6th+Edition-p-9780470669549"
  - authors: "Alan Stuart & J. Keith Ord"
    year: 1994
    title: "Probability and Statistical Inference"
    in: "Kendall's Advanced Theory of Statistics, Vol. 1: Distribution Theory"
    pages: "ch. 8.6, p. 289, eq. 8.7"
    url: "https://www.wiley.com/en-us/Kendall%27s+Advanced+Theory+of+Statistics%2C+3+Volumes%2C+Set%2C+6th+Edition-p-9780470669549"
  - authors: "Wikipedia"
    year: 2021
    title: "Law of total probability"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-08-08"
    url: "https://en.wikipedia.org/wiki/Law_of_total_probability#Statement"

proof_id: "P248"
shortcut: "prob-tot"
username: "JoramSoch"
---


**Theorem:** Let $A$ be a subset of [sample space](/D/samp-spc) $\Omega$ and let $B_1, \ldots, B_n$ be finite or countably infinite partition of $\Omega$, such that $B_i \cap B_j = \emptyset$ for all $i \neq j$ and $\cup_i \, B_i = \Omega$. Then, the [probability](/D/prob) of the event $A$ is

$$ \label{eq:prob-tot}
P(A) = \sum_i P(A \cap B_i) \; .
$$


**Proof:** Because all $B_i$ are disjoint, sets $(A \cap B_i)$ are also disjoint:

$$ \label{eq:B-disjoint}
B_i \cap B_j = \emptyset \quad \Rightarrow \quad (A \cap B_i) \cap (A \cap B_j) = A \cap (B_i \cap B_j) = A \cap \emptyset = \emptyset \; .
$$

Because the $B_i$ are exhaustive, the sets $(A \cap B_i)$ are also exhaustive:

$$ \label{eq:B-exhaustive}
\cup_i \, B_i = \Omega \quad \Rightarrow \quad \cup_i \, (A \cap B_i) = A \cap \left( \cup_i \, B_i \right) = A \cap \Omega = A \; .
$$

Thus, the [third axiom of probability](/D/prob-ax) implies that

$$ \label{eq:prob-tot-qed}
P(A) = \sum_i P(A \cap B_i) \; .
$$