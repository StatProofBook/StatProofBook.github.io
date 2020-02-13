---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-01-31 15:41:00

title: "Probability density function of the continuous uniform distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Continuous uniform distribution"
theorem: "Probability density function"

sources:

proof_id: "P37"
shortcut: "cuni-pdf"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [continuous uniform distribution](/D/cuni):

$$ \label{eq:cuni}
X \sim \mathcal{U}(a, b) \; .
$$

Then, the [probability density function](/D/pdf) of $X$ is

$$ \label{eq:cuni-pdf}
f_X(x) = \left\{
\begin{array}{rl}
\frac{1}{b-a} \; , & \text{if} \; a \leq x \leq b \\
0 \; , & \text{otherwise} \; .
\end{array}
\right.
$$


**Proof:** A [continuous uniform variable is defined as](/D/cuni) having a constant probability density between minimum $a$ and maximum $b$. Therefore,

$$ \label{eq:cuni-pdf-s1}
\begin{split}
f_X(x) &\propto 1 \quad \text{for all} \quad x \in [a,b] \quad \text{and} \\
f_X(x) &= 0, \quad\!\! \text{if} \quad x < a \quad \text{or} \quad x > b \; .
\end{split}
$$

To ensure that $f_X(x)$ [is a proper probability density function](/D/pdf), the integral over all non-zero probabilities has to sum to $1$. Therefore,

$$ \label{eq:cuni-pdf-s2}
f_X(x) = \frac{1}{c(a,b)} \quad \text{for all} \quad x \in [a,b]
$$

where the normalization factor $c(a,b)$ is specified, such that

$$ \label{eq:cuni-pdf-s3}
\frac{1}{c(a,b)} \int_{a}^{b} 1 \, \mathrm{d}x = 1 \; .
$$

Solving this for $c(a,b)$, we obtain:

$$ \label{eq:cuni-pdf-s4}
\begin{split}
\int_{a}^{b} 1 \, \mathrm{d}x &= c(a,b) \\
[x]_a^b &= c(a,b) \\
c(a,b) &= b-a \; .
\end{split}
$$