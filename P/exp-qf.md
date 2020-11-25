---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-02-12 15:48:00

title: "Quantile function of the exponential distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Exponential distribution"
theorem: "Quantile function"

sources:

proof_id: "P50"
shortcut: "exp-qf"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following an [exponential distribution](/D/exp):

$$ \label{eq:exp}
X \sim \mathrm{Exp}(\lambda) \; .
$$

Then, the [quantile function](/D/qf) of $X$ is

$$ \label{eq:exp-qf}
Q_X(p) = \left\{
\begin{array}{rl}
-\infty \; , & \text{if} \; p = 0 \\
-\frac{\ln(1-p)}{\lambda} \; , & \text{if} \; p > 0 \; .
\end{array}
\right.
$$


**Proof:** The [cumulative distribution function of the exponential distribution](/P/exp-cdf) is:

$$ \label{eq:exp-cdf}
F_X(x) = \left\{
\begin{array}{rl}
0 \; , & \text{if} \; x < 0 \\
1 - \exp[-\lambda x] \; , & \text{if} \; x \geq 0 \; .
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

This can be derived by rearranging equation \eqref{eq:exp-cdf}:

$$ \label{eq:exp-qf-s2}
\begin{split}
p &= 1 - \exp[-\lambda x] \\
\exp[-\lambda x] &= 1-p \\
-\lambda x &= \ln(1-p) \\
x &= -\frac{\ln(1-p)}{\lambda} \; .
\end{split}
$$