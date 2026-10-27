---
layout: proof
mathjax: true

author: "Kenneth Petrykowski"
affiliation: "University of Warsaw"
e_mail: "kenneth.petrykowski@gmail.com"
date: 2026-10-18 11:00:00

title: "Coverage of Bayesian credible sets when averaging over the prior distribution"
chapter: "General Theorems"
section: "Estimation theory"
topic: "Interval estimates"
theorem: "Prior predictive calibration of Bayesian credible sets"

sources:
  - authors: "George Casella, Roger L. Berger"
    year: 2002
    title: "Bayesian intervals"
    in: "Statistical Inference"
    pages: "Second edition, Section 9.2.4, pp. 435-436"

proof_id: "P560"
shortcut: "crs-priorpred"
username: "kjpetrykowski"
---


**Theorem:** Let $\theta$ and $X$ have a proper [joint Bayesian distribution](/D/dist-joint): $\theta$ has [prior probability](/D/prior) measure $\Pi$, and $X$ given $\theta$ has [sampling law](/D/lf) $P_\theta$. Let $0<\alpha<1$. Suppose $C(X)$ is a data-dependent set for which the event $\lbrace \theta\in C(X)\rbrace$ is measurable and

$$ \label{eq:posterior}
\begin{gathered}
\mathrm{Pr}\left( \theta \in C(X) \mid X \right) = 1-\alpha \\
\text{almost surely under the prior-predictive law of} \; X \; .
\end{gathered}
$$

The [prior predictive law](/D/prior-pred) is the [marginal distribution](/D/dist-marg) of $X$ under the [joint Bayesian model](/D/fpm). Then, the joint coverage is $1-\alpha$. Equivalently, if $c(\vartheta) = P_\vartheta(\vartheta \in C(X))$ denotes frequentist coverage at the fixed parameter value $\vartheta$, then

$$ \label{eq:result}
  \mathrm{Pr}\left( \theta \in C(X) \right)
= \int c(\vartheta) \, \Pi(\mathrm{d}\vartheta) = 1-\alpha \; .
$$

The integration variable $\vartheta$ distinguishes a fixed parameter value in a sampling experiment from the random parameter $\theta$ in the Bayesian joint model. The prior-weighted average $\int c(\vartheta)\Pi(\mathrm{d}\vartheta)$ means $\int c(\vartheta)\pi(\vartheta)\,\mathrm{d}\vartheta$ for a prior density $\pi$, or $\sum_\vartheta c(\vartheta)\Pi(\lbrace \vartheta\rbrace )$ for a countable prior. The theorem allows sets of any shape and requires the stated exact posterior probability.


**Proof:** Define the zero-one indicator $I = \mathbf{1}_{\lbrace \theta \in C(X) \rbrace}$. The [expectation of an event's indicator equals its probability](/P/bern-mean). Conditional on the data, $\mathrm{E}(I \mid X)$ is therefore the [posterior probability](/D/post) in \eqref{eq:posterior}. Applying the [law of total expectation](/P/mean-tot) gives

$$ \label{eq:data-first}
  \mathrm{Pr}\left( \theta \in C(X) \right)
= \mathrm{E}(I)
= \mathrm{E}[\mathrm{E}(I\ mid X)]
= \mathrm{E}(1-\alpha)=1-\alpha \; .
$$

Alternatively, apply [total expectation](/P/mean-tot) while conditioning first on the parameter. Once $\theta=\vartheta$ is fixed, only the [data](/D/data) vary, and the [expected](/D/mean) indicator is $c(\vartheta)$. Thus:

$$ \label{eq:parameter-first}
\mathrm{E}(I)
=\int \mathrm{E}(I\mid\theta=\vartheta)\,\Pi(\mathrm{d}\vartheta)
=\int c(\vartheta)\,\Pi(\mathrm{d}\vartheta) \; .
$$

Combining \eqref{eq:data-first} and \eqref{eq:parameter-first}, this proves \eqref{eq:result}.