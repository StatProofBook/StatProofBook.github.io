---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-01-02 18:27:00

title: "Quantile function of the continuous uniform distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Continuous uniform distribution"
theorem: "Quantile function"

sources:

proof_id: "P39"
shortcut: "cuni-qf"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [continuous uniform distribution](/D/cuni):

$$ \label{eq:cuni}
X \sim \mathcal{U}(a, b) \; .
$$

Then, the [quantile function](/D/qf) of $X$ is

$$ \label{eq:cuni-qf}
Q_X(p) = \left\{
\begin{array}{rl}
-\infty \; , & \text{if} \; p = 0 \\
bp + a(1-p) \; , & \text{if} \; p > 0 \; .
\end{array}
\right.
$$


**Proof:** The [cumulative distribution function of the continuous uniform distribution](/P/cuni-cdf) is:

$$ \label{eq:cuni-cdf}
F_X(x) = \left\{
\begin{array}{rl}
0 \; , & \text{if} \; x < a \\
\frac{x-a}{b-a} \; , & \text{if} \; a \leq x \leq b \\
1 \; , & \text{if} \; x > b \; .
\end{array}
\right.
$$

The quantile function $Q_X(p)$ [is defined as](/D/qf) the smallest $x$, such that $F_X(x) = p$:

$$ \label{eq:qf}
Q_X(p) = \min \left\lbrace x \in \mathbb{R} \, \vert \, F_X(x) = p \right\rbrace \; .
$$

Thus, we have $Q_X(p) = -\infty$, if $p = 0$. When $p > 0$, [it holds that](/P/qf-cdf)

$$ \label{eq:exp-qf-s1}
Q_X(p) = F_X^{-1}(x) \; .
$$

This can be derived by rearranging equation \eqref{eq:cuni-cdf}:

$$ \label{eq:cuni-cdf-s2}
\begin{split}
p &= \frac{x-a}{b-a} \\
x &= p(b-a) + a \\
x &= bp + a(1-p) \; .
\end{split}
$$