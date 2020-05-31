---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-05-31 23:26:00

title: "Additivity of the Kullback-Leibler divergence for independent distributions"
chapter: "General Theorems"
section: "Information theory"
topic: "Kullback-Leibler divergence"
theorem: "Additivity for independent distributions"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Kullback-Leibler divergence"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-05-31"
    url: "https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence#Properties"

proof_id: "P116"
shortcut: "kl-add"
username: "JoramSoch"
---


**Theorem:** The [Kullback-Leibler divergence](/D/kl) is additive for independent distributions, i.e.

$$ \label{eq:KL-add}
\mathrm{KL}[P||Q] = \mathrm{KL}[P_1||Q_1] + \mathrm{KL}[P_2||Q_2]
$$

where $P_1$ and $P_2$ are [independent](/D/ind) [distributions](/D/dist) with the [joint distribution](/D/dist-joint) $P$, such that $p(x,y) = p_1(x) \, p_2(y)$, and equivalently for $Q_1$, $Q_2$ and $Q$.


**Proof:** The continuous [Kullback-Leibler divergence](/D/kl) is defined as

$$ \label{eq:KL}
\mathrm{KL}[P||Q] = \int_{\mathcal{X}} p(x) \cdot \log \frac{p(x)}{q(x)} \, \mathrm{d}x
$$

which, applied to the joint distributions $P$ and $Q$, yields

$$ \label{eq:KL-s1}
\mathrm{KL}[P||Q] = \int_{\mathcal{X}} \int_{\mathcal{Y}} p(x,y) \cdot \log \frac{p(x,y)}{q(x,y)} \, \mathrm{d}y \, \mathrm{d}x \; .
$$

Applying $p(x,y) = p_1(x) \, p_2(y)$ and $q(x,y) = q_1(x) \, q_2(y)$, we have

$$ \label{eq:KL-s2}
\mathrm{KL}[P||Q] = \int_{\mathcal{X}} \int_{\mathcal{Y}} p_1(x) \, p_2(y) \cdot \log \frac{p_1(x) \, p_2(y)}{q_1(x) \, q_2(y)} \, \mathrm{d}y \, \mathrm{d}x \; .
$$

Now we can separate the logarithm and evaluate the integrals:

$$ \label{eq:KL-qed}
\begin{split}
\mathrm{KL}[P||Q] &= \int_{\mathcal{X}} \int_{\mathcal{Y}} p_1(x) \, p_2(y) \cdot \left( \log \frac{p_1(x)}{q_1(x)} + \log \frac{p_2(y)}{q_2(y)} \right) \, \mathrm{d}y \, \mathrm{d}x \\
&= \int_{\mathcal{X}} \int_{\mathcal{Y}} p_1(x) \, p_2(y) \cdot \log \frac{p_1(x)}{q_1(x)} \, \mathrm{d}y \, \mathrm{d}x + \int_{\mathcal{X}} \int_{\mathcal{Y}} p_1(x) \, p_2(y) \cdot \log \frac{p_2(y)}{q_2(y)} \, \mathrm{d}y \, \mathrm{d}x \\
&= \int_{\mathcal{X}} p_1(x) \cdot \log \frac{p_1(x)}{q_1(x)} \int_{\mathcal{Y}} p_2(y) \, \mathrm{d}y \, \mathrm{d}x + \int_{\mathcal{Y}} p_2(y) \cdot \log \frac{p_2(y)}{q_2(y)} \int_{\mathcal{X}} p_1(x) \, \mathrm{d}x \, \mathrm{d}y \\
&= \int_{\mathcal{X}} p_1(x) \cdot \log \frac{p_1(x)}{q_1(x)} \, \mathrm{d}x + \int_{\mathcal{Y}} p_2(y) \cdot \log \frac{p_2(y)}{q_2(y)} \, \mathrm{d}y \\
&\overset{\eqref{eq:KL}}{=} \mathrm{KL}[P_1||Q_1] + \mathrm{KL}[P_2||Q_2] \; .
\end{split}
$$