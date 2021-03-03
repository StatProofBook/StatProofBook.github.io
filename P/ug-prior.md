---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-03-03 08:54:00

title: "Conjugate prior distribution for the univariate Gaussian"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Univariate Gaussian"
theorem: "Conjugate prior distribution"

sources:
  - authors: "Bishop CM"
    year: 2006
    title: "Bayesian inference for the Gaussian"
    in: "Pattern Recognition for Machine Learning"
    pages: "pp. 97-102, eq. 2.154"
    url: "http://users.isr.ist.utl.pt/~wurmd/Livros/school/Bishop%20-%20Pattern%20Recognition%20And%20Machine%20Learning%20-%20Springer%20%202006.pdf"

proof_id: "P201"
shortcut: "ug-prior"
username: "JoramSoch"
---


**Theorem:** Let

$$ \label{eq:ug}
y = \left\lbrace y_1, \ldots, y_n \right\rbrace, \quad y_i \sim \mathcal{N}(\mu, \sigma^2), \quad i = 1, \ldots, n
$$

be a [univariate Gaussian data set](/D/ug) with unknown mean $\mu$ and unknown variance $\sigma^2$. Then, the [conjugate prior](/D/prior-conj) for this model is a [normal-gamma distribution](/D/ng)

$$ \label{eq:UG-NG-prior}
p(\mu,\tau) = \mathcal{N}(\mu; \mu_0, (\tau \lambda_0)^{-1}) \cdot \mathrm{Gam}(\tau; a_0, b_0)
$$

where $\tau = 1/\sigma^2$ is the inverse variance or precision.


**Proof:** By definition, a [conjugate prior](/D/prior-conj) is a [prior distribution](/D/prior) that, when combined with the [likelihood function](/D/lf), leads to a [posterior distribution](/D/post) that belongs to the same family of [probability distributions](/D/dist). This is fulfilled when the prior density and the likelihood function are proportional to the model model parameters in the same way, i.e. the model parameters appear in the same functional form in both.

Equation \eqref{eq:ug} implies the following [likelihood function](/D/lf)

$$ \label{eq:UG-LF-class}
\begin{split}
p(y|\mu,\sigma^2) &= \prod_{i=1}^{n} \mathcal{N}(y_i; \mu, \sigma^2) \\
&= \prod_{i=1}^{n} \frac{1}{\sqrt{2 \pi} \sigma} \cdot \exp\left[ -\frac{1}{2} \left( \frac{y_i-\mu}{\sigma} \right)^2 \right] \\
&= \frac{1}{(\sqrt{2 \pi \sigma^2})^n} \cdot \exp\left[ -\frac{1}{2 \sigma^2} \sum_{i=1}^{n} \left( y_i-\mu \right)^2 \right]
\end{split}
$$

which, for mathematical convenience, can also be parametrized as

$$ \label{eq:UG-LF-Bayes}
\begin{split}
p(y|\mu,\tau) &= \prod_{i=1}^{n} \mathcal{N}(y_i; \mu, \tau^{-1}) \\
&= \prod_{i=1}^{n} \sqrt{\frac{\tau}{2 \pi}} \cdot \exp\left[ -\frac{\tau}{2} \left( y_i-\mu \right)^2 \right] \\
&= \left( \sqrt{\frac{\tau}{2 \pi}} \right)^n \cdot \exp\left[ -\frac{\tau}{2} \sum_{i=1}^{n} \left( y_i-\mu \right)^2 \right]
\end{split}
$$

using the inverse variance or precision $\tau = 1/\sigma^2$.

<br>
Seperating constant and variable terms, we have:

$$ \label{eq:UG-LF-s1}
p(y|\mu,\tau) = \sqrt{\frac{1}{(2 \pi)^n}} \cdot \tau^{n/2} \cdot \exp\left[ -\frac{\tau}{2} \sum_{i=1}^{n} \left( y_i-\mu \right)^2 \right] \; .
$$

Expanding the product in the exponent, we have

$$ \label{eq:UG-LF-s2}
\begin{split}
p(y|\mu,\tau) &= \sqrt{\frac{1}{(2 \pi)^n}} \cdot \tau^{n/2} \cdot \exp\left[ -\frac{\tau}{2} \sum_{i=1}^{n} \left( y_i^2 - 2 \mu y_i + \mu^2 \right) \right] \\
&= \sqrt{\frac{1}{(2 \pi)^n}} \cdot \tau^{n/2} \cdot \exp\left[ -\frac{\tau}{2} \left( \sum_{i=1}^{n} y_i^2 - 2 \mu \sum_{i=1}^{n} y_i + n \mu^2 \right) \right] \\
&= \sqrt{\frac{1}{(2 \pi)^n}} \cdot \tau^{n/2} \cdot \exp\left[ -\frac{\tau}{2} \left( y^\mathrm{T} y - 2 \mu n \bar{y} + n \mu^2 \right) \right] \\
&= \sqrt{\frac{1}{(2 \pi)^n}} \cdot \tau^{n/2} \cdot \exp\left[ -\frac{\tau n}{2} \left( \frac{1}{n} y^\mathrm{T} y - 2 \mu \bar{y} + \mu^2 \right) \right]
\end{split}
$$

where $\bar{y} = \frac{1}{n} \sum_{i=1}^{n} y_i$ is the mean of data points and $y^\mathrm{T} y = \sum_{i=1}^{n} y_i^2$ is the sum of squared data points.

Completing the square over $\mu$, finally gives

$$ \label{eq:UG-LF-s3}
p(y|\mu,\tau) = \sqrt{\frac{1}{(2 \pi)^n}} \cdot \tau^{n/2} \cdot \exp\left[ -\frac{\tau n}{2} \left( (\mu-\bar{y})^2 - \bar{y}^2 + \frac{1}{n} y^\mathrm{T} y \right) \right]
$$

<br>
In other words, the [likelihood function](/D/lf) is proportional to a power of $\tau$ times an exponential of $\tau$ and an exponential of a squared form of $\mu$, weighted by $\tau$:

$$ \label{eq:UG-LF-s4}
p(y|\mu,\tau) \propto \tau^{n/2} \cdot \exp\left[ -\frac{\tau}{2} \left( y^\mathrm{T} y - n \bar{y}^2 \right) \right] \cdot \exp\left[ -\frac{\tau n}{2} \left( \mu-\bar{y} \right)^2 \right] \; .
$$

The same is true for a [normal-gamma distribution](/D/ng) over $\mu$ and $\tau$

$$ \label{eq:UG-prior-s1}
p(\mu,\tau) = \mathcal{N}(\mu; \mu_0, (\tau \lambda_0)^{-1}) \cdot \mathrm{Gam}(\tau; a_0, b_0)
$$

the [probability density function of which](/P/ng-pdf)

$$ \label{eq:UG-prior-s2}
p(\mu,\tau) = \sqrt{\frac{\tau \lambda_0}{2 \pi}} \cdot \exp\left[ -\frac{\tau \lambda_0}{2} \left( \mu-\mu_0 \right)^2 \right] \cdot \frac{ {b_0}^{a_0} }{\Gamma(a_0)} \, \tau^{a_0-1} \exp[-b_0 \tau]
$$

exhibits the same proportionality

$$ \label{eq:UG-prior-s3}
p(\mu,\tau) \propto \tau^{a_0+1/2-1} \cdot \exp[-\tau b_0] \cdot \exp\left[ -\frac{\tau \lambda_0}{2} \left( \mu-\mu_0 \right)^2 \right]
$$

and is therefore conjugate relative to the likelihood.