---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-02-19 19:10:00

title: "Non-negativity of the Shannon entropy"
chapter: "General Theorems"
section: "Information theory"
topic: "Shannon entropy"
theorem: "Non-negativity"

sources:
  - authors: "Cover TM, Thomas JA"
    year: 1991
    title: "Elements of Information Theory"
    pages: "p. 15"
    url: "https://www.wiley.com/en-us/Elements+of+Information+Theory%2C+2nd+Edition-p-9780471241959"

proof_id: "P57"
shortcut: "ent-nonneg"
username: "JoramSoch"
---


**Theorem:** The entropy of a discrete [random variable](/D/rvar) is a non-negative number:

$$ \label{eq:ent-nonneg}
\mathrm{H}(X) \geq 0 \; .
$$


**Proof:** The [entropy of a discrete random variable](/D/ent) is defined as

$$ \label{eq:ent}
\mathrm{H}(X) = - \sum_{x \in \mathcal{X}} p(x) \cdot \log_b p(x)
$$

The minus sign can be moved into the sum:

$$ \label{eq:ent-dev}
\mathrm{H}(X) = \sum_{x \in \mathcal{X}} \left[ p(x) \cdot \left( - \log_b p(x) \right) \right]
$$

Because the co-domain of [probability mass functions](/D/pmf) is $[0,1]$, we can deduce:

$$ \label{eq:nonneg}
\begin{array}{rcccl}
0 &\leq &p(x) &\leq &1 \\
-\infty &\leq &\log_b p(x) &\leq &0 \\
0 &\leq &-\log_b p(x) &\leq &+\infty \\
0 &\leq &p(x) \cdot \left(-\log_b p(x)\right) &\leq &+\infty \; .
\end{array}
$$

By convention, $0 \cdot \log_b(0)$ is taken to be $0$ when calculating entropy, consistent with

$$ \label{eq:lim-0log0}
\lim_{p \to 0} \left[ p \log_b(p) \right] = 0 \; .
$$

Taking this together, each addend in \eqref{eq:ent-dev} is positive or zero and thus, the entire sum must also be non-negative.