---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2024-08-08 11:46:08

title: "Monotonicity of probability"
chapter: "General Theorems"
section: "Probability theory"
topic: "Probability axioms"
theorem: "Monotonicity of probability"

sources:
  - authors: "Ostwald, Dirk"
    year: 2023
    title: "Elementare Wahrscheinlichkeiten"
    in: "Wahrscheinlichkeitstheorie und Frequentistische Inferenz"
    pages: "Einheit (2), Folien 8-10"
    url: "https://www.ipsy.ovgu.de/ipsy_media/Methodenlehre+I/Wintersemester+2324/Wahrscheinlichkeitstheorie+und+Frequentistische+Inferenz/2_Elementare_Wahrscheinlichkeiten.pdf"

proof_id: "P465"
shortcut: "prob-mon2"
username: "JoramSoch"
---


**Theorem:** [Probability](/D/prob) is monotonic, i.e. if $A$ is a subset of or equal to $B$, then the probability of $A$ is smaller than or equal to $B$:

$$ \label{eq:prob-mon}
A \subseteq B \quad \Rightarrow \quad P(A) \leq P(B) \; .
$$


**Proof:** When $A \subseteq B$, then $B$ is equal to the union of $A$ and the intersection of $B$ with the complement of $A$:

$$ \label{eq:A-cup}
B = A \cup (B \cap A^\mathrm{c}) \; .
$$

Moreover, the intersection of A and the intersection of $B$ with the complement of $A$ is equal to the empty set:

$$ \label{eq:A-cap}
A \cap (B \cap A^\mathrm{c}) = \emptyset \; .
$$

Thus, the [third axiom of probability](/D/prob-ax) implies:

$$ \label{eq:prob-mon-qed}
\begin{split}
P(B) &= P(A) + P(B \cap A^\mathrm{c}) \\
P(A) &= P(B) - P(B \cap A^\mathrm{c}) \; .
\end{split}
$$

Since $P(B \cap A^\mathrm{c}) \geq 0$ by the [first axiom of probability](/D/prob-ax), it must hold that $P(A) \leq P(B)$.