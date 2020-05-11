---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-05-11 22:58:00

title: "Probability mass function of the categorical distribution"
chapter: "Probability Distributions"
section: "Multivariate discrete distributions"
topic: "Categorical distribution"
theorem: "Probability mass function"

sources:

proof_id: "P98"
shortcut: "cat-pmf"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random vector](/D/rvec) following a [categorical distribution](/D/cat):

$$ \label{eq:cat}
X \sim \mathrm{Cat}(\left[p_1, \ldots, p_k \right]) \; .
$$

Then, the [probability mass function](/D/pmf) of $X$ is

$$ \label{eq:cat-pmf}
f_X(x) = \left\{
\begin{array}{rl}
p_1 \; , & \text{if} \; x = e_1 \\
\vdots \; \hphantom{,} & \quad \vdots \\
p_k \; , & \text{if} \; x = e_k \; . \\
\end{array}
\right.
$$

where $e_1, \ldots, e_k$ are the $1 \times k$ elementary row vectors.


**Proof:** This follows directly from the [definition of the categorical distribution](/D/cat).