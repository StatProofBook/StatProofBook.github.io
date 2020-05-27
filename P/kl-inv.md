---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-05-28 00:18:00

title: "Invariance of the Kullback-Leibler divergence under parameter transformation"
chapter: "General Theorems"
section: "Information theory"
topic: "Kullback-Leibler divergence"
theorem: "Invariance under parameter transformation"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Kullback-Leibler divergence"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-05-27"
    url: "https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence#Properties"
  - authors: "shimao"
    year: 2018
    title: "KL divergence invariant to affine transformation?"
    in: "StackExchange CrossValidated"
    pages: "retrieved on 2020-05-28"
    url: "https://stats.stackexchange.com/questions/341922/kl-divergence-invariant-to-affine-transformation"

proof_id: "P115"
shortcut: "kl-inv"
username: "JoramSoch"
---


**Theorem:** The [Kullback-Leibler divergence](/D/kl) is invariant under parameter transformation, i.e.

$$ \label{eq:KL-inv}
\mathrm{KL}[p(x)||q(x)] = \mathrm{KL}[p(y)||q(y)]
$$

where $y(x) = mx + n$ is an affine transformation of $x$ and $p(x)$ and $q(x)$ are the [probability density functions](/D/pdf) of the [probability distributions](/D/dist) $P$ and $Q$ on the continuous [random variable](/D/rvar) $X$.


**Proof:** The continuous [Kullback-Leibler divergence](/D/kl) (KL divergence) is defined as

$$ \label{eq:KL}
\mathrm{KL}[p(x)||q(x)] = \int_{a}^{b} p(x) \cdot \log \frac{p(x)}{q(x)} \, \mathrm{d}x
$$

where $a = \mathrm{min}(\mathcal{X})$ and $b = \mathrm{max}(\mathcal{X})$ are the lower and upper bound of the possible outcomes $\mathcal{X}$ of $X$.

Due to the identity of the differentials

$$ \label{eq:diff}
\begin{split}
p(x) \, \mathrm{d}x &= p(y) \, \mathrm{d}y \\
q(x) \, \mathrm{d}x &= q(y) \, \mathrm{d}y
\end{split}
$$

which can be rearranged into

$$ \label{eq:diff-dev}
\begin{split}
p(x) &= p(y) \, \frac{\mathrm{d}y}{\mathrm{d}x} \\
q(x) &= q(y) \, \frac{\mathrm{d}y}{\mathrm{d}x} \; ,
\end{split}
$$

the KL divergence can be evaluated as follows:

$$ \label{eq:MDE-DCE}
\begin{split}
\mathrm{KL}[p(x)||q(x)] &= \int_{a}^{b} p(x) \cdot \log \frac{p(x)}{q(x)} \, \mathrm{d}x \\
&= \int_{y(a)}^{y(b)} p(y) \, \frac{\mathrm{d}y}{\mathrm{d}x} \cdot \log \left( \frac{p(y) \, \frac{\mathrm{d}y}{\mathrm{d}x}}{q(y) \, \frac{\mathrm{d}y}{\mathrm{d}x}} \right) \, \mathrm{d}x \\
&= \int_{y(a)}^{y(b)} p(y) \cdot \log \frac{p(y)}{q(y)} \, \mathrm{d}y \\
&= \mathrm{KL}[p(y)||q(y)] \; .
\end{split}
$$