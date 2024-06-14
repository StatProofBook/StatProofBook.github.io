---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2024-06-14 14:45:06

title: "Log-likelihood ratio"
chapter: "General Theorems"
section: "Frequentist statistics"
topic: "Likelihood theory"
definition: "Log-likelihood ratio"

sources:
  - authors: "Wikipedia"
    year: 2024
    title: "Likelihood-ratio test"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2024-06-14"
    url: "https://en.wikipedia.org/wiki/Likelihood-ratio_test#Definition"

def_id: "D199"
shortcut: "llr"
username: "JoramSoch"
---


**Definition:** Let $m_0$ and $m_1$ be two [generative models](/D/gm) describing the same measured data $y$ using different model parameters $\theta_0 \in \Theta_0$ and $\theta_1 \in \Theta_1$. Then, the logarithmized quotient of the [maximized likelihood functions](/D/mle) of these two models is denoted as $\log \Lambda_{01}$ and is called the [log-likelihood](/D/llf) ratio of $m_0$ relative to $m_1$:

$$ \label{eq:llr}
\log \Lambda_{01}
= \log \frac{\operatorname*{max}_{\theta_0 \in \Theta_0} \mathcal{L}_{m_0}(\theta_0)}{\operatorname*{max}_{\theta_1 \in \Theta_1} \mathcal{L}_{m_1}(\theta_1)}
= \log p(y|\hat{\theta}_0,m_0) - \log p(y|\hat{\theta}_1,m_1) \; .
$$