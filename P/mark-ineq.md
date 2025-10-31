---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2025-01-10 11:50:03

title: "Markov's inequality"
chapter: "General Theorems"
section: "Probability theory"
topic: "Expected value"
theorem: "Markov's inequality"

sources:
  - authors: "Probability and Statistics"
    year: 2023
    title: "On Markov's Inequality"
    in: "X"
    pages: "retrieved on 2025-01-10"
    url: "https://x.com/probnstat/status/1713998688530370794"
  - authors: "Wikipedia"
    year: 2025
    title: "Markov's inequality"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2025-01-10"
    url: "https://en.wikipedia.org/wiki/Markov%27s_inequality#Probability-theoretic_proof"

proof_id: "P481"
shortcut: "mark-ineq"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [non-negative](/P/mean-nnrvar) [random variable](/D/rvar) and let $a > 0$ be a positive real number. Then, the [probability](/D/prob) that $X$ is larger than or equal to $a$ is smaller than or equal to the [expected value](/D/mean) of $X$, divided by $a$:

$$ \label{eq:mark-ineq}
\mathrm{Pr}(X \geq a) \leq \frac{\mathrm{E}(X)}{a} \; .
$$


**Proof:** Let us define an indicator variable that is one whenever $X$ is larger than or equal to $a$:

$$ \label{eq:I-X-a}
\mathrm{I}_{X \geq a} = \left\{
\begin{array}{rl}
0 \; , & \text{if} \; X < a \\
1 \; , & \text{if} \; X \geq a \; .
\end{array}
\right.
$$

It is clear that the following inequality holds:

$$ \label{eq:a-I-X}
a \, \mathrm{I}_{X \geq a} \leq X \; .
$$

Taking the [expectation](/D/mean) on both sides, we have:

$$ \label{eq:mark-ineq-qed}
\begin{split}
\mathrm{E}\left( a \, \mathrm{I}_{X \geq a} \right) &\leq \mathrm{E}(X) \\
a \, \mathrm{E}\left( \mathrm{I}_{X \geq a} \right) &\leq \mathrm{E}(X) \\
a \, \left[ 0 \cdot \mathrm{Pr}(\mathrm{I}_{X \geq a}=0) + 1 \cdot \mathrm{Pr}(\mathrm{I}_{X \geq a}=1) \right] &\leq \mathrm{E}(X) \\
a \, \mathrm{Pr}(X \geq a) &\leq \mathrm{E}(X) \\
\mathrm{Pr}(X \geq a) &\leq \frac{\mathrm{E}(X)}{a} \; .
\end{split}
$$