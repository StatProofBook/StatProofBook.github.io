---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2025-04-04 14:38:05

title: "Bernoulli distribution is a special case of categorical distribution"
chapter: "Probability Distributions"
section: "Univariate discrete distributions"
topic: "Bernoulli distribution"
theorem: "Special case of categorical distribution"

sources:

proof_id: "P494"
shortcut: "bern-cat"
username: "JoramSoch"
---


**Theorem:** The [Bernoulli distribution](/D/bern) with success probability $p$ is a special case of the [categorical distribution](/D/cat) with category probabilities $p_1 = p$ and $p_2 = 1-p$:

$$ \label{eq:bern-cat}
X \sim \mathrm{Cat}\left( [p, 1-p] \right)
\quad \Rightarrow \quad
X \sim \mathrm{Bern}(p) \; .
$$


**Proof:** The [probability mass function of the categorical distribution](/P/cat-pmf), where $x$ is a $1 \times k$ vector and $e_1, \ldots, e_k$ are the $1 \times k$ elementary row vectors, is as follows:

$$ \label{eq:cat-pmf}
\mathrm{Cat}\left( x; [p_1, \ldots, p_k] \right) = \left\{
\begin{array}{rl}
p_1 \; , & \text{if} \; x = e_1 \\
\vdots \; \hphantom{,} & \quad \vdots \\
p_k \; , & \text{if} \; x = e_k \; . \\
\end{array}
\right.
$$

If we let $k = 2$, $p_1 = p$ and $p_2 = 1-p$, we obtain

$$ \label{eq:cat-pmf-bern-s1}
\mathrm{Cat}\left( x; [p, 1-p] \right) = \left\{
\begin{array}{rl}
  p \; , & \text{if} \; x = [1, 0] \\
1-p \; , & \text{if} \; x = [0, 1] \; . \\
\end{array}
\right.
$$

Writing this in terms of the first entry $x_1 \in \left\lbrace 0, 1 \right\rbrace$, we get

$$ \label{eq:cat-pmf-bern-s2}
\mathrm{Cat}\left( x; [p, 1-p] \right) = \left\{
\begin{array}{rl}
  p \; , & \text{if} \; x_1 = 1 \\
1-p \; , & \text{if} \; x_1 = 0 \\
\end{array}
\right.
$$

which is equivalent to the [probability mass function of the Bernoulli distribution](/P/bern-pmf).