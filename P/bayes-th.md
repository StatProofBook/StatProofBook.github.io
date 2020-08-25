---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2019-09-27 16:24:00

title: "Bayes' theorem"
chapter: "General Theorems"
section: "Bayesian statistics"
topic: "Bayesian inference"
theorem: "Bayes' theorem"

sources:
  - authors: "Koch, Karl-Rudolf"
    year: 2007
    title: "Rules of Probability"
    in: "Introduction to Bayesian Statistics"
    pages: "Springer, Berlin/Heidelberg, 2007, pp. 6/13, eqs. 2.12/2.38"
    url: "https://www.springer.com/de/book/9783540727231"
    doi: "10.1007/978-3-540-72726-2"

proof_id: "P4"
shortcut: "bayes-th"
username: "JoramSoch"
---


**Theorem:** Let $A$ and $B$ be two arbitrary statements about [random variables](/D/rvar), such as statements about the presence or absence of an event or about the value of a scalar, vector or matrix. Then, the conditional probability that $A$ is true, given that $B$ is true, is equal to

$$ \label{eq:BT}
p(A|B) = \frac{p(B|A) \, p(A)}{p(B)} \; .
$$


**Proof:** The [conditional probability](/D/prob-cond) is defined as the ratio of [joint probability](/D/prob-joint), i.e. the probability of both statements being true, and [marginal probability](/D/prob-marg), i.e. the probability of only the second one being true:

$$ \label{eq:LCP}
p(A|B) = \frac{p(A,B)}{p(B)} \; .
$$

It can also be written down for the reverse situation, i.e. to calculate the probability that $B$ is true, given that $A$ is true:

$$ \label{eq:LCP-rev}
p(B|A) = \frac{p(A,B)}{p(A)} \; .
$$

Both equations can be rearranged for the joint probability

$$ \label{eq:JP}
p(A|B) \, p(B) \overset{\eqref{eq:LCP}}{=} p(A,B) \overset{\eqref{eq:LCP-rev}}{=} p(B|A) \, p(A)
$$

from which Bayes' theorem can be directly derived:

$$ \label{eq:BT-proof}
p(A|B) \overset{\eqref{eq:JP}}{=} \frac{p(B|A) \, p(A)}{p(B)} \; .
$$