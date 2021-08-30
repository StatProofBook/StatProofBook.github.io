---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-08-30 09:14:00

title: "Probability mass function of a sum of independent discrete random variables"
chapter: "General Theorems"
section: "Probability theory"
topic: "Probability functions"
theorem: "Probability mass function of sum of independents"

sources:
  - authors: "Taboga, Marco"
    year: 2017
    title: "Sums of independent random variables"
    in: "Lectures on probability and mathematical statistics"
    pages: "retrieved on 2021-08-30"
    url: "https://www.statlect.com/fundamentals-of-probability/sums-of-independent-random-variables"

proof_id: "P257"
shortcut: "pmf-sumind"
username: "JoramSoch"
---


**Theorem:** Let $X$ and $Y$ be two [independent](/D/ind) [discrete](/D/rvar-disc) [random variables](/D/rvar) with possible values $\mathcal{X}$ and $\mathcal{Y}$ and let $Z = X + Y$. Then, the [probability mass function](/D/pmf) of $Z$ is given by

$$ \label{eq:pmf-sumind}
\begin{split}
f_Z(z) &= \sum_{y \in \mathcal{Y}} f_X(z-y) f_Y(y)  \\
\text{or} \quad f_Z(z) &= \sum_{x \in \mathcal{X}} f_Y(z-x) f_X(x)
\end{split}
$$

where $f_X(x)$, $f_Y(y)$ and $f_Z(z)$ are the [probability mass functions](/D/pmf) of $X$, $Y$ and $Z$.


**Proof:** Using the definition of the [probability mass function](/D/pmf) and the [expected value](/D/mean), the first equation can be derived as follows:

$$ \label{eq:pmf-sumind-qed}
\begin{split}
f_Z(z) &= \mathrm{Pr}(Z = z) \\
&= \mathrm{Pr}(X + Y = z) \\
&= \mathrm{Pr}(X = z - Y) \\
&= \mathrm{E} \left[ \mathrm{Pr}(X = z - Y \vert Y = y) \right] \\
&= \mathrm{E} \left[ \mathrm{Pr}(X = z - Y) \right] \\
&= \mathrm{E} \left[ f_X(z-Y) \right] \\
&= \sum_{y \in \mathcal{Y}} f_X(z-y) f_Y(y) \; .
\end{split}
$$

Note that the third-last transition is justified by the fact that $X$ and $Y$ are [independent](/D/ind), such that [conditional probabilities are equal to marginal probabilities](/P/prob-ind). The second equation can be derived by switching $X$ and $Y$.