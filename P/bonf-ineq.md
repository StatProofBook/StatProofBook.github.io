---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
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
p(A \cap B) \geq p(A) + p(B) - 1 \; .
$$


**Proof:** The [addition law of probability](/P/prob-add) states that, for two [events](/D/reve) $A$ and $B$, it holds true that

$$ \label{eq:prob-add}
p(A \cup B) = p(A) + p(B) - p(A \cap B) \; .
$$

Rearranging for $p(A \cap B)$, we have:

$$ \label{eq:bool-ineq-s1}
p(A \cap B) = p(A) + p(B) - p(A \cup B) \; .
$$

The [range of probability](/P/prob-range) is

$$ \label{eq:prob-range}
0 \leq p(E) \leq 1 \; .
$$

Thus, $p(A \cup B)$ is at most one. (This is the case, if $A$ and $B$ are [collectively exhaustive](/P/prob-exh) and their union is thus [equal to the sample space](/D/prob-ax) $\Omega$.) With this, we are able to derive a lower bound for $p(A \cap B)$, as given by the theorem:

$$ \label{eq:bool-ineq-qed}
p(A \cap B) \geq p(A) + p(B) - 1 \; .
$$