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
topic: "Probabilistic modeling"
theorem: "Posterior mean is optimal under squared error loss"

sources:
  - authors: "Gary Koop, Dale J. Poirier, Justin L. Tobias"
    year: 2007
    title: "Point estimation"
    in: "Bayesian Econometric Methods"
    pages: "Exercise 3.1, p. 31"

proof_id: "P561"
shortcut: "post-meansqr"
username: "kjpetrykowski"
---


**Theorem:** Let $\theta$ be a real [parameter](/D/para) treated as [random](/D/rvar) under a [proper prior and sampling model](/D/fpm), and let $X$ denote the [data](/D/data) which may be a [vector](/D/rvec). Assume $\mathrm{E}(\theta^2)<\infty$ under their [joint distribution](/D/dist-joint). Write the [posterior](/D/post) [mean](/D/mean) as $m(X)=\mathrm{E}(\theta \mid X)$.

An [estimator](/D/est) $\delta(X)$ is a [measurable, real-valued function](/D/meas-fct) of the data. For any such estimator with $\mathrm{E}[\delta(X)^2]<\infty$,

$$ \label{eq:identity}
  \mathrm{E}\left[(\theta-\delta(X))^2\mid X\right]
= \mathrm{Var}(\theta\mid X)+[m(X)-\delta(X)]^2 \; .
$$

Consequently, $m(X)$ uniquely minimizes posterior expected squared [loss](/D/loss-fct), apart from data outcomes having prior-predictive probability zero. It also minimizes the integrated Bayes [risk](/D/risk-fct) $r(\delta)=\mathrm{E}[(\theta-\delta(X))^2]$ over these estimators.

Here, the [prior predictive distribution](/D/prior-pred) is the distribution of $X$ obtained by first drawing $\theta$ from its prior and then drawing $X$ from the sampling model. All expectations in this theorem use this [joint Bayesian model](/D/fpm). The parameter and its estimates have the same units.

The [posterior](/D/post) [variance](/D/var) is $\mathrm{Var}(\theta \mid X)=\mathrm{E}([\theta-m(X)]^2 \mid X)$. Before observing the data, the posterior mean and variance are functions of the random data $X$: after observing $x$, they are fixed.


**Proof:** Add and subtract the posterior mean inside the estimation error:

$$ \label{eq:expand}
\begin{split}
\theta-\delta(X) &= [\theta-m(X)]+[m(X)-\delta(X)], \\
(\theta-\delta(X))^2 &= [\theta-m(X)]^2 + 2[\theta-m(X)][m(X)-\delta(X)] + [m(X)-\delta(X)]^2 \; .
\end{split}
$$

Once we condition on $X$, both $m(X)$ and $\delta(X)$ are fixed numbers. The cross-term has conditional expectation zero, because

$$ \label{eq:centered}
  \mathrm{E}[\theta-m(X) \mid X]
= \mathrm{E}(\theta \mid X)-m(X)
= 0 \; .
$$

The conditional expectation of the first squared term is equivalent to the definition of $\mathrm{Var}(\theta\mid X)$. The last squared term stays unchanged. This proves \eqref{eq:identity}.

Only the nonnegative term $[m(X)-\delta(X)]^2$ depends on the choice of the [estimator](/D/est). It is zero, exactly when $\delta(X)=m(X)$. Taking expectations over $X$ gives

$$ \label{eq:risk}
\begin{split}
r(\delta) &= \mathrm{E}[\mathrm{Var}(\theta\mid X)] + \mathrm{E}\left([m(X)-\delta(X)]^2\right), \\
r(\delta)-r(m) &= \mathrm{E}\left([m(X)-\delta(X)]^2\right)\ geq0 \; .
\end{split}
$$

The [posterior mean](/D/post) also has a finite second moment, as required. [Jensen's inequality](/P/jens-ineq), applied to the posterior distribution and the convex function $z \mapsto z^2$, gives $m(X)^2 \leq \mathrm{E}(\theta^2 \mid X)$; taking the expectation and applying the [law of total expectation](/P/mean-tot) gives $\mathrm{E}[m(X)^2] \leq \mathrm{E}(\theta^2)$. Equality of the risks occurs only when $\delta(X)=m(X)$ almost surely under the [prior predictive distribution](/D/prior-pred). This proves both conclusions.

For each posterior distribution, this is the [mean-minimizes-squared-error property](/P/mean-mse). Averaging over the data also gives the integrated-risk conclusion.