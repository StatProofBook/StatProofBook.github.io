---
layout: proof
mathjax: true

author: "Osvaldo Martin"
affiliation: "Aalto University"
e_mail: "aloctavodia@gmail.com"
date: 2026-11-24 09:29:00

title: "Leave-one-out posterior predictive density is harmonic mean of the likelihood"
chapter: "General Theorems"
section: "Machine learning"
topic: "Cross-validation"
theorem: "Leave-one-out predictive density"

sources:
  - authors: "Vehtari A, Mononen T, Tolvanen V, Sivula T, Winther O"
    year: 2016
    title: "Bayesian leave-one-out cross-validation approximations for Gaussian latent variable models"
    in: "Journal of Machine Learning Research"
    pages: "vol. 17, pp. 1-38, eq. 24"
    url: "https://jmlr.org/papers/v17/14-540.html"

proof_id: "P572"
shortcut: "cv-loo"
username: "aloctavodia"
---


**Theorem:** Let $y = \left\lbrace y_1, \ldots, y_n \right\rbrace$ be a [data set](/D/data) and let $y_i$ be the observation that is left out in the $i$-th [cross-validation](/D/cv) fold, with $y_{\neg i} = y \setminus \left\lbrace y_i \right\rbrace$. Assume a [generative model](/D/gm) with [model parameters](/D/para) $\theta$, [likelihood function](/D/lf) $p(y \vert \theta)$ and [prior distribution](/D/prior) $p(\theta)$, and assume that the observations are [conditionally independent](/D/ind-cond) given $\theta$. Then, the [leave-one-out](/D/loo) [posterior predictive density](/D/post-pred) of the left-out observation is the harmonic mean of its likelihood with respect to the full posterior distribution:

$$ \label{eq:lpd-hm}
p(y_i \vert y_{\neg i}) = \frac{1}{\mathrm{E}_{\theta \vert y}\!\left[ \frac{1}{p(y_i \vert \theta)} \right]} \; .
$$


**Proof:** By [the definition of conditional probability](/D/prob-cond), the leave-one-out predictive density is the ratio of the marginal likelihoods

$$ \label{eq:lpd-def}
p(y_i \vert y_{\neg i}) = \frac{p(y_i, y_{\neg i})}{p(y_{\neg i})} = \frac{p(y)}{p(y_{\neg i})} \; .
$$

The [marginal likelihood](/D/ml) of the remaining observations is obtained by marginalizing over the model parameters

$$ \label{eq:ml-loo}
p(y_{\neg i}) = \int p(y_{\neg i} \vert \theta) \, p(\theta) \, \mathrm{d}\theta \; .
$$

Because the observations are [conditionally independent](/D/ind-cond) given $\theta$, the likelihood factorizes as $p(y \vert \theta) = p(y_i \vert \theta) \, p(y_{\neg i} \vert \theta)$, such that

$$ \label{eq:ml-loo-fact}
p(y_{\neg i}) = \int \frac{1}{p(y_i \vert \theta)} \, p(y \vert \theta) \, p(\theta) \, \mathrm{d}\theta \; .
$$

By [Bayes' theorem](/P/bayes-th), $p(y \vert \theta) \, p(\theta) = p(\theta \vert y) \, p(y)$, and since $p(y)$ does not depend on $\theta$, it can be taken out of the integral

$$ \label{eq:ml-loo-post}
p(y_{\neg i}) = p(y) \int \frac{1}{p(y_i \vert \theta)} \, p(\theta \vert y) \, \mathrm{d}\theta = p(y) \, \mathrm{E}_{\theta \vert y}\!\left[ \frac{1}{p(y_i \vert \theta)} \right] \; .
$$

Inserting \eqref{eq:ml-loo-post} into \eqref{eq:lpd-def}, the marginal likelihood $p(y)$ cancels out

$$
p(y_i \vert y_{\neg i}) = \frac{1}{\mathrm{E}_{\theta \vert y}\!\left[ \frac{1}{p(y_i \vert \theta)} \right]} \; ,
$$

such that we have \eqref{eq:lpd-hm}. This completes the proof.