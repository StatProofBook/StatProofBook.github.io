---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-11-25 07:28:00

title: "Uniform-prior log model evidence"
chapter: "Model Selection"
section: "Bayesian model selection"
topic: "Log model evidence"
definition: "Uniform-prior log model evidence"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Lindley's paradox"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-11-25"
    url: "https://en.wikipedia.org/wiki/Lindley%27s_paradox#Bayesian_approach"

def_id: "D113"
shortcut: "uplme"
username: "JoramSoch"
---


**Definition:** Assume a [generative model](/D/gm) $m$ with [likelihood function](/D/lf) $p(y \vert \theta, m)$ and a [uniform](/D/prior-uni) [prior distribution](/D/prior) $p_{\mathrm{uni}}(\theta \vert m)$. Then, the [log model evidence](/D/lme) of this model is called "log model evidence with uniform prior" or "uniform-prior log model evidence" (upLME):

$$ \label{eq:upLME}
\mathrm{upLME}(m) = \log \int p(y \vert \theta, m) \, p_{\mathrm{uni}}(\theta \vert m) \, \mathrm{d}\theta \; .
$$