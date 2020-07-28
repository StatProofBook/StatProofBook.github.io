---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-01-02 18:05:00

title: "Cumulative distribution function of the continuous uniform distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Continuous uniform distribution"
theorem: "Cumulative distribution function"

sources:

proof_id: "P38"
shortcut: "cuni-cdf"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [continuous uniform distribution](/D/cuni):

$$ \label{eq:cuni}
X \sim \mathcal{U}(a, b) \; .
$$

Then, the [cumulative distribution function](/D/cdf) of $X$ is

$$ \label{eq:cuni-cdf}
F_X(x) = \left\{
\begin{array}{rl}
0 \; , & \text{if} \; x < a \\
\frac{x-a}{b-a} \; , & \text{if} \; a \leq x \leq b \\
1 \; , & \text{if} \; x > b \; .
\end{array}
\right.
$$


**Proof:** The [probability density function of the continuous uniform distribution](/P/cuni-pdf) is:

$$ \label{eq:cuni-pdf}
\mathcal{U}(x; a, b) = \left\{
\begin{array}{rl}
\frac{1}{b-a} \; , & \text{if} \; a \leq x \leq b \\
0 \; , & \text{otherwise} \; .
\end{array}
\right.
$$

Thus, the [cumulative distribution function](/D/cdf) is:

$$ \label{eq:cuni-cdf-s1}
F_X(x) = \int_{-\infty}^{x} \mathcal{U}(z; a, b) \, \mathrm{d}z
$$

First of all, if $x < a$, we have

$$ \label{eq:cuni-cdf-s2a}
F_X(x) = \int_{-\infty}^{x} 0 \, \mathrm{d}z = 0 \; .
$$

Moreover, if $a \leq x \leq b$, we have using \eqref{eq:cuni-pdf}

$$ \label{eq:cuni-cdf-s2b}
\begin{split}
F_X(x) &= \int_{-\infty}^{a} \mathcal{U}(z; a, b) \, \mathrm{d}z + \int_{a}^{x} \mathcal{U}(z; a, b) \, \mathrm{d}z \\
&= \int_{-\infty}^{a} 0 \, \mathrm{d}z + \int_{a}^{x} \frac{1}{b-a} \, \mathrm{d}z \\
&= 0 + \frac{1}{b-a} [z]_a^x \\
&= \frac{x-a}{b-a} \; .
\end{split}
$$

Finally, if $x > b$, we have

$$ \label{eq:cuni-cdf-s2c}
\begin{split}
F_X(x) &= \int_{-\infty}^{b} \mathcal{U}(z; a, b) \, \mathrm{d}z + \int_{b}^{x} \mathcal{U}(z; a, b) \, \mathrm{d}z \\
&= F_X(b) + \int_{b}^{x} 0 \, \mathrm{d}z \\
&= \frac{b-a}{b-a} + 0 \\
&= 1 \; .
\end{split}
$$

This completes the proof.