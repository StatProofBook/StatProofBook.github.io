---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-08-30 08:53:00

title: "Cumulative distribution function of a sum of independent random variables"
chapter: "General Theorems"
section: "Probability theory"
topic: "Probability functions"
theorem: "Cumulative distribution function of sum of independents"

sources:
  - authors: "Taboga, Marco"
    year: 2017
    title: "Sums of independent random variables"
    in: "Lectures on probability and mathematical statistics"
    pages: "retrieved on 2021-08-30"
    url: "https://www.statlect.com/fundamentals-of-probability/sums-of-independent-random-variables"

proof_id: "P256"
shortcut: "cdf-sumind"
username: "JoramSoch"
---


**Theorem:** Let $X$ and $Y$ be two [independent](/D/ind) [random variables](/D/rvar) and let $Z = X + Y$. Then, the [cumulative distribution function](/D/cdf) of $Z$ is given by

$$ \label{eq:cdf-sumind}
\begin{split}
F_Z(z) &= \mathrm{E}\left[ F_X(z-Y) \right] \\
\text{or} \quad F_Z(z) &= \mathrm{E}\left[ F_Y(z-X) \right]
\end{split}
$$

where $F_X(x)$, $F_Y(y)$ and $F_Z(z)$ are the [cumulative distribution functions](/D/cdf) of $X$, $Y$ and $Z$ and $\mathrm{E}\left[ \cdot \right]$ denotes the [expected value](/D/mean).


**Proof:** Using the definition of the [cumulative distribution function](/D/cdf), the first equation can be derived as follows:

$$ \label{eq:cdf-sumind-qed}
\begin{split}
F_Z(z) &= \mathrm{Pr}(Z \leq z) \\
&= \mathrm{Pr}(X + Y \leq z) \\
&= \mathrm{Pr}(X \leq z - Y) \\
&= \mathrm{E} \left[ \mathrm{Pr}(X \leq z - Y \vert Y = y) \right] \\
&= \mathrm{E} \left[ \mathrm{Pr}(X \leq z - Y) \right] \\
&= \mathrm{E} \left[ F_X(z-Y) \right] \; .
\end{split}
$$

Note that the second-last transition is justified by the fact that $X$ and $Y$ are [independent](/D/ind), such that [conditional probabilities are equal to marginal probabilities](/P/prob-ind). The second equation can be derived by switching $X$ and $Y$.