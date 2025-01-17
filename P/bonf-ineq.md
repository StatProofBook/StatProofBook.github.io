---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2025-01-10 14:56:16

title: "Bonferroni's inequality"
chapter: "General Theorems"
section: "Probability theory"
topic: "Probability axioms"
theorem: "Bonferroni's inequality"

sources:
  - authors: "Probability Fact"
    year: 2021
    title: "Bonferroni's inequality"
    in: "X"
    pages: "retrieved on 2025-01-10"
    url: "https://x.com/ProbFact/status/1462828945968189443"
  - authors: "Wikipedia"
    year: 2025
    title: "Boole's inequality"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2025-01-10"
    url: "https://en.wikipedia.org/wiki/Boole%27s_inequality#Bonferroni_inequalities"

proof_id: "P484"
shortcut: "bonf-ineq"
username: "JoramSoch"
---


**Theorem:** The [probability](/D/prob) of the intersection of $A$ and $B$ is larger than or equal to the sum of the probabilities of $A$ and $B$ minus one:

$$ \label{eq:bool-ineq}
P(A \cap B) \geq P(A) + P(B) - 1 \; .
$$


**Proof:** The [addition law of probability](/P/prob-add) states that, for two [events](/D/reve) $A$ and $B$, it holds true that

$$ \label{eq:prob-add}
P(A \cup B) = P(A) + P(B) - P(A \cap B) \; .
$$

Rearranging for $P(A \cap B)$, we have:

$$ \label{eq:bool-ineq-s1}
P(A \cap B) = P(A) + P(B) - P(A \cup B) \; .
$$

The [range of probability](/P/prob-range) is

$$ \label{eq:prob-range}
0 \leq P(E) \leq 1 \; .
$$

Thus, $P(A \cup B)$ is at most one. (This is the case, if $A$ and $B$ are [collectively exhaustive](/P/prob-exh) and their union is thus [equal to the sample space](/D/prob-ax) $\Omega$.) With this, we are able to derive a lower bound for $P(A \cap B)$, as given by the theorem:

$$ \label{eq:bool-ineq-qed}
P(A \cap B) \geq P(A) + P(B) - 1 \; .
$$