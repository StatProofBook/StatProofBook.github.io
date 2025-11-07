---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-03-27 23:14:00

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
    year: 2022
    title: "Probability axioms"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2022-03-27"
    url: "https://en.wikipedia.org/wiki/Probability_axioms#Consequences"

proof_id: "P319"
shortcut: "prob-exh2"
username: "JoramSoch"
---


**Theorem:** Let $B_1, \ldots, B_n$ be [mutually exclusive](/D/exc) and collectively exhaustive subsets of a [sample space](/D/samp-spc) $\Omega$. Then, their [total probability](/P/prob-tot) is one:

$$ \label{eq:prob-exh}
\sum_i p(B_i) = 1 \; .
$$


**Proof:** The [addition law of probability](/P/prob-add) states that for two [events](/D/reve) $A$ and $B$, the [probability](/D/prob) of at least one of them occurring is:

$$ \label{eq:prob-add}
p(A \cup B) = p(A) + p(B) - p(A \cap B) \; .
$$

Recursively applying this law to the events $B_1, \ldots, B_n$, we have:

$$ \label{eq:prob-all-s1}
\begin{split}
p(B_1 \cup \ldots \cup B_n) &= p(B_1) + p(B_2 \cup \ldots \cup B_n) - p(B_1 \cap [B_2 \cup \ldots \cup B_n]) \\
&= p(B_1) + p(B_2) + p(B_3 \cup \ldots \cup B_n) - p(B_2 \cap [B_3 \cup \ldots \cup B_n])- p(B_1 \cap [B_2 \cup \ldots \cup B_n]) \\
&\;\; \vdots \\
&= p(B_1) + \ldots + p(B_n) - p(B_1 \cap [B_2 \cup \ldots \cup B_n]) - \ldots - p(B_{n-1} \cap B_n) \\
p(\cup_i^n \, B_i) &= \sum_i^n p(B_i) - \sum_i^{n-1} p(B_i \cap [\cup_{j=i+1}^n B_j]) \\
&= \sum_i^n p(B_i) - \sum_i^{n-1} p(\cup_{j=i+1}^n [B_i \cap B_j]) \; .
\end{split}
$$

Because all $B_i$ are mutually exclusive, we have:

$$ \label{eq:B-exclusive}
B_i \cap B_j = \emptyset \quad \text{for all} \quad i \neq j \; .
$$

Since [the probability of the empty set is zero](/P/prob-emp), this means that the second sum on the right-hand side of \eqref{eq:prob-all-s1} disappears:

$$ \label{eq:prob-all-s2}
p(\cup_i^n \, B_i) = \sum_i^n p(B_i) \; .
$$

Because the $B_i$ are collectively exhaustive, we have:

$$ \label{eq:B-exhaustive}
\cup_i \, B_i = \Omega \; .
$$

Since [the probability of the sample space is one](/D/prob-ax), this means that the left-hand side of \eqref{eq:prob-all-s2} becomes equal to one:

$$ \label{eq:prob-all-s3}
1 = \sum_i^n p(B_i) \; .
$$

This proofs the statement in \eqref{eq:prob-exh}.