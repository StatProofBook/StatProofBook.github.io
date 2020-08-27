---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-07-22 07:27:00

title: "Derivation of the log Bayes factor"
chapter: "Model Selection"
section: "Bayesian model selection"
topic: "Log Bayes factor"
theorem: "Derivation"

sources:

proof_id: "P137"
shortcut: "lbf-der"
username: "JoramSoch"
---


**Theorem:** Let there be two [generative models](/D/gm) $m_1$ and $m_2$ with [model evidences](/D/ml) $p(y \vert m_1)$ and $p(y \vert m_2)$. Then, the [log Bayes factor](/D/lbf)

$$ \label{eq:LBF-term}
\mathrm{LBF}_{12} = \log \mathrm{BF}_{12}
$$

can be expressed as

$$ \label{eq:LBF-ratio}
\mathrm{LBF}_{12} = \log \frac{p(y|m_1)}{p(y|m_2)} \; .
$$


**Proof:** The [Bayes factor](/D/bf) is defined as the [posterior](/D/post) [odds ratio](/D/odds) when both [models](/D/gm) are equally likely [apriori](/D/prior):

$$ \label{eq:BF-s1}
\mathrm{BF}_{12} = \frac{p(m_1|y)}{p(m_2|y)}
$$

Plugging in the posterior odds ratio according to [Bayes' rule](/P/bayes-rule), we have

$$ \label{eq:BF-s2}
\mathrm{BF}_{12} = \frac{p(y|m_1)}{p(y|m_2)} \cdot \frac{p(m_1)}{p(m_2)} \; .
$$

When both models are equally likely apriori, the [prior](/D/prior) [odds ratio](/D/odds) is one, such that

$$ \label{eq:BF-s3}
\mathrm{BF}_{12} = \frac{p(y|m_1)}{p(y|m_2)} \; .
$$

Equation \eqref{eq:LBF-ratio} follows by logarithmizing both sides of \eqref{eq:BF-s3}.