---
layout: definition
mathjax: true

author: "Thomas J. Faulkenberry"
affiliation: "Tarleton State University"
e_mail: "faulkenberry@tarleton.edu"
date: 2020-08-26 12:00:00

title: "Bayes factor"
chapter: "Model Selection"
section: "Bayesian model selection"
topic: "Bayes factor"
definition: "Definition"

sources:
  - authors: "Kass, Robert E. and Raftery, Adrian E."
    year: 1995
    title: "Bayes Factors"
    in: "Journal of the American Statistical Association"
    pages: "vol. 90, no. 430, pp. 773-795"
    url: "https://dx.doi.org/10.1080/01621459.1995.10476572"
    doi: "10.1080/01621459.1995.10476572"

def_id: "D92"
shortcut: "bf"
username: "tomfaulkenberry"
---


**Definition:** Consider two competing [generative models](/D/gm) $m_1$ and $m_2$ for observed data $y$. Then the Bayes factor in favor $m_1$ over $m_2$ is the ratio of [marginal likelihoods](/D/ml) of $m_1$ and $m_2$:

$$ \label{eq:BF}
\text{BF}_{12} = \frac{p(y\mid m_1)}{p(y\mid m_2)}.
$$

Note that by [Bayes' theorem](/P/bayes-th), the ratio of [posterior model probabilities](/D/pmp) (i.e., the posterior model odds) can be written as

$$ \label{eq:odds}
\frac{p(m_1 \mid y)}{p(m_2 \mid y)} = \frac{p(m_1)}{p(m_2)} \cdot \frac{p(y\mid m_1)}{p(y\mid m_2)},
$$

or equivalently by \eqref{eq:BF},

$$ \label{eq:odds2}
\frac{p(m_1 \mid y)}{p(m_2 \mid y)} = \frac{p(m_1)}{p(m_2)} \cdot \text{BF}_{12}.
$$

In other words, the Bayes factor can be viewed as the factor by which the prior model odds are updated (after observing data $y$) to posterior model odds – which is also expressed by [Bayes' rule](/P/bayes-rule).