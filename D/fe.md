---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-10-20 09:57:00

title: "Family evidence"
chapter: "Model Selection"
section: "Bayesian model selection"
topic: "Family evidence"
definition: "Definition"

sources:
  - authors: "Soch J, Allefeld C"
    year: 2018
    title: "MACS – a new SPM toolbox for model assessment, comparison and selection"
    in: "Journal of Neuroscience Methods"
    pages: "vol. 306, pp. 19-31, eq. 16"
    url: "https://www.sciencedirect.com/science/article/pii/S0165027018301468"
    doi: "10.1016/j.jneumeth.2018.05.017"

def_id: "D180"
shortcut: "fe"
username: "JoramSoch"
---


**Definition:** Let $f$ be a family of $M$ [generative models](/D/gm) $m_1, \ldots, m_M$, such that the following statement holds true:

$$ \label{eq:fam}
f \Leftrightarrow m_1 \vee \ldots \vee m_M \; .
$$

Then, the family evidence (FE) of $f$ is defined as the [marginal probability](/D/prob-marg) relative to the [model evidences](/D/me) $p(y \vert m_i), conditional only on $f$:

$$ \label{eq:fe}
\mathrm{FE}(f) = p(y|f) \; .
$$