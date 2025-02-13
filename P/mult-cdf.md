---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2025-02-06 15:15:25

title: "Cumulative distribution function of the multinomial distribution"
chapter: "Probability Distributions"
section: "Multivariate discrete distributions"
topic: "Multinomial distribution"
theorem: "Cumulative distribution function"

sources:

proof_id: "P489"
shortcut: "mult-cdf"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random vector](/D/rvec) following a [multinomial distribution](/D/mult):

$$ \label{eq:mult}
X \sim \mathrm{Mult}(n,\left[p_1, \ldots, p_k \right]) \; .
$$

Then, 1) the [joint cumulative distribution function](/D/cdf-joint) of $X$ is

$$ \label{eq:mult-cdf-joint}
F_X(x) = {n \choose {x_1, \ldots, x_k}} \, \prod_{i=1}^k {p_i}^{x_i}
$$

and 2) the [marginal](/D/dist-marg) [cumulative distribution function](/D/cdf) of each $X_i$ is

$$ \label{eq:mult-cdf-marg}
F_{X_i}(x_i) = \sum_{k=0}^{x_i} {n \choose k} \, p_i^k \, (1-p_i)^{n-k} \; .
$$


**Proof:** The [probability mass function of the multinomial distribution](/P/mult-pmf) is

$$ \label{eq:mult-pmf}
f_X(x) = {n \choose {x_1, \ldots, x_k}} \, \prod_{i=1}^k {p_i}^{x_i} \; ,
$$

1) The [joint cumulative distribution function (CDF) of a random vector](/D/cdf-joint) is defined as

$$ \label{eq:cdf-joint}
F_X(x) = \mathrm{Pr}(X_1 \leq x_1, \ldots, X_n \leq x_n)
$$

which, [in terms of the probability mass function, is given by](/P/cdf-pmf)

$$ \label{eq:cdf-pmf}
F_X(x) = \sum_{t_1 \leq x_1} \ldots \sum_{t_n \leq x_n} f_X(t_1, \ldots, t_n) \; .
$$

For a given set of counts $x_1, \ldots, x_k$ satisfying $\sum_{i=1}^k x_i = n$, we define the set of eligible values $t_1, \ldots, t_k$ for the CDF:

$$ \label{eq:ti-set}
\mathcal{T}(x) = \left\lbrace (t_1, \ldots, t_k) \mid t_i \in \mathbb{N}_0, \; 0 \leq t_i \leq x_i, \; \sum_{i=1}^k t_i = n \right\rbrace \; .
$$

Since any eligible set of counts $t_1, \ldots, t_k$ must add up to $n$, this set is equivalent to

$$ \label{eq:ti-set-eq}
\mathcal{T}(x) = \left\lbrace (x_1, \ldots, x_k) \right\rbrace \; .
$$

Therefore, the CDF is equal to the probability mass function at $t = x$:

$$ \label{eq:mult-cdf-joint-qed}
F_X(x) \overset{\eqref{eq:cdf-pmf}}{=} \sum_{t \in \mathcal{T}(x)} f_X(t_1, \ldots, t_k) = f_X(x_1, \ldots, x_k) \; .
$$

so that the joint cumulative distribution function of the multinomial distribution becomes

$$ \label{eq:xi-ni-con}
F_X(x) \overset{\eqref{eq:mult-pmf}}{=} {n \choose {x_1, \ldots, x_k}} \, \prod_{i=1}^k {p_i}^{x_i} \; .
$$

2) The [marginal distributions for the multinomial distribution](/P/mult-marg) are

$$ \label{eq:mult-marg}
X_i \sim \mathrm{Bin}(n, p_i)
\quad \text{for all} \quad
i = 1, \ldots, k \; .
$$

Thus, the marginal cumulative distribution function of any entry $X_i$ is equal to the [cumulative distribution function of the binomial distribution](/P/bin-cdf):

$$ \label{eq:mult-cdf-marg-qed}
F_{X_i}(x_i) = \sum_{k=0}^{x_i} {n \choose k} \, p_i^k \, (1-p_i)^{n-k} \; .
$$