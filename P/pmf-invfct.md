---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-08-30 05:13:00

title: "Probability mass function of an invertible function of a random vector"
chapter: "General Theorems"
section: "Probability theory"
topic: "Probability functions"
theorem: "Probability mass function of invertible function"

sources:
  - authors: "Taboga, Marco"
    year: 2017
    title: "Functions of random vectors and their distribution"
    in: "Lectures on probability and mathematical statistics"
    pages: "retrieved on 2021-08-30"
    url: "https://www.statlect.com/fundamentals-of-probability/functions-of-random-vectors"

proof_id: "P253"
shortcut: "pmf-invfct"
username: "JoramSoch"
---


**Theorem:** Let $X$ be an $n \times 1$ [random vector](/D/rvec) of [discrete random variables](/D/rvar-disc) with possible outcomes $\mathcal{X}$ and let $g: \; \mathbb{R}^n \rightarrow \mathbb{R}^n$ be an invertible function on the support of $X$. Then, the [probability mass function](/D/pmf) of $Y = g(X)$ is given by

$$ \label{eq:pmf-invfct}
f_Y(y) = \left\{
\begin{array}{rl}
f_X(g^{-1}(y)) \; , & \text{if} \; y \in \mathcal{Y} \\
0 \; , & \text{if} \; y \notin \mathcal{Y}
\end{array}
\right.
$$

where $g^{-1}(y)$ is the inverse function of $g(x)$ and $\mathcal{Y}$ is the set of possible outcomes of $Y$:

$$ \label{eq:Y-range}
\mathcal{Y} = \left\lbrace y = g(x): x \in \mathcal{X} \right\rbrace \; .
$$


**Proof:** Because an invertible function is a one-to-one mapping, the [probability mass function](/D/pmf) of $Y$ can be derived as follows:

$$ \label{eq:pmf-invfct-qed}
\begin{split}
f_Y(y) &= \mathrm{Pr}(Y = y) \\
&= \mathrm{Pr}(g(X) = y) \\
&= \mathrm{Pr}(X = g^{-1}(y)) \\
&= f_X(g^{-1}(y)) \; .
\end{split}
$$