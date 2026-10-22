---
layout: proof
mathjax: true

author: "Kenneth Petrykowski"
affiliation: "University of Warsaw"
e_mail: "kenneth.petrykowski@gmail.com"
date: 2026-10-18 11:00:00

title: "Prior predictive calibration of Bayesian credible sets"
chapter: "General Theorems"
section: "Bayesian statistics"
topic: "Bayesian inference"
theorem: "Prior-averaged coverage of credible sets"

sources:
  - authors: "George Casella, Roger L. Berger"
    year: 2002
    title: "Bayesian intervals"
    in: "Statistical Inference"
    pages: "Second edition, Section 9.2.4, pp. 435-436"

proof_id: "P560"
shortcut: "cred-calibration"
username: "kjpetrykowski"
---

**Theorem:** Let $\theta$ and $X$ have a proper joint Bayesian distribution: $\theta$ has prior probability measure $\Pi$, and $X$ given $\theta$ has sampling law $P_\theta$. Let $0<\alpha<1$. Suppose $C(X)$ is a data-dependent set for which the event $\lbrace \theta\in C(X)\rbrace $ is measurable and

$$ \label{eq:cred-calibration-posterior}
\begin{gathered}
\mathrm{Pr}\{\theta\in C(X)\mid X\}=1-\alpha
\\
\text{almost surely under the prior-predictive}\\
\text{law of }X \; .
\end{gathered}
$$

The prior-predictive law is the marginal distribution of $X$ under the joint Bayesian model. Then, the joint coverage is $1-\alpha$. Equivalently, if $c(\vartheta)=P_\vartheta\lbrace \vartheta\in C(X)\rbrace $ denotes frequentist coverage at the fixed parameter value $\vartheta$,

$$ \label{eq:cred-calibration-result}
\mathrm{Pr}\{\theta\in C(X)\}
=\int c(\vartheta)\,\Pi(\mathrm{d}\vartheta)=1-\alpha \; .
$$

The integration variable $\vartheta$ distinguishes a fixed parameter value in a sampling experiment from the random parameter $\theta$ in the Bayesian joint model. The prior-weighted average $\int c(\vartheta)\Pi(\mathrm{d}\vartheta)$ means $\int c(\vartheta)\pi(\vartheta)\,\mathrm{d}\vartheta$ for a prior density $\pi$, or $\sum_\vartheta c(\vartheta)\Pi(\lbrace \vartheta\rbrace )$ for a countable prior. The theorem allows sets of any shape and requires the stated exact posterior probability.

**Proof:** Define the zero-one indicator $I=\mathbf{1}\lbrace \theta\in C(X)\rbrace $. The expectation of an event's indicator equals its probability. Conditional on the data, $\mathrm{E}(I\mid X)$ is therefore the posterior probability in \eqref{eq:cred-calibration-posterior}. [Total expectation](/P/mean-tot) gives

$$ \label{eq:cred-calibration-data-first}
\mathrm{Pr}\{\theta\in C(X)\}
=\mathrm{E}(I)
=\mathrm{E}[\mathrm{E}(I\mid X)]
=\mathrm{E}(1-\alpha)=1-\alpha \; .
$$

Alternatively, apply total expectation while conditioning first on the parameter. Once $\theta=\vartheta$ is fixed, only the data vary, and the expected indicator is $c(\vartheta)$. Thus:

$$ \label{eq:cred-calibration-parameter-first}
\mathrm{E}(I)
=\int \mathrm{E}(I\mid\theta=\vartheta)\,\Pi(\mathrm{d}\vartheta)
=\int c(\vartheta)\,\Pi(\mathrm{d}\vartheta) \; .
$$

Combining the two ways of calculating the same probability proves \eqref{eq:cred-calibration-result}.
