---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-07-17 17:41:00

title: "Posterior credibility region against the omnibus null hypothesis for Bayesian linear regression"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Bayesian linear regression"
theorem: "Posterior credibility region excluding null hypothesis"

sources:
  - authors: "Koch, Karl-Rudolf"
    year: 2007
    title: "Multivariate t-distribution"
    in: "Introduction to Bayesian Statistics"
    pages: "Springer, Berlin/Heidelberg, 2007, eqs. 2.235, 2.236, 2.213, 2.210, 2.211, 2.183"
    url: "https://www.springer.com/de/book/9783540727231"
    doi: "10.1007/978-3-540-72726-2"

proof_id: "P134"
shortcut: "blr-pcr"
username: "JoramSoch"
---


**Theorem:** Let there be a [linear regression model](/D/mlr) with [normally distributed](/D/mvn) errors:

$$ \label{eq:GLM}
y = X \beta + \varepsilon, \; \varepsilon \sim \mathcal{N}(0, \sigma^2 V)
$$

and assume a [normal-gamma](/D/ng) [prior distribution](/D/prior) over the model parameters $\beta$ and $\tau = 1/\sigma^2$:

$$ \label{eq:GLM-NG-prior}
p(\beta,\tau) = \mathcal{N}(\beta; \mu_0, (\tau \Lambda_0)^{-1}) \cdot \mathrm{Gam}(\tau; a_0, b_0) \; .
$$

Then, the largest [posterior](/D/post) [credibility region](/D/cr) that does not contain the omnibus [null hypothesis](/D/h0)

$$ \label{eq:GLM-H0}
\mathrm{H}_0: \, C^\mathrm{T} \beta = 0
$$

is given by the [credibility level](/D/cr)

$$ \label{eq:GLM-NG-PCR}
(1-\alpha) = \mathrm{F}\left( \left[ \mu^\mathrm{T} C (C^\mathrm{T} \Sigma \, C)^{-1} C^\mathrm{T} \mu \right]/q; q, \nu \right)
$$

where $C$ is a $p \times q$ [contrast matrix](/D/con), $\mathrm{F}(x; v, w)$ is the [cumulative distribution function](/D/cdf) of the [F-distribution](/D/f) with $v$ numerator [degrees of freedom](/D/dof), $w$ denominator [degrees of freedom](/D/dof) and $\mu$, $\Sigma$ and $\nu$ can be obtained from the [posterior hyperparameters](/D/post) of Bayesian linear regression.


**Proof:** The [posterior distribution for Bayesian linear regression](/P/blr-post) is given by a [normal-gamma distribution](/D/ng) over $\beta$ and $\tau = 1/\sigma^2$

$$ \label{eq:GLM-NG-post}
p(\beta,\tau|y) = \mathcal{N}(\beta; \mu_n, (\tau \Lambda_n)^{-1}) \cdot \mathrm{Gam}(\tau; a_n, b_n)
$$

with the [posterior hyperparameters](/D/post)

$$ \label{eq:GLM-NG-post-par}
\begin{split}
\mu_n &= \Lambda_n^{-1} (X^\mathrm{T} P y + \Lambda_0 \mu_0) \\
\Lambda_n &= X^\mathrm{T} P X + \Lambda_0 \\
a_n &= a_0 + \frac{n}{2} \\
b_n &= b_0 + \frac{1}{2} (y^\mathrm{T} P y + \mu_0^\mathrm{T} \Lambda_0 \mu_0 - \mu_n^\mathrm{T} \Lambda_n \mu_n) \; .
\end{split}
$$

The [marginal distribution of a normal-gamma distribution is a multivariate t-distribution](/P/ng-marg), such that the [marginal](/D/dist-marg) [posterior](/D/post) distribution of $\beta$ is

$$ \label{eq:GLM-NG-post-beta}
p(\beta|y) = t(\beta; \mu, \Sigma, \nu)
$$

with the [posterior hyperparameters](/D/post)

$$ \label{eq:GLM-NG-post-par-beta}
\begin{split}
\mu &= \mu_n \\
\Sigma &= \left( \frac{a_n}{b_n} \Lambda_n \right)^{-1} \\
\nu &= 2 \, a_n \; .
\end{split}
$$

Define the quantity $\gamma = C^\mathrm{T} \beta$. According to the [linear transformation theorem for the multivariate t-distribution](/P/mvt-ltt), $\gamma$ also follows a [multivariate t-distribution](/D/mvt):

$$ \label{eq:GLM-NG-post-gamma}
p(\gamma|y) = t(\gamma; C^\mathrm{T} \mu, C^\mathrm{T} \Sigma \, C, \nu) \; .
$$

Because $C^\mathrm{T}$ is a $q \times p$ matrix, $\gamma$ is a $q \times 1$ vector. The [quadratic form of a multivariate t-distributed random variable has an F-distribution](/P/mvt-f), such that we can write:

$$ \label{eq:GLM-NG-post-qf}
\mathrm{QF}(\gamma) = (\gamma - C^\mathrm{T} \mu)^\mathrm{T} (C^\mathrm{T} \Sigma \, C)^{-1} (\gamma - C^\mathrm{T} \mu) /q \, \sim \mathrm{F}(q,\nu) \; .
$$

Therefore, the largest posterior credibility region for $\gamma$ which does not contain $\gamma = 0_q$ (i.e. only touches this origin point) can be obtained by plugging $\mathrm{QF}(0)$ into the cumulative distribution function of the F-distribution:

$$ \label{eq:GLM-NG-post-cred-reg-not-H0}
\begin{split}
(1-\alpha) &= \mathrm{F}\left( \mathrm{QF}(0); q, \nu \right) \\
&= \mathrm{F}\left( \left[ \mu^\mathrm{T} C (C^\mathrm{T} \Sigma \, C)^{-1} C^\mathrm{T} \mu \right]/q; q, \nu \right) \; .
\end{split}
$$