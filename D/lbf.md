---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-07-22 07:02:00

title: "Log Bayes factor"
chapter: "Model Selection"
section: "Bayesian model selection"
topic: "Log Bayes factor"
definition: "Definition"

sources:
  - authors: "Soch J, Allefeld C"
    year: 2018
    title: "MACS – a new SPM toolbox for model assessment, comparison and selection"
    in: "Journal of Neuroscience Methods"
    pages: "vol. 306, pp. 19-31, eq. 18"
    url: "https://www.sciencedirect.com/science/article/pii/S0165027018301468"
    doi: "10.1016/j.jneumeth.2018.05.017"

def_id: "D84"
shortcut: "lbf"
username: "JoramSoch"
---


**Definition:** Let there be two [generative models](/D/gm) $m_1$ and $m_2$ which are mutually exclusive, but not necessarily collectively exhaustive:

$$ \label{eq:m12}
\neg (m_1 \land m_2)
$$

Then, the Bayes factor in favor of $m_1$ and against $m_2$ is the ratio of the [model evidences](/D/ml) of $m_1$ and $m_2$:

$$ \label{eq:bf}
\mathrm{BF}_{12} = \frac{p(y|m_1)}{p(y|m_2)} \; .
$$

The log Bayes factor is given by the logarithm of the Bayes factor:

$$ \label{eq:lbf}
\mathrm{LBF}_{12} = \log \mathrm{BF}_{12} = \log \frac{p(y|m_1)}{p(y|m_2)} \; .
$$