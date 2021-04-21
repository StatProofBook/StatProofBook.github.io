---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-03-24 03:48:00

title: "Maximum likelihood estimation for the univariate Gaussian with known variance"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Univariate Gaussian with known variance"
theorem: "Maximum likelihood estimation"

sources:
  - authors: "Bishop, Christopher M."
    year: 2006
    title: "Bayesian inference for the Gaussian"
    in: "Pattern Recognition for Machine Learning"
    pages: "ch. 2.3.6, p. 98, eq. 2.143"
    url: "http://users.isr.ist.utl.pt/~wurmd/Livros/school/Bishop%20-%20Pattern%20Recognition%20And%20Machine%20Learning%20-%20Springer%20%202006.pdf"

proof_id: "P207"
shortcut: "ugkv-mle"
username: "JoramSoch"
---


**Theorem:** Let there be [univariate Gaussian data with known variance](/D/ugkv) $y = \left\lbrace y_1, \ldots, y_n \right\rbrace$:

$$ \label{eq:ugkv}
y_i \sim \mathcal{N}(\mu, \sigma^2), \quad i = 1, \ldots, n \; .
$$

Then, the [maximum likelihood estimate](/D/mle) for the mean $\mu$ is given by

$$ \label{eq:ugkv-MLE}
\hat{\mu} = \bar{y}
$$

where $\bar{y}$ is the [sample mean](/D/mean-samp)

$$ \label{eq:y-mean}
\bar{y} = \frac{1}{n} \sum_{i=1}^n y_i \; .
$$


**Proof:** The [likelihood function](/D/lf) for each observation is given by the [probability density function of the normal distribution](/P/norm-pdf)

$$ \label{eq:ugkv-yi}
p(y_i|\mu) = \mathcal{N}(x; \mu, \sigma^2) = \frac{1}{\sqrt{2 \pi \sigma^2}} \cdot \exp \left[ -\frac{1}{2} \left( \frac{y_i-\mu}{\sigma} \right)^2 \right]
$$

and because observations are [independent](/D/ind), the likelihood function for all observations is the product of the individual ones:

$$ \label{eq:ugkv-LF-s1}
p(y|\mu) = \prod_{i=1}^n p(y_i|\mu) = \sqrt{ \frac{1}{(2 \pi \sigma^2)^n} } \cdot \exp \left[ -\frac{1}{2} \sum_{i=1}^{n} \left( \frac{y_i-\mu}{\sigma} \right)^2 \right] \; .
$$

This can be developed into

$$ \label{eq:ugkv-LF-s2}
\begin{split}
p(y|\mu) &= \left( \frac{1}{2 \pi \sigma^2} \right)^{n/2} \cdot \exp \left[ -\frac{1}{2} \sum_{i=1}^{n} \left( \frac{y_i^2 - 2 y_i \mu + \mu^2}{\sigma^2} \right) \right] \\
&= \left( \frac{1}{2 \pi \sigma^2} \right)^{n/2} \cdot \exp \left[ -\frac{1}{2 \sigma^2} \left( y^\mathrm{T} y - 2 n \bar{y} \mu + n \mu^2 \right) \right]
\end{split}
$$

where $\bar{y} = \frac{1}{n} \sum_{i=1}^{n} y_i$ is the mean of data points and $y^\mathrm{T} y = \sum_{i=1}^{n} y_i^2$ is the sum of squared data points.

Thus, the [log-likelihood function](/D/llf) is

$$ \label{eq:ugkv-LL}
\mathrm{LL}(\mu) = \log p(y|\mu) = -\frac{n}{2} \log (2 \pi \sigma^2) - \frac{1}{2 \sigma^2} \left( y^\mathrm{T} y - 2 n \bar{y} \mu + n \mu^2 \right) \; .
$$

The derivatives of the log-likelihood with respect to $\mu$ are

$$ \label{eq:ugkv-dLLdl-d2LLdl2}
\begin{split}
\frac{\mathrm{d}\mathrm{LL}(\mu)}{\mathrm{d}\mu} &= \frac{n \bar{y}}{\sigma^2} - \frac{n \mu}{\sigma^2} = \frac{n}{\sigma^2} (\bar{y}-\mu) \\
\frac{\mathrm{d}^2\mathrm{LL}(\mu)}{\mathrm{d}\mu^2} &= - \frac{n}{\sigma^2} \; . \\
\end{split}
$$

Setting the first derivative to zero, we obtain:

$$ \label{eq:ugkv-dLLdl}
\begin{split}
\frac{\mathrm{d}\mathrm{LL}(\hat{\mu})}{\mathrm{d}\mu} &= 0 \\
0 &= \frac{n}{\sigma^2} (\bar{y}-\hat{\mu}) \\
0 &= \bar{y}-\hat{\mu} \\
\hat{\mu} &= \bar{y} \\
\end{split}
$$

Plugging this value into the second derivative, we confirm:

$$ \label{eq:ugkv-d2LLdl2}
\frac{\mathrm{d}^2\mathrm{LL}(\hat{\mu})}{\mathrm{d}\mu^2} = -\frac{n}{\sigma^2} < 0 \; .
$$

This demonstrates that the estimate $\hat{\mu} = \bar{y}$ maximizes the likelihood $p(y \vert \mu)$.