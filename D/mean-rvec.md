---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-07-08 08:34:00

title: "Expected value of a random vector"
chapter: "General Theorems"
section: "Probability theory"
topic: "Expected value"
definition: "Expected value of a random vector"

sources:
  - authors: "Taboga, Marco"
    year: 2017
    title: "Expected value"
    in: "Lectures on probability theory and mathematical statistics"
    pages: "retrieved on 2021-07-08"
    url: "https://www.statlect.com/fundamentals-of-probability/expected-value#hid12"
  - authors: "Wikipedia"
    year: 2021
    title: "Multivariate random variable"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-07-08"
    url: "https://en.wikipedia.org/wiki/Multivariate_random_variable#Expected_value"

def_id: "D154"
shortcut: "mean-rvec"
username: "JoramSoch"
---


**Definition:** Let $X$ be an $n \times 1$ [random vector](/D/rvec). Then, the [expected value](/D/mean) of $X$ is an $n \times 1$ vector whose entries correspond to the expected values of the entries of the random vector:

$$ \label{eq:mean-rvec}
\mathrm{E}(X) = \mathrm{E}\left( \left[ \begin{array}{c} X_1 \\ \vdots \\ X_n \end{array} \right] \right) = \left[ \begin{array}{c} \mathrm{E}(X_1) \\ \vdots \\ \mathrm{E}(X_n) \end{array} \right] \; .
$$