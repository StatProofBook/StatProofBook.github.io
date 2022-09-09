---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-09-02 12:21:00

title: "Entropy of the Bernoulli distribution"
chapter: "Probability Distributions"
section: "Univariate discrete distributions"
topic: "Bernoulli distribution"
theorem: "Shannon entropy"

sources:
  - authors: "Wikipedia"
    year: 2022
    title: "Bernoulli distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2022-09-02"
    url: "https://en.wikipedia.org/wiki/Bernoulli_distribution"
  - authors: "Wikipedia"
    year: 2022
    title: "Binary entropy function"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2022-09-02"
    url: "https://en.wikipedia.org/wiki/Binary_entropy_function"

proof_id: "P334"
shortcut: "bern-ent"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [Bernoulli distribution](/D/bern):

$$ \label{eq:bern}
X \sim \mathrm{Bern}(p) \; .
$$

Then, the [(Shannon) entropy](/D/ent) of $X$ in bits is

$$ \label{eq:bern-ent}
\mathrm{H}(X) = -p \log_2 p - (1-p) \log_2 (1-p) \; .
$$


**Proof:** The [entropy](/D/ent) is defined as the probability-weighted average of the logarithmized probabilities for all possible values:

$$ \label{eq:ent}
\mathrm{H}(X) = - \sum_{x \in \mathcal{X}} p(x) \cdot \log_b p(x) \; .
$$

Entropy is measured in bits by setting $b = 2$. Since there are only [two possible outcomes for a Bernoulli random variable](/P/bern-pmf), we have:

$$ \label{eq:bern-ent-qed}
\begin{split}
\mathrm{H}(X) &= - \mathrm{Pr}(X = 0) \cdot \log_2 \mathrm{Pr}(X = 0) - \mathrm{Pr}(X = 1) \cdot \log_2 \mathrm{Pr}(X = 1) \\
&= -p \log_2 p - (1-p) \log_2 (1-p) \; . \\
\end{split}
$$