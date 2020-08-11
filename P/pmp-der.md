---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-07-28 03:58:00

title: "Derivation of the posterior model probability"
chapter: "Model Selection"
section: "Bayesian model selection"
topic: "Posterior model probability"
theorem: "Derivation"

sources:

proof_id: "P139"
shortcut: "pmp-der"
username: "JoramSoch"
---


**Theorem:** Let there be a set of [generative models](/D/gm) $m_1, \ldots, m_M$ with [model evidences](/D/ml) $p(y \vert m_1), \ldots, p(y \vert m_M)$ and [prior probabilities](/D/prior)  $p(m_1), \ldots, p(m_M)$. Then, the [posterior probability](/D/pmp) of model $m_i$ is given by

$$ \label{eq:PMP}
p(m_i|y) = \frac{p(y|m_i) \, p(m_i)}{\sum_{j=1}^{M} p(y|m_j) \, p(m_j)}, \; i = 1, \ldots, M \; .
$$


**Proof:** From [Bayes' theorem](/P/bayes-th), the [posterior model probability](/D/pmp) of the $i$-th model can be derived as

$$ \label{eq:PMP-s1}
p(m_i|y) = \frac{p(y|m_i) \, p(m_i)}{p(y)} \; .
$$

Using the [law of marginal probability](/D/prob-marg), the denominator can be rewritten, such that

$$ \label{eq:PMP-s2}
p(m_i|y) = \frac{p(y|m_i) \, p(m_i)}{\sum_{j=1}^{M} p(y,m_j)} \; .
$$

Finally, using the [law of conditional probability](/D/prob-cond), we have

$$ \label{eq:PMP-s3}
p(m_i|y) = \frac{p(y|m_i) \, p(m_i)}{\sum_{j=1}^{M} p(y|m_j) \, p(m_j)} \; .
$$