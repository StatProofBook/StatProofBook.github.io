---
layout: proof
mathjax: true

author: "Kenneth Petrykowski"
affiliation: "University of Warsaw"
e_mail: "kenneth.petrykowski@gmail.com"
date: 2026-10-18 22:15:00

title: "Posterior mean optimality under squared error loss"
chapter: "General Theorems"
section: "Bayesian statistics"
topic: "Bayesian inference"
theorem: "Posterior mean optimality under squared error loss"

sources:
  - authors: "Gary Koop, Dale J. Poirier, Justin L. Tobias"
    year: 2007
    title: "Point estimation"
    in: "Bayesian Econometric Methods"
    pages: "Exercise 3.1, p. 31"

proof_id: "P561"
shortcut: "bayes-sqerr"
username: "kjpetrykowski"
---

**Theorem:** Let $\theta$ be a real parameter treated as random under a proper prior and sampling model, and let $X$ denote the data, which may be a vector. Assume $\mathrm{E}(\theta^2)<\infty$ under their joint distribution. Write $m(X)=\mathrm{E}(\theta\mid X)$.

An estimator $\delta(X)$ is a measurable, real-valued function of the data. For any such estimator with $\mathrm{E}[\delta(X)^2]<\infty$,

$$ \label{eq:bayes-sqerr-identity}
\mathrm{E}\left[(\theta-\delta(X))^2\mid X\right]
=\mathrm{Var}(\theta\mid X)+[m(X)-\delta(X)]^2 \; .
$$

Consequently, $m(X)$ uniquely minimizes posterior expected squared loss, apart from data outcomes having prior-predictive probability zero. It also minimizes the integrated Bayes risk $r(\delta)=\mathrm{E}[(\theta-\delta(X))^2]$ over these estimators.

Here, the prior-predictive distribution is the distribution of $X$ obtained by first drawing $\theta$ from its prior and then drawing $X$ from the sampling model. All expectations in this theorem use this joint Bayesian model. The parameter and its estimates have the same units.

The posterior variance is $\mathrm{Var}(\theta\mid X)=\mathrm{E}([\theta-m(X)]^2\mid X)$. Before observing the data, the posterior mean and variance are functions of the random data $X$: after observing $x$, they are numbers.

**Proof:** Add and subtract the posterior mean inside the estimation error:

$$ \label{eq:bayes-sqerr-expand}
\begin{split}
\theta-\delta(X)&=[\theta-m(X)]+[m(X)-\delta(X)],\\
(\theta-\delta(X))^2
&=[\theta-m(X)]^2
 +2[\theta-m(X)][m(X)-\delta(X)]\\
&\quad{}+[m(X)-\delta(X)]^2 \; .
\end{split}
$$

Once we condition on $X$, both $m(X)$ and $\delta(X)$ are fixed numbers. The cross term has conditional expectation zero because

$$ \label{eq:bayes-sqerr-centered}
\mathrm{E}[\theta-m(X)\mid X]
=\mathrm{E}(\theta\mid X)-m(X)=0 \; .
$$

The conditional expectation of the first squared term is the definition of $\mathrm{Var}(\theta\mid X)$. The last squared term stays unchanged. This proves \eqref{eq:bayes-sqerr-identity}.

Only the nonnegative term $[m(X)-\delta(X)]^2$ depends on the choice of estimator. It is zero exactly when $\delta(X)=m(X)$. Taking expectations over $X$ gives

$$ \label{eq:bayes-sqerr-risk}
\begin{split}
r(\delta)
&=\mathrm{E}[\mathrm{Var}(\theta\mid X)]
 +\mathrm{E}\left([m(X)-\delta(X)]^2\right),\\
r(\delta)-r(m)
&=\mathrm{E}\left([m(X)-\delta(X)]^2\right)\geq0 \; .
\end{split}
$$

The posterior mean also has a finite second moment, as required. [Jensen's inequality](/P/jens-ineq), applied to the posterior distribution and the convex function $z\mapsto z^2$, gives $m(X)^2\leq\mathrm{E}(\theta^2\mid X)$; averaging gives $\mathrm{E}[m(X)^2]\leq\mathrm{E}(\theta^2)$. Equality of the risks occurs only when $\delta(X)=m(X)$ almost surely under the prior-predictive distribution. This proves both conclusions.

For each posterior distribution, this is the [mean-minimizes-squared-error property](/P/mean-mse). Averaging over the data also gives the integrated-risk conclusion.
