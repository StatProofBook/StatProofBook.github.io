---
layout: proof
mathjax: true

author: "Osvaldo Martin"
affiliation: "Aalto University"
e_mail: "aloctavodia@gmail.com"
date: 2026-11-21 11:36:00

title: "Importance weights for cross-validation"
chapter: "General Theorems"
section: "Bayesian statistics"
topic: "Probabilistic modeling"
theorem: "Importance weights for cross-validation"

sources:
  - authors: "Vehtari A, Mononen T, Tolvanen V, Sivula T, Winther O"
    year: 2016
    title: "Bayesian leave-one-out cross-validation approximations for Gaussian latent variable models"
    in: "Journal of Machine Learning Research"
    pages: "vol. 17, pp. 1-38, eq. 42"
    url: "https://jmlr.org/papers/v17/14-540.html"

proof_id: "P566"
shortcut: "cv-iw"
username: "aloctavodia"
---


**Theorem:** Let $y = \left\lbrace y_1, \ldots, y_n \right\rbrace$ be a [data set](/D/data) and let $y_i$ be the observation that is left out in the $i$-th fold of a [cross-validation](/D/cvlme), with $y_{\neg i} = y \setminus \left\lbrace y_i \right\rbrace$. Assume a [generative model](/D/gm) with [model parameters](/D/para) $\theta$, [likelihood function](/D/lf) $p(y \vert \theta)$ and [prior distribution](/D/prior) $p(\theta)$, and assume that the observations are conditionally independent given $\theta$. Then, the importance weights relating the leave-one-out posterior distribution to the full [posterior distribution](/D/post) are proportional to the reciprocal of the likelihood of the left-out observation:

$$ \label{eq:iw-prop}
w_i(\theta) \propto \frac{1}{p(y_i \vert \theta)} \; .
$$


**Proof:** By [Bayes' theorem](/P/bayes-th), the full posterior is proportional to the likelihood times the prior

$$ \label{eq:post-full}
p(\theta \vert y) \propto p(y \vert \theta) \, p(\theta) \; ,
$$

and the leave-one-out posterior is

$$ \label{eq:post-loo}
p(\theta \vert y_{\neg i}) \propto p(y_{\neg i} \vert \theta) \, p(\theta) \; ,
$$

where the marginal likelihoods $p(y)$ and $p(y_{\neg i})$ are dropped because they do not depend on $\theta$.

The importance weights are defined as the ratio of the leave-one-out posterior to the full posterior:

$$ \label{eq:iw-der}
w_i(\theta) = \frac{p(\theta \vert y_{\neg i})}{p(\theta \vert y)} \propto \frac{p(y_{\neg i} \vert \theta) \, p(\theta)}{p(y \vert \theta) \, p(\theta)} \; .
$$

The prior terms $p(\theta)$ cancel out, leaving only the likelihood terms:

$$
w_i(\theta) \propto \frac{p(y_{\neg i} \vert \theta)}{p(y \vert \theta)} \; .
$$

Because the observations are conditionally independent given $\theta$, the likelihood is a product over observations, so that

$$
w_i(\theta) \propto \frac{\prod_{j \neq i} p(y_j \vert \theta)}{\prod_{j=1}^{n} p(y_j \vert \theta)} \; .
$$

All terms in the numerator and the denominator cancel out except the one for the left-out observation $y_i$, which remains in the denominator:

$$
w_i(\theta) \propto \frac{1}{p(y_i \vert \theta)} \; ,
$$

as stated in \eqref{eq:iw-prop}. This completes the proof.