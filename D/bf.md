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


**Definition:** Consider two competing [generative models](/D/gm) $\mathcal{M}_1$ and $\mathcal{M}_2$ for observed data $y$. Then the Bayes factor in favor $\mathcal{M}_1$ over $\mathcal{M}_2$ is the ratio of [marginal likelihoods](/D/ml) of $\mathcal{M}_1$ and $\mathcal{M}_2$:

$$ \label{eq:BF}
\text{BF}_{12} = \frac{p(y\mid \mathcal{M}_1)}{p(y\mid \mathcal{M}_2)}.
$$

Note: by [Bayes Theorem](/P/bayes-th), the ratio of [posterior model probabilities](/D/pmp) (i.e., the posterior model odds) can be written as

$$ \label{eq:odds}
\frac{p(\mathcal{M}_1\mid y)}{p(\mathcal{M}_2\mid y)} = \frac{p(\mathcal{M}_1)}{p(\mathcal{M}_2)} \cdot \frac{p(y\mid \mathcal{M}_1)}{p(y\mid \mathcal{M}_2)},
$$

or equivalently by \eqref{eq:BF},

$$ \label{eq:odds2}
\frac{p(\mathcal{M}_1\mid y)}{p(\mathcal{M}_2\mid y)} = \frac{p(\mathcal{M}_1)}{p(\mathcal{M}_2)} \cdot \text{BF}_{12}.
$$

In other words, the Bayes factor can be viewed as the factor by which the prior model odds are updated (after observing data $y$) to posterior model odds.
