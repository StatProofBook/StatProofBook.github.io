---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2019-05-03 07:55:00

title: "Bayes' theorem"
chapter: "General Theorems"
section: "Probability theory"
topic: "Bayesian inference"
theorem: "Bayes' theorem"

proof_id: "P4"
shortcut: "bayes-th"
username: "JoramSoch"
---


**Theorem:** Let $A$ and $B$ be two arbitrary statements about random variables, such as statements about the presence or absence of an event or about the value of a scalar, vector or matrix. Then, the conditional probability that $A$ is true, given that $B$ is true, is equal to

$$ \label{eq:BT}
p(A|B) = \frac{p(B|A) \, p(A)}{p(B)} \; .
$$


**Proof:** The conditional probability is defined as the ratio of joint probability, i.e. the probability of both statements being true, and marginal probability, i.e. the probability of only the second one being true:

$$ \label{eq:LCP}
p(A|B) = \frac{p(A,B)}{p(B)} \; .
$$

It can also be written down for the reverse situation, i.e. to calculate the probability that $B$ is true, given that $A$ is true:

$$ \label{eq:LCP-rev}
p(B|A) = \frac{p(A,B)}{p(A)} \; .
$$

Both equations can be rearranged for the joint probability

$$ \label{eq:JP}
p(A|B) \, p(B) \overset{(\ref{eq:LCP})}{=} p(A,B) \overset{(\ref{eq:LCP-rev})}{=} p(B|A) \, p(A)
$$

from which Bayes' theorem can be directly derived:

$$ \label{eq:BT-proof}
p(A|B) \overset{(\ref{eq:JP})}{=} \frac{p(B|A) \, p(A)}{p(B)} \; .
$$

<div align="right">&#8718;</div>


**Dependencies:**

- law of conditional probability, also called "product rule of probability"


**Source:**

- Koch, Karl-Rudolf (2007): *Introduction to Bayesian Statistics*, second edition, Springer, Berlin/Heidelberg, 2007, pp. 6/13, eqs. 2.12/2.38.