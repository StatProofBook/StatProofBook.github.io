---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2025-03-14 14:56:00

title: "Location parameter"
chapter: "General Theorems"
section: "Probability theory"
topic: "Probability distributions"
definition: "Location parameter"

sources:
  - authors: "Wikipedia"
    year: 2025
    title: "Location–scale family"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2025-03-14"
    url: "https://en.wikipedia.org/wiki/Location%E2%80%93scale_family"
  - authors: "Wikipedia"
    year: 2025
    title: "Location parameter"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2025-03-14"
    url: "https://en.wikipedia.org/wiki/Location_parameter#Definition"

def_id: "D217"
shortcut: "para-loc"
username: "JoramSoch"
---


**Definition:** Let $\mathcal{D}(\mu, \lambda)$ denote a family of [probability distributions](/D/dist) with [statistical parameters](/D/para) $\mu$ and $\lambda$. Then, the parameter $\mu$ is referred to as a "location parameter", if and only if the following holds: When a [random variable](/D/rvar) $X$ is following the probability distribution $\mathcal{D}(\mu^{*}, \lambda^{*})$, then the random variable $Y = X-\mu^{*}$ is following the probability distribution $\mathcal{D}(0, \lambda^{*})$.

$$ \label{eq:para-loc}
X \sim \mathcal{D}(\mu^{*}, \lambda^{*})
\quad \Rightarrow \quad
Y = X-\mu^{*} \sim \mathcal{D}(0, \lambda^{*}) \; .
$$

This implies an identity of the [cumulative distribution functions](/D/cdf):

$$ \label{eq:para-loc-cdf}
\begin{split}
F_Y(y) &= F_X(y+\mu^{*}) \\
F_\mathcal{D}(y; \, 0, \lambda^{*}) &= F_\mathcal{D}(y+\mu^{*}; \, \mu^{*}, \lambda^{*}) \; .
\end{split}
$$

The [parameter](/D/para) $\mu$ can be scalar-, vector- or matrix-valued for random [variables](/D/rvar), [vectors](/D/rvec) or [matrices](/D/rmat) $X$.