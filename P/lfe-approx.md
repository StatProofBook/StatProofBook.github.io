---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2023-09-15 16:33:38

title: "Approximation of log family evidences based on log model evidences"
chapter: "Model Selection"
section: "Bayesian model selection"
topic: "Family evidence"
theorem: "Approximation of log family evidences"

sources:
  - authors: "Soch J"
    year: 2018
    title: "cvBMS and cvBMA: filling in the gaps"
    in: "arXiv stat.ME"
    pages: "1807.01585, sect. 2.3, pp. 6-7, eq. 32"
    url: "https://arxiv.org/abs/1807.01585"

proof_id: "P415"
shortcut: "lfe-approx"
username: "JoramSoch"
---


**Theorem:** Let $m_1, \ldots, m_M$ be $M$ statistical models with [log model evidences](/D/lme) $\mathrm{LME}(m_1), \ldots, \mathrm{LME}(m_M)$ and belonging to $F$ [mutually exclusive](/D/exc) [model families](/D/fe) $f_1, \ldots, f_F$.

1) Then, the [log family evidences](/D/lfe) can be approximated as

$$ \label{eq:LFE-approx-v1}
\mathrm{LFE}(f_j) = \mathrm{L}^{*}(f_j) + \log \left[ \sum_{m_i \in f_j} \exp[\mathrm{L}'(m_i)] \cdot p(m_i|f_j) \right]
$$

where $\mathrm{L}^{*}(f_j)$ is the maximum log model evidence in family $f_j$, $\mathrm{L}'(m_i)$ is the difference of each log model evidence to each family's maximum and $p(m_i \vert f_j)$ are [within-family prior model probabilities](/P/fe-der).

2) Under the condition that prior model probabilities are equal within model families, the approximation simplifies to

$$ \label{eq:LFE-approx-v2}
\mathrm{LFE}(f_j) = \mathrm{L}^{*}(f_j) + \log \sum_{m_i \in f_j} \exp[\mathrm{L}'(m_i)] - \log M_j
$$

where $M_j$ is the number of models within family $f_j$.


**Proof:** The [log family evidence is given in terms of log model evidences](/P/lfe-lme) as

$$ \label{eq:LFE-LME}
\mathrm{LFE}(f_j) = \log \sum_{m_i \in f_j} \left[ \exp[\mathrm{LME}(m_i)] \cdot p(m_i|f_j) \right] \; .
$$

Often, especially for complex models or many observations, [log model evidences](/D/lme) are highly negative, such that calculation of the term $\exp[\mathrm{LME}(m_i)]$ in modern computers will give [model evidences](/D/me) as zero, making calculation of LFEs impossible.

1) As a solution, we select the maximum LME within each family

$$ \label{eq:LME-max}
\mathrm{L}^{*}(f_j) = \max_{m_i \in f_j} \left[ \mathrm{LME}(m_i) \right]
$$

and define differences between LMEs and maximum LME as

$$ \label{eq:LME-diff}
\mathrm{L}'(m_i) = \mathrm{LME}(m_i) - \mathrm{L}^{*}(f_j) \; .
$$

In this way, only the differences $\mathrm{L}'(m_i)$ need to be
exponentiated. If such a difference is highly negative, this model's contribution to the LFE will be zero -- making this an approximation. However, the model is also much less evident that the family's best model in this case -- making the approximation acceptable.

Using the relation \eqref{eq:LME-diff}, equation \eqref{eq:LFE-LME} can be reworked into

$$ \label{eq:LFE-approx-v1-qed}
\begin{split}
\mathrm{LFE}(f_j) &= \log \sum_{m_i \in f_j} \exp[\mathrm{L}'(m_i) + \mathrm{L}^{*}(f_j)] \cdot p(m_i|f_j) \\
&= \log \sum_{m_i \in f_j} \exp[\mathrm{L}'(m_i)] \cdot \exp[\mathrm{L}^{*}(f_j)] \cdot p(m_i|f_j) \\
&= \log \left[ \exp[\mathrm{L}^{*}(f_j)] \cdot \sum_{m_i \in f_j} \exp[\mathrm{L}'(m_i)] \cdot p(m_i|f_j) \right] \\
&= \mathrm{L}^{*}(f_j) + \log \left[ \sum_{m_i \in f_j} \exp[\mathrm{L}'(m_i)] \cdot p(m_i|f_j) \right] \; .
\end{split}
$$

2) Under uniform [within-family prior model probabilities](/P/fe-der), we have

$$ \label{eq:PMP-uni}
p(m_i|f_j) = \frac{1}{M_j} \quad \text{for all} \quad m_i \in f_j \; ,
$$

such that the approximated [log family evidences](/D/lfe) becomes

$$ \label{eq:LFE-approx-v2-qed}
\begin{split}
\mathrm{LFE}(f_j) &= \mathrm{L}^{*}(f_j) + \log \left[ \sum_{m_i \in f_j} \exp[\mathrm{L}'(m_i)] \cdot \frac{1}{M_j} \right] \\
&= \mathrm{L}^{*}(f_j) + \log \left[ \frac{1}{M_j} \cdot \sum_{m_i \in f_j} \exp[\mathrm{L}'(m_i)] \right] \\
&= \mathrm{L}^{*}(f_j) + \log \sum_{m_i \in f_j} \exp[\mathrm{L}'(m_i)] - \log M_j \; .
\end{split}
$$