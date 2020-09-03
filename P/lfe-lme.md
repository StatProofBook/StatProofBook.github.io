---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-02-27 21:16:00

title: "Log family evidences in terms of log model evidences"
chapter: "Model Selection"
section: "Bayesian model selection"
topic: "Log family evidence"
theorem: "Calculation from log model evidences"

sources:
  - authors: "Soch J, Allefeld C"
    year: 2018
    title: "MACS – a new SPM toolbox for model assessment, comparison and selection"
    in: "Journal of Neuroscience Methods"
    pages: "vol. 306, pp. 19-31, eq. 16"
    url: "https://www.sciencedirect.com/science/article/pii/S0165027018301468"
    doi: "10.1016/j.jneumeth.2018.05.017"

proof_id: "P65"
shortcut: "lfe-lme"
username: "JoramSoch"
---


**Theorem:** Let $m_1, \ldots, m_M$ be $M$ statistical models with [log model evidences](/D/lme) $\mathrm{LME}(m_1), \ldots, \mathrm{LME}(m_M)$ and belonging to $F$ mutually exclusive model families $f_1, \ldots, f_F$. Then, the [log family evidences](/D/lfe) are given by:

$$ \label{eq:LFE-LME}
\mathrm{LFE}(f_j) = \log \sum_{m_i \in f_j} \left[ \exp[\mathrm{LME}(m_i)] \cdot p(m_i|f_j) \right], \quad j = 1, \ldots, F,
$$

where $p(m_i \vert f_j)$ are within-[family](/D/lfe) [prior](/D/prior) [model](/D/gm) [probabilities](/D/prob).


**Proof:** Let us consider the (unlogarithmized) family evidence $p(y \vert f_j)$. According to the [law of marginal probability](/D/prob-marg), this conditional probability is given by

$$ \label{eq:FE-ME-s1}
p(y|f_j) = \sum_{m_i \in f_j} \left[ p(y|m_i,f_j) \cdot p(m_i|f_j) \right] \; .
$$

Because model families are mutually exclusive, it holds that $p(y \vert m_i,f_j) = p(y \vert m_i)$, such that

$$ \label{eq:FE-ME-s2}
p(y|f_j) = \sum_{m_i \in f_j} \left[ p(y|m_i) \cdot p(m_i|f_j) \right] \; .
$$

Logarithmizing transforms the family evidence $p(y \vert f_j)$ into the log family evidence $\mathrm{LFE}(f_j)$:

$$ \label{eq:LFE-LME-s1}
\mathrm{LFE}(f_j) = \log \sum_{m_i \in f_j} \left[ p(y|m_i) \cdot p(m_i|f_j) \right] \; .
$$

The definition of the [log model evidence](/D/lme)

$$ \label{eq:LME}
\mathrm{LME}(m) = \log p(y|m)
$$

can be exponentiated to then read

$$ \label{eq:ME}
\exp\left[ \mathrm{LME}(m) \right] = p(y|m)
$$

and applying \eqref{eq:ME} to \eqref{eq:LFE-LME-s1}, we finally have:

$$ \label{eq:LFE-LME-s2}
\mathrm{LFE}(f_j) = \log \sum_{m_i \in f_j} \left[ \exp[\mathrm{LME}(m_i)] \cdot p(m_i|f_j) \right] \; .
$$