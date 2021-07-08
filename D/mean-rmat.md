---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-07-08 08:42:00

title: "Expected value of a random matrix"
chapter: "General Theorems"
section: "Probability theory"
topic: "Expected value"
definition: "Expected value of a random matrix"

sources:
  - authors: "Taboga, Marco"
    year: 2017
    title: "Expected value"
    in: "Lectures on probability theory and mathematical statistics"
    pages: "retrieved on 2021-07-08"
    url: "https://www.statlect.com/fundamentals-of-probability/expected-value#hid13"

def_id: "D155"
shortcut: "mean-rmat"
username: "JoramSoch"
---


**Definition:** Let $X$ be an $n \times p$ [random matrix](/D/rmat). Then, the [expected value](/D/mean) of $X$ is an $n \times p$ matrix whose entries correspond to the expected values of the entries of the random matrix:

$$ \label{eq:mean-rmat}
\mathrm{E}(X) = \mathrm{E}\left( \left[ \begin{array}{ccc} X_{11} & \ldots & X_{1p} \\ \vdots & \ddots & \vdots \\ X_{n1} & \ldots & X_{np} \end{array} \right] \right) = \left[ \begin{array}{ccc} \mathrm{E}(X_{11}) & \ldots & \mathrm{E}(X_{1p}) \\ \vdots & \ddots & \vdots \\ \mathrm{E}(X_{n1}) & \ldots & \mathrm{E}(X_{np}) \end{array} \right] \; .
$$