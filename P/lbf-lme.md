---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-02-27 20:51:00

title: "Log Bayes factor in terms of log model evidences"
chapter: "Model Selection"
section: "Bayesian model selection"
topic: "Log Bayes factor"
theorem: "Calculation from log model evidences"

sources:
  - authors: "Soch J, Allefeld C"
    year: 2018
    title: "MACS – a new SPM toolbox for model assessment, comparison and selection"
    in: "Journal of Neuroscience Methods"
    pages: "vol. 306, pp. 19-31, eq. 18"
    url: "https://www.sciencedirect.com/science/article/pii/S0165027018301468"
    doi: "10.1016/j.jneumeth.2018.05.017"

proof_id: "P64"
shortcut: "lbf-lme"
username: "JoramSoch"
---


**Theorem:** Let $m_1$ and $m_2$ be two statistical models with [log model evidences](/D/lme) $\mathrm{LME}(m_1)$ and $\mathrm{LME}(m_2)$. Then, the [log Bayes factor](/D/lbf) in favor of model $m_1$ and against model $m_2$ is the difference of the log model evidences:

$$ \label{eq:LBF-LME}
\mathrm{LBF}_{12} = \mathrm{LME}(m_1) - \mathrm{LME}(m_2) \; .
$$


**Proof:** The [Bayes factor](/D/bf) is defined as the ratio of the [model evidences](/D/ml) of $m_1$ and $m_2$

$$ \label{eq:BF}
\mathrm{BF}_{12} = \frac{p(y|m_1)}{p(y|m_2)}
$$

and the [log Bayes factor](/D/lbf) is defined as the logarithm of the Bayes factor

$$ \label{eq:LBF}
\mathrm{LBF}_{12} = \log \mathrm{BF}_{12} = \log \frac{p(y|m_1)}{p(y|m_2)} \; .
$$

With the definition of the [log model evidence](/D/lme)

$$ \label{eq:LME}
\mathrm{LME}(m) = \log p(y|m)
$$

the log Bayes factor can be expressed as:

Resolving the logarithm and applying the definition of the [log model evidence](/D/lme), we finally have:

$$ \label{eq:LBF-LME-qed}
\begin{split}
\mathrm{LBF}_{12} &= \log p(y|m_1) - \log p(y|m_2) \\
&= \mathrm{LME}(m_1) - \mathrm{LME}(m_2) \; .
\end{split}
$$