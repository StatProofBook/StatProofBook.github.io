---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-07-30 11:11:00

title: "Kolmogorov axioms of probability"
chapter: "General Theorems"
section: "Probability theory"
topic: "Probability axioms"
definition: "Axioms of probability"

sources:
  - authors: "A.N. Kolmogorov"
    year: 1950
    title: "Elementary Theory of Probability"
    in: "Foundations of the Theory of Probability"
    pages: "p. 2"
    url: "https://archive.org/details/foundationsofthe00kolm/page/2/mode/2up"
  - authors: "Alan Stuart & J. Keith Ord"
    year: 1994
    title: "Probability and Statistical Inference"
    in: "Kendall's Advanced Theory of Statistics, Vol. 1: Distribution Theory"
    pages: "ch. 8.6, p. 288, eqs. 8.2-8.4"
    url: "https://www.wiley.com/en-us/Kendall%27s+Advanced+Theory+of+Statistics%2C+3+Volumes%2C+Set%2C+6th+Edition-p-9780470669549"
  - authors: "Wikipedia"
    year: 2021
    title: "Probability axioms"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-07-30"
    url: "https://en.wikipedia.org/wiki/Probability_axioms#Axioms"

def_id: "D158"
shortcut: "prob-ax"
username: "JoramSoch"
---


**Definition:** Let there be a [sample space](/D/samp-spc) $\Omega$, an [event space](/D/eve-spc) $\mathcal{E}$ and a [probability measure](/D/prob-meas) $P$, such that $P(E)$ is the [probability](/D/prob) of some [event](/D/reve) $E \in \mathcal{E}$. Then, we introduce three axioms of probability:

* First axiom: The probability of an event is a non-negative real number:

$$ \label{eq:prob-ax1}
P(E) \in \mathbb{R}, \; P(E) \geq 0, \; \text{for all } E \in \mathcal{E} \; .
$$

* Second axiom: The probability that at least one elementary event in the sample space will occur is one:

$$ \label{eq:prob-ax2}
P(\Omega) = 1 \; .
$$

* Third axiom: The probability of any countable sequence of disjoint (i.e. [mutually exclusive](/D/exc)) events $E_1, E_2, E_3, \ldots$ is equal to the sum of the probabilities of the individual events:

$$ \label{eq:prob-ax3}
P\left(\bigcup_{i=1}^\infty E_i \right) = \sum_{i=1}^\infty P(E_i) \; .
$$