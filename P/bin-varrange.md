---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-01-27 09:20:00

title: "Range of the variance of the binomial distribution"
chapter: "Probability Distributions"
section: "Univariate discrete distributions"
topic: "Binomial distribution"
theorem: "Range of variance"

sources:

proof_id: "P304"
shortcut: "bin-varrange"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [binomial distribution](/D/bin):

$$ \label{eq:bin}
X \sim \mathrm{Bin}(n,p) \; .
$$

Then, the [variance](/D/var) of $X$ is necessarily between 0 and $n/4$:

$$ \label{eq:bin-var-range}
0 \leq \mathrm{Var}(X) \leq \frac{n}{4} \; .
$$


**Proof:** By definition, [a binomial random variable](/D/bin) is the sum of $n$ [independent and identical](/D/iid) [Bernoulli trials](/D/bern) with success probability $p$. Therefore, the variance is

$$ \label{eq:bin-var-s1}
\mathrm{Var}(X) = \mathrm{Var}(X_1 + \ldots + X_n)
$$

and because [variances add up under independence](/P/var-add), this is equal to

$$ \label{eq:bin-var-s2}
\mathrm{Var}(X) = \mathrm{Var}(X_1) + \ldots + \mathrm{Var}(X_n) = \sum_{i=1}^{n} \mathrm{Var}(X_i) \; .
$$

As the [variance of a Bernoulli random variable is always between 0 and 1/4](/P/bern-varrange)

$$ \label{eq:bern-var-range}
0 \leq \mathrm{Var}(X_i) \leq \frac{1}{4} \quad \text{for all} \quad i = 1,\ldots,n \; ,
$$

the minimum variance of $X$ is

$$ \label{eq:bin-var-min}
\mathrm{min}\left[\mathrm{Var}(X)\right] = n \cdot 0 = 0
$$

and the maximum variance of $X$ is

$$ \label{eq:bin-var-max}
\mathrm{max}\left[\mathrm{Var}(X)\right] = n \cdot \frac{1}{4} = \frac{n}{4} \; .
$$

Thus, we have:

$$ \label{eq:bin-var-int}
\mathrm{Var}(X) \in \left[ 0, \; \frac{n}{4} \right] \; .
$$