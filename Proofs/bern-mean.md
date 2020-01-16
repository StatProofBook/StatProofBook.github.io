---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-01-16 10:58:00

title: "Mean of the Bernoulli distribution"
chapter: "Probability Distributions"
section: "Univariate discrete distributions"
topic: "Bernoulli distribution"
theorem: "Mean"

dependencies:
  - theorem: "probability mass function of the Bernoulli distribution"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Bernoulli distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-01-16"
    url: "https://en.wikipedia.org/wiki/Bernoulli_distribution#Mean"

proof_id: "P22"
shortcut: "bern-mean"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a random variable following a Bernoulli distribution:

$$ \label{eq:bern}
X \sim \mathrm{Bern}(p) \; .
$$

Then, the mean or expected value of $X$ is

$$ \label{eq:bern-mean}
\mathrm{E}(X) = p \; .
$$


**Proof:** The expected value is the probability-weighted average of all possible values:

$$ \label{eq:mean}
\mathrm{E}(X) = \sum_{x \in \mathcal{X}} x \cdot \mathrm{Pr}(X = x) \; .
$$

Since there are only two possible outcomes for a Bernoulli random variable, we have:

$$ \label{eq:bern-mean-qed}
\begin{split}
\mathrm{E}(X) &= 0 \cdot \mathrm{Pr}(X = 0) + 1 \cdot \mathrm{Pr}(X = 1) \\
&= 0 \cdot (1-p) + 1 \cdot p \\
&= p \; . \\
\end{split}
$$