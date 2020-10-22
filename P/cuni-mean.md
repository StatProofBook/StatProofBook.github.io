---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-03-16 16:12:00

title: "Mean of the continuous uniform distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Continuous uniform distribution"
theorem: "Mean"

sources:

proof_id: "P82"
shortcut: "cuni-mean"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [continuous uniform distribution](/D/cuni):

$$ \label{eq:cuni}
X \sim \mathcal{U}(a, b) \; .
$$

Then, the [mean or expected value](/D/mean) of $X$ is

$$ \label{eq:cuni-mean}
\mathrm{E}(X) = \frac{1}{2} (a+b) \; .
$$


**Proof:** The [expected value](/D/mean) is the probability-weighted average over all possible values:

$$ \label{eq:mean}
\mathrm{E}(X) = \int_{\mathcal{X}} x \cdot f_X(x) \, \mathrm{d}x \; .
$$

With the [probability density function of the continuous uniform distribution](/P/cuni-pdf), this becomes:

$$ \label{eq:cuni-mean-qed}
\begin{split}
\mathrm{E}(X) &= \int_a^b x \cdot \frac{1}{b-a} \, \mathrm{d}x \\
&= \left[ \frac{1}{2} \, \frac{x^2}{b-a} \right]_a^b \\
&= \frac{1}{2} \, \frac{b^2 - a^2}{b-a} \\
&= \frac{1}{2} \, \frac{(b+a)(b-a)}{b-a} \\
&= \frac{1}{2} (a+b) \; .
\end{split}
$$