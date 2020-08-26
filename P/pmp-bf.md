---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-03-03 13:13:00

title: "Posterior model probabilities in terms of Bayes factors"
chapter: "Model Selection"
section: "Bayesian model selection"
topic: "Posterior model probability"
theorem: "Calculation from Bayes factors"

sources:
  - authors: "Hoeting JA, Madigan D, Raftery AE, Volinsky CT"
    year: 1999
    title: "Bayesian Model Averaging: A Tutorial"
    in: "Statistical Science"
    pages: "vol. 14, no. 4, pp. 382–417, eq. 9"
    url: "https://projecteuclid.org/euclid.ss/1009212519"
    doi: "10.1214/ss/1009212519"

proof_id: "P74"
shortcut: "pmp-bf"
username: "JoramSoch"
---


**Theorem:** Let $m_0, m_1, \ldots, m_M$ be $M+1$ statistical models with [model evidences](/D/lme) $p(y \vert m_0), p(y \vert m_1), \ldots, p(y \vert m_M)$. Then, the [posterior model probabilities](/D/pmp) of the models $m_1, \ldots, m_M$ are given by

$$ \label{eq:PMP-BF}
p(m_i|y) = \frac{\mathrm{BF}_{i,0} \cdot \alpha_i}{\sum_{j=1}^{M} \mathrm{BF}_{j,0} \cdot \alpha_j}, \quad i = 1,\ldots,M \; ,
$$

where $\mathrm{BF}_{i,0}$ is the [Bayes factor](/D/bf) comparing model $m_i$ with $m_0$ and $\alpha_i$ is the [prior](/D/prior) [odds ratio](/D/odds) of model $m_i$ against $m_0$.


**Proof:** Define the [Bayes factor](/D/bf) for $m_i$

$$ \label{eq:BF-i0}
\mathrm{BF}_{i,0} = \frac{p(y|m_i)}{p(y|m_0)}
$$

and prior odds ratio of $m_i$ against $m_0$

$$ \label{eq:prior-i0}
\alpha_i = \frac{p(m_i)}{p(m_0)} \; .
$$

The [posterior model probability](/P/pmp-der) of $m_i$ is given by

$$ \label{eq:PMP-s1}
p(m_i|y) = \frac{p(y|m_i) \cdot p(m_i)}{\sum_{j=1}^{M} p(y|m_j) \cdot p(m_j)} \; .
$$

Now applying \eqref{eq:BF-i0} and \eqref{eq:prior-i0} to \eqref{eq:PMP-s1}, we have

$$ \label{eq:PMP-s2}
\begin{split}
p(m_i|y) &= \frac{ \mathrm{BF}_{i,0} \, p(y|m_0) \cdot \alpha_i \, p(m_0)}{\sum_{j=1}^{M} \mathrm{BF}_{j,0} \, p(y|m_0) \cdot \alpha_j \, p(m_0)} \\
&= \frac{\left[ p(y|m_0) \, p(m_0) \right] \mathrm{BF}_{i,0} \cdot \alpha_i}{\left[ p(y|m_0) \, p(m_0) \right] \sum_{j=1}^{M} \mathrm{BF}_{j,0} \cdot \alpha_j} \; ,
\end{split}
$$

such that

$$ \label{eq:PMP-BF-qed}
p(m_i|y)= \frac{\mathrm{BF}_{i,0} \cdot \alpha_i}{\sum_{j=1}^{M} \mathrm{BF}_{j,0} \cdot \alpha_j} \; .
$$