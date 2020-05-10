---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-05-10 20:20:00

title: "Kullback-Leibler divergence"
chapter: "General Theorems"
section: "Information theory"
topic: "Kullback-Leibler divergence"
definition: "Definition"

sources:
  - authors: "MacKay, David J.C."
    year: 2003
    title: "Probability, Entropy, and Inference"
    in: "Information Theory, Inference, and Learning Algorithms"
    pages: "ch. 2.6, eq. 2.45, p. 34"
    url: "https://www.inference.org.uk/itprnn/book.pdf"

def_id: "D52"
shortcut: "kl"
username: "JoramSoch"
---


**Definition:** Let $X$ be a [random variable](/D/rvar) with possible outcomes $\mathcal{X}$ and let $P$ and $Q$ be two [probability distributions](/D/dist) on $X$.

1) The Kullback-Leibler divergence of $P$ from $Q$ for a discrete random variable $X$ is defined as

$$ \label{eq:KL-disc}
\mathrm{KL}[P||Q] = \sum_{x \in \mathcal{X}} p(x) \cdot \log \frac{p(x)}{q(x)}
$$

where $p(x)$ and $q(x)$ are the [probability mass functions](/D/pmf) of $P$ and $Q$.

2) The Kullback-Leibler divergence of $P$ from $Q$ for a continuous random variable $X$ is defined as

$$ \label{eq:KL-cont}
\mathrm{KL}[P||Q] = \int_{\mathcal{X}} p(x) \cdot \log \frac{p(x)}{q(x)} \, \mathrm{d}x
$$

where $p(x)$ and $q(x)$ are the [probability density functions](/D/pdf) of $P$ and $Q$.