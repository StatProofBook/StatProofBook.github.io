---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-07-13 22:58:00

title: "Derivation of the log family evidence"
chapter: "Model Selection"
section: "Bayesian model selection"
topic: "Log family evidence"
theorem: "Derivation"

sources:

proof_id: "P132"
shortcut: "lfe-der"
username: "JoramSoch"
---


**Theorem:** Let $f$ be a family of $M$ [generative models](/D/gm) $m_1, \ldots, m_M$ with [model evidences](/D/ml) $p(y \vert m_1), \ldots, p(y \vert m_M)$. Then, the [log family evidence](/D/lfe)

$$ \label{eq:LFE-term}
\mathrm{LFE}(f) = \log p(y|f)
$$

can be expressed as

$$ \label{eq:LFE-marg}
\mathrm{LFE}(f) = \log \sum_{i=1}^M p(y|m_i) \, p(m_i|f)
$$

where $p(m_i \vert f)$ are the within-[family](/D/lfe) [prior](/D/prior) [model](/D/gm) [probabilities](/D/prob).


**Proof:** We will assume "prior addivivity"

$$ \label{eq:fam-prior}
p(f) = \sum_{i=1}^M p(m_i)
$$

and "posterior additivity" for family probabilities:

$$ \label{eq:fam-post}
p(f|y) = \sum_{i=1}^M p(m_i|y)
$$

[Bayes' theorem](/P/bayes-th) for the [family evidence](/D/lfe) gives

$$ \label{eq:fe-bayes-th}
p(y|f) = \frac{p(f|y) \, p(y)}{p(f)} \; .
$$

Applying \eqref{eq:fam-prior} and \eqref{eq:fam-post}, we have

$$ \label{eq:fe-me}
p(y|f) = \frac{\sum_{i=1}^M p(m_i|y) \, p(y)}{\sum_{i=1}^M p(m_i)} \; .
$$

[Bayes' theorem](/P/bayes-th) for the [model evidence](/D/lfe) gives

$$ \label{eq:me-bayes-th}
p(y|m_i) = \frac{p(m_i|y) \, p(y)}{p(m_i)}
$$

which can be rearranged into

$$ \label{eq:me-bayes-th-dev}
p(m_i|y) \, p(y) = p(y|m_i) \, p(m_i) \; .
$$

Plugging \eqref{eq:me-bayes-th-dev} into \eqref{eq:fe-me}, we have

$$ \label{eq:fe-marg-qed}
\begin{split}
p(y|f) &= \frac{\sum_{i=1}^M p(y|m_i) \, p(m_i)}{\sum_{i=1}^M p(m_i)} \\
&= \sum_{i=1}^M p(y|m_i) \cdot \frac{p(m_i)}{\sum_{i=1}^M p(m_i)} \\
&= \sum_{i=1}^M p(y|m_i) \cdot \frac{p(m_i,f)}{p(f)} \\
&= \sum_{i=1}^M p(y|m_i) \cdot p(m_i|f) \; .
\end{split}
$$

Equation \eqref{eq:LFE-marg} follows by logarithmizing both sides of \eqref{eq:fe-marg-qed}.