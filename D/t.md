---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-04-21 07:53:00

title: "t-distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "t-distribution"
definition: "Definition"

sources:
  - authors: "Wikipedia"
    year: 2021
    title: "Student's t-distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-04-21"
    url: "https://en.wikipedia.org/wiki/Student%27s_t-distribution#Characterization"

def_id: "D147"
shortcut: "t"
username: "JoramSoch"
---


**Definition:** Let $Z$ and $V$ be [independent](/D/ind) [random variables](/D/rvar) following a [standard normal distribution](/D/snorm) and a [chi-squared distribution](/D/chi2) with $\nu$ [degrees of freedom](/D/dof), respectively:

$$ \label{eq:snorm-chi2}
\begin{split}
Z &\sim \mathcal{N}(0,1) \\
V &\sim \chi^{2}(\nu) \; .
\end{split}
$$

Then, the ratio of $Z$ to the square root of $V$, divided by the respective degrees of freedom, is said to be $t$-distributed with degrees of freedom $\nu$:

$$ \label{eq:t}
Y = \frac{Z}{\sqrt{V/\nu}} \sim t(\nu) \; .
$$

The $t$-distribution is also called "Student's $t$-distribution", after William S. Gosset a.k.a. "Student".