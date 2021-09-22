---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-09-22 09:20:00

title: "Characteristic function"
chapter: "General Theorems"
section: "Probability theory"
topic: "Probability functions"
definition: "Characteristic function"

sources:
  - authors: "Wikipedia"
    year: 2021
    title: "Characteristic function (probability theory)"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-09-22"
    url: "https://en.wikipedia.org/wiki/Characteristic_function_(probability_theory)#Definition"

def_id: "D159"
shortcut: "cf"
username: "JoramSoch"
---


**Definition:**

1) The characteristic function of a [random variable](/D/rvar) $X \in \mathbb{R}$ is

$$ \label{eq:cf-var}
\varphi_X(t) = \mathrm{E} \left[ e^{itX} \right], \quad t \in \mathbb{R} \; .
$$

2) The characteristic function of a [random vector](/D/rvec) $X \in \mathbb{R}^n$ is

$$ \label{eq:cf-vec}
\varphi_X(t) = \mathrm{E} \left[ e^{i t^\mathrm{T}X} \right], \quad t \in \mathbb{R}^n \; .
$$

3) The characteristic function of a [random matrix](/D/rmat) $X \in \mathbb{R}^{n \times p}$ is

$$ \label{eq:cf-mat}
\varphi_X(t) = \mathrm{E} \left[ e^{i \, \mathrm{tr} \left( t^\mathrm{T}X \right)} \right], \quad t \in \mathbb{R}^{n \times p} \; .
$$