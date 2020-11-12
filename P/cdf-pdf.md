---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-11-12 06:33:00

title: "Cumulative distribution function in terms of probability density function of a continuous random variable"
chapter: "General Theorems"
section: "Probability theory"
topic: "Probability functions"
theorem: "Cumulative distribution function of continuous random variable"

sources:

proof_id: "P190"
shortcut: "cdf-pdf"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [continuous](/D/rvar-disc) [random variable](/D/rvar) with possible values $\mathcal{X}$ and [probability density function](/D/pdf) $f_X(x)$. Then, the [cumulative distribution function](/D/cdf) of $X$ is

$$ \label{eq:cdf-pdf}
F_X(x) = \int_{-\infty}^{x} f_X(t) \, \mathrm{d}t \; .
$$


**Proof:** The [cumulative distribution function](/D/cdf) of a [random variable](/D/rvar) $X$ is defined as the probability that $X$ is smaller than $x$:

$$ \label{eq:cdf}
F_X(x) = \mathrm{Pr}(X \leq x) \; .
$$

The [probability density function](/D/pdf) of a [continuous](/D/rvar-disc) [random variable](/D/rvar) $X$ can be used to calculate the probability that $X$ falls into a particular interval $A$:

$$ \label{eq:pdf}
\mathrm{Pr}(X \in A) = \int_{A} f_X(x) \, \mathrm{d}x \; .
$$

Taking these two definitions together, we have:

$$ \label{eq:cdf-pdf-qed}
\begin{split}
F_X(x) &\overset{\eqref{eq:cdf}}{=} \mathrm{Pr}(X \in (-\infty, x]) \\
&\overset{\eqref{eq:pdf}}{=} \int_{-\infty}^{x} f_X(t) \, \mathrm{d}t \; .
\end{split}
$$