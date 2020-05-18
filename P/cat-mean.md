---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-01-16 11:17:00

title: "Mean of the categorical distribution"
chapter: "Probability Distributions"
section: "Multivariate discrete distributions"
topic: "Categorical distribution"
theorem: "Mean"

sources:

proof_id: "P24"
shortcut: "cat-mean"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random vector](/D/rvec) following a [categorical distribution](/D/cat):

$$ \label{eq:cat}
X \sim \mathrm{Cat}(\left[p_1, \ldots, p_k \right]) \; .
$$

Then, the [mean or expected value](/D/mean) of $X$ is

$$ \label{eq:cat-mean}
\mathrm{E}(X) = \left[p_1, \ldots, p_k \right] \; .
$$


**Proof:** If we conceive the [outcome of a categorical distribution](/D/cat) to be a $1 \times k$ vector, then the elementary row vectors $e_1 = \left[1, 0, \ldots, 0 \right]$, ..., $e_k = \left[0, \ldots, 0, 1 \right]$ are all the possible outcomes and they occur with probabilities $\mathrm{Pr}(X = e_1) = p_1$, ..., $\mathrm{Pr}(X = e_k) = p_k$. Consequently, the [expected value](/D/mean) is

$$ \label{eq:cat-mean-qed}
\begin{split}
\mathrm{E}(X) &= \sum_{x \in \mathcal{X}} x \cdot \mathrm{Pr}(X = x) \\
&= \sum_{i=1}^k e_i \cdot \mathrm{Pr}(X = e_i) \\
&= \sum_{i=1}^k e_i \cdot p_i \\
&= \left[p_1, \ldots, p_k \right] \; .
\end{split}
$$