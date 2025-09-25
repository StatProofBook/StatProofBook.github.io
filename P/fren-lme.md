---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2025-09-25 11:24:36

title: "The variational free energy is a lower bound on the log model evidence"
chapter: "General Theorems"
section: "Bayesian statistics"
topic: "Bayesian inference"
theorem: "Free energy is lower bound on log model evidence"

sources:
  - authors: "Zeidman et al."
    year: 2023
    title: "A primer on Variational Laplace (VL)"
    in: "NeuroImage"
    pages: "vol. 279, art. 120310, pp. 4-5, eqs. 9-11"
    url: "https://www.sciencedirect.com/science/article/pii/S1053811923004615"
    doi: "10.1016/j.neuroimage.2023.120310"

proof_id: "P517"
shortcut: "fren-lme"
username: "JoramSoch"
---


**Theorem:** Let $m$ be a [generative model](/D/gm) with [likelihood function](/D/lf) $p(y \vert \theta,m) = p(y \vert \theta)$ and [prior distribution](/D/prior) $p(\theta \vert m) = p(\theta)$. Then, under a [variational Bayesian](/D/vb) treatment using the [approximate posterior](/D/vb) distribution $q(\theta \vert m) = q(\theta) \approx p(\theta \vert y)$, the [variational free energy](/D/vblme) is a lower bound on the [log model evidence](/D/lme):

$$ \label{eq:vb-fe-lme}
\mathrm{F}[q(\theta)] \leq \log p(y) = \log \int_{\Theta} p(y,\theta \vert m) \, \mathrm{d}\theta \; .
$$


**Proof:** Using a [decomposition of the variational free energy](/P/fren-dec), it can be shown that the free energy is equal to the difference between the [log model evidence](/D/lme) and the [Kullback-Leibler divergence](/D/kl) of approximate from true posterior distribution:

$$ \label{eq:vb-fe-dec}
\mathrm{F}[q(\theta)] = \log p(y) - \mathrm{KL}[q(\theta) || p(\theta \vert y)]
$$

Since the [KL divergence is zero or positive for any two distributions](/P/kl-nonneg3)

$$ \label{eq:kl-nonneg}
\mathrm{KL}[P||Q] \geq 0 \; ,
$$

the free energy must be smaller than or equal to the log model evidence:

$$ \label{eq:vb-fe-lme-qed}
\mathrm{F}[q(\theta)] \leq \log p(y) \; .
$$
