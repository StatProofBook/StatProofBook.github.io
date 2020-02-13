---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-02-11 14:48:00

title: "Cumulative distribution function of the exponential distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Exponential distribution"
theorem: "Cumulative distribution function"

sources:

proof_id: "P48"
shortcut: "exp-cdf"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following an [exponential distribution](/D/exp):

$$ \label{eq:exp}
X \sim \mathrm{Exp}(\lambda) \; .
$$

Then, the [cumulative distribution function](/D/cdf) of $X$ is

$$ \label{eq:exp-cdf}
F_X(x) = \left\{
\begin{array}{rl}
0 \; , & \text{if} \; x < 0 \\
1 - \exp[-\lambda x] \; , & \text{if} \; x \geq 0 \; .
\end{array}
\right.
$$


**Proof:**  The [probability density function of the exponential distribution](/P/exp-pdf) is:

$$ \label{eq:exp-pdf}
\mathrm{Exp}(x; \lambda) = \left\{
\begin{array}{rl}
0 \; , & \text{if} \; x < 0 \\
\lambda \exp[-\lambda x] \; , & \text{if} \; x \geq 0 \; .
\end{array}
\right.
$$

Thus, the [cumulative distribution function](/D/cdf) is:

$$ \label{eq:exp-cdf-s1}
F_X(x) = \int_{-\infty}^{x} \mathrm{Exp}(z; \lambda) \, \mathrm{d}z \; .
$$

If $x < 0$, we have:

$$ \label{eq:exp-cdf-s2a}
F_X(x) = \int_{-\infty}^{x} 0 \, \mathrm{d}z = 0 \; .
$$

If $x \geq 0$, we have using \eqref{eq:exp-pdf}:

$$ \label{eq:exp-cdf-s2b}
\begin{split}
F_X(x) &= \int_{-\infty}^{0} \mathrm{Exp}(z; \lambda) \, \mathrm{d}z + \int_{0}^{x} \mathrm{Exp}(z; \lambda) \, \mathrm{d}z \\
&= \int_{-\infty}^{0} 0 \, \mathrm{d}z + \int_{0}^{x} \lambda \exp[-\lambda z] \, \mathrm{d}z \\
&= 0 + \lambda \left[ -\frac{1}{\lambda} \exp[-\lambda z] \right]_{0}^{x} \\
&= \lambda \left[ \left( -\frac{1}{\lambda} \exp[-\lambda x] \right) - \left( -\frac{1}{\lambda} \exp[-\lambda \cdot 0] \right) \right] \\
&= 1 - \exp[-\lambda x] \; .
\end{split}
$$