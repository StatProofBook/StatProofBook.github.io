---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-07-23 17:19:00

title: "Probability under mutual exclusivity"
chapter: "General Theorems"
section: "Probability theory"
topic: "Probability"
theorem: "Probability under exclusivity"

sources:
  - authors: "Wikipedia"
    year: 2021
    title: "Mutual exclusivity"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-07-23"
    url: "https://en.wikipedia.org/wiki/Mutual_exclusivity#Probability"

proof_id: "P242"
shortcut: "prob-exc"
username: "JoramSoch"
---


**Theorem:** Let $A$ and $B$ be two statements about [random variables](/D/rvar). Then, if $A$ and $B$ are [mutually exclusive](/D/exc), the [probability](/D/prob) of their disjunction is equal to the sum of the [marginal probabilities](/D/prob-marg):

$$ \label{eq:prob-exc}
p(A \vee B) = p(A) + p(B) \; .
$$


**Proof:** If $A$ and $B$ are [mutually exclusive](/D/exc), then their [joint probability](/D/prob-joint) is zero:

$$ \label{eq:exc}
p(A,B) = 0 \; .
$$

The [addition law of probability](/D/prob-marg) states that

$$ \label{eq:prob-add-set}
p(A \cup B) = p(A) + p(B) - p(A \cap B)
$$

which, in logical rather than set-theoretic expression, becomes

$$ \label{eq:prob-add-log}
p(A \vee B) = p(A) + p(B) - p(A,B) \; .
$$

Because the [union of mutually exclusive events is the empty set](/D/exc) and the [probability of the empty set is zero](/P/prob-emp), the [joint probability](/D/prob-joint) term cancels out:

$$ \label{eq:prob-exc-qed}
p(A \vee B) = p(A) + p(B) - p(A,B) \overset{\eqref{eq:exc}}{=} p(A) + p(B) \; .
$$