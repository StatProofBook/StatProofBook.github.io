---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-01-06 20:55:00

title: "Bayes' rule"
chapter: "General Theorems"
section: "Probability theory"
topic: "Bayesian inference"
theorem: "Bayes' theorem"

dependencies:
  - theorem: "Bayes' theorem"
    shortcut: "bayes-th"

sources:
  - authors: "Wikipedia"
    year: "2019"
    title: "Bayes' theorem"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-01-06"
    url: "https://en.wikipedia.org/wiki/Bayes%27_theorem#Bayes%E2%80%99_rule"

proof_id: "P12"
shortcut: "bayes-rule"
username: "JoramSoch"
---


**Theorem:** Let $A_1$, $A_2$ and $B$ be arbitrary statements about random variables where $A_1$ and $A_2$ are mutually exclusive. Then, Bayes' rule states that the posterior odds are equal to the Bayes factor times the prior odds, i.e.

$$ \label{eq:bayes-rule}
\frac{p(A_1|B)}{p(A_2|B)} = \frac{p(B|A_1)}{p(B|A_2)} \cdot \frac{p(A_1)}{p(A_2)} \; .
$$


**Proof:** Using Bayes' theorem, the conditional probabilities on the left are given by

$$ \label{eq:bayes-th-A1}
p(A_1|B) = \frac{p(B|A_1) \cdot p(A_1)}{p(B)}
$$

$$ \label{eq:bayes-th-A2}
p(A_2|B) = \frac{p(B|A_2) \cdot p(A_2)}{p(B)} \; .
$$

Dividing the two condition probabilities by each other

$$ \label{eq:bayes-rule-pr}
\begin{split}
\frac{p(A_1|B)}{p(A_2|B)} &= \frac{p(B|A_1) \cdot p(A_1) / p(B)}{p(B|A_2) \cdot p(A_2) / p(B)} \\
&= \frac{p(B|A_1)}{p(B|A_2)} \cdot \frac{p(A_1)}{p(A_2)} \; ,
\end{split}
$$

one obtains the posterior odds ratio as given by the theorem.
