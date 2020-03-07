---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-01-16 11:26:00

title: "Mean of the multinomial distribution"
chapter: "Probability Distributions"
section: "Multivariate discrete distributions"
topic: "Multinomial distribution"
theorem: "Mean"

sources:

proof_id: "P25"
shortcut: "mult-mean"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random vector](/D/rvec) following a [multinomial distribution](/D/mult):

$$ \label{eq:mult}
X \sim \mathrm{Mult}(n,\left[p_1, \ldots, p_k \right]) \; .
$$

Then, the [mean or expected value](/D/mean) of $X$ is

$$ \label{eq:bin-mean}
\mathrm{E}(X) = \left[n p_1, \ldots, n p_k \right] \; .
$$


**Proof:** By definition, [a multinomial random variable](/D/mult) is the sum of $n$ independent and identical [categorical trials](/D/cat) with category probabilities $p_1, \ldots, p_k$. Therefore, the expected value is

$$ \label{eq:mult-mean-s1}
\mathrm{E}(X) = \mathrm{E}(X_1 + \ldots + X_n)
$$

and because the [expected value is a linear operator](/P/mean-lin), this is equal to

$$ \label{eq:mult-mean-s2}
\begin{split}
\mathrm{E}(X) &= \mathrm{E}(X_1) + \ldots + \mathrm{E}(X_n) \\
&= \sum_{i=1}^{n} \mathrm{E}(X_i) \; .
\end{split}
$$

With the [expected value of the categorical distribution](/P/cat-mean), we have:

$$ \label{eq:mult-mean-s3}
\mathrm{E}(X) = \sum_{i=1}^{n} \left[p_1, \ldots, p_k \right] = n \cdot \left[p_1, \ldots, p_k \right] = \left[n p_1, \ldots, n p_k \right] \; .
$$