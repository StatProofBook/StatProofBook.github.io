---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-10-29 05:55:00

title: "Probability mass function of a strictly increasing function of a discrete random variable"
chapter: "General Theorems"
section: "Probability theory"
topic: "Probability functions"
theorem: "Probability mass function of strictly increasing function"

sources:
  - authors: "Taboga, Marco"
    year: 2017
    title: "Functions of random variables and their distribution"
    in: "Lectures on probability and mathematical statistics"
    pages: "retrieved on 2020-10-29"
    url: "https://www.statlect.com/fundamentals-of-probability/functions-of-random-variables-and-their-distribution#hid3"

proof_id: "P184"
shortcut: "pmf-sifct"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [discrete](/D/rvar-disc) [random variable](/D/rvar) with possible outcomes $\mathcal{X}$ and let $g(x)$ be a strictly increasing function on the support of $X$. Then, the [probability mass function](/D/pmf) of $Y = g(X)$ is given by

$$ \label{eq:pmf-sifct}
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


**Proof:** Because a strictly increasing function is invertible, the [probability mass function](/D/pmf) of $Y$ can be derived as follows:

$$ \label{eq:pmf-sifct-qed}
\begin{split}
f_Y(y) &= \mathrm{Pr}(Y = y) \\
&= \mathrm{Pr}(g(X) = y) \\
&= \mathrm{Pr}(X = g^{-1}(y)) \\
&= f_X(g^{-1}(y)) \; .
\end{split}
$$