---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-07-28 06:17:00

title: "Quantile function of the discrete uniform distribution"
chapter: "Probability Distributions"
section: "Univariate discrete distributions"
topic: "Discrete uniform distribution"
theorem: "Quantile function"

sources:

proof_id: "P142"
shortcut: "duni-qf"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [discrete uniform distribution](/D/duni):

$$ \label{eq:duni}
X \sim \mathcal{U}(a, b) \; .
$$

Then, the [quantile function](/D/qf) of $X$ is

$$ \label{eq:duni-qf}
Q_X(p) = \left\{
\begin{array}{rl}
-\infty \; , & \text{if} \; p = 0 \\
a (1-p) + (b+1) p - 1 \; , & \text{when} \; p \in \left\lbrace \frac{1}{n}, \frac{2}{n}, \ldots, \frac{b-a}{n}, 1 \right\rbrace \; .
\end{array}
\right.
$$

with $n = b - a + 1$.


**Proof:** The [cumulative distribution function of the discrete uniform distribution](/P/duni-cdf) is:

$$ \label{eq:duni-cdf}
F_X(x) = \left\{
\begin{array}{rl}
0 \; , & \text{if} \; x < a \\
\frac{\left\lfloor{x}\right\rfloor - a + 1}{b - a + 1} \; , & \text{if} \; a \leq x \leq b \\
1 \; , & \text{if} \; x > b \; .
\end{array}
\right.
$$

The quantile function $Q_X(p)$ [is defined as](/D/qf) the smallest $x$, such that $F_X(x) = p$:

$$ \label{eq:qf}
Q_X(p) = \min \left\lbrace x \in \mathbb{R} \, \vert \, F_X(x) = p \right\rbrace \; .
$$

Because [the CDF only returns](/P/duni-cdf) multiples of $1/n$ with $n = b - a + 1$, the [quantile function](/D/qf) is only defined for such values. First, we have $Q_X(p) = -\infty$, if $p = 0$. Second, since [the cumulative probability increases step-wise](/P/duni-cdf) by $1/n$ at each integer between and including $a$ and $b$, the minimum $x$ at which

$$ \label{eq:duni-cdf-p}
F_X(x) = \frac{c}{n} \quad \text{where} \quad c \in \left\lbrace 1, \ldots, n \right\rbrace
$$

is given by

$$ \label{eq:duni-qf-p}
Q_X\left( \frac{c}{n} \right) = a + \frac{c}{n} \cdot n - 1 \; .
$$

Substituting $p = c/n$ and $n = b - a + 1$, we can finally show:

$$ \label{eq:duni-qf-qed}
\begin{split}
Q_X(p) &= a + p \cdot (b-a+1) - 1 \\
&= a + pb - pa + p - 1 \\
&= a (1-p) + (b+1) p - 1 \; .
\end{split}
$$