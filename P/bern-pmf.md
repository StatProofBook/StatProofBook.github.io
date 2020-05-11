---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-05-11 22:10:00

title: "Probability mass function of the Bernoulli distribution"
chapter: "Probability Distributions"
section: "Univariate discrete distributions"
topic: "Bernoulli distribution"
theorem: "Probability mass function"

sources:

proof_id: "P96"
shortcut: "bern-pmf"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [Bernoulli distribution](/D/bern):

$$ \label{eq:Bern}
X \sim \mathrm{Bern}(p) \; .
$$

Then, the [probability mass function](/D/pmf) of $X$ is

$$ \label{eq:Bern-pmf}
f_X(x) = \left\{
\begin{array}{rl}
p \; , & \text{if} \; x = 1 \\
1-p \; , & \text{if} \; x = 0 \; . \\
\end{array}
\right. \; .
$$


**Proof:** This follows directly from the [definition of the Bernoulli distribution](/D/bern).