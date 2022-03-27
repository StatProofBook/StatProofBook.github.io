---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-03-27 23:56:00

title: "Confidence interval"
chapter: "General Theorems"
section: "Estimation theory"
topic: "Interval estimates"
definition: "Confidence interval"

sources:
  - authors: "Wikipedia"
    year: 2022
    title: "Confidence interval"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2022-03-27"
    url: "https://en.wikipedia.org/wiki/Confidence_interval#Definition"

def_id: "D174"
shortcut: "ci"
username: "JoramSoch"
---


**Definition:** Let $y$ be a [random sample](/D/samp) from a [probability distributions](/D/dist) governed by a [parameter](/D/para) of interest $\theta$ and quantities not of interest $\varphi$. A confidence interval for $\theta$ is defined as an interval $[u(y), v(y)]$ determined by the [random variables](/D/rvar) $u(y)$ and $v(y)$ with the property

$$ \label{eq:ci}
\mathrm{Pr}(u(y) < \theta < v(y) \, \vert \, \theta, \varphi) = \gamma \quad \text{for all} \quad (\theta, \varphi) \; .
$$

where $\gamma = 1 - \alpha$ is called the confidence level.