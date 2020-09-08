---
layout: proof
mathjax: true

author: "Thomas J. Faulkenberry"
affiliation: "Tarleton State University"
e_mail: "faulkenberry@tarleton.edu"
date: 2020-09-07 12:00:00

title: "Transitivity of Bayes Factors"
chapter: "Model Selection"
section: "Bayesian model selection"
topic: "Bayes factor"
theorem: "Transitivity"

sources:

proof_id: "P163"
shortcut: "bf-trans"
username: "tomfaulkenberry"
---


**Theorem:** Consider three competing [models](/D/gm) $m_1$, $m_2$, and $m3$ for observed data $y$. Then the [Bayes factor](/D/bf) for $m_1$ over $m_3$ can be written as:

$$ \label{eq:bf-trans}
\text{BF}_{13} = \text{BF}_{12}\cdot \text{BF}_{23}.
$$

**Proof:** By [definition](/D/bf), the Bayes factor $\text{BF}_{13}$ is the ratio of marginal likelihoods of data $y$ over $m_1$ and $m_3$, respectively. That is,

$$ \label{eq:bf}
\text{BF}_{13}=\frac{p(y \mid m_1)}{p(y \mid m_3)}.
$$

We can equivalently write 

$$
\begin{split}
  \text{BF}_{13} &\overset{\eqref{eq:bf}}{=} \frac{p(y \mid m_1)}{p(y \mid m_3)}\\
  &= \frac{p(y \mid m_1)}{p(y \mid m_3)} \cdot \frac{p(y \mid m_2)}{p(y \mid m_2)}\\
  &=\frac{p(y \mid m_1)}{p(y \mid m_2)} \cdot \frac{p(y \mid m_2)}{p(y \mid m_3)}\\
  &\overset{\eqref{eq:bf}}{=}\text{BF}_{12} \cdot \text{BF}_{23},
\end{split}
$$

which completes the proof of \eqref{eq:bf-trans}.