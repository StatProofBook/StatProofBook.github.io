---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-02-27 21:33:00

title: "Posterior model probabilities in terms of log model evidences"
chapter: "Model Selection"
section: "Bayesian model selection"
topic: "Posterior model probability"
theorem: "Calculation from log model evidences"

sources:
  - authors: "Soch J, Allefeld C"
    year: 2018
    title: "MACS – a new SPM toolbox for model assessment, comparison and selection"
    in: "Journal of Neuroscience Methods"
    pages: "vol. 306, pp. 19-31, eq. 23"
    url: "https://www.sciencedirect.com/science/article/pii/S0165027018301468"
    doi: "10.1016/j.jneumeth.2018.05.017"

proof_id: "P66"
shortcut: "pmp-lme"
username: "JoramSoch"
---


**Theorem:** Let $m_1, \ldots, m_M$ be $M$ statistical models with [log model evidences](/D/lme) $\mathrm{LME}(m_1), \ldots, \mathrm{LME}(m_M)$. Then, the [posterior model probabilities](/D/pmp) are given by:

$$ \label{eq:PMP-LME}
p(m_i|y) = \frac{\exp[\mathrm{LME}(m_i)] \, p(m_i)}{\sum_{j=1}^{M} \exp[\mathrm{LME}(m_j)] \, p(m_j)}, \quad i = 1,\ldots,M \; ,
$$

where $p(m_i)$ are [prior](/D/prior) model probabilities.


**Proof:** The [posterior model probability](/P/pmp-der) can be derived as

$$ \label{eq:PMP-s1}
p(m_i|y) = \frac{p(y|m_i) \, p(m_i)}{\sum_{j=1}^{M} p(y|m_j) \, p(m_j)} \; .
$$

The definition of the [log model evidence](/D/lme)

$$ \label{eq:LME}
\mathrm{LME}(m) = \log p(y|m)
$$

can be exponentiated to then read

$$ \label{eq:ME}
\exp\left[ \mathrm{LME}(m) \right] = p(y|m)
$$

and applying \eqref{eq:ME} to \eqref{eq:PMP-s1}, we finally have:

$$ \label{eq:PMP-s2}
p(m_i|y) = \frac{\exp[\mathrm{LME}(m_i)] \, p(m_i)}{\sum_{j=1}^{M} \exp[\mathrm{LME}(m_j)] \, p(m_j)} \; .
$$