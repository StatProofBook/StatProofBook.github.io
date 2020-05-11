---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-05-11 23:30:00

title: "Probability mass function of the multinomial distribution"
chapter: "Probability Distributions"
section: "Multivariate discrete distributions"
topic: "Multinomial distribution"
theorem: "Probability mass function"

sources:

proof_id: "P99"
shortcut: "mult-pmf"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random vector](/D/rvec) following a [multinomial distribution](/D/mult):

$$ \label{eq:mult}
X \sim \mathrm{Mult}(n, \left[p_1, \ldots, p_k \right]) \; .
$$

Then, the [probability mass function](/D/pmf) of $X$ is

$$ \label{eq:mult-pmf}
f_X(x) = {n \choose {x_1, \ldots, x_k}} \, \prod_{i=1}^k {p_i}^{x_i} \; .
$$


**Proof:** A multinomial variable [is defined as](/D/mult) a vector of the numbers of observations belonging to $k$ distinct categories in $n$ [independent](/D/ind) trials, where each trial has [$k$ possible outcomes](/D/cat) and the category [probabilities](/D/prob) are identical across trials.

The probability of a particular series of $x_1$ observations for category $1$, $x_2$ observations for category $2$ etc., when order does matter, is

$$ \label{eq:mult-prob}
\prod_{i=1}^k {p_i}^{x_i} \; .
$$

When order does not matter, there is a number of series consisting of $x_1$ observations for category $1$, ..., $x_k$ observations for category $k$. This number is equal to the number of possibilities in which $x_1$ category $1$ objects, ..., $x_k$ category $k$ objects can be distributed in a sequence of $n$ objects which is given by the multinomial coefficient that can be expressed in terms of factorials:

$$ \label{eq:mult-coeff}
{n \choose {x_1, \ldots, x_k}} = \frac{n!}{x_1! \cdot \ldots \cdot x_k!} \; .
$$

In order to obtain the probability of $x_1$ observations for category $1$, ..., $x_k$ observations for category $k$, when order does not matter, the probability in \eqref{eq:mult-prob} has to be multiplied with the number of possibilities in \eqref{eq:mult-coeff} which gives

$$ \label{eq:mult-pmf-qed}
p(X=x|n,\left[p_1, \ldots, p_k \right]) = {n \choose {x_1, \ldots, x_k}} \, \prod_{i=1}^k {p_i}^{x_i}
$$

which is equivalent to the expression above.