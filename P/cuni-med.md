---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-03-16 16:19:00

title: "Median of the continuous uniform distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Continuous uniform distribution"
theorem: "Median"

sources:

proof_id: "P83"
shortcut: "cuni-med"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [continuous uniform distribution](/D/cuni):

$$ \label{eq:cuni}
X \sim \mathcal{U}(a, b) \; .
$$

Then, the [median](/D/med) of $X$ is

$$ \label{eq:cuni-med}
\mathrm{median}(X) = \frac{1}{2} (a+b) \; .
$$


**Proof:** The [median](/D/med) is the value at which the [cumulative distribution function](/D/cdf) is $1/2$:

$$ \label{eq:median}
F_X(\mathrm{median}(X)) = \frac{1}{2} \; .
$$

The [cumulative distribution function of the continuous uniform distribution](/P/cuni-cdf) is

$$ \label{eq:cuni-cdf}
F_X(x) = \left\{
\begin{array}{rl}
0 \; , & \text{if} \; x < a \\
\frac{x-a}{b-a} \; , & \text{if} \; a \leq x \leq b \\
1 \; , & \text{if} \; x > b \; .
\end{array}
\right.
$$

Thus, the [inverse CDF](/P/cuni-qf) is

$$ \label{eq:cuni-cdf-inv}
x = bp + a(1-p) \; .
$$

Setting $p = 1/2$, we obtain:

$$ \label{eq:cuni-med-qed}
\mathrm{median}(X) = b \cdot \frac{1}{2} + a \cdot \left( 1-\frac{1}{2} \right) = \frac{1}{2} (a+b) \; .
$$