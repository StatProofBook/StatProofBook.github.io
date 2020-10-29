---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-10-29 05:35:00

title: "Cumulative distribution function of a strictly increasing function of a random variable"
chapter: "General Theorems"
section: "Probability theory"
topic: "Probability functions"
theorem: "Cumulative distribution function of strictly increasing function"

sources:
  - authors: "Taboga, Marco"
    year: 2017
    title: "Functions of random variables and their distribution"
    in: "Lectures on probability and mathematical statistics"
    pages: "retrieved on 2020-10-29"
    url: "https://www.statlect.com/fundamentals-of-probability/functions-of-random-variables-and-their-distribution#hid2"

proof_id: "P183"
shortcut: "cdf-sifct"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) with possible outcomes $\mathcal{X}$ and let $g(x)$ be a strictly increasing function on the support of $X$. Then, the [cumulative distribution function](/D/cdf) of $Y = g(X)$ is given by

$$ \label{eq:cdf-sifct}
F_Y(y) = \left\{
\begin{array}{rl}
0 \; , & \text{if} \; y < \mathrm{min}(\mathcal{Y}) \\
F_X(g^{-1}(y)) \; , & \text{if} \; y \in \mathcal{Y} \\
1 \; , & \text{if} \; y > \mathrm{max}(\mathcal{Y})
\end{array}
\right.
$$

where $g^{-1}(y)$ is the inverse function of $g(x)$ and $\mathcal{Y}$ is the set of possible outcomes of $Y$:

$$ \label{eq:Y-range}
\mathcal{Y} = \left\lbrace y = g(x): x \in \mathcal{X} \right\rbrace \; .
$$


**Proof:** The support of $Y$ is determined by $g(x)$ and by the set of possible outcomes of $X$. Moreover, if $g(x)$ is strictly increasing, then $g^{-1}(y)$ is also strictly increasing. Therefore, the [cumulative distribution function](/D/cdf) of $Y$ can be derived as follows:

1) If $y$ is lower than the [lowest value](/D/min) $Y$ can take, then $\mathrm{Pr}(Y \leq y) = 0$, so

$$ \label{eq:cdf-sifct-p1}
F_Y(y) = 0, \quad \text{if} \quad y < \mathrm{min}(\mathcal{Y}) \; .
$$

2) If $y$ belongs to the support of $Y$, then $F_Y(y)$ can be derived as follows:

$$ \label{eq:cdf-sifct-p2}
\begin{split}
F_Y(y) &= \mathrm{Pr}(Y \leq y) \\
&= \mathrm{Pr}(g(X) \leq y) \\
&= \mathrm{Pr}(X \leq g^{-1}(y)) \\
&= F_X(g^{-1}(y)) \; .
\end{split}
$$

3) If $y$ is higher than the [highest value](/D/max) $Y$ can take, then $\mathrm{Pr}(Y \leq y) = 1$, so

$$ \label{eq:cdf-sifct-p3}
F_Y(y) = 1, \quad \text{if} \quad y > \mathrm{max}(\mathcal{Y}) \; .
$$

Taking together \eqref{eq:cdf-sifct-p1}, \eqref{eq:cdf-sifct-p2}, \eqref{eq:cdf-sifct-p3}, eventually proves \eqref{eq:cdf-sifct}.