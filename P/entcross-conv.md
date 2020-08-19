---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-08-11 09:16:00

title: "Convexity of the cross-entropy"
chapter: "General Theorems"
section: "Information theory"
topic: "Shannon entropy"
theorem: "Convexity of cross-entropy"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Cross entropy"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-08-11"
    url: "https://en.wikipedia.org/wiki/Cross_entropy#Definition"
  - authors: "gunes"
    year: 2019
    title: "Convexity of cross entropy"
    in: "StackExchange CrossValidated"
    pages: "retrieved on 2020-11-08"
    url: "https://stats.stackexchange.com/questions/394463/convexity-of-cross-entropy"

proof_id: "P150"
shortcut: "entcross-conv"
username: "JoramSoch"
---


**Theorem:** The [cross-entropy](/D/ent-cross) is convex in the [probability distribution](/D/dist) $q$, i.e.

$$ \label{eq:ent-cross-conv}
\mathrm{H}[p,\lambda q_1 + (1-\lambda) q_2] \leq \lambda \mathrm{H}[p,q_1] + (1-\lambda) \mathrm{H}[p,q_2]
$$

where $p$ is a fixed and $q_1$ and $q_2$ are any two probability distributions and $0 \leq \lambda \leq 1$.


**Proof:** The [relationship between Kullback-Leibler divergence, entropy and cross-entropy](/P/kl-ent) is:

$$ \label{eq:kl-ent}
\mathrm{KL}[P||Q] = \mathrm{H}(P,Q) - \mathrm{H}(P) \; .
$$

Note that the [KL divergence is convex](/P/kl-conv) in the pair of [probability distributions](/D/dist) $(p,q)$:

$$ \label{eq:kl-conv}
\mathrm{KL}[\lambda p_1 + (1-\lambda) p_2||\lambda q_1 + (1-\lambda) q_2] \leq \lambda \mathrm{KL}[p_1||q_1] + (1-\lambda) \mathrm{KL}[p_2||q_2]
$$

A special case of this is given by

$$ \label{eq:kl-conv-p}
\begin{split}
\mathrm{KL}[\lambda p + (1-\lambda) p||\lambda q_1 + (1-\lambda) q_2] &\leq \lambda \mathrm{KL}[p||q_1] + (1-\lambda) \mathrm{KL}[p||q_2] \\
\mathrm{KL}[p||\lambda q_1 + (1-\lambda) q_2] &\leq \lambda \mathrm{KL}[p||q_1] + (1-\lambda) \mathrm{KL}[p||q_2]
\end{split}
$$

and applying equation \eqref{eq:kl-ent}, we have

$$ \label{eq:ent-cross-conv-qed}
\begin{split}
\mathrm{H}[p,\lambda q_1 + (1-\lambda) q_2] - \mathrm{H}[p] &\leq \lambda \left( \mathrm{H}[p,q_1] - \mathrm{H}[p] \right) + (1-\lambda) \left( \mathrm{H}[p,q_2] - \mathrm{H}[p] \right) \\
\mathrm{H}[p,\lambda q_1 + (1-\lambda) q_2] - \mathrm{H}[p] &\leq \lambda \mathrm{H}[p,q_1] + (1-\lambda) \mathrm{H}[p,q_2] - \mathrm{H}[p] \\
\mathrm{H}[p,\lambda q_1 + (1-\lambda) q_2] &\leq \lambda \mathrm{H}[p,q_1] + (1-\lambda) \mathrm{H}[p,q_2]
\end{split}
$$

which is equivalent to \eqref{eq:ent-cross-conv}.