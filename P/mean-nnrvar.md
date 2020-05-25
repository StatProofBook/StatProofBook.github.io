---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-05-18 23:54:00

title: "Expected value of a non-negative random variable"
chapter: "General Theorems"
section: "Probability theory"
topic: "Expected value"
theorem: "Non-negative random variable"

sources:
  - authors: "Kemp, Graham"
    year: 2014
    title: "Expected value of a non-negative random variable"
    in: "StackExchange Mathematics"
    pages: "retrieved on 2020-05-18"
    url: "https://math.stackexchange.com/questions/958472/expected-value-of-a-non-negative-random-variable"

proof_id: "P103"
shortcut: "mean-nnrvar"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a non-negative [random variable](/D/rvar). Then, the [expected value](/D/mean) of $X$ is

$$ \label{eq:mean-cdf}
\mathrm{E}(X) = \int_{0}^{\infty} (1 - F_X(x)) \, \mathrm{d}x
$$

where $F_X(x)$ is the [cumulative distribution function](/D/cdf) of $X$.


**Proof:** Because the cumulative distribution function [gives the probability of a random variable being smaller than a given value](/D/cdf),

$$ \label{eq:cdf-Pr-leq}
F_X(x) = \mathrm{Pr}(X \leq x) \; ,
$$

we have

$$ \label{eq:cdf-Pr-geq}
1 - F_X(x) = \mathrm{Pr}(X > x) \; ,
$$

such that

$$ \label{eq:mean-cdf-s1}
\int_{0}^{\infty} (1 - F_X(x)) \, \mathrm{d}x = \int_{0}^{\infty} \mathrm{Pr}(X > x) \, \mathrm{d}x
$$

which, using the [probability density function](/D/pdf) of $X$, can be rewritten as

$$ \label{eq:mean-cdf-s2}
\begin{split}
\int_{0}^{\infty} (1 - F_X(x)) \, \mathrm{d}x &= \int_{0}^{\infty} \int_{x}^{\infty} f_X(z) \, \mathrm{d}z \, \mathrm{d}x \\
&= \int_{0}^{\infty} \int_{0}^{z} f_X(z) \, \mathrm{d}x \, \mathrm{d}z \\
&= \int_{0}^{\infty} f_X(z) \int_{0}^{z} 1 \, \mathrm{d}x \, \mathrm{d}z \\
&= \int_{0}^{\infty} [x]_{0}^{z} \cdot f_X(z) \, \mathrm{d}z \\
&= \int_{0}^{\infty} z \cdot f_X(z) \, \mathrm{d}z \\
\end{split}
$$

and by applying the [definition of the expected value](/D/mean), we see that

$$ \label{eq:mean-cdf-s3}
\int_{0}^{\infty} (1 - F_X(x)) \, \mathrm{d}x = \int_{0}^{\infty} z \cdot f_X(z) \, \mathrm{d}z = \mathrm{E}(X)
$$

which proves the identity given above.
