---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2025-02-06 16:14:14

title: "Odds ratio, prior and posterior odds"
chapter: "General Theorems"
section: "Bayesian statistics"
topic: "Bayesian inference"
definition: "Odds ratios"

sources:
  - authors: "Wikipedia"
    year: 2025
    title: "Odds ratio"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2025-02-06"
    url: "https://en.wikipedia.org/wiki/Odds_ratio"

def_id: "D215"
shortcut: "odds"
username: "JoramSoch"
---


**Definition:** Let $A_1$, $A_2$ and $B$ be arbitrary statements about [random variables](/D/rvar) where $A_1$ and $A_2$ are [mutually exclusive](/D/exc), but not nessarily [collectively exhaustive](/P/prob-exh).

Then, the "odds" or "[prior](/D/prior) odds ratio" in favor of $A_1$ against $A_2$ is defined as the ratio of the probabilities of $A_1$ and $A_2$, unconditional on $B$

$$ \label{eq:odds-prior}
\frac{p(A_1)}{p(A_2)}
$$

and the "[posterior](/D/post) odds ratio" in favor of $A_1$ against $A_2$ is defined as the ratio of the probabilities of $A_1$ and $A_2$, conditional on $B$

$$ \label{eq:odds-post}
\frac{p(A_1|B)}{p(A_2|B)}
$$

where $p(\cdot)$ is a [probability mass function](/D/pmf) or [probability density function](/D/pdf). Prior and posterior odds ratio are related to each other via the [Bayes factor](/D/bf) through [Bayes' rule](/P/bayes-rule).