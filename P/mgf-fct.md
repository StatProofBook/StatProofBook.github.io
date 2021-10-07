---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-09-22 09:00:00

title: "Moment-generating function of a function of a random variable"
chapter: "General Theorems"
section: "Probability theory"
topic: "Probability functions"
theorem: "Moment-generating function of arbitrary function"

sources:
  - authors: "Taboga, Marco"
    year: 2017
    title: "Functions of random vectors and their distribution"
    in: "Lectures on probability and mathematical statistics"
    pages: "retrieved on 2021-09-22"
    url: "https://www.statlect.com/fundamentals-of-probability/functions-of-random-vectors"

proof_id: "P260"
shortcut: "mgf-fct"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) with the [expected value](/D/mean) function $\mathrm{E}_X[\cdot]$. Then, the [moment-generating function](/D/mgf) of $Y = g(X)$ is equal to

$$ \label{eq:mgf-fct}
M_Y(t) = \mathrm{E}_X \left[ \mathrm{exp}(t \, g(X)) \right] \; .
$$


**Proof:** The [moment-generating function](/D/mgf) is defined as

$$ \label{eq:mgf}
M_Y(t) = \mathrm{E} \left[ \mathrm{exp}(t \, Y) \right] \; .
$$

Due of the [law of the unconscious statistician](/P/mean-lotus)

$$ \label{eq:mean-lotus}
\begin{split}
\mathrm{E}[g(X)] &= \sum_{x \in \mathcal{X}} g(x) f_X(x) \\
\mathrm{E}[g(X)] &= \int_{\mathcal{X}} g(x) f_X(x) \, \mathrm{d}x \; ,
\end{split}
$$

$Y = g(X)$ can simply be substituted into \eqref{eq:mgf} to give

$$ \label{eq:mgf-fct-qed}
M_Y(t) = \mathrm{E}_X \left[ \mathrm{exp}(t \, g(X)) \right] \; .
$$