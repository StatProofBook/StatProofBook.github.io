---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2024-01-19 08:42:32

title: "Conjugate prior distribution for Bayesian linear regression with known covariance"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Bayesian linear regression with known covariance"
theorem: "Conjugate prior distribution"

sources:
  - authors: "Bishop CM"
    year: 2006
    title: "Bayesian linear regression"
    in: "Pattern Recognition for Machine Learning"
    pages: "pp. 152-161, eq. 3.48"
    url: "https://www.springer.com/gp/book/9780387310732"
  - authors: "Penny WD"
    year: 2012
    title: "Comparing Dynamic Causal Models using AIC, BIC and Free Energy"
    in: "NeuroImage"
    pages: "vol. 59, iss. 2, pp. 319-330, eq. 9"
    url: "https://www.sciencedirect.com/science/article/pii/S1053811911008160"
    doi: "10.1016/j.neuroimage.2011.07.039"

proof_id: "P432"
shortcut: "blrkc-prior"
username: "JoramSoch"
---


**Theorem:** Let

$$ \label{eq:GLM}
y = X \beta + \varepsilon, \; \varepsilon \sim \mathcal{N}(0, \Sigma)
$$

be a [linear regression model](/D/mlr) with measured $n \times 1$ data vector $y$, known $n \times p$ design matrix $X$ and known $n \times n$ covariance matrix $\Sigma$ as well as unknown $p \times 1$ regression coefficients $\beta$.

Then, the [conjugate prior](/D/prior-conj) for this model is a [multivariate normal distribution](/D/mvn)

$$ \label{eq:GLM-N-prior}
p(\beta) = \mathcal{N}(\beta; \mu_0, \Sigma_0) \; .
$$


**Proof:** By definition, a [conjugate prior](/D/prior-conj) is a [prior distribution](/D/prior) that, when combined with the [likelihood function](/D/lf), leads to a [posterior distribution](/D/post) that belongs to the same family of [probability distributions](/D/dist). This is fulfilled when the prior density and the likelihood function are proportional to the model parameters in the same way, i.e. the model parameters appear in the same functional form in both.

Equation \eqref{eq:GLM} implies the following [likelihood function](/D/lf):

$$ \label{eq:GLM-LF}
p(y|\beta) = \mathcal{N}(y; X \beta, \Sigma) = \sqrt{\frac{1}{(2 \pi)^n |\Sigma|}} \, \exp\left[ -\frac{1}{2} (y-X\beta)^\mathrm{T} \Sigma^{-1} (y-X\beta) \right] \; .
$$

Expanding the product in the exponent, we have:

$$ \label{eq:GLM-LF-s1}
p(y|\beta) = \sqrt{\frac{1}{(2 \pi)^n |\Sigma|}} \cdot \exp\left[ -\frac{1}{2} \left( y^\mathrm{T} \Sigma^{-1} y - y^\mathrm{T} \Sigma^{-1} X \beta - \beta^\mathrm{T} X^\mathrm{T} \Sigma^{-1} y + \beta^\mathrm{T} X^\mathrm{T} \Sigma^{-1} X \beta \right) \right] \; .
$$

Completing the square over $\beta$, one obtains

$$ \label{eq:GLM-LF-s2}
p(y|\beta) = \sqrt{\frac{1}{(2 \pi)^n |\Sigma|}} \cdot \exp\left[ -\frac{1}{2} \left( (\beta - \tilde{X}y)^\mathrm{T} X^\mathrm{T} \Sigma^{-1} X (\beta - \tilde{X}y) - y^\mathrm{T} Q y + y^\mathrm{T} \Sigma^{-1} y \right) \right]
$$

where $\tilde{X} = \left( X^\mathrm{T} \Sigma^{-1} X \right)^{-1} X^\mathrm{T} \Sigma^{-1}$ and $Q = \tilde{X}^\mathrm{T} \left( X^\mathrm{T} \Sigma^{-1} X \right) \tilde{X}$.

<br>
Separating constant and variable terms, we get:

$$ \label{eq:GLM-LF-s3}
p(y|\beta) = \sqrt{\frac{1}{(2 \pi)^n |\Sigma|}} \cdot \exp\left[ -\frac{1}{2} \left( y^\mathrm{T} Q y + y^\mathrm{T} \Sigma^{-1} y \right) \right] \cdot \exp\left[ -\frac{1}{2} (\beta - \tilde{X}y)^\mathrm{T} X^\mathrm{T} \Sigma^{-1} X (\beta - \tilde{X}y) \right] \; .
$$

In other words, the [likelihood function](/D/lf) is proportional to an exponential of a squared form of $\beta$:

$$ \label{eq:GLM-LF-s4}
p(y|\beta) \propto \exp\left[ -\frac{1}{2} (\beta - \tilde{X}y)^\mathrm{T} X^\mathrm{T} \Sigma^{-1} X (\beta - \tilde{X}y) \right] \; .
$$

The same is true for a [multivariate normal distribution](/D/mvn) over $\beta$

$$ \label{eq:GLM-N-prior-s1}
p(\beta) = \mathcal{N}(\beta; \mu_0, \Sigma_0)
$$

the [probability density function of which](/P/mvn-pdf)

$$ \label{eq:GLM-N-prior-s2}
p(\beta) = \sqrt{\frac{1}{(2 \pi)^p |\Sigma_0|}} \cdot \exp\left[ -\frac{1}{2} (\beta-\mu_0)^\mathrm{T} \Sigma_0^{-1} (\beta-\mu_0) \right]
$$

exhibits the same proportionality

$$ \label{eq:GLM-N-prior-s3}
p(\beta) \propto \exp\left[ -\frac{1}{2} (\beta-\mu_0)^\mathrm{T} \Sigma_0^{-1} (\beta-\mu_0) \right]
$$

and is therefore conjugate relative to the likelihood.