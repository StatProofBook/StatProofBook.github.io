---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2026-04-20 16:01:24

title: "Circular expected value"
chapter: "General Theorems"
section: "Probability theory"
topic: "Expected value"
definition: "Circular expected value"

sources:
  - authors: "Mardia KV, Jupp PE"
    year: 2000
    title: "Moments and Measures of Location and Dispersion"
    in: "Directional Statistics"
    pages: "ch. 3.4, pp. 28-31"
    url: "https://onlinelibrary.wiley.com/doi/book/10.1002/9780470316979"
    doi: "10.1002/9780470316979"

def_id: "D230"
shortcut: "mean-circ"
username: "JoramSoch"
---


**Definition:** The expected value (or, mean) of a [circular](/D/rvar-circ) [random variable](/D/rvar) $X$ with domain $\mathcal{X} = [0, 2 \pi)$ is defined as the value of $\mu$ satisfying

$$ \label{eq:mean-circ-eq}
\mathrm{E}\left( e^{iX} \right) = r \cdot e^{i\mu}
$$

or, equivalently,

$$ \label{eq:mean-circ}
\mu = \mathrm{E}(X) = \mathrm{atan2}\left( \mathrm{E}(\sin X), \mathrm{E}(\sin X) \right)
$$

where $\sin$ and $\cos$ are the sine and cosine function, respectively, and $\mathrm{atan2}$ is the two-argument arctangent function.