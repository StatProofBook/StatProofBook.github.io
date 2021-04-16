---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-04-07 08:47:00

title: "Inverse transformation method using cumulative distribution function"
chapter: "General Theorems"
section: "Probability theory"
topic: "Probability functions"
theorem: "Inverse transformation method"

sources:
  - authors: "Wikipedia"
    year: 2021
    title: "Inverse transform sampling"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-04-07"
    url: "https://en.wikipedia.org/wiki/Inverse_transform_sampling#Proof_of_correctness"

proof_id: "P221"
shortcut: "cdf-itm"
username: "JoramSoch"
---


**Theorem:** Let $U$ be a [continuous](/D/rvar-disc) [random variable](/D/rvar) having a [standard uniform distribution](/D/suni). Then, the [random variable](/D/rvar)

$$ \label{eq:cdf-itm}
X = F_X^{-1}(U)
$$

has a [probability distribution](/D/dist) characterized by the [invertible](/D/qf) [cumulative distribution function](/D/cdf) $F_X(x)$.


**Proof:** The [cumulative distribution function](/D/cdf) of the transformation $X = F_X^{-1}(U)$ can be derived as

$$ \label{eq:cdf-itm-qed}
\begin{split}
&\hphantom{=} \;\; \mathrm{Pr}(X \leq x) \\
&= \mathrm{Pr}(F_X^{-1}(U) \leq x) \\
&= \mathrm{Pr}(U \leq F_X(x)) \\
&= F_X(x) \; ,
\end{split}
$$

because the [cumulative distribution function](/D/cdf) of the [standard uniform distribution](/D/suni) $\mathcal{U}(0,1)$ is

$$ \label{eq:suni-cdf}
U \sim \mathcal{U}(0,1) \quad \Rightarrow \quad F_U(u) = \mathrm{Pr}(U \leq u) = u \; .
$$