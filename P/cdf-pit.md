---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-04-07 08:47:00

title: "Probability integral transform using cumulative distribution function"
chapter: "General Theorems"
section: "Probability theory"
topic: "Probability functions"
theorem: "Probability integral transform"

sources:
  - authors: "Wikipedia"
    year: 2021
    title: "Probability integral transform"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-04-07"
    url: "https://en.wikipedia.org/wiki/Probability_integral_transform#Proof"

proof_id: "P220"
shortcut: "cdf-pit"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [continuous](/D/rvar-disc) [random variable](/D/rvar) with [invertible](/D/qf) [cumulative distribution function](/D/cdf) $F_X(x)$. Then, the [random variable](/D/rvar)

$$ \label{eq:cdf-pit}
Y = F_X(X)
$$

has a [standard uniform distribution](/D/suni).


**Proof:** The [cumulative distribution function](/D/cdf) of $Y = F_X(X)$ can be derived as

$$ \label{eq:cdf-pit-qed}
\begin{split}
F_Y(y) &= \mathrm{Pr}(Y \leq y) \\
&= \mathrm{Pr}(F_X(X) \leq y) \\
&= \mathrm{Pr}(X \leq F_X^{-1}(y)) \\
&= F_X(F_X^{-1}(y)) \\
&= y \\
\end{split}
$$

which is the [cumulative distribution function of a continuous uniform distribution](/P/cuni-cdf) with $a = 0$ and $b = 1$, i.e. the [cumulative distribution function](/D/cdf) of the [standard uniform distribution](/D/suni) $\mathcal{U}(0,1)$.