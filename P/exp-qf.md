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
Q_X(p) = -\frac{\ln(1-p)}{\lambda} \; .
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

Thus, the [quantile function](/D/qf) is:

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