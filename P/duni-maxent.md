---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2023-08-18 16:43:00

title: "Discrete uniform distribution maximizes entropy for finite support"
chapter: "Probability Distributions"
section: "Univariate discrete distributions"
topic: "Discrete uniform distribution"
theorem: "Maximum entropy distribution"

sources:
  - authors: "Probability Fact"
    year: 2023
    title: "The entropy of a distribution with finite domain"
    in: "Twitter"
    pages: "retrieved on 2023-08-18"
    url: "https://twitter.com/ProbFact/status/1673787091610750980"

proof_id: "P411"
shortcut: "duni-maxent"
username: "JoramSoch"
---


**Theorem:** The [discrete uniform distribution](/D/duni) maximizes [(Shannon) entropy](/D/ent) for a [random variable](/D/rvar) with finite support.


**Proof:** A random variable with finite support is a [discrete random variable](/D/rvar-disc). Let $X$ be such a random variable. Without loss of generality, we can assume that the possible values of the $X$ can be enumerated from $1$ to $n$.

Let $g(x)$ be the discrete uniform distribution with $a=1$ and maximum $b=n$ which assigns to equal probability to all $n$ possible values and let $f(x)$ be an arbitrary [discrete](/D/rvar-disc) [probability distribution](/D/dist) on the set $\left\lbrace 1, 2, \ldots, n-1, n \right\rbrace$.

For a [discrete random variable](/D/rvar-disc) $X$ with set of possible values $\mathcal{X}$ and [probability mass function](/D/pmf) $p(x)$, the [Shannon entropy](/D/ent) is defined as:

$$ \label{eq:ent}
\mathrm{H}(X) = - \sum_{x \in \mathcal{X}} p(x) \log p(x)
$$

Consider the [Kullback-Leibler divergence](/D/kl) of distribution $f(x)$ from distribution $g(x)$ [which is non-negative](/P/kl-nonneg):

$$ \label{eq:kl-fg}
\begin{split}
0 \leq \mathrm{KL}[f||g] &= \sum_{x \in \mathcal{X}} f(x) \log \frac{f(x)}{g(x)} \\
&= \sum_{x \in \mathcal{X}} f(x) \log f(x) - \sum_{x \in \mathcal{X}} f(x) \log g(x) \\
&\overset{\eqref{eq:ent}}{=} - \mathrm{H}[f(x)] - \sum_{x \in \mathcal{X}} f(x) \log g(x) \; .
\end{split}
$$

By plugging the [probability mass function of the discrte uniform distribution](/P/duni-pmf) into the second term, we obtain:

$$ \label{eq:sum-fg-s1}
\begin{split}
\sum_{x \in \mathcal{X}} f(x) \log g(x) &= \sum_{x=1}^{n} f(x) \log \frac{1}{n-1+1} \\
&= \log \frac{1}{n} \sum_{x=1}^{n} f(x) \\
&= -\log(n) \; .
\end{split}
$$

This is actually the negative of the [entropy of the discrete uniform distribution](/P/duni-ent), such that:

$$ \label{eq:sum-fg-s2}
\sum_{x \in \mathcal{X}} f(x) \log g(x) = -\mathrm{H}[\mathcal{U}(1,n)] = -\mathrm{H}[g(x)] \; .
$$

Combining \eqref{eq:kl-fg} with \eqref{eq:sum-fg-s2}, we can show that

$$ \label{eq:duni-maxent}
\begin{split}
0 &\leq \mathrm{KL}[f||g] \\
0 &\leq - \mathrm{H}[f(x)] - \left( -\mathrm{H}[g(x)] \right) \\
\mathrm{H}[g(x)] &\geq \mathrm{H}[f(x)]
\end{split}
$$

which means that the [entropy](/D/ent) of the [discrete uniform distribution](/D/duni) $\mathcal{U}(a,b)$ will be larger than or equal to any other [distribution](/D/dist) defined on the same set of values $\left\lbrace a, \ldots, b \right\rbrace$.