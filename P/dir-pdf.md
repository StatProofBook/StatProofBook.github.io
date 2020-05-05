---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-05-05 21:22:00

title: "Probability density function of the Dirichlet distribution"
chapter: "Probability Distributions"
section: "Multivariate continuous distributions"
topic: "Dirichlet distribution"
theorem: "Probability density function"

sources:

proof_id: "P95"
shortcut: "dir-pdf"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random vector](/D/rvec) following a [Dirichlet distribution](/D/dir):

$$ \label{eq:Dir}
X \sim \mathrm{Dir}(\alpha) \; .
$$

Then, the [probability density function](/D/pdf) of $X$ is

$$ \label{eq:Dir-pdf}
f_X(x) = \frac{\Gamma\left( \sum_{i=1}^k \alpha_i \right)}{\prod_{i=1}^k \Gamma(\alpha_i)} \, \prod_{i=1}^k {x_i}^{\alpha_i-1} \; .
$$


**Proof:** This follows directly from the [definition of the Dirichlet distribution](/D/dir).