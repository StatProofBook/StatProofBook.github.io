---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-07-28 04:57:00

title: "Probability mass function of the discrete uniform distribution"
chapter: "Probability Distributions"
section: "Univariate discrete distributions"
topic: "Discrete uniform distribution"
theorem: "Probability mass function"

sources:

proof_id: "P140"
shortcut: "duni-pmf"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [discrete uniform distribution](/D/duni):

$$ \label{eq:duni}
X \sim \mathcal{U}(a, b) \; .
$$

Then, the [probability mass function](/D/pmf) of $X$ is

$$ \label{eq:duni-pmf}
f_X(x) = \frac{1}{b-a+1} \quad \text{where} \quad x \in \left\lbrace a, a+1, \ldots, b-1, b \right\rbrace \; .
$$


**Proof:** A [discrete uniform variable is defined as](/D/duni) having the same probability for each integer between and including $a$ and $b$. The number of integers between and including $a$ and $b$ is

$$ \label{eq:n}
n = b - a + 1
$$

and because [the sum across all probabilities](/D/pmf) is

$$ \label{eq:1}
\sum_{x=a}^{b} f_X(x) = 1 \; ,
$$

we have

$$ \label{eq:duni-pmf-qed}
f_X(x) = \frac{1}{n} = \frac{1}{b-a+1} \; .
$$