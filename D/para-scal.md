---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2025-03-14 15:02:00

title: "Scale parameter"
chapter: "General Theorems"
section: "Probability theory"
topic: "Probability distributions"
definition: "Scale parameter"

sources:
  - authors: "Wikipedia"
    year: 2025
    title: "Location–scale family"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2025-03-14"
    url: "https://en.wikipedia.org/wiki/Location%E2%80%93scale_family"
  - authors: "Wikipedia"
    year: 2025
    title: "Scale parameter"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2025-03-14"
    url: "https://en.wikipedia.org/wiki/Scale_parameter#Definition"

def_id: "D218"
shortcut: "para-scal"
username: "JoramSoch"
---


**Definition:** Let $\mathcal{D}(\lambda, \sigma)$ denote a family of [probability distributions](/D/dist) with [statistical parameters](/D/para) $\lambda$ and $\sigma$. Then, the parameter $\sigma$ is referred to as a "scale parameter", if and only if the following holds: When a [random variable](/D/rvar) $X$ is following the probability distribution $\mathcal{D}(\lambda^{\*}, \sigma^{\*})$, then the random variable $Y = X/\sigma^{\*}$ is following the probability distribution $\mathcal{D}(\lambda^{\*}, 1)$.

$$ \label{eq:para-scal}
X \sim \mathcal{D}(\lambda^{*}, \sigma^{*})
\quad \Rightarrow \quad
Y = \frac{X}{\sigma^{*}} \sim \mathcal{D}(\lambda^{*}, 1) \; .
$$

This implies an identity of the [cumulative distribution functions](/D/cdf):

$$ \label{eq:para-scal-cdf}
\begin{split}
F_Y(y) &= F_X(\sigma^{*} y) \\
F_\mathcal{D}(y; \, \lambda^{*}, 1) &= F_\mathcal{D}(\sigma^{*} y; \, \lambda^{*}, \sigma^{*}) \; .
\end{split}
$$

The [parameter](/D/para) $\sigma$ can be scalar for a [random variable](/D/rvar) $X$ or matrix-valued for a [random matrix](/D/rmat) $X$.