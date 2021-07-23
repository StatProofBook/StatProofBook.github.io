---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-07-23 16:05:00

title: "Probability under statistical independence"
chapter: "General Theorems"
section: "Probability theory"
topic: "Probability"
theorem: "Probability under independence"

sources:
  - authors: "Wikipedia"
    year: 2021
    title: "Independence (probability theory)"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-07-23"
    url: "https://en.wikipedia.org/wiki/Independence_(probability_theory)#Definition"

proof_id: "P241"
shortcut: "prob-ind"
username: "JoramSoch"
---


**Theorem:** Let $A$ and $B$ be two statements about [random variables](/D/rvar). Then, if $A$ and $B$ are [independent](/D/ind), [marginal](/D/prob-marg) and [conditional](/D/prob-cond) probabilities are equal:

$$ \label{eq:prob-ind}
\begin{split}
p(A) &= p(A|B) \\
p(B) &= p(B|A) \; .
\end{split}
$$


**Proof:** If $A$ and $B$ are [independent](/D/ind), then the [joint probability](/D/prob-joint) is equal to the product of the [marginal probabilities](/D/prob-marg):

$$ \label{eq:ind}
p(A,B) = p(A) \cdot p(B) \; .
$$

The [law of conditional probability](/D/prob-cond) states that

$$ \label{eq:prob-cond}
p(A|B) = \frac{p(A,B)}{p(B)} \; .
$$

Combining \eqref{eq:ind} and \eqref{eq:prob-cond}, we have:

$$ \label{eq:prob-ind-qed-A}
p(A|B) = \frac{p(A) \cdot p(B)}{p(B)} = p(A) \; .
$$

Equivalently, we can write:

$$ \label{eq:prob-ind-qed-B}
p(B|A) \overset{\eqref{eq:prob-cond}}{=} \frac{p(A,B)}{p(A)} \overset{\eqref{eq:ind}}{=} \frac{p(A) \cdot p(B)}{p(A)} = p(B) \; .
$$