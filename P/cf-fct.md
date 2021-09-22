---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-09-22 09:12:00

title: "Characteristic function of a function of a random variable"
chapter: "General Theorems"
section: "Probability theory"
topic: "Probability functions"
theorem: "Characteristic function of arbitrary function"

sources:
  - authors: "Taboga, Marco"
    year: 2017
    title: "Functions of random vectors and their distribution"
    in: "Lectures on probability and mathematical statistics"
    pages: "retrieved on 2021-09-22"
    url: "https://www.statlect.com/fundamentals-of-probability/functions-of-random-vectors"

proof_id: "P259"
shortcut: "cf-fct"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) with the [expected value](/D/mean) function $\mathrm{E}_X[\cdot]$. Then, the [characteristic function](/D/cf) of $Y = g(X)$ is equal to

$$ \label{eq:cf-fct}
\varphi_Y(t) = \mathrm{E}_X \left[ \mathrm{exp}(it \, g(X)) \right] \; .
$$


**Proof:** The [characteristic function](/D/cf) is defined as

$$ \label{eq:cf}
\varphi_Y(t) = \mathrm{E} \left[ \mathrm{exp}(it \, Y) \right] \; .
$$

Due of the [law of the unconscious statistician](/P/mean-lotus)

$$ \label{eq:mean-lotus}
\begin{split}
\mathrm{E}[g(X)] &= \sum_{x \in \mathcal{X}} g(x) f_X(x) \\
\mathrm{E}[g(X)] &= \int_{\mathcal{X}} g(x) f_X(x) \, \mathrm{d}x \; ,
\end{split}
$$

$Y = g(X)$ can simply be substituted into \eqref{eq:cf} to give

$$ \label{eq:cf-fct-qed}
\varphi_Y(t) = \mathrm{E}_X \left[ \mathrm{exp}(it \, g(X)) \right] \; .
$$