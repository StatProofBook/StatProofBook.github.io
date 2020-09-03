---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-08-11 08:29:00

title: "Concavity of the Shannon entropy"
chapter: "General Theorems"
section: "Information theory"
topic: "Shannon entropy"
theorem: "Concavity"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Entropy (information theory)"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-08-11"
    url: "https://en.wikipedia.org/wiki/Entropy_(information_theory)#Further_properties"
  - authors: "Cover TM, Thomas JA"
    year: 1991
    title: "Elements of Information Theory"
    pages: "p. 30"
    url: "https://www.wiley.com/en-us/Elements+of+Information+Theory%2C+2nd+Edition-p-9780471241959"
  - authors: "Xie, Yao"
    year: 2012
    title: "Chain Rules and Inequalities"
    in: "ECE587: Information Theory"
    pages: "Lecture 3, Slide 25"
    url: "https://www2.isye.gatech.edu/~yxie77/ece587/Lecture3.pdf"
  - authors: "Goh, Siong Thye"
    year: 2016
    title: "Understanding the proof of the concavity of entropy"
    in: "StackExchange Mathematics"
    pages: "retrieved on 2020-11-08"
    url: "https://math.stackexchange.com/questions/2000194/understanding-the-proof-of-the-concavity-of-entropy"

proof_id: "P149"
shortcut: "ent-conc"
username: "JoramSoch"
---


**Theorem:** The [entropy](/D/ent) is concave in the [probability mass function](/D/pmf) $p$, i.e.

$$ \label{eq:ent-conc}
\mathrm{H}[\lambda p_1 + (1-\lambda) p_2] \geq \lambda \mathrm{H}[p_1] + (1-\lambda) \mathrm{H}[p_2]
$$

where $p_1$ and $p_2$ are probability mass functions and $0 \leq \lambda \leq 1$.


**Proof:** Let $X$ be a discrete [random variable](/D/rvar) with possible outcomes $\mathcal{X}$ and let $u(x)$ be the [probability mass function](/D/pmf) of a [discrete uniform distribution](/D/duni) on $X \in \mathcal{X}$. Then, the [entropy](/D/ent) of an arbitrary [probability mass function](/D/pmf) $p(x)$ can be rewritten as

$$ \label{eq:ent-kl}
\begin{split}
\mathrm{H}[p] &= - \sum_{x \in \mathcal{X}} p(x) \cdot \log p(x) \\
&= - \sum_{x \in \mathcal{X}} p(x) \cdot \log \frac{p(x)}{u(x)} u(x) \\
&= - \sum_{x \in \mathcal{X}} p(x) \cdot \log \frac{p(x)}{u(x)} - \sum_{x \in \mathcal{X}} p(x) \cdot \log u(x) \\
&= - \mathrm{KL}[p||u] - \log \frac{1}{|\mathcal{X}|} \sum_{x \in \mathcal{X}} p(x) \\
&= \log |\mathcal{X}| - \mathrm{KL}[p||u] \\
\log |\mathcal{X}| - \mathrm{H}[p] &= \mathrm{KL}[p||u]
\end{split}
$$

where we have applied the [definition of the Kullback-Leibler divergence](/D/kl), the [probability mass function of the discrete uniform distribution](/P/duni-pmf) and [the total sum over the probability mass function](/D/pmf).

Note that the [KL divergence is convex](/P/kl-conv) in the pair of [probability distributions](/D/dist) $(p,q)$:

$$ \label{eq:kl-conv}
\mathrm{KL}[\lambda p_1 + (1-\lambda) p_2||\lambda q_1 + (1-\lambda) q_2] \leq \lambda \mathrm{KL}[p_1||q_1] + (1-\lambda) \mathrm{KL}[p_2||q_2]
$$

A special case of this is given by

$$ \label{eq:kl-conv-u}
\begin{split}
\mathrm{KL}[\lambda p_1 + (1-\lambda) p_2||\lambda u + (1-\lambda) u] &\leq \lambda \mathrm{KL}[p_1||u] + (1-\lambda) \mathrm{KL}[p_2||u] \\
\mathrm{KL}[\lambda p_1 + (1-\lambda) p_2||u] &\leq \lambda \mathrm{KL}[p_1||u] + (1-\lambda) \mathrm{KL}[p_2||u]
\end{split}
$$

and applying equation \eqref{eq:ent-kl}, we have

$$ \label{eq:ent-conc-qed}
\begin{split}
\log |\mathcal{X}| - \mathrm{H}[\lambda p_1 + (1-\lambda) p_2] &\leq \lambda \left( \log |\mathcal{X}| - \mathrm{H}[p_1] \right) + (1-\lambda) \left( \log |\mathcal{X}| - \mathrm{H}[p_2] \right) \\
\log |\mathcal{X}| - \mathrm{H}[\lambda p_1 + (1-\lambda) p_2] &\leq \log |\mathcal{X}| - \lambda \mathrm{H}[p_1] - (1-\lambda) \mathrm{H}[p_2] \\
- \mathrm{H}[\lambda p_1 + (1-\lambda) p_2] &\leq - \lambda \mathrm{H}[p_1] - (1-\lambda) \mathrm{H}[p_2] \\
\mathrm{H}[\lambda p_1 + (1-\lambda) p_2] &\geq \lambda \mathrm{H}[p_1] + (1-\lambda) \mathrm{H}[p_2]
\end{split}
$$

which is equivalent to \eqref{eq:ent-conc}.