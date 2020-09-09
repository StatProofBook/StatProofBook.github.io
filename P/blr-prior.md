---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-01-03 15:26:00

title: "Conjugate prior distribution for Bayesian linear regression"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Bayesian linear regression"
theorem: "Conjugate prior distribution"

sources:
  - authors: "Bishop CM"
    year: 2006
    title: "Bayesian linear regression"
    in: "Pattern Recognition for Machine Learning"
    pages: "pp. 152-161, ex. 3.12, eq. 3.112"
    url: "https://www.springer.com/gp/book/9780387310732"

proof_id: "P9"
shortcut: "blr-prior"
username: "JoramSoch"
---


**Theorem:** Let

$$ \label{eq:GLM}
y = X \beta + \varepsilon, \; \varepsilon \sim \mathcal{N}(0, \sigma^2 V)
$$

be a [linear regression model](/D/mlr) with measured $n \times 1$ data vector $y$, known $n \times p$ design matrix $X$, known $n \times n$ covariance structure $V$ as well as unknown $p \times 1$ regression coefficients $\beta$ and unknown noise variance $\sigma^2$.

Then, the [conjugate prior](/D/prior-conj) for this model is a [normal-gamma distribution](/D/ng)

$$ \label{eq:GLM-NG-prior}
p(\beta,\tau) = \mathcal{N}(\beta; \mu_0, (\tau \Lambda_0)^{-1}) \cdot \mathrm{Gam}(\tau; a_0, b_0)
$$

where $\tau = 1/\sigma^2$ is the inverse noise variance or noise precision.


**Proof:** By definition, a [conjugate prior](/D/prior-conj) is a [prior distribution](/D/prior) that, when combined with the [likelihood function](/D/lf), leads to a [posterior distribution](/D/post) that belongs to the same family of [probability distributions](/D/dist). This is fulfilled when the prior density and the likelihood function are proportional to the model parameters in the same way, i.e. the model parameters appear in the same functional form in both.

Equation \eqref{eq:GLM} implies the following [likelihood function](/D/lf)

$$ \label{eq:GLM-LF-class}
p(y|\beta,\sigma^2) = \mathcal{N}(y; X \beta, \sigma^2 V) = \sqrt{\frac{1}{(2 \pi)^n |\sigma^2 V|}} \, \exp\left[ -\frac{1}{2 \sigma^2} (y-X\beta)^\mathrm{T} V^{-1} (y-X\beta) \right]
$$

which, for mathematical convenience, can also be parametrized as

$$ \label{eq:GLM-LF-Bayes}
p(y|\beta,\tau) = \mathcal{N}(y; X \beta, (\tau P)^{-1}) = \sqrt{\frac{|\tau P|}{(2 \pi)^n}} \, \exp\left[ -\frac{\tau}{2} (y-X\beta)^\mathrm{T} P (y-X\beta) \right]
$$

using the noise precision $\tau = 1/\sigma^2$ and the $n \times n$ precision matrix $P = V^{-1}$.

<br>
Seperating constant and variable terms, we have:

$$ \label{eq:GLM-LF-s1}
p(y|\beta,\tau) = \sqrt{\frac{|P|}{(2 \pi)^n}} \cdot \tau^{n/2} \cdot \exp\left[ -\frac{\tau}{2} (y-X\beta)^\mathrm{T} P (y-X\beta) \right] \; .
$$

Expanding the product in the exponent, we have:

$$ \label{eq:GLM-LF-s2}
p(y|\beta,\tau) = \sqrt{\frac{|P|}{(2 \pi)^n}} \cdot \tau^{n/2} \cdot \exp\left[ -\frac{\tau}{2} \left( y^\mathrm{T} P y - y^\mathrm{T} P X \beta - \beta^\mathrm{T} X^\mathrm{T} P y + \beta^\mathrm{T} X^\mathrm{T} P X \beta \right) \right] \; .
$$

Completing the square over $\beta$, finally gives

$$ \label{eq:GLM-LF-s3}
p(y|\beta,\tau) = \sqrt{\frac{|P|}{(2 \pi)^n}} \cdot \tau^{n/2} \cdot \exp\left[ -\frac{\tau}{2} \left( (\beta - \tilde{X}y)^\mathrm{T} X^\mathrm{T} P X (\beta - \tilde{X}y) - y^\mathrm{T} Q y + y^\mathrm{T} P y \right) \right]
$$

where $\tilde{X} = \left( X^\mathrm{T} P X \right)^{-1} X^\mathrm{T} P$ and $Q = \tilde{X}^\mathrm{T} \left( X^\mathrm{T} P X \right) \tilde{X}$.

<br>
In other words, the [likelihood function](/D/lf) is proportional to a power of $\tau$, times an exponential of $\tau$ and an exponential of a squared form of $\beta$, weighted by $\tau$:

$$ \label{eq:GLM-LF-s4}
p(y|\beta,\tau) \propto \tau^{n/2} \cdot \exp\left[ -\frac{\tau}{2} \left( y^\mathrm{T} P y - y^\mathrm{T} Q y \right) \right] \cdot \exp\left[ -\frac{\tau}{2} (\beta - \tilde{X}y)^\mathrm{T} X^\mathrm{T} P X (\beta - \tilde{X}y) \right] \; .
$$

The same is true for a [normal-gamma distribution](/D/ng) over $\beta$ and $\tau$

$$ \label{eq:BLR-prior-s1}
p(\beta,\tau) = \mathcal{N}(\beta; \mu_0, (\tau \Lambda_0)^{-1}) \cdot \mathrm{Gam}(\tau; a_0, b_0)
$$

the [probability density function of which](/P/ng-pdf)

$$ \label{eq:BLR-prior-s2}
p(\beta,\tau) = \sqrt{\frac{|\tau \Lambda_0|}{(2 \pi)^p}} \exp\left[ -\frac{\tau}{2} (\beta-\mu_0)^\mathrm{T} \Lambda_0 (\beta-\mu_0) \right] \cdot \frac{ {b_0}^{a_0}}{\Gamma(a_0)} \, \tau^{a_0-1} \exp[-b_0 \tau]
$$

exhibits the same proportionality

$$ \label{eq:BLR-prior-s3}
p(\beta,\tau) \propto \tau^{a_0+p/2-1} \cdot \exp[-\tau b_0] \cdot \exp\left[ -\frac{\tau}{2} (\beta-\mu_0)^\mathrm{T} \Lambda_0 (\beta-\mu_0) \right]
$$

and is therefore conjugate relative to the likelihood.