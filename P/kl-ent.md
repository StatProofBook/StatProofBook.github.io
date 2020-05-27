---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-05-27 23:20:00

title: "Relation of Kullback-Leibler divergence to entropy"
chapter: "General Theorems"
section: "Information theory"
topic: "Kullback-Leibler divergence"
theorem: "Relation to discrete entropy"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Kullback-Leibler divergence"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-05-27"
    url: "https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence#Motivation"

proof_id: "P113"
shortcut: "kl-ent"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a discrete [random variable](/D/rvar) with possible outcomes $\mathcal{X}$ and let $P$ and $Q$ be two [probability distributions](/D/dist) on $X$. Then, the [Kullback-Leibler divergence](/D/kl) of $P$ from $Q$ can be expressed as

$$ \label{eq:kl-ent}
\mathrm{KL}[P||Q] = \mathrm{H}(P,Q) - \mathrm{H}(P)
$$

where $\mathrm{H}(P,Q)$ is the [cross-entropy](/D/ent-cross) of $P$ and $Q$ and $\mathrm{H}(P)$ is the [marginal entropy](/D/ent) of $P$.


**Proof:** The discrete [Kullback-Leibler divergence](/D/kl) is defined as

$$ \label{eq:KL}
\mathrm{KL}[P||Q] = \sum_{x \in \mathcal{X}} p(x) \cdot \log \frac{p(x)}{q(x)}
$$

where $p(x)$ and $q(x)$ are the [probability mass functions](/D/pmf) of $P$ and $Q$.

Separating the logarithm, we have:

$$ \label{eq:KL-dev}
\mathrm{KL}[P||Q] = - \sum_{x \in \mathcal{X}} p(x) \, \log q(x) + \sum_{x \in \mathcal{X}} p(x) \, \log p(x) \; .
$$

Now considering the definitions of [marginal entropy](/D/ent) and [cross-entropy](/D/ent-cross)

$$ \label{eq:ME-CE}
\begin{split}
\mathrm{H}(P) &= - \sum_{x \in \mathcal{X}} p(x) \, \log p(x) \\
\mathrm{H}(P,Q) &= - \sum_{x \in \mathcal{X}} p(x) \, \log q(x) \; ,
\end{split}
$$

we can finally show:

$$ \label{eq:KL-qed}
\mathrm{KL}[P||Q] = \mathrm{H}(P,Q) - \mathrm{H}(P) \; .
$$