---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-03-02 20:49:00

title: "Exponential distribution is a special case of gamma distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Exponential distribution"
theorem: "Special case of gamma distribution"

sources:

proof_id: "P69"
shortcut: "exp-gam"
username: "JoramSoch"
---


**Theorem:** The [exponential distribution](/D/exp) is a special case of the [gamma distribution](/D/gam) with shape $a = 1$ and rate $b = \lambda$.


**Proof:** The [probability density function of the gamma distribution](/P/gam-pdf) is

$$ \label{eq:gam-pdf}
\mathrm{Gam}(x; a, b) = \frac{b^a}{\Gamma(a)} x^{a-1} \exp[-b x] \; .
$$

Setting $a = 1$ and $b = \lambda$, we obtain

$$ \label{eq:exp-pdf}
\begin{split}
\mathrm{Gam}(x; 1, \lambda) &= \frac{\lambda^1}{\Gamma(1)} x^{1-1} \exp[-\lambda x] \\
&= \frac{x^0}{\Gamma(1)} \lambda \exp[-\lambda x] \\
&= \lambda \exp[-\lambda x]
\end{split}
$$

which is equivalent to the [probability density function of the exponential distribution](/P/exp-pdf).