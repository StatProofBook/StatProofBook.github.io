---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2025-02-06 14:37:29

title: "Cumulative distribution function of the binomial distribution"
chapter: "Probability Distributions"
section: "Univariate discrete distributions"
topic: "Binomial distribution"
theorem: "Cumulative distribution function"

sources:
  - authors: "Wikipedia"
    year: 2025
    title: "Binomial distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2025-02-06"
    url: "https://en.wikipedia.org/wiki/Binomial_distribution#Cumulative_distribution_function"

proof_id: "P488"
shortcut: "bin-cdf"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [binomial distribution](/D/bin):

$$ \label{eq:bin}
X \sim \mathrm{Bin}(n,p) \; .
$$

Then, the [cumulative distribution function](/D/cdf) of $X$ is

$$ \label{eq:bin-cdf}
F_X(x) = \sum_{k=0}^{x} {n \choose k} \, p^k \, (1-p)^{n-k} \; .
$$


**Proof:** The [cumulative distribution function](/D/cdf) is defined as

$$ \label{eq:cdf}
F_X(x) = \mathrm{Pr}(X \leq x)
$$

which, [in terms of the probability mass function, is given by](/P/cdf-pmf)

$$ \label{eq:cdf-pmf}
F_X(x) = \sum_{\substack{t \in \mathcal{X} \\ t \leq x}} f_X(t) \; .
$$

The [probability mass function of the binomial distribution](/P/bin-pmf) is

$$ \label{eq:bin-pmf}
f_X(x) = {n \choose x} \, p^x \, (1-p)^{n-x} \; ,
$$

so that the cumulative distribution function of the binomial distribution becomes

$$ \label{eq:bin-cdf-qed}
\begin{split}
 F_X(x)
&\overset{\eqref{eq:cdf-pmf}}{=} \sum_{k=0}^{x} f_X(k) \\
&\overset{\eqref{eq:bin-pmf}}{=} \sum_{k=0}^{x} {n \choose k} \, p^k \, (1-p)^{n-k} \; .
\end{split}
$$