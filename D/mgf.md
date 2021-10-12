---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-01-22 10:58:00

title: "Moment-generating function"
chapter: "General Theorems"
section: "Probability theory"
topic: "Probability functions"
definition: "Moment-generating function"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Moment-generating function"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-01-22"
    url: "https://en.wikipedia.org/wiki/Moment-generating_function#Definition"
  - authors: "Taboga, Marco"
    year: 2017
    title: "Joint moment generating function"
    in: "Lectures on probability and mathematical statistics"
    pages: "retrieved on 2021-10-07"
    url: "https://www.statlect.com/fundamentals-of-probability/joint-moment-generating-function"

def_id: "D2"
shortcut: "mgf"
username: "JoramSoch"
---


**Definition:**

1) The moment-generating function of a [random variable](/D/rvar) $X \in \mathbb{R}$ is

$$ \label{eq:mgf-var}
M_X(t) = \mathrm{E} \left[ e^{tX} \right], \quad t \in \mathbb{R} \; .
$$

2) The moment-generating function of a [random vector](/D/rvec) $X \in \mathbb{R}^n$ is

$$ \label{eq:mgf-vec}
M_X(t) = \mathrm{E} \left[ e^{t^\mathrm{T}X} \right], \quad t \in \mathbb{R}^n \; .
$$