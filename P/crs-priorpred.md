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

**Theorem:** Draw the parameter $\theta$ from the [prior distribution](/D/prior) $\Pi$ of total probability one. Given the drawn value $\theta=\vartheta$, draw the data $X$ from $P\_\vartheta$. For each possible observation $x$, a procedure returns a set $C(x)$ of parameter values. Assume membership is measurable in the parameter and the data together, so we can assign a probability to the event that the set covers the parameter, $\theta\in C(X)$.

Fix $0<\alpha<1$. Suppose the procedure returns a [credible set](/D/crs) with [posterior probability](/D/post) exactly $1-\alpha$ [with probability one](/D/almost-sure), meaning that the exceptional data values together have probability zero under the [prior predictive distribution](/D/prior-pred) of $X$:

$$ \label{eq:posterior}
\mathrm{Pr}(\theta\in C(X)\mid X)=1-\alpha
\quad\text{with probability one} \; .
$$

Then the joint probability of coverage is

$$ \label{eq:result}
\mathrm{Pr}(\theta\in C(X))=1-\alpha \; .
$$

For a fixed parameter value $\vartheta$, write the coverage over repeated draws of $X$ as

$$ \label{eq:fixed-coverage}
c(\vartheta)=P_\vartheta\lbrace\vartheta\in C(X)\rbrace \; .
$$

Individual values of $c(\vartheta)$ may differ from $1-\alpha$. Their average over the prior satisfies

$$ \label{eq:averaged-coverage}
\int c(\vartheta)\,\Pi(\mathrm{d}\vartheta)=1-\alpha \; .
$$


**Proof:** Let $I$ be the [indicator](/D/ind-fct) of coverage, equal to 1 when the returned set contains the parameter and 0 otherwise:

$$ \label{eq:indicator}
I=\mathbf{1}_{\lbrace\theta\in C(X)\rbrace} \; .
$$

[The expectation of $I$ is the probability of coverage](/P/bern-mean). Conditioning on the data gives the posterior probability in \eqref{eq:posterior}:

$$ \label{eq:indicator-mean}
\mathrm{E}(I\mid X)
=\mathrm{Pr}(\theta\in C(X)\mid X)
=1-\alpha
\quad\text{with probability one} \; .
$$

By the [law of total expectation](/P/mean-tot),

$$ \label{eq:data-first}
\begin{split}
\mathrm{Pr}(\theta\in C(X))
&=\mathrm{E}(I)\\
&=\mathrm{E}[\mathrm{E}(I\mid X)]\\
&=\mathrm{E}(1-\alpha)=1-\alpha \; .
\end{split}
$$

Now condition on the parameter. Given $\theta=\vartheta$, the data have distribution $P\_\vartheta$, so the conditional expectation of $I$ is $c(\vartheta)$ except on a set of parameter values of prior probability zero:

$$ \label{eq:conditional-coverage}
\mathrm{E}(I\mid\theta=\vartheta)
=P_\vartheta\lbrace\vartheta\in C(X)\rbrace
=c(\vartheta) \; .
$$

Average over $\vartheta$ using the prior weights $\Pi(\mathrm{d}\vartheta)$. For a discrete prior this gives a weighted sum, and for a prior with density $\pi$ the weight is $\pi(\vartheta)\,\mathrm{d}\vartheta$:

$$ \label{eq:parameter-first}
\mathrm{E}(I)
=\int\mathrm{E}(I\mid\theta=\vartheta)\,\Pi(\mathrm{d}\vartheta)
=\int c(\vartheta)\,\Pi(\mathrm{d}\vartheta) \; .
$$

Both \eqref{eq:data-first} and \eqref{eq:parameter-first} equal $\mathrm{E}(I)$, which gives \eqref{eq:averaged-coverage}. If the posterior probability in \eqref{eq:posterior} is only known to be at least $1-\alpha$ with probability one, the same averaging gives joint coverage of at least $1-\alpha$.
