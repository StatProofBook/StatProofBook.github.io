---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2024-08-08 11:41:32

title: "Probability of the empty set"
chapter: "General Theorems"
section: "Probability theory"
topic: "Probability axioms"
theorem: "Probability of the empty set"

sources:
  - authors: "Ostwald, Dirk"
    year: 2023
    title: "Wahrscheinlichkeitsräume"
    in: "Wahrscheinlichkeitstheorie und Frequentistische Inferenz"
    pages: "Einheit (1), Folie 19"
    url: "https://www.ipsy.ovgu.de/ipsy_media/Methodenlehre+I/Wintersemester+2324/Wahrscheinlichkeitstheorie+und+Frequentistische+Inferenz/1_Wahrscheinlichkeitsr%C3%A4ume.pdf"

proof_id: "P464"
shortcut: "prob-emp2"
username: "JoramSoch"
---


**Theorem:** The [probability](/D/prob) of the empty set is zero:

$$ \label{eq:prob-emp}
p(\emptyset) = 0 \; .
$$


**Proof:** Let $E_i = \emptyset$ for $i = 1,2,\ldots$ Then, $E_i \cap E_j = \emptyset \cap \emptyset = \emptyset$ for $i,j \geq 1$ and $\bigcup_{i=1}^\infty E_i = \bigcup_{i=1}^\infty \emptyset = \emptyset$. Thus, $E_1, E_2, \ldots$ is a countable sequence of disjoint events so that, with the [third axiom of probability](/D/prob-ax), it holds that:

$$ \label{eq:prob-emp-qed}
\begin{split}
p\left(\bigcup_{i=1}^\infty E_i \right) &= \sum_{i=1}^\infty p(E_i) \\
p(\emptyset) &= \sum_{i=1}^\infty p(\emptyset) \; .
\end{split}
$$

Since, by the [first axiom of probability](/D/prob-ax), probabilities are non-negative, i.e. $p(\emptyset) \geq 0$, we are searching for a non-negative number which, when added to itself infinitely, is equal to itself. The only such number is zero, i.e. $p(\emptyset) = 0$.