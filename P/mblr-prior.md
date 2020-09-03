---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-09-03 07:33:00

title: "Conjugate prior distribution for multivariate Bayesian linear regression"
chapter: "Statistical Models"
section: "Multivariate normal data"
topic: "Multivariate Bayesian linear regression"
theorem: "Conjugate prior distribution"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Bayesian multivariate linear regression"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-09-03"
    url: "https://en.wikipedia.org/wiki/Bayesian_multivariate_linear_regression#Conjugate_prior_distribution"

proof_id: "P159"
shortcut: "mblr-prior"
username: "JoramSoch"
---


**Theorem:** Let

$$ \label{eq:GLM}
Y = X B + E, \; E \sim \mathcal{MN}(0, V, \Sigma)
$$

be a [general linear model](/D/glm) with measured $n \times v$ data matrix $Y$, known $n \times p$ design matrix $X$, known $n \times n$ [covariance structure](/D/matn) $V$ as well as unknown $p \times v$ regression coefficients $B$ and unknown $v \times v$ [noise covariance](/D/matn) $\Sigma$.

Then, the [conjugate prior](/D/prior-conj) for this model is a [normal-Wishart distribution](/D/nw)

$$ \label{eq:GLM-NW-prior}
p(B,T) = \mathcal{MN}(B; M_0, \Lambda_0^{-1}, T^{-1}) \cdot \mathcal{W}(T; \Omega_0^{-1}, \nu_0)
$$

where $T = \Sigma^{-1}$ is the inverse [noise covariance](/D/covmat) or noise [precision matrix](/D/precmat).


**Proof:** By definition, a [conjugate prior](/D/prior-conj) is a [prior distribution](/D/prior) that, when combined with the [likelihood function](/D/lf), leads to a [posterior distribution](/D/post) that belongs to the same family of [probability distributions](/D/dist). This is fulfilled when the prior density and the likelihood function are proportional to the model parameters in the same way, i.e. the model parameters appear in the same functional form in both.

Equation \eqref{eq:GLM} implies the following [likelihood function](/D/lf)

$$ \label{eq:GLM-LF-Class}
p(Y|B,\Sigma) = \mathcal{MN}(Y; X B, V, \Sigma) = \sqrt{\frac{1}{(2 \pi)^{nv} |\Sigma|^n |V|^v}} \, \exp\left[ -\frac{1}{2} \mathrm{tr}\left( \Sigma^{-1} (Y-XB)^\mathrm{T} V^{-1} (Y-XB) \right) \right]
$$

which, for mathematical convenience, can also be parametrized as

$$ \label{eq:GLM-LF-Bayes}
p(Y|B,T) = \mathcal{MN}(Y; X B, P, T^{-1}) = \sqrt{\frac{|T|^n |P|^v}{(2 \pi)^{nv}}} \, \exp\left[ -\frac{1}{2} \mathrm{tr}\left( T (Y-XB)^\mathrm{T} P (Y-XB) \right) \right]
$$

using the $v \times v$ [precision matrix](/D/precmat) $T = \Sigma^{-1}$ and the $n \times n$ [precision matrix](/D/precmat) $P = V^{-1}$.

<br>
Seperating constant and variable terms, we have:

$$ \label{eq:GLM-LF-s1}
p(Y|B,T) = \sqrt{\frac{|P|^v}{(2 \pi)^{nv}}} \cdot |T|^{n/2} \cdot \exp\left[ -\frac{1}{2} \mathrm{tr}\left( T (Y-XB)^\mathrm{T} P (Y-XB) \right) \right] \; .
$$

Expanding the product in the exponent, we have:

$$ \label{eq:GLM-LF-s2}
p(Y|B,T) = \sqrt{\frac{|P|^v}{(2 \pi)^{nv}}} \cdot |T|^{n/2} \cdot \exp\left[ -\frac{1}{2} \mathrm{tr}\left( T \left[ Y^\mathrm{T} P Y - Y^\mathrm{T} P X B - B^\mathrm{T} X^\mathrm{T} P Y + B^\mathrm{T} X^\mathrm{T} P X B \right] \right) \right] \; .
$$

Completing the square over $\beta$, finally gives

$$ \label{eq:GLM-LF-s3}
p(Y|B,T) = \sqrt{\frac{|P|^v}{(2 \pi)^{nv}}} \cdot |T|^{n/2} \cdot \exp\left[ -\frac{1}{2} \mathrm{tr}\left( T \left[ (B - \tilde{X}Y)^\mathrm{T} X^\mathrm{T} P X (B - \tilde{X}Y) - Y^\mathrm{T} Q Y + Y^\mathrm{T} P Y \right] \right) \right]
$$

where $\tilde{X} = \left( X^\mathrm{T} P X \right)^{-1} X^\mathrm{T} P$ and $Q = \tilde{X}^\mathrm{T} \left( X^\mathrm{T} P X \right) \tilde{X}$.

<br>
In other words, the [likelihood function](/D/lf) is proportional to a power of the determinant of $T$, times an exponential of the trace of $T$ and an exponential of the trace of a squared form of $B$, weighted by $T$:

$$ \label{eq:GLM-LF-s4}
p(Y|B,T) \propto |T|^{n/2} \cdot \exp\left[ -\frac{1}{2} \mathrm{tr}\left( T \left[ Y^\mathrm{T} P Y - Y^\mathrm{T} Q Y \right] \right) \right] \cdot \exp\left[ -\frac{1}{2} \mathrm{tr}\left( T \left[ (B - \tilde{X}Y)^\mathrm{T} X^\mathrm{T} P X (B - \tilde{X}Y) \right] \right) \right] \; .
$$

The same is true for a [normal-Wishart distribution](/D/nw) over $B$ and $T$

$$ \label{eq:MBLR-prior-s1}
p(B,T) = \mathcal{MN}(B; M_0, \Lambda_0^{-1}, T^{-1}) \cdot \mathcal{W}(T; \Omega_0^{-1}, \nu_0)
$$

the [probability density function of which](/P/nw-pdf)

$$ \label{eq:MBLR-prior-s2}
p(B,T) = \sqrt{\frac{|T|^p |\Lambda_0|^v}{(2 \pi)^{pv}}} \, \exp\left[ -\frac{1}{2} \mathrm{tr}\left( T (B-M_0)^\mathrm{T} \Lambda_0 (B-M_0) \right) \right] \cdot \frac{1}{\Gamma_v \left( \frac{\nu_0}{2} \right)} \sqrt{\frac{|\Omega_0|^{\nu_0}}{2^{\nu_0 v}}} |T|^{(\nu_0-v-1)/2} \exp\left[ -\frac{1}{2} \mathrm{tr}\left( \Omega_0 T \right) \right]
$$

exhibits the same proportionality

$$ \label{eq:MBLR-prior-s3}
p(B,T) \propto |T|^{(\nu_0+p-v-1)/2} \cdot \exp\left[ -\frac{1}{2} \mathrm{tr}\left( T \Omega_0 \right) \right] \cdot \exp\left[ -\frac{1}{2} \mathrm{tr}\left( T \left[ (B-M_0)^\mathrm{T} \Lambda_0 (B-M_0) \right] \right) \right]
$$

and is therefore conjugate relative to the likelihood.