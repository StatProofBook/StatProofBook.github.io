---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-01-20 15:19:00

title: "Variance of the binomial distribution"
chapter: "Probability Distributions"
section: "Univariate discrete distributions"
topic: "Binomial distribution"
theorem: "Variance"

sources:
  - authors: "Wikipedia"
    year: 2022
    title: "Binomial distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2022-01-20"
    url: "https://en.wikipedia.org/wiki/Binomial_distribution#Expected_value_and_variance"

proof_id: "P302"
shortcut: "bin-var"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [binomial distribution](/D/bin):

$$ \label{eq:bin}
X \sim \mathrm{Bin}(n,p) \; .
$$

Then, the [variance](/D/var) of $X$ is

$$ \label{eq:bin-var}
\mathrm{Var}(X) = n p \, (1-p) \; .
$$


**Proof:** By definition, [a binomial random variable](/D/bin) is the sum of $n$ [independent and identical](/D/iid) [Bernoulli trials](/D/bern) with success probability $p$. Therefore, the variance is

$$ \label{eq:bin-var-s1}
\mathrm{Var}(X) = \mathrm{Var}(X_1 + \ldots + X_n)
$$

and because [variances add up under independence](/P/var-add), this is equal to

$$ \label{eq:bin-var-s2}
\mathrm{Var}(X) = \mathrm{Var}(X_1) + \ldots + \mathrm{Var}(X_n) = \sum_{i=1}^{n} \mathrm{Var}(X_i) \; .
$$

With the [variance of the Bernoulli distribution](/P/bern-var), we have:

$$ \label{eq:bin-var-s3}
\mathrm{Var}(X) = \sum_{i=1}^{n} p \, (1-p) = n p \, (1-p) \; .
$$