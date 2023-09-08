---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2023-09-08 11:56:27

title: "Equivalence of operations for model evidence and log model evidence"
chapter: "Model Selection"
section: "Bayesian model selection"
topic: "Model evidence"
theorem: "Subtraction of mean from LMEs"

sources:
  - authors: "Penny, Will"
    year: 2015
    title: "Bayesian model selection for group studies using Gibbs sampling"
    in: "SPM12"
    pages: "retrieved on 2023-09-08"
    url: "https://github.com/spm/spm12/blob/master/spm_BMS_gibbs.m"
  - authors: "Soch, Joram"
    year: 2018
    title: "Random Effects Bayesian Model Selection using Variational Bayes"
    in: "MACS – a new SPM toolbox for model assessment, comparison and selection"
    pages: "retrieved on 2023-09-08"
    url: "https://github.com/JoramSoch/MACS/blob/master/ME_BMS_RFX_VB.m"
    doi: "10.5281/zenodo.845404"

proof_id: "P414"
shortcut: "lme-mean"
username: "JoramSoch"
---


**Theorem:** Subtracting the arithmetic mean from a set of [log model evidences](/D/lme) is equivalent to dividing the corresponding [model evidences](/D/me) by their geometric mean.

**Proof:** Consider a model space $\mathcal{M} = \left\lbrace m_1, \ldots, m_M \right\rbrace$ consisting of $M$ [models](/D/gm). Then, the normalized [log model evidence](/D/lme) of any model $m_i$, denoted as $\mathrm{LME}^{*}(m_i)$, may be calculated by subtracting the mean across model space:

$$ \label{eq:lme-norm}
\mathrm{LME}^{*}(m_i) = \log p(y|m_i) - \frac{1}{M} \sum_{j=1}^M \log p(y|m_j) \; .
$$

To prove the theorem, we will now rewrite the right-hand side until we arrive at an expression for the normalized [model evidence](/D/lme). First, applying $c \log_b a = \log_b a^c$, we obtain

$$ \label{eq:lme-mean-s1}
\mathrm{LME}^{*}(m_i) = \log p(y|m_i) - \sum_{j=1}^M \left[ \log p(y|m_j)^{1/M} \right] \; .
$$

Then, exponentiating both sides, we have:

$$ \label{eq:lme-mean-s2}
\begin{split}
\mathrm{exp}\left[ \mathrm{LME}^{*}(m_i) \right] &= \frac{\mathrm{exp}\left[ \log p(y|m_i) \right]}{\mathrm{exp}\left[ \sum_{j=1}^M \left[ \log p(y|m_j)^{1/M} \right] \right]} \\
&= \frac{p(y|m_i)}{\prod_{j=1}^M \mathrm{exp}\left[ \log p(y|m_j)^{1/M} \right]} \\
&= \frac{p(y|m_i)}{\prod_{j=1}^M p(y|m_j)^{1/M}} \\
&= \frac{p(y|m_i)}{\left( \prod_{j=1}^M p(y|m_j) \right)^{1/M}} \\ 
&= \frac{p(y|m_i)}{\sqrt[M]{\prod_{j=1}^M p(y|m_j)}} \; .
\end{split}
$$

Finally, the right-hand side is equal to ratio of $m_i$'s model evidence to the geometric mean of all model evidences.