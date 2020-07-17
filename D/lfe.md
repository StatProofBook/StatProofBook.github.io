---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-07-13 22:31:00

title: "Log family evidence"
chapter: "Model Selection"
section: "Bayesian model selection"
topic: "Log family evidence"
definition: "Definition"

sources:
  - authors: "Soch J, Allefeld C"
    year: 2018
    title: "MACS – a new SPM toolbox for model assessment, comparison and selection"
    in: "Journal of Neuroscience Methods"
    pages: "vol. 306, pp. 19-31, eq. 16"
    url: "https://www.sciencedirect.com/science/article/pii/S0165027018301468"
    doi: "10.1016/j.jneumeth.2018.05.017"

def_id: "D80"
shortcut: "lfe"
username: "JoramSoch"
---


**Definition:** Let $f$ be a family of $M$ [generative models](/D/gm) $m_1, \ldots, m_M$, such that the following statement holds true:

$$ \label{eq:fam}
f \Leftrightarrow m_1 \vee \ldots \vee m_M \; .
$$

Then, the family evidence of $f$ is the weighted average of the [model evidences](/D/ml) of $m_1, \ldots, m_M$ where the weights are the within-family [prior model probabilities](/D/prior)

$$ \label{eq:fe}
p(y|f) = \sum_{i=1}^M p(y|m_i) \, p(m_i|f) \; .
$$

The log family evidence is given by the logarithm of the family evidence:

$$ \label{eq:lfe}
\mathrm{LFE}(f) = \log p(y|f) = \log \sum_{i=1}^M p(y|m_i) \, p(m_i|f) \; .
$$