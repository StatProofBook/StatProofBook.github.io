---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-09-09 15:41:00

title: "Entropy of the categorical distribution"
chapter: "Probability Distributions"
section: "Multivariate discrete distributions"
topic: "Categorical distribution"
theorem: "Shannon entropy"

sources:

proof_id: "P336"
shortcut: "cat-ent"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random vector](/D/rvec) following a [categorical distribution](/D/cat):

$$ \label{eq:cat}
X \sim \mathrm{Cat}(p) \; .
$$

Then, the [(Shannon) entropy](/D/ent) of $X$ is

$$ \label{eq:cat-ent}
\mathrm{H}(X) = - \sum_{i=1}^{k} p_i \cdot \log p_i \; .
$$


**Proof:** The [entropy](/D/ent) is defined as the probability-weighted average of the logarithmized probabilities for all possible values:

$$ \label{eq:ent}
\mathrm{H}(X) = - \sum_{x \in \mathcal{X}} p(x) \cdot \log_b p(x) \; .
$$

Since there are $k$ [possible values for a categorical random vector](/D/cat) with [probabilities given by the entries](/P/cat-pmf) of the $1 \times k$ vector $p$, we have:

$$ \label{eq:cat-ent-qed}
\begin{split}
\mathrm{H}(X) &= - \mathrm{Pr}(X = e_1) \cdot \log \mathrm{Pr}(X = e_1) - \ldots - \mathrm{Pr}(X = e_k) \cdot \log \mathrm{Pr}(X = e_k) \\
\mathrm{H}(X) &= - \sum_{i=1}^{k} \mathrm{Pr}(X = e_i) \cdot \log \mathrm{Pr}(X = e_i) \\
\mathrm{H}(X) &= - \sum_{i=1}^{k} p_i \cdot \log p_i \; . \\
\end{split}
$$