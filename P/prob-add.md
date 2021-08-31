---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-07-30 12:45:00

title: "Addition law of probability"
chapter: "General Theorems"
section: "Probability theory"
topic: "Probability axioms"
theorem: "Addition law of probability"

sources:
  - authors: "A.N. Kolmogorov"
    year: 1950
    title: "Elementary Theory of Probability"
    in: "Foundations of the Theory of Probability"
    pages: "p. 2"
    url: "https://archive.org/details/foundationsofthe00kolm/page/2/mode/2up"
  - authors: "Alan Stuart & J. Keith Ord"
    year: 1994
    title: "Probability and Statistical Inference"
    in: "Kendall's Advanced Theory of Statistics, Vol. 1: Distribution Theory"
    pages: "ch. 8.6, p. 288, eq. (a)"
    url: "https://www.wiley.com/en-us/Kendall%27s+Advanced+Theory+of+Statistics%2C+3+Volumes%2C+Set%2C+6th+Edition-p-9780470669549"
  - authors: "Wikipedia"
    year: 2021
    title: "Probability axioms"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-07-30"
    url: "https://en.wikipedia.org/wiki/Probability_axioms#Further_consequences"

proof_id: "P247"
shortcut: "prob-add"
username: "JoramSoch"
---


**Theorem:** The [probability](/D/prob) of the union of $A$ and $B$ is the sum of the probabilities of $A$ and $B$ minus the probability of the intersection of $A$ and $B$:

$$ \label{eq:prob-add}
P(A \cup B) = P(A) + P(B) - P(A \cap B) \; .
$$


**Proof:** Let $E_1 = A$ and $E_2 = B \setminus A$, such that $E_1 \cup E_2 = A \cup B$. Then, by the [third axiom of probability](/D/prob-ax), we have:

$$ \label{eq:pAoB}
\begin{split}
P(A \cup B) &= P(A) + P(B \setminus A) \\
P(A \cup B) &= P(A) + P(B \setminus [A \cap B]) \; .
\end{split}
$$

Then, let $E_1 = B \setminus [A \cap B]$ and $E_2 = A \cap B$, such that $E_1 \cup E_2 = B$. Again, from the [third axiom of probability](/D/prob-ax), we obtain:

$$ \label{eq:pB}
\begin{split}
P(B) &= P(B \setminus [A \cap B]) + P(A \cap B) \\
P(B \setminus [A \cap B]) &= P(B) - P(A \cap B) \; .
\end{split}
$$

Plugging \eqref{eq:pB} into \eqref{eq:pAoB}, we finally get:

$$ \label{eq:prob-add-qed}
P(A \cup B) = P(A) + P(B) - P(A \cap B) \; .
$$