---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-01-06 20:55:00

title: "Bayes' rule"
chapter: "General Theorems"
section: "Bayesian statistics"
topic: "Bayesian inference"
theorem: "Bayes' rule"

sources:
  - authors: "Wikipedia"
    year: 2019
    title: "Bayes' theorem"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-01-06"
    url: "https://en.wikipedia.org/wiki/Bayes%27_theorem#Bayes%E2%80%99_rule"

proof_id: "P12"
shortcut: "bayes-rule"
username: "JoramSoch"
---


**Theorem:** Let $A_1$, $A_2$ and $B$ be arbitrary statements about [random variables](/D/rvar) where $A_1$ and $A_2$ are mutually exclusive. Then, Bayes' rule states that the [posterior odds](/D/post-odd) are equal to the [Bayes factor](/D/bf) times the [prior odds](/D/prior-odd), i.e.

$$ \label{eq:bayes-rule}
\frac{p(A_1|B)}{p(A_2|B)} = \frac{p(B|A_1)}{p(B|A_2)} \cdot \frac{p(A_1)}{p(A_2)} \; .
$$


**Proof:** Using [Bayes' theorem](/P/bayes-th), the [conditional probabilities](/D/prob-cond) on the left are given by

$$ \label{eq:bayes-th-A1}
p(A_1|B) = \frac{p(B|A_1) \cdot p(A_1)}{p(B)}
$$

$$ \label{eq:bayes-th-A2}
p(A_2|B) = \frac{p(B|A_2) \cdot p(A_2)}{p(B)} \; .
$$

Dividing the two conditional probabilities by each other

$$ \label{eq:bayes-rule-qed}
\begin{split}
\frac{p(A_1|B)}{p(A_2|B)} &= \frac{p(B|A_1) \cdot p(A_1) / p(B)}{p(B|A_2) \cdot p(A_2) / p(B)} \\
&= \frac{p(B|A_1)}{p(B|A_2)} \cdot \frac{p(A_1)}{p(A_2)} \; ,
\end{split}
$$

one obtains the posterior odds ratio as given by the theorem.