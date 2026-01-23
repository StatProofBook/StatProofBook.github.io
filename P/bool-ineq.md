---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2025-01-10 13:10:53

title: "Boole's inequality"
chapter: "General Theorems"
section: "Probability theory"
topic: "Probability axioms"
theorem: "Boole's inequality"

sources:
  - authors: "Wikipedia"
    year: 2025
    title: "Boole's inequality"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2025-01-10"
    url: "https://en.wikipedia.org/wiki/Boole%27s_inequality#Proof_using_induction"

proof_id: "P483"
shortcut: "bool-ineq"
username: "JoramSoch"
---


**Theorem:** The [probability](/D/prob) of any countable sequence of [events](/D/reve) $A_1, A_2, A_3, \ldots$ is smaller than or equal to the sum of the [probabilities of the individual events](/D/prob-ax):

$$ \label{eq:bool-ineq}
p\left( \bigcup_{i=1}^\infty A_i \right) \leq \sum_{i=1}^\infty p(A_i) \; .
$$


**Proof:** The [addition law of probability](/P/prob-add) states that, for two [events](/D/reve) $A$ and $B$, we have:

$$ \label{eq:prob-add}
p(A \cup B) = p(A) + p(B) - p(A \cap B) \; .
$$

We will prove the statement by induction, i.e. observe that it holds for $n=1$ event and show that, if it holds for $n$ events, it also holds for $n+1$ events. For $n=1$, it is obviously true that:

$$ \label{eq:bi-1}
p\left( A_1 \right) \leq p(A_1) \; .
$$

We shall suppose that statement \eqref{eq:bool-ineq} holds for $A_1, \ldots, A_n$:

$$ \label{eq:bi-n}
p\left( \bigcup_{i=1}^n A_i \right) \leq \sum_{i=1}^n p(A_i) \; .
$$

Using \eqref{eq:prob-add}, for $A_1, \ldots, A_n, A_{n+1}$, we then have:

$$ \label{eq:bi-n+1-s1}
  p\left( \bigcup_{i=1}^{n+1} A_i \right)
= p\left( \bigcup_{i=1}^{n} A_i \cup A_{n+1} \right)
= p\left( \bigcup_{i=1}^{n} A_i \right) + p(A_{n+1}) - p\left( \bigcup_{i=1}^{n} A_i \cap A_{n+1} \right) \; .
$$

Since, by the [first axiom of probability](/D/prob-ax), any probability is positive

$$ \label{eq:prob-pos}
\begin{split}
p\left( \bigcup_{i=1}^{n} A_i \cap A_{n+1} \right) \geq 0 \; ,
\end{split}
$$

it follows from \eqref{eq:bi-n+1-s1} that

$$ \label{eq:bi-n+1-s2}
p\left( \bigcup_{i=1}^{n+1} A_i \right) \leq p\left( \bigcup_{i=1}^{n} A_i \right) + p(A_{n+1})
$$

and using \eqref{eq:bi-n}, we get

$$ \label{eq:bi-n+1-s3}
p\left( \bigcup_{i=1}^{n+1} A_i \right) \leq \sum_{i=1}^n p(A_i) + p(A_{n+1}) \; ,
$$

such that

$$ \label{eq:bi-n+1-s4}
p\left( \bigcup_{i=1}^{n+1} A_i \right) \leq \sum_{i=1}^{n+1} p(A_i) \; .
$$

Together, \eqref{eq:bi-1} and the transition from \eqref{eq:bi-n} to \eqref{eq:bi-n+1-s4}, prove the theorem.