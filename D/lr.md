---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2024-06-14 14:44:50

title: "Likelihood ratio"
chapter: "General Theorems"
section: "Frequentist statistics"
topic: "Likelihood theory"
definition: "Likelihood ratio"

sources:
  - authors: "Wikipedia"
    year: 2024
    title: "Neyman-Pearson lemma"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2024-06-14"
    url: "https://en.wikipedia.org/wiki/Neyman%E2%80%93Pearson_lemma#Example"

def_id: "D198"
shortcut: "lr"
username: "JoramSoch"
---


**Definition:** Let $m_0$ and $m_1$ be two [generative models](/D/gm) describing the same measured data $y$ using different model parameters $\theta_0 \in \Theta_0$ and $\theta_1 \in \Theta_1$. Then, the quotient of the [maximized likelihood functions](/D/mle) of these two models is denoted as $\Lambda_{01}$ and is called the [likelihood](/D/lf) ratio of $m_0$ relative to $m_1$:

$$ \label{eq:lr}
\Lambda_{01}
= \frac{\operatorname*{max}_{\theta_0 \in \Theta_0} \mathcal{L}_{m_0}(\theta_0)}{\operatorname*{max}_{\theta_1 \in \Theta_1} \mathcal{L}_{m_1}(\theta_1)}
= \frac{p(y|\hat{\theta}_0,m_0)}{p(y|\hat{\theta}_1,m_1)} \; .
$$