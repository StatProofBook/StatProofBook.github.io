---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-10-20 10:47:00

title: "Derivation of the family evidence"
chapter: "Model Selection"
section: "Bayesian model selection"
topic: "Family evidence"
theorem: "Derivation"

sources:

proof_id: "P368"
shortcut: "fe-der"
username: "JoramSoch"
---


**Theorem:** Let $f$ be a family of $M$ [generative models](/D/gm) $m_1, \ldots, m_M$ with [model evidences](/D/me) $p(y \vert m_1), \ldots, p(y \vert m_M)$. Then, the [family evidence](/D/fe) can be expressed in terms of the model evidences as

$$ \label{eq:FE-marg}
\mathrm{FE}(f) = \sum_{i=1}^M p(y|m_i) \, p(m_i|f)
$$

where $p(m_i \vert f)$ are the within-[family](/D/lfe) [prior](/D/prior) [model](/D/gm) [probabilities](/D/prob).


**Proof:** This a consequence of the [law of marginal probability](/D/prob-marg) for [discrete variables](/D/rvar-disc)

$$ \label{eq:prob-marg}
p(y|f) = \sum_{i=1}^M p(y,m_i|f)
$$

and the [law of conditional probability](/D/prob-cond) according to which

$$ \label{eq:prob-cond}
p(y,m_i|f) = p(y|m_i,f) \, p(m_i|f) \; .
$$

Since models are [nested within model families](/D/fe), such that $m_i \wedge f \leftrightarrow m_i$, we have the following equality of probabilities:

$$ \label{eq:prob-equal}
p(y|m_i,f) = p(y|m_i \wedge f) = p(y|m_i) \; .
$$

Plugging \eqref{eq:prob-cond} into \eqref{eq:prob-marg} and applying \eqref{eq:prob-equal}, we obtain:

$$ \label{eq:ME-marg-qed}
\mathrm{FE}(f) = p(y|f) = \sum_{i=1}^M p(y|m_i) \, p(m_i|f) \; .
$$