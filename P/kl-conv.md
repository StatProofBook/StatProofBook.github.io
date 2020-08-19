---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-08-11 07:30:00

title: "Convexity of the Kullback-Leibler divergence"
chapter: "General Theorems"
section: "Information theory"
topic: "Kullback-Leibler divergence"
theorem: "Convexity"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Kullback-Leibler divergence"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-08-11"
    url: "https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence#Properties"
  - authors: "Xie, Yao"
    year: 2012
    title: "Chain Rules and Inequalities"
    in: "ECE587: Information Theory"
    pages: "Lecture 3, Slides 22/24"
    url: "https://www2.isye.gatech.edu/~yxie77/ece587/Lecture3.pdf"

proof_id: "P148"
shortcut: "kl-conv"
username: "JoramSoch"
---


**Theorem:**  The [Kullback-Leibler divergence](/D/kl) is convex in the pair of [probability distributions](/D/dist) $(p,q)$, i.e.

$$ \label{eq:KL-conv}
\mathrm{KL}[\lambda p_1 + (1-\lambda) p_2||\lambda q_1 + (1-\lambda) q_2] \leq \lambda \mathrm{KL}[p_1||q_1] + (1-\lambda) \mathrm{KL}[p_2||q_2]
$$

where $(p_1,q_1)$ and $(p_2,q_2)$ are two pairs of probability distributions and $0 \leq \lambda \leq 1$.


**Proof:** The [Kullback-Leibler divergence](/D/kl) of $P$ from $Q$ is defined as

$$ \label{eq:KL}
\mathrm{KL}[P||Q] = \sum_{x \in \mathcal{X}} p(x) \cdot \log \frac{p(x)}{q(x)}
$$

and the [log sum inequality](/P/logsum-ineq) states that

$$ \label{eq:logsum-ineq}
\sum_{i=1}^n a_i \log \frac{a_i}{b_i} \geq \left( \sum_{i=1}^n a_i \right) \log \frac{\sum_{i=1}^n a_i}{\sum_{i=1}^n b_i}
$$

where $a_1, \ldots, a_n$ and $b_1, \ldots, b_n$ are non-negative real numbers.

Thus, we can rewrite the KL divergence of the mixture distribution as

$$ \label{eq:KL-conv-qed}
\begin{split}
&\mathrm{KL}[\lambda p_1 + (1-\lambda) p_2||\lambda q_1 + (1-\lambda) q_2] \\
\overset{\eqref{eq:KL}}{=} &\sum_{x \in \mathcal{X}} \left[ \left[ \lambda p_1(x) + (1-\lambda) p_2(x) \right] \cdot \log \frac{\lambda p_1(x) + (1-\lambda) p_2(x)}{\lambda q_1(x) + (1-\lambda) q_2(x)} \right] \\
\overset{\eqref{eq:logsum-ineq}}{\leq} &\sum_{x \in \mathcal{X}} \left[ \lambda p_1(x) \cdot \log \frac{\lambda p_1(x)}{\lambda q_1(x)} + (1-\lambda) p_2(x) \cdot \log \frac{(1-\lambda) p_2(x)}{(1-\lambda) q_2(x)} \right] \\
= &\lambda \sum_{x \in \mathcal{X}} p_1(x) \cdot \log \frac{p_1(x)}{q_1(x)} + (1-\lambda) \sum_{x \in \mathcal{X}} p_2(x) \cdot \log \frac{p_2(x)}{q_2(x)} \\
\overset{\eqref{eq:KL}}{=} &\lambda \, \mathrm{KL}[p_1||q_1] + (1-\lambda) \, \mathrm{KL}[p_2||q_2]
\end{split}
$$

which is equivalent to \eqref{eq:KL-conv}.