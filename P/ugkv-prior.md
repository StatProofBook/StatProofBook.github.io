---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-03-24 05:57:00

title: "Conjugate prior distribution for the univariate Gaussian with known variance"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Univariate Gaussian with known variance"
theorem: "Conjugate prior distribution"

sources:
  - authors: "Bishop, Christopher M."
    year: 2006
    title: "Bayesian inference for the Gaussian"
    in: "Pattern Recognition for Machine Learning"
    pages: "ch. 2.3.6, pp. 97-98, eq. 2.138"
    url: "http://users.isr.ist.utl.pt/~wurmd/Livros/school/Bishop%20-%20Pattern%20Recognition%20And%20Machine%20Learning%20-%20Springer%20%202006.pdf"

proof_id: "P211"
shortcut: "ugkv-prior"
username: "JoramSoch"
---


**Theorem:** Let

$$ \label{eq:ugkv}
y = \left\lbrace y_1, \ldots, y_n \right\rbrace, \quad y_i \sim \mathcal{N}(\mu, \sigma^2), \quad i = 1, \ldots, n
$$

be a [univariate Gaussian data set](/D/ugkv) with unknown mean $\mu$ and known variance $\sigma^2$. Then, the [conjugate prior](/D/prior-conj) for this model is a [normal distribution](/D/norm)

$$ \label{eq:UGkv-prior}
p(\mu) = \mathcal{N}(\mu; \mu_0, \lambda_0^{-1})
$$

with [prior](/D/prior) [mean](/D/mean) $\mu_0$ and [prior](/D/prior) [precision](/D/prec) $\lambda_0$.


**Proof:** By definition, a [conjugate prior](/D/prior-conj) is a [prior distribution](/D/prior) that, when combined with the [likelihood function](/D/lf), leads to a [posterior distribution](/D/post) that belongs to the same family of [probability distributions](/D/dist). This is fulfilled when the prior density and the likelihood function are proportional to the model model parameters in the same way, i.e. the model parameters appear in the same functional form in both.

Equation \eqref{eq:ugkv} implies the following [likelihood function](/D/lf)

$$ \label{eq:UGkv-LF-class}
\begin{split}
p(y|\mu) &= \prod_{i=1}^{n} \mathcal{N}(y_i; \mu, \sigma^2) \\
&= \prod_{i=1}^{n} \frac{1}{\sqrt{2 \pi} \sigma} \cdot \exp\left[ -\frac{1}{2} \left( \frac{y_i-\mu}{\sigma} \right)^2 \right] \\
&= \left( \sqrt{\frac{1}{2 \pi \sigma^2}} \right)^n \cdot \exp\left[ -\frac{1}{2 \sigma^2} \sum_{i=1}^{n} \left( y_i-\mu \right)^2 \right]
\end{split}
$$

which, for mathematical convenience, can also be parametrized as

$$ \label{eq:UGkv-LF-Bayes}
\begin{split}
p(y|\mu) &= \prod_{i=1}^{n} \mathcal{N}(y_i; \mu, \tau^{-1}) \\
&= \prod_{i=1}^{n} \sqrt{\frac{\tau}{2 \pi}} \cdot \exp\left[ -\frac{\tau}{2} \left( y_i-\mu \right)^2 \right] \\
&= \left( \sqrt{\frac{\tau}{2 \pi}} \right)^n \cdot \exp\left[ -\frac{\tau}{2} \sum_{i=1}^{n} \left( y_i-\mu \right)^2 \right]
\end{split}
$$

using the inverse variance or precision $\tau = 1/\sigma^2$.

<br>
Expanding the product in the exponent, we have

$$ \label{eq:UGkv-LF-s2}
\begin{split}
p(y|\mu) &= \left( \frac{\tau}{2 \pi} \right)^{n/2} \cdot \exp\left[ -\frac{\tau}{2} \sum_{i=1}^{n} \left( y_i^2 - 2 \mu y_i + \mu^2 \right) \right] \\
&= \left( \frac{\tau}{2 \pi} \right)^{n/2} \cdot \exp\left[ -\frac{\tau}{2} \left( \sum_{i=1}^{n} y_i^2 - 2 \mu \sum_{i=1}^{n} y_i + n \mu^2 \right) \right] \\
&= \left( \frac{\tau}{2 \pi} \right)^{n/2} \cdot \exp\left[ -\frac{\tau}{2} \left( y^\mathrm{T} y - 2 \mu n \bar{y} + n \mu^2 \right) \right] \\
&= \left( \frac{\tau}{2 \pi} \right)^{n/2} \cdot \exp\left[ -\frac{\tau n}{2} \left( \frac{1}{n} y^\mathrm{T} y - 2 \mu \bar{y} + \mu^2 \right) \right]
\end{split}
$$

where $\bar{y} = \frac{1}{n} \sum_{i=1}^{n} y_i$ is the mean of data points and $y^\mathrm{T} y = \sum_{i=1}^{n} y_i^2$ is the sum of squared data points.

Completing the square over $\mu$, finally gives

$$ \label{eq:UGkv-LF-s3}
p(y|\mu) = \left( \frac{\tau}{2 \pi} \right)^{n/2} \cdot \exp\left[ -\frac{\tau n}{2} \left( (\mu-\bar{y})^2 - \bar{y}^2 + \frac{1}{n} y^\mathrm{T} y \right) \right]
$$

<br>
In other words, the [likelihood function](/D/lf) is proportional to an exponential of a squared form of $\mu$, weighted by some constant:

$$ \label{eq:UGkv-LF-s4}
p(y|\mu) \propto \exp\left[ -\frac{\tau n}{2} \left( \mu-\bar{y} \right)^2 \right] \; .
$$

The same is true for a [normal distribution](/D/norm) over $\mu$

$$ \label{eq:UGkv-prior-s1}
p(\mu) = \mathcal{N}(\mu; \mu_0, \lambda_0^{-1})
$$

the [probability density function of which](/P/norm-pdf)

$$ \label{eq:UGkv-prior-s2}
p(\mu) = \sqrt{\frac{\lambda_0}{2 \pi}} \cdot \exp\left[ -\frac{\lambda_0}{2} \left( \mu-\mu_0 \right)^2 \right]
$$

exhibits the same proportionality

$$ \label{eq:UGkv-prior-s3}
p(\mu) \propto \exp\left[ -\frac{\lambda_0}{2} \left( \mu-\mu_0 \right)^2 \right]
$$

and is therefore conjugate relative to the likelihood.