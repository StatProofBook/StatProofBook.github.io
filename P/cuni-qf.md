---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-01-02 18:27:00

title: "Quantile function of the continuous uniform distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Continuous uniform distribution"
theorem: "Quantile function"

sources:

proof_id: "P39"
shortcut: "cuni-qf"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a random variable following a continuous uniform distribution:

$$ \label{eq:cuni}
X \sim \mathcal{U}(a, b) \; .
$$

Then, the quantile function of $X$ is

$$ \label{eq:cuni-qf}
Q_X(p) = bp + a(1-p) \; .
$$


**Proof:** The [cumulative distribution function of the continuous uniform distribution](/P/cuni-cdf.html) is:

$$ \label{eq:cuni-cdf}
F_X(x) =
\begin{cases}
\;\; 0 & , \text{if} \; x < a \\
\frac{x-a}{b-a} & , \text{if} \; a \leq x \leq b \\
\;\; 1 & , \text{if} \; x > b \; .
\end{cases}
$$

Thus, the [quantile function](/D/qf.html) is:

$$ \label{eq:cuni-qf-s1}
Q_X(p) = F_X^{-1}(x) \; .
$$

This can be derived by rearranging equation \eqref{eq:cuni-cdf}:

$$ \label{eq:cuni-cdf-s2}
\begin{split}
p &= \frac{x-a}{b-a} \\
x &= p(b-a) + a \\
x &= bp + a(1-p) = Q_X(p) \; .
\end{split}
$$