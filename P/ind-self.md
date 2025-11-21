---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2024-09-20 14:04:20

title: "Self-independence of random event"
chapter: "General Theorems"
section: "Probability theory"
topic: "Probability"
theorem: "Self-independence"

sources:
  - authors: "Wikipedia"
    year: 2024
    title: "Independence (probability theory)"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2024-09-20"
    url: "https://en.wikipedia.org/wiki/Independence_(probability_theory)#Self-independence"
  - authors: "Soch, Joram"
    year: 2023
    title: "Suppose A is an event. Can A be independent of itself?"
    in: "X"
    pages: "Aug 7, 2023, 03:59 PM"
    url: "https://x.com/JoramSoch/status/1688550557034651648"

proof_id: "P470"
shortcut: "ind-self"
username: "JoramSoch"
---


**Theorem:** Let $E$ be a [random event](/D/reve). Then, $E$ is [independent of itself](/D/ind), if and only if its [probability](/D/prob) is zero or one:

$$ \label{eq:ind-self}
E \; \text{self-independent} \quad \Leftrightarrow \quad p(E) = 0 \quad \text{or} \quad p(E) = 1 \; .
$$


**Proof:** According to the definition of [statistical independence](/D/ind), it must hold that:

$$ \label{eq:ind}
\begin{split}
p(E,E) &= p(E) \cdot p(E) \\
p(E)   &= \left( p(E) \right)^2 \; .
\end{split}
$$

For $0 \leq p(E) \leq 1$, this is only fulfilled, if

$$ \label{eq:ind-self-qed}
p(E) = 0 \quad \text{or} \quad p(E) = 1 \; .
$$

Both is possible, since the [lower bound of probability is zero](/D/prob-ax) and the [upper bound of probability is one](/P/prob-range).