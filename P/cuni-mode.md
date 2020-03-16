---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-03-16 16:29:00

title: "Mode of the continuous uniform distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Continuous uniform distribution"
theorem: "Mode"

sources:

proof_id: "P84"
shortcut: "cuni-med"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [continuous uniform distribution](/D/cuni):

$$ \label{eq:cuni}
X \sim \mathcal{U}(a, b) \; .
$$

Then, the [mode](/D/mode) of $X$ is

$$ \label{eq:cuni-mode}
\mathrm{mode}(X) \in [a,b] \; .
$$


**Proof:**  The [mode](/D/mode) is the value which maximizes the [probability density function](/D/pdf):

$$ \label{eq:mode}
\mathrm{mode}(X) = \operatorname*{arg\,max}_x f_X(x) \; .
$$

The [probability density function of the continuous uniform distribution](/P/cuni-pdf) is:

$$ \label{eq:cuni-pdf}
f_X(x) = \left\{
\begin{array}{rl}
\frac{1}{b-a} \; , & \text{if} \; a \leq x \leq b \\
0 \; , & \text{otherwise} \; .
\end{array}
\right.
$$

Since the PDF attains its only non-zero value whenever $a \leq x \leq b$,

$$ \label{eq:cuni-pdf-max}
\operatorname*{max}_x f_X(x) = \frac{1}{b-a} \; ,
$$

any value in the interval $[a,b]$ may be considered the mode of $X$.