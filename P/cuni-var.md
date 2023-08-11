---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-12-20 18:04:00

title: "Variance of the continuous uniform distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Continuous uniform distribution"
theorem: "Variance"

sources:

proof_id: "P396"
shortcut: "cuni-var"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [continuous uniform distribution](/D/cuni):

$$ \label{eq:cuni}
X \sim \mathcal{U}(a, b) \; .
$$

Then, the [variance](/D/var) of $X$ is

$$ \label{eq:cuni-var}
\mathrm{Var}(X) = \frac{1}{12} (b-a)^2 \; .
$$


**Proof:** The [variance](/D/var) is the probability-weighted average of the squared deviation from the [mean](/D/mean):

$$ \label{eq:var}
\mathrm{Var}(X) = \int_{\mathbb{R}} (x - \mathrm{E}(X))^2 \cdot f_\mathrm{X}(x) \, \mathrm{d}x \; .
$$

With the [expected value](/P/cuni-mean) and [probability density function](/P/cuni-pdf) of the continuous uniform distribution, this reads:

$$ \label{eq:cuni-var-qed}
\begin{split}
\mathrm{Var}(X) &= \int_a^b \left( x - \frac{1}{2} (a+b) \right)^2 \cdot \frac{1}{b-a} \, \mathrm{d}x \\
&= \frac{1}{b-a} \cdot \int_a^b \left( x - \frac{a+b}{2} \right)^2 \, \mathrm{d}x \\
&= \frac{1}{b-a} \cdot \left[ \frac{1}{3} \left( x - \frac{a+b}{2} \right)^3 \right]_a^b \\
&= \frac{1}{3(b-a)} \cdot \left[ \left( \frac{2x-(a+b)}{2} \right)^3 \right]_a^b \\
&= \frac{1}{3(b-a)} \cdot \left[ \frac{1}{8} ( 2x-a-b )^3 \right]_a^b \\
&= \frac{1}{24(b-a)} \cdot \left[ ( 2x-a-b )^3 \right]_a^b \\
&= \frac{1}{24(b-a)} \cdot \left[ ( 2b-a-b )^3 - ( 2a-a-b )^3 \right] \\
&= \frac{1}{24(b-a)} \cdot \left[ ( b-a )^3 - ( a-b )^3 \right] \\
&= \frac{1}{24(b-a)} \cdot \left[ ( b-a )^3 + (-1)^3 ( a-b )^3 \right] \\
&= \frac{1}{24(b-a)} \cdot \left[ ( b-a )^3 + ( b-a )^3 \right] \\
&= \frac{2}{24(b-a)} (b-a)^3 \\
&= \frac{1}{12} (b-a)^2 \; .
\end{split}
$$