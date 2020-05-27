---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-05-27 23:32:00

title: "Relation of continuous Kullback-Leibler divergence to differential entropy"
chapter: "General Theorems"
section: "Information theory"
topic: "Kullback-Leibler divergence"
theorem: "Relation to differential entropy"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Kullback-Leibler divergence"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-05-27"
    url: "https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence#Motivation"

proof_id: "P114"
shortcut: "kl-dent"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a continuous [random variable](/D/rvar) with possible outcomes $\mathcal{X}$ and let $P$ and $Q$ be two [probability distributions](/D/dist) on $X$. Then, the [Kullback-Leibler divergence](/D/kl) of $P$ from $Q$ can be expressed as

$$ \label{eq:kl-dent}
\mathrm{KL}[P||Q] = \mathrm{h}(P,Q) - \mathrm{h}(P)
$$

where $\mathrm{h}(P,Q)$ is the [differential cross-entropy](/D/dent-cross) of $P$ and $Q$ and $\mathrm{h}(P)$ is the [marginal differential entropy](/D/dent) of $P$.


**Proof:** The continuous [Kullback-Leibler divergence](/D/kl) is defined as

$$ \label{eq:KL}
\mathrm{KL}[P||Q] = \int_{\mathcal{X}} p(x) \cdot \log \frac{p(x)}{q(x)} \, \mathrm{d}x
$$

where $p(x)$ and $q(x)$ are the [probability density functions](/D/pdf) of $P$ and $Q$.

Separating the logarithm, we have:

$$ \label{eq:KL-dev}
\mathrm{KL}[P||Q] = - \int_{\mathcal{X}} p(x) \, \log q(x) \, \mathrm{d}x + \int_{\mathcal{X}} p(x) \, \log p(x) \, \mathrm{d}x \; .
$$

Now considering the definitions of [marginal differential entropy](/D/dent) and [differential cross-entropy](/D/dent-cross)

$$ \label{eq:MDE-DCE}
\begin{split}
\mathrm{h}(P) &= - \int_{\mathcal{X}} p(x) \, \log p(x) \, \mathrm{d}x \\
\mathrm{h}(P,Q) &= - \int_{\mathcal{X}} p(x) \, \log q(x) \, \mathrm{d}x \; ,
\end{split}
$$

we can finally show:

$$ \label{eq:KL-qed}
\mathrm{KL}[P||Q] = \mathrm{h}(P,Q) - \mathrm{h}(P) \; .
$$