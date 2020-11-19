---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-11-12 06:03:00

title: "Cumulative distribution function in terms of probability mass function of a discrete random variable"
chapter: "General Theorems"
section: "Probability theory"
topic: "Probability functions"
theorem: "Cumulative distribution function of discrete random variable"

sources:

proof_id: "P189"
shortcut: "cdf-pmf"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [discrete](/D/rvar-disc) [random variable](/D/rvar) with possible values $\mathcal{X}$ and [probability mass function](/D/pmf) $f_X(x)$. Then, the [cumulative distribution function](/D/cdf) of $X$ is

$$ \label{eq:cdf-pmf}
F_X(x) = \sum_{\overset{t \in \mathcal{X}}{t \leq x}} f_X(t) \; .
$$


**Proof:** The [cumulative distribution function](/D/cdf) of a [random variable](/D/rvar) $X$ is defined as the probability that $X$ is smaller than $x$:

$$ \label{eq:cdf}
F_X(x) = \mathrm{Pr}(X \leq x) \; .
$$

The [probability mass function](/D/pmf) of a [discrete](/D/rvar-disc) [random variable](/D/rvar) $X$ returns the probability that $X$ takes a particular value $x$:

$$ \label{eq:pmf}
f_X(x) = \mathrm{Pr}(X = x) \; .
$$

Taking these two definitions together, we have:

$$ \label{eq:cdf-pmf-qed}
\begin{split}
F_X(x) &\overset{\eqref{eq:cdf}}{=} \sum_{\overset{t \in \mathcal{X}}{t \leq x}} \mathrm{Pr}(X = t) \\
&\overset{\eqref{eq:pmf}}{=} \sum_{\overset{t \in \mathcal{X}}{t \leq x}} f_X(t) \; .
\end{split}
$$