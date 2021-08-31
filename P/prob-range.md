---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-07-30 12:25:00

title: "Range of probability"
chapter: "General Theorems"
section: "Probability theory"
topic: "Probability axioms"
theorem: "Range of probability"

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
    url: "https://en.wikipedia.org/wiki/Probability_axioms#The_numeric_bound"

proof_id: "P246"
shortcut: "prob-range"
username: "JoramSoch"
---


**Theorem:** The [probability](/D/prob) of an event is bounded between 0 and 1:

$$ \label{eq:prob-range}
0 \leq P(E) \leq 1 \; .
$$


**Proof:** From the [first axiom of probability](/D/prob-ax), we have:

$$ \label{eq:pEg0}
P(E) \geq 0 \; .
$$

By combining the [first axiom of probability](/D/prob-ax) and the [probability of the complement](/P/prob-comp), we obtain:

$$ \label{eq:pEl1}
\begin{split}
1- P(E) = P(E^\mathrm{c}) &\geq 0 \\
1- P(E) &\geq 0 \\
P(E) &\leq 1 \; .
\end{split}
$$

Together, \eqref{eq:pEg0} and \eqref{eq:pEl1} imply that

$$ \label{eq:prob-range-qed}
0 \leq P(E) \leq 1 \; .
$$