---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-06-02 20:50:00

title: "Partition of covariance into expected values"
chapter: "General Theorems"
section: "Probability theory"
topic: "Covariance"
theorem: "Partition into expected values"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Covariance"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-06-02"
    url: "https://en.wikipedia.org/wiki/Covariance#Definition"

proof_id: "P118"
shortcut: "cov-mean"
username: "JoramSoch"
---


**Theorem:** Let $X$ and $Y$ be [random variables](/D/rvar). Then, the [covariance](/D/cov) of $X$ and $Y$ is equal to the [mean](/D/mean) of the product of $X$ and $Y$ minus the product of the [means](/D/mean) of $X$ and $Y$:

$$ \label{eq:cov-mean}
\mathrm{Cov}(X,Y) = \mathrm{E}(X Y) - \mathrm{E}(X) \mathrm{E}(Y) \; .
$$


**Proof:** The [covariance](/D/cov) of $X$ and $Y$ is defined as

$$ \label{eq:cov}
\mathrm{Cov}(X,Y) = \mathrm{E}\left[ (X-\mathrm{E}[X]) (Y-\mathrm{E}[Y]) \right] \; .
$$

which, due to the [linearity of the expected value](/P/mean-lin), can be rewritten as

$$ \label{eq:cov-mean-qed}
\begin{split}
\mathrm{Cov}(X,Y) &= \mathrm{E}\left[ (X-\mathrm{E}[X]) (Y-\mathrm{E}[Y]) \right] \\
&= \mathrm{E}\left[ X Y - X \, \mathrm{E}(Y) - \mathrm{E}(X) \, Y + \mathrm{E}(X) \mathrm{E}(Y) \right] \\
&= \mathrm{E}(X Y) - \mathrm{E}(X) \mathrm{E}(Y) - \mathrm{E}(X) \mathrm{E}(Y) + \mathrm{E}(X) \mathrm{E}(Y) \\
&= \mathrm{E}(X Y) - \mathrm{E}(X) \mathrm{E}(Y) \; .
\end{split}
$$