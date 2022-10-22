---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-10-20 09:43:00

title: "Model evidence"
chapter: "Model Selection"
section: "Bayesian model selection"
topic: "Model evidence"
definition: "Definition"

sources:
  - authors: "Penny WD"
    year: 2012
    title: "Comparing Dynamic Causal Models using AIC, BIC and Free Energy"
    in: "NeuroImage"
    pages: "vol. 59, iss. 2, pp. 319-330, eq. 15"
    url: "https://www.sciencedirect.com/science/article/pii/S1053811911008160"
    doi: "10.1016/j.neuroimage.2011.07.039"

def_id: "D179"
shortcut: "me"
username: "JoramSoch"
---


**Definition:** Let $m$ be a [generative model](/D/gm) with [likelihood function](/D/lf) $p(y \vert \theta, m)$ and [prior distribution](/D/prior) $p(\theta \vert m)$. Then, the model evidence (ME) of $m$ is defined as the [marginal likelihood](/D/ml) of this model:

$$ \label{eq:ME}
\mathrm{ME}(m) = p(y|m) \; .
$$