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
topic: "Log-evidence derivatives"
theorem: "Log Bayes factor in terms of log model evidences"

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
\mathrm{LBF}_{1,2} = \mathrm{LME}(m_1) - \mathrm{LME}(m_2) \; .
$$


**Proof:** The [log Bayes factor](/D/lbf) (LBF) is defined as the logarithm of the [Bayes factor](/D/bf) (BF) which is defined as the posterior odds ratio when both models are equally likely apriori:

$$ \label{eq:LBF-s1}
\begin{split}
\mathrm{LBF}_{1,2} &= \log \mathrm{BF}_{1,2} \\
&= \log \frac{p(m_1|y)}{p(m_2|y)} \; .
\end{split}
$$

Plugging in the posterior odds ratio according to [Bayes' rule](/P/bayes-rule), we have

$$ \label{eq:LBF-s2}
\mathrm{LBF}_{1,2} = \log \left[ \frac{p(y|m_1)}{p(y|m_2)} \cdot \frac{p(m_1)}{p(m_2)} \right] \; .
$$

When both models are equally likely apriori, the prior odds ratio is one, such that

$$ \label{eq:LBF-s3}
\mathrm{LBF}_{1,2} = \log \frac{p(y|m_1)}{p(y|m_2)} \; .
$$

Resolving the logarithm and applying the definition of the [log model evidence](/D/lme), we finally have:

$$ \label{eq:LBF-s4}
\begin{split}
\mathrm{LBF}_{1,2} &= \log p(y|m_1) - \log p(y|m_2) \\
&= \mathrm{LME}(m_1) - \mathrm{LME}(m_2) \; .
\end{split}
$$