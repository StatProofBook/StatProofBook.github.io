---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-09-09 07:02:00

title: "Non-negativity of the Kullback-Leibler divergence"
chapter: "General Theorems"
section: "Information theory"
topic: "Kullback-Leibler divergence"
theorem: "Non-negativity"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Log sum inequality"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-09-09"
    url: "https://en.wikipedia.org/wiki/Log_sum_inequality#Applications"

proof_id: "P166"
shortcut: "kl-nonneg2"
username: "JoramSoch"
---


**Theorem:** The [Kullback-Leibler divergence](/D/kl) is always non-negative

$$ \label{eq:KL-nonneg}
\mathrm{KL}[P||Q] \geq 0
$$

with $\mathrm{KL}[P \vert \vert Q] = 0$, if and only if $P = Q$.


**Proof:** The discrete [Kullback-Leibler divergence](/D/kl) is defined as

$$ \label{eq:KL}
\mathrm{KL}[P||Q] = \sum_{x \in \mathcal{X}} p(x) \cdot \log \frac{p(x)}{q(x)} \; .
$$

The [log sum inequality](/P/logsum-ineq) states that

$$ \label{eq:logsum-ineq}
\sum_{i=1}^n a_i \, \log_c \frac{a_i}{b_i} \geq a \, \log_c \frac{a}{b} \; .
$$

where $a_1, \ldots, a_n$ and $b_1, \ldots, b_n$ be non-negative real numbers and $a = \sum_{i=1}^{n} a_i$ and $b = \sum_{i=1}^{n} b_i$. Because $p(x)$ and $q(x)$ are [probability mass functions](/D/pmf), such that

$$ \label{eq:p-q-pmf}
\begin{split}
p(x) \geq 0, \quad \sum_{x \in \mathcal{X}} p(x) &= 1 \quad \text{and} \\
q(x) \geq 0, \quad \sum_{x \in \mathcal{X}} q(x) &= 1 \; ,
\end{split}
$$

theorem \eqref{eq:KL-nonneg} is simply a special case of \eqref{eq:logsum-ineq}, i.e.

$$ \label{eq:KL-nonneg-qed}
\mathrm{KL}[P||Q] \overset{\eqref{eq:KL}}{=} \sum_{x \in \mathcal{X}} p(x) \cdot \log \frac{p(x)}{q(x)} \overset{\eqref{eq:logsum-ineq}}{\geq} 1 \, \log \frac{1}{1} = 0 \; .
$$