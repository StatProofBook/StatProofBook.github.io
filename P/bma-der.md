---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-08-03 22:05:00

title: "Derivation of Bayesian model averaging"
chapter: "Model Selection"
section: "Bayesian model selection"
topic: "Bayesian model averaging"
theorem: "Derivation"

sources:

proof_id: "P143"
shortcut: "bma-der"
username: "JoramSoch"
---


**Theorem:** Let $m_1, \ldots, m_M$ be $M$ [statistical models](/D/fpm) with [posterior model probabilities](/D/pmp) $p(m_1 \vert y), \ldots, p(m_M \vert y)$ and [posterior distributions](/D/post) $p(\theta \vert y, m_1), \ldots, p(\theta \vert y, m_M)$. Then, the [marginal](/D/dist-marg) [posterior](/D/post) [density](/D/pdf), [conditional](/D/prob-cond) on the measured data $y$, but [unconditional](/D/prob-marg) on the modelling approach $m$, is given by:

$$ \label{eq:BMA}
p(\theta|y) = \sum_{i=1}^{M} p(\theta|y,m_i) \cdot p(m_i|y) \; .
$$


**Proof:** Using the [law of marginal probability](/D/prob-marg), the probability distribution of the shared parameters $\theta$ [conditional](/D/prob-cond) on the measured data $y$ can be obtained by [marginalizing](/D/prob-marg) over the discrete [random variable](/D/rvar) model $m$:

$$ \label{eq:BMA-s1}
p(\theta|y) = \sum_{i=1}^{M} p(\theta,m_i|y) \; .
$$

Using the [law of the conditional probability](/D/prob-cond), the summand can be expanded to give

$$ \label{eq:BMA-s2}
p(\theta|y) = \sum_{i=1}^{M} p(\theta|y,m_i) \cdot p(m_i|y)
$$

where $p(\theta \vert y,m_i)$ is the [posterior distribution](/D/post) of the $i$-th model and $p(m_i \vert y)$ happens to be the [posterior probability](/D/pmp) of the $i$-th model.