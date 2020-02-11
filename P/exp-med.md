---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-02-11 15:03:00

title: "Median of the exponential distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Exponential distribution"
theorem: "Median"

sources:

proof_id: "P49"
shortcut: "exp-med"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a random variable following an [exponential distribution](/D/exp.html):

$$ \label{eq:exp}
X \sim \mathrm{Exp}(\lambda) \; .
$$

Then, the mean or expected value of $X$ is

$$ \label{eq:exp-mean}
\mathrm{E}(X) = \frac{1}{\lambda} \; .
$$


**Proof:** The [expected value](/D/ev.html) is the probability-weighted average over all possible values:

$$ \label{eq:mean}
\mathrm{E}(X) = \int_{\mathbb{R}} x \cdot f_\mathrm{X}(x) \, \mathrm{d}x \; .
$$

With the [probability density function of the exponential distribution](/P/exp-pdf.html), this reads:

$$ \label{eq:exp-mean-s1}
\begin{split}
\mathrm{E}(X) &= \int_{0}^{+\infty} x \cdot \lambda \exp(-\lambda x) \, \mathrm{d}x \\
&= \lambda \int_{0}^{+\infty} x \cdot \exp(-\lambda x) \, \mathrm{d}x \; .
\end{split}
$$

Using the following anti-deriative

$$ \label{eq:exp-mean-s2}
\int x \cdot \exp(-\lambda x) \, \mathrm{d}x = \left( - \frac{1}{\lambda} x - \frac{1}{\lambda^2} \right) \exp(-\lambda x) \; ,
$$

the expected value becomes

$$ \label{eq:exp-mean-s3}
\begin{split}
\mathrm{E}(X) &= \lambda \left[ \left( - \frac{1}{\lambda} x - \frac{1}{\lambda^2} \right) \exp(-\lambda x) \right]_{0}^{+\infty} \\
&= \lambda \left[ \lim_{x \to \infty} \left( - \frac{1}{\lambda} x - \frac{1}{\lambda^2} \right) \exp(-\lambda x) - \left( - \frac{1}{\lambda} \cdot 0 - \frac{1}{\lambda^2} \right) \exp(-\lambda \cdot 0) \right] \\
&= \lambda \left[ 0 + \frac{1}{\lambda^2} \right] \\
&= \frac{1}{\lambda} \; .
\end{split}
$$