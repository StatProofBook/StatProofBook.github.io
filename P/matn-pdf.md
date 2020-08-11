---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-03-02 21:03:00

title: "Probability density function of the matrix-normal distribution"
chapter: "Probability Distributions"
section: "Matrix-variate continuous distributions"
topic: "Matrix-normal distribution"
theorem: "Probability density function"

sources:

proof_id: "P70"
shortcut: "matn-pdf"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random matrix](/D/rmat) following a [matrix-normal distribution](/D/matn):

$$ \label{eq:matn}
X \sim \mathcal{MN}(M, U, V) \; .
$$

Then, the [probability density function](/D/pdf) of $X$ is

$$ \label{eq:matn-pdf}
f(X) = \frac{1}{\sqrt{(2\pi)^{np} |V|^n |U|^p}} \cdot \exp\left[-\frac{1}{2} \mathrm{tr}\left( V^{-1} (X-M)^\mathrm{T} \, U^{-1} (X-M) \right) \right] \; .
$$


**Proof:** This follows directly from the [definition of the matrix-normal distribution](/D/matn).