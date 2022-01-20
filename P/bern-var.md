---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-01-20 15:06:00

title: "Variance of the Bernoulli distribution"
chapter: "Probability Distributions"
section: "Univariate discrete distributions"
topic: "Bernoulli distribution"
theorem: "Variance"

sources:
  - authors: "Wikipedia"
    year: 2022
    title: "Bernoulli distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2022-01-20"
    url: "https://en.wikipedia.org/wiki/Bernoulli_distribution#Variance"

proof_id: "P301"
shortcut: "bern-var"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [Bernoulli distribution](/D/bern):

$$ \label{eq:bern}
X \sim \mathrm{Bern}(p) \; .
$$

Then, the [variance](/D/mean) of $X$ is

$$ \label{eq:bern-var}
\mathrm{Var}(X) = p \, (1-p) \; .
$$


**Proof:** The [variance](/D/mean) is the probability-weighted average of the squared deviation from the [expected value](/D/mean) across all possible values

$$ \label{eq:var}
\mathrm{Var}(X) = \sum_{x \in \mathcal{X}} (x - \mathrm{E}(X))^2 \cdot \mathrm{Pr}(X = x)
$$

and [can also be written in terms of the expected values](/P/var-mean):

$$ \label{eq:var-mean}
\mathrm{Var}(X) = \mathrm{E}\left( X^2 \right) - \mathrm{E}(X)^2 \; .
$$

The [mean of a Bernoulli random variable](/P/bern-mean) is

$$ \label{eq:bern-mean}
X \sim \mathrm{Bern}(p) \quad \Rightarrow \quad \mathrm{E}(X) = p
$$

and the mean of a squared Bernoulli random variable is

$$ \label{eq:bern-sqr-mean}
\mathrm{E}\left( X^2 \right) = 0^2 \cdot \mathrm{Pr}(X = 0) + 1^2 \cdot \mathrm{Pr}(X = 1) = 0 \cdot (1-p) + 1 \cdot p = p \; .
$$

Combining \eqref{eq:var-mean}, \eqref{eq:bern-mean} and \eqref{eq:bern-sqr-mean}, we have:

$$ \label{eq:bern-var-qed}
\mathrm{Var}(X) = p - p^2 = p \, (1-p) \; .
$$