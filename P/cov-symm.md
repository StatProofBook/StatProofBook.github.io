---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-09-26 12:14:00

title: "Symmetry of the covariance"
chapter: "General Theorems"
section: "Probability theory"
topic: "Covariance"
theorem: "Symmetry"

sources:
  - authors: "Wikipedia"
    year: 2022
    title: "Covariance"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2022-09-26"
    url: "https://en.wikipedia.org/wiki/Covariance#Covariance_of_linear_combinations"

proof_id: "P353"
shortcut: "cov-symm"
username: "JoramSoch"
---


**Theorem:** The [covariance](/D/cov) of two [random variables](/D/rvar) is a symmetric function:

$$ \label{eq:cov-symm}
\mathrm{Cov}(X,Y) = \mathrm{Cov}(Y,X) \; .
$$


**Proof:** The [covariance](/D/cov) of [random variables](/D/rvar) $X$ and $Y$ is defined as:

$$ \label{eq:cov}
\mathrm{Cov}(X,Y) = \mathrm{E}\left[ (X-\mathrm{E}[X]) (Y-\mathrm{E}[Y]) \right] \; .
$$

Switching $X$ and $Y$ in \eqref{eq:cov}, we can easily see:

$$ \label{eq:cov-symm-qed}
\begin{split}
\mathrm{Cov}(Y,X) &\overset{\eqref{eq:cov}}{=} \mathrm{E}\left[ (Y-\mathrm{E}[Y]) (X-\mathrm{E}[X]) \right] \\
&= \mathrm{E}\left[ (X-\mathrm{E}[X]) (Y-\mathrm{E}[Y]) \right] \\
&= \mathrm{Cov}(X,Y) \; .
\end{split}
$$