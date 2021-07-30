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


**Theorem:** Let $A$ and $B$ be two statements about [random variables](/D/rvar). Then, if $A$ and $B$ are [mutually exclusive](/D/exc), their [joint probability](/D/prob-joint) is zero:

$$ \label{eq:prob-exc}
p(A,B) = 0 \; .
$$


**Proof:** If $A$ and $B$ are [mutually exclusive](/D/exc), then the [probability](/D/prob) of their disjunction is the sum of the [marginal probabilities](/D/prob-marg):

$$ \label{eq:exc}
p(A \vee B) = p(A) + p(B) \; .
$$

The [law of marginal probability](/D/prob-marg) implies that

$$ \label{eq:prob-marg}
\begin{split}
p(A) &= p(A,B) + p(A,\overline{B}) \\
p(B) &= p(A,B) + p(\overline{A},B)
\end{split}
$$

where $\overline{A}$ and $\overline{B}$ are the complements of $A$ and $B$. The probability of the disjunction $p(A \vee B)$ can also be expressed as the probability of a disjunction of three mutually exclusive statements

$$ \label{eq:prob-exc-s1}
p(A \vee B) = p\left([A \wedge \overline{B}] \vee [\overline{A} \wedge B] \vee [A \wedge B] \right) \; ,
$$

such that the definition of exclusivity can be applied to give

$$ \label{eq:prob-exc-s2}
\begin{split}
p(A \vee B) &\overset{\eqref{eq:prob-exc-s1}}{=} p\left([A \wedge \overline{B}] \vee [\overline{A} \wedge B] \vee [A \wedge B] \right) \\
&\overset{\eqref{eq:exc}}{=} p(A,\overline{B}) + p(\overline{A},B) + p(A,B) \\
&= [p(A,\overline{B}) + p(A,B)] + [p(\overline{A},B) + p(A,B)] - p(A,B) \\
&\overset{\eqref{eq:prob-marg}}{=} p(A) + p(B) - p(A,B) \; .
\end{split}
$$

Since $A$ and $B$ are [mutually exclusive](/D/exc), we obtain:

$$ \label{eq:prob-exc-qed}
\begin{split}
p(A \vee B) &\overset{\eqref{eq:prob-exc-s2}}{=} p(A) + p(B) - p(A,B) \\
p(A \vee B) &\overset{\eqref{eq:exc}}{=} p(A \vee B) - p(A,B) \\
p(A,B) &= 0 \; .
\end{split}
$$