---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-05-31 23:43:00

title: "Non-negativity of the Kullback-Leibler divergence"
chapter: "General Theorems"
section: "Information theory"
topic: "Kullback-Leibler divergence"
theorem: "Non-negativity"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Kullback-Leibler divergence"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-05-31"
    url: "https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence#Properties"

proof_id: "P117"
shortcut: "kl-nonneg"
username: "JoramSoch"
---


**Theorem:** The [Kullback-Leibler divergence](/D/kl) is always non-negative

$$ \label{eq:KL-nonneg}
\mathrm{KL}[P||Q] \geq 0
$$

with $\mathrm{KL}[P \vert \vert Q] = 0$, if and only if $P = Q$.


**Proof:** The discrete [Kullback-Leibler divergence](/D/kl) is defined as

$$ \label{eq:KL}
\mathrm{KL}[P||Q] = \sum_{x \in \mathcal{X}} p(x) \cdot \log \frac{p(x)}{q(x)}
$$

which can be reformulated into

$$ \label{eq:KL-dev}
\mathrm{KL}[P||Q] = \sum_{x \in \mathcal{X}} p(x) \cdot \log p(x) - \sum_{x \in \mathcal{X}} p(x) \cdot \log q(x) \; .
$$

[Gibbs' inequality](/P/gibbs-ineq) states that the [entropy](/D/ent) of a probability distribution is always less than or equal to the [cross-entropy](/D/ent-cross) with another probability distribution – with equality only if the distributions are identical –,

$$ \label{eq:Gibbs-ineq}
- \sum_{i=1}^n p(x_i) \, \log p(x_i) \leq - \sum_{i=1}^n p(x_i) \, \log q(x_i)
$$

which can be reformulated into

$$ \label{eq:Gibbs-ineq-dev}
\sum_{i=1}^n p(x_i) \, \log p(x_i) - \sum_{i=1}^n p(x_i) \, \log q(x_i) \geq 0 \; .
$$

Applying \eqref{eq:Gibbs-ineq-dev} to \eqref{eq:KL-dev}, this proves equation \eqref{eq:KL-nonneg}.