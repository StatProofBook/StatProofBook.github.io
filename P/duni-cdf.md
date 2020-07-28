---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-07-28 05:34:00

title: "Cumulative distribution function of the discrete uniform distribution"
chapter: "Probability Distributions"
section: "Univariate discrete distributions"
topic: "Discrete uniform distribution"
theorem: "Cumulative distribution function"

sources:

proof_id: "P141"
shortcut: "duni-cdf"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [discrete uniform distribution](/D/duni):

$$ \label{eq:duni}
X \sim \mathcal{U}(a, b) \; .
$$

Then, the [cumulative distribution function](/D/cdf) of $X$ is

$$ \label{eq:duni-cdf}
F_X(x) = \left\{
\begin{array}{rl}
0 \; , & \text{if} \; x < a \\
\frac{\left\lfloor{x}\right\rfloor - a + 1}{b - a + 1} \; , & \text{if} \; a \leq x \leq b \\
1 \; , & \text{if} \; x > b \; .
\end{array}
\right.
$$


**Proof:** The [probability mass function of the discrete uniform distribution](/P/duni-pmf) is

$$ \label{eq:duni-pmf}
\mathcal{U}(x; a, b) = \frac{1}{b-a+1} \quad \text{where} \quad x \in \left\lbrace a, a+1, \ldots, b-1, b \right\rbrace \; .
$$

Thus, the [cumulative distribution function](/D/cdf) is:

$$ \label{eq:duni-cdf-s1}
F_X(x) = \int_{-\infty}^{x} \mathcal{U}(z; a, b) \, \mathrm{d}z
$$

From \eqref{eq:duni-pmf}, it follows that the cumulative probability increases step-wise by $1/n$ at each integer between and including $a$ and $b$ where

$$ \label{eq:n}
n = b - a + 1
$$

is the number of integers between and including $a$ and $b$. This can be expressed by noting that

$$ \label{eq:duni-cdf-s2b}
F_X(x) \overset{\eqref{eq:duni-pmf}}{=} \frac{\left\lfloor{x}\right\rfloor - a + 1}{n}, \; \text{if} \; a \leq x \leq b \; .
$$

Also, because $\mathrm{Pr}(X < a) = 0$, we have

$$ \label{eq:duni-cdf-s2a}
F_X(x) \overset{\eqref{eq:duni-cdf-s1}}{=} \int_{-\infty}^{x} 0 \, \mathrm{d}z = 0, \; \text{if} \; x < a
$$

and because $\mathrm{Pr}(X > b) = 0$, we have

$$ \label{eq:duni-cdf-s2c}
\begin{split}
F_X(x) &\overset{\eqref{eq:duni-cdf-s1}}{=} \int_{-\infty}^{x} \mathcal{U}(z; a, b) \, \mathrm{d}z \\
&= \int_{-\infty}^{b} \mathcal{U}(z; a, b) \, \mathrm{d}z + \int_{b}^{x} \mathcal{U}(z; a, b) \, \mathrm{d}z \\
&= F_X(b) + \int_{b}^{x} 0 \, \mathrm{d}z \overset{\eqref{eq:duni-cdf-s2b}}{=} 1 + 0 \\
&= 1, \; \text{if} \; x > b \; .
\end{split}
$$

This completes the proof.