---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
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
A \subseteq B \quad \Rightarrow \quad p(A) \leq p(B) \; .
$$


**Proof:** When $A \subseteq B$, then $B$ is equal to the union of $A$ and the intersection of $B$ with the [complement](/P/prob-comp) of $A$:

$$ \label{eq:A-cup}
B = A \cup (B \cap \overline{A}) \; .
$$

Moreover, the intersection of A and the intersection of $B$ with the complement of $A$ is equal to the empty set:

$$ \label{eq:A-cap}
A \cap (B \cap \overline{A}) = \emptyset \; .
$$

Thus, the [third axiom of probability](/D/prob-ax) implies:

$$ \label{eq:prob-mon-qed}
\begin{split}
p(B) &= p(A) + p(B \cap \overline{A}) \\
p(A) &= p(B) - p(B \cap \overline{A}) \; .
\end{split}
$$

Since $p(B \cap \overline{A}) \geq 0$ by the [first axiom of probability](/D/prob-ax), it must hold that $p(A) \leq p(B)$.