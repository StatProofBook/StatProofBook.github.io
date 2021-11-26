---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-11-26 10:57:00

title: "Law of total expectation"
chapter: "General Theorems"
section: "Probability theory"
topic: "Expected value"
theorem: "Law of total expectation"

sources:
  - authors: "Wikipedia"
    year: 2021
    title: "Law of total expectation"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-11-26"
    url: "https://en.wikipedia.org/wiki/Law_of_total_expectation#Proof_in_the_finite_and_countable_cases"

proof_id: "P291"
shortcut: "mean-tot"
username: "JoramSoch"
---


**Theorem:** (law of total expectation, also called "law of iterated expectations") Let $X$ be a [random variable](/D/rvar) with [expected value](/D/mean) $\mathrm{E}(X)$ and let $Y$ be any [random variable](/D/var) defined on the same [probability space](/D/prob-spc). Then, the [expected value](/D/mean) of the [conditional expectation](/D/mean-cond) of $X$ given $Y$ is the same as the [expected value](/D/mean) of $X$:

$$ \label{eq:mean-tot}
\mathrm{E}(X) = \mathrm{E}[\mathrm{E}(X \vert Y)] \; .
$$


**Proof:** Let $X$ and $Y$ be [discrete random variables](/D/rvar-disc) with sets of possible outcomes $\mathcal{X}$ and $\mathcal{Y}$. Then, the expectation of the conditional expetectation can be rewritten as:

$$ \label{eq:mean-tot-s1}
\begin{split}
\mathrm{E}[\mathrm{E}(X \vert Y)] &= \mathrm{E}\left[ \sum_{x \in \mathcal{X}} x \cdot \mathrm{Pr}(X = x \vert Y) \right] \\
&= \sum_{y \in \mathcal{Y}} \left[ \sum_{x \in \mathcal{X}} x \cdot \mathrm{Pr}(X = x \vert Y = y) \right] \cdot \mathrm{Pr}(Y = y) \\
&= \sum_{x \in \mathcal{X}} \sum_{y \in \mathcal{Y}} x \cdot \mathrm{Pr}(X = x \vert Y = y) \cdot \mathrm{Pr}(Y = y) \; .
\end{split}
$$

Using the [law of conditional probability](/D/prob-cond), this becomes:

$$ \label{eq:mean-tot-s2}
\begin{split}
\mathrm{E}[\mathrm{E}(X \vert Y)] &= \sum_{x \in \mathcal{X}} \sum_{y \in \mathcal{Y}} x \cdot \mathrm{Pr}(X = x, Y = y) \\
&= \sum_{x \in \mathcal{X}} x \sum_{y \in \mathcal{Y}} \mathrm{Pr}(X = x, Y = y) \; .
\end{split}
$$

Using the [law of marginal probability](/D/prob-marg), this becomes:

$$ \label{eq:mean-tot-s3}
\begin{split}
\mathrm{E}[\mathrm{E}(X \vert Y)] &= \sum_{x \in \mathcal{X}} x \cdot \mathrm{Pr}(X = x) \\
&= \mathrm{E}(X) \; .
\end{split}
$$