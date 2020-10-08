---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-02-27 21:58:00

title: "Bayesian model averaging in terms of log model evidences"
chapter: "Model Selection"
section: "Bayesian model selection"
topic: "Bayesian model averaging"
theorem: "Calculation from log model evidences"

sources:
  - authors: "Soch J, Allefeld C"
    year: 2018
    title: "MACS – a new SPM toolbox for model assessment, comparison and selection"
    in: "Journal of Neuroscience Methods"
    pages: "vol. 306, pp. 19-31, eq. 25"
    url: "https://www.sciencedirect.com/science/article/pii/S0165027018301468"
    doi: "10.1016/j.jneumeth.2018.05.017"

proof_id: "P67"
shortcut: "bma-lme"
username: "JoramSoch"
---


**Theorem:** Let $m_1, \ldots, m_M$ be $M$ [statistical models](/D/fpm) describing the same measured data $y$ with [log model evidences](/D/lme) $\mathrm{LME}(m_1), \ldots, \mathrm{LME}(m_M)$ and shared model parameters $\theta$. Then, [Bayesian model averaging](/D/bma) determines the following posterior distribution over $\theta$:

$$ \label{eq:BMA-LME}
p(\theta|y) = \sum_{i=1}^{M} p(\theta|m_i,y) \cdot \frac{\exp[\mathrm{LME}(m_i)] \, p(m_i)}{\sum_{j=1}^{M} \exp[\mathrm{LME}(m_j)] \, p(m_j)} \; ,
$$

where $p(\theta \vert m_i,y)$ is the posterior distributions over $\theta$ obtained using $m_i$.


**Proof:** According to the [law of marginal probability](/D/prob-marg), the probability of the shared parameters $\theta$ conditional on the measured data $y$ [can be obtained](/P/bma-der) by marginalizing over the discrete variable model $m$:

$$ \label{eq:BMA-PMP}
p(\theta|y) = \sum_{i=1}^{M} p(\theta|m_i,y) \cdot p(m_i|y) \; ,
$$

where $p(m_i \vert y)$ is the [posterior probability](/D/pmp) of the $i$-th model. One can express [posterior model probabilities in terms of log model evidences](/P/pmp-lme) as

$$ \label{eq:PMP-LME}
p(m_i|y) = \frac{\exp[\mathrm{LME}(m_i)] \, p(m_i)}{\sum_{j=1}^{M} \exp[\mathrm{LME}(m_j)] \, p(m_j)}
$$

and by plugging \eqref{eq:PMP-LME} into \eqref{eq:BMA-PMP}, one arrives at \eqref{eq:BMA-LME}.