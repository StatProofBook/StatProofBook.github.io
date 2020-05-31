---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-05-31 23:46:00

title: "Cumulant-generating function"
chapter: "General Theorems"
section: "Probability theory"
topic: "Probability functions"
definition: "Cumulant-generating function"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Cumulant"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-05-31"
    url: "https://en.wikipedia.org/wiki/Cumulant#Definition"

def_id: "D68"
shortcut: "cgf"
username: "JoramSoch"
---


**Definition:**

1) The cumulant-generating function of a [random variable](/D/rvar) $X \in \mathbb{R}$ is

$$ \label{eq:cgf-var}
K_X(t) = \log \mathrm{E} \left[ e^{tX} \right], \quad t \in \mathbb{R} \; .
$$

2) The cumulant-generating function of a [random vector](/D/rvec) $X \in \mathbb{R}^n$ is

$$ \label{eq:cgf-vec}
K_X(t) = \log \mathrm{E} \left[ e^{t^\mathrm{T}X} \right], \quad t \in \mathbb{R}^n \; .
$$