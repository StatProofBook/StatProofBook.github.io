---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-05-19 00:17:00

title: "Partition of variance into expected values"
chapter: "General Theorems"
section: "Probability theory"
topic: "Variance"
theorem: "Partition into expected values"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Variance"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-05-19"
    url: "https://en.wikipedia.org/wiki/Variance#Definition"

proof_id: "P104"
shortcut: "var-mean"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar). Then, the [variance](/D/var) of $X$ is equal to the [mean](/D/mean) of the square of $X$ minus the square of the [mean](/D/mean) of $X$:

$$ \label{eq:var-mean}
\mathrm{Var}(X) = \mathrm{E}(X^2) - \mathrm{E}(X)^2 \; .
$$


**Proof:** The [variance](/D/var) of $X$ is defined as

$$ \label{eq:var}
\mathrm{Var}(X) = \mathrm{E}\left[ \left( X - \mathrm{E}[X] \right)^2 \right]
$$

which, due to the [linearity of the expected value](/P/mean-lin), can be rewritten as

$$ \label{eq:var-mean-qed}
\begin{split}
\mathrm{Var}(X) &= \mathrm{E}\left[ \left( X - \mathrm{E}[X] \right)^2 \right] \\
&= \mathrm{E}\left[ X^2 - 2 \, X \, \mathrm{E}(X) + \mathrm{E}(X)^2 \right] \\
&= \mathrm{E}(X^2) - 2 \, \mathrm{E}(X) \, \mathrm{E}(X) + \mathrm{E}(X)^2 \\
&= \mathrm{E}(X^2) - \mathrm{E}(X)^2 \; .
\end{split}
$$