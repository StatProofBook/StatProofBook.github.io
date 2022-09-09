---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-09-09 16:33:00

title: "Entropy of the multinomial distribution"
chapter: "Probability Distributions"
section: "Multivariate discrete distributions"
topic: "Multinomial distribution"
theorem: "Shannon entropy"

sources:

proof_id: "P337"
shortcut: "mult-ent"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random vector](/D/rvec) following a [multinomial distribution](/D/mult):

$$ \label{eq:mult}
X \sim \mathrm{Mult}(n,p) \; .
$$

Then, the [(Shannon) entropy](/D/ent) of $X$ is

$$ \label{eq:mult-ent}
\mathrm{H}(X) = n \cdot \mathrm{H}_\mathrm{cat}(p) - \mathrm{E}_\mathrm{lmc}(n,p)
$$

where $\mathrm{H}_\mathrm{cat}(p)$ is the categorical entropy function, i.e. the [(Shannon) entropy of the categorical distribution](/P/cat-ent) with category probabilities $p$

$$ \label{eq:H-cat}
\mathrm{H}_\mathrm{cat}(p) = - \sum_{i=1}^{k} p_i \cdot \log p_i
$$

and $\mathrm{E}_\mathrm{lmc}(n,p)$ is the [expected value](/D/mean) of the logarithmized [multinomial coefficient](/P/mult-pmf) with superset size $n$

$$ \label{eq:E-lmf}
\mathrm{E}_\mathrm{lmf}(n,p) = \mathrm{E}\left[ \log {n \choose {X_1, \ldots, X_k}} \right] \quad \text{where} \quad X \sim \mathrm{Mult}(n,p) \; .
$$


**Proof:** The [entropy](/D/ent) is defined as the probability-weighted average of the logarithmized probabilities for all possible values:

$$ \label{eq:ent}
\mathrm{H}(X) = - \sum_{x \in \mathcal{X}} p(x) \cdot \log_b p(x) \; .
$$

The [probability mass function of the multinomial distribution](/P/mult-pmf) is

$$ \label{eq:mult-pmf}
f_X(x) = {n \choose {x_1, \ldots, x_k}} \, \prod_{i=1}^k {p_i}^{x_i}
$$

Let $\mathcal{X}_{n,k}$ be the set of all vectors $x \in \mathbb{N}^{1 \times k}$ satisfying $\sum_{i=1}^{k} x_i = n$. Then, we have:

$$ \label{eq:mult-ent-s1}
\begin{split}
\mathrm{H}(X) &= - \sum_{x \in \mathcal{X}_{n,k}} f_X(x) \cdot \log f_X(x) \\
&= - \sum_{x \in \mathcal{X}_{n,k}} f_X(x) \cdot \log \left[ {n \choose {x_1, \ldots, x_k}} \, \prod_{i=1}^k {p_i}^{x_i} \right] \\
&= - \sum_{x \in \mathcal{X}_{n,k}} f_X(x) \cdot \left[ \log {n \choose {x_1, \ldots, x_k}} + \sum_{i=1}^{k} x_i \cdot \log p_i \right] \; .
\end{split}
$$

Since the first factor in the sum corresponds to the [probability mass](/D/pmf) of $X=x$, we can rewrite this as the sum of the [expected values](/D/mean) [of the functions](/P/mean-lotus) of the [discrete random variable](/D/rvar-disc) $x$ in the square bracket:

$$ \label{eq:mult-ent-s2}
\begin{split}
\mathrm{H}(X) &= - \left\langle \log {n \choose {x_1, \ldots, x_k}} \right\rangle_{p(x)} - \left\langle \sum_{i=1}^{k} x_i \cdot \log p_i \right\rangle_{p(x)} \\
&= - \left\langle \log {n \choose {x_1, \ldots, x_k}} \right\rangle_{p(x)} - \sum_{i=1}^{k} \left\langle x_i \cdot \log p_i \right\rangle_{p(x)} \; .
\end{split}
$$

Using the [expected value of the multinomial distribution](/P/mult-mean), i.e. $X \sim \mathrm{Mult}(n,p) \Rightarrow \left\langle x_i \right\rangle = n p_i$, this gives:

$$ \label{eq:mult-ent-s3}
\begin{split}
\mathrm{H}(X) &= - \left\langle \log {n \choose {x_1, \ldots, x_k}} \right\rangle_{p(x)} - \sum_{i=1}^{k} n p_i \cdot \log p_i \\
&= - \left\langle\log {n \choose {x_1, \ldots, x_k}} \right\rangle_{p(x)} - n \sum_{i=1}^{k} p_i \cdot \log p_i \; .
\end{split}
$$

Finally, we note that the first term is the negative [expected value](/D/mean) of the logarithm of a [multinomial coefficient](/P/mult-pmf) and that the second term is the [entropy of the categorical distribution](/P/cat-ent), such that we finally get:

$$ \label{eq:mult-ent-s4}
\mathrm{H}(X) = n \cdot \mathrm{H}_\mathrm{cat}(p) - \mathrm{E}_\mathrm{lmc}(n,p) \; .
$$