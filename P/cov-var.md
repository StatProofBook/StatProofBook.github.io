---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-09-26 12:08:00

title: "Self-covariance equals variance"
chapter: "General Theorems"
section: "Probability theory"
topic: "Covariance"
theorem: "Self-covariance"

sources:
  - authors: "Wikipedia"
    year: 2022
    title: "Covariance"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2022-09-26"
    url: "https://en.wikipedia.org/wiki/Covariance#Covariance_with_itself"

proof_id: "P352"
shortcut: "cov-var"
username: "JoramSoch"
---


**Theorem:** The [covariance](/D/cov) of a [random variable](/D/rvar) with itself is equal to the [variance](/D/var):

$$ \label{eq:cov-var}
\mathrm{Cov}(X,X) = \mathrm{Var}(X) \; .
$$


**Proof:** The [covariance](/D/cov) of [random variables](/D/rvar) $X$ and $Y$ is defined as:

$$ \label{eq:cov}
\mathrm{Cov}(X,Y) = \mathrm{E}\left[ (X-\mathrm{E}[X]) (Y-\mathrm{E}[Y]) \right] \; .
$$

Inserting $X$ for $Y$ in \eqref{eq:cov}, the result is the [variance](/D/var) of $X$:

$$ \label{eq:cov-var-qed}
\begin{split}
\mathrm{Cov}(X,X) &\overset{\eqref{eq:cov}}{=} \mathrm{E}\left[ (X-\mathrm{E}[X]) (X-\mathrm{E}[X]) \right] \\
&= \mathrm{E}\left[ (X-\mathrm{E}[X])^2 \right] \\
&= \mathrm{Var}(X) \; .
\end{split}
$$