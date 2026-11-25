---
layout: proof
mathjax: true

author: "Lee Crossley"
affiliation: ""
e_mail: ""
date: 2026-11-21 22:12:03

title: "Mean and covariance of the multivariate t-distribution"
chapter: "Probability Distributions"
section: "Multivariate continuous distributions"
topic: "Multivariate t-distribution"
theorem: "Mean and covariance"

sources:
  - authors: "Taboga, Marco"
    year: 2021
    title: "Multivariate Student's t distribution"
    in: "Lectures on probability theory and mathematical statistics"
    pages: "Online appendix"
    url: "https://www.statlect.com/probability-distributions/multivariate-student-t-distribution"

proof_id: "P570"
shortcut: "mvt-cov"
username: "leecrossley"
---


**Theorem:** Let $X \sim t(\mu,\Sigma,\nu)$ be a [multivariate $t$-vector](/D/mvt), where $\mu \in \mathbb{R}^n$ is its location, $\Sigma \in \mathbb{R}^{n \times n}$ is a positive-definite scale matrix and $\nu>0$. Its [mean](/D/mean-rvec) exists exactly when $\nu>1$, and its finite [covariance matrix](/D/covmat) exists exactly when $\nu>2$. In those respective ranges, we have

$$ \label{eq:mvt-mean-cov}
\mathrm{E}[X] = \mu
\quad \text{and} \quad
\mathrm{Cov}(X) = \frac{\nu}{\nu-2}\Sigma \; .
$$


**Proof:** The [normal mixture representation](/P/mvt-mvn) gives $X$ the same distribution as $\mu+Y/\sqrt{U}$, where $Y \sim \mathcal \mathcal{N}(0,\Sigma)$ and $U \sim \mathrm{Gam}(\nu/2, \nu/2)$ and $U$ is independent of $Y$. For $s>0$, using the [gamma density](/D/gam-pdf) gives

$$ \label{eq:E-U-pow}
  \mathrm{E}[U^{-s}]
= \frac{a^a}{\Gamma(a)} \int_0^\infty u^{a-s-1} e^{-au} \, \mathrm{d}u
= a^s \frac{\Gamma(a-s)}{\Gamma(a)} \qquad (s<a) \; .
$$

For $s\geq a$, the integral diverges at zero. Each $Y_i$ is a [non-degenerate normal variable](/D/norm) with $0 < \mathrm{E}\lvert Y_i \rvert < \infty$. By [independence](/D/ind), $\mathrm{E}\lvert X_i-\mu_i \rvert = \mathrm{E}\lvert Y_i \rvert \, \mathrm{E}[U^{-1/2}]$ is finite exactly when $\nu>1$. In that case, $\mathrm{E}[Y_i] = 0$ gives $\mathrm{E}[X_i] = \mu_i$.

For $\nu>2$, use $s=1$ and $\Gamma(a) = (a-1)\Gamma(a-1)$ to obtain $\mathrm{E}[U^{-1}] = a/(a-1)$. Hence, we have

$$ \label{eq:E-X-mu-sqr}
  \mathrm{E}\left[ (X-\mu) (X-\mu)^\mathrm{T} \right]
= \mathrm{E}[ YY^\mathrm{T} ] \, \mathrm{E}[U^{-1}]
= \frac{\nu}{\nu-2}\Sigma \; .
$$

For $0 < \nu \leq 2$, every diagonal [second moment about the location](/P/momcent-2nd) is infinite because $\mathrm{E}[Y_i^2] = \Sigma_{ii} > 0$ and $\mathrm{E}[U^{-1}] = \infty$. This establishes both thresholds.