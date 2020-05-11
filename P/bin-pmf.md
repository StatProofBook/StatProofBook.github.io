---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-05-11 22:35:00

title: "Probability mass function of the binomial distribution"
chapter: "Probability Distributions"
section: "Univariate discrete distributions"
topic: "Binomial distribution"
theorem: "Probability mass function"

sources:

proof_id: "P97"
shortcut: "bin-pmf"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [binomial distribution](/D/bin):

$$ \label{eq:bin}
X \sim \mathrm{Bin}(n,p) \; .
$$

Then, the [probability mass function](/D/pmf) of $X$ is

$$ \label{eq:bin-pmf}
f_X(x) = {n \choose x} \, p^x \, (1-p)^{n-x} \; .
$$


**Proof:** A binomial variable [is defined as](/D/bin) the number of successes observed in $n$ [independent](/D/ind) trials, where each trial has [two possible outcomes](/D/bern) (success/failure) and the [probability](/D/prob) of success and failure are identical across trials ($p$/$q = 1-p$).

If one has obtained $x$ successes in $n$ trials, one has also obtained $(n-x)$ failures. The probability of a particular series of $x$ successes and $(n-x)$ failures, when order does matter, is

$$ \label{eq:bin-prob}
p^x \, (1-p)^{n-x} \; .
$$

When order does not matter, there is a number of series consisting of $x$ successes and $(n-x)$ failures. This number is equal to the number of possibilities in which $x$ objects can be choosen from $n$ objects which is given by the binomial coefficient:

$$ \label{eq:bin-coeff}
{n \choose x} \; .
$$

In order to obtain the probability of $x$ successes and $(n-x)$ failures, when order does not matter, the probability in \eqref{eq:bin-prob} has to be multiplied with the number of possibilities in \eqref{eq:bin-coeff} which gives

$$ \label{eq:bin-pmf-qed}
p(X=x|n,p) = {n \choose x} \, p^x \, (1-p)^{n-x}
$$

which is equivalent to the expression above.