---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-04-16 11:03:00

title: "Maximum likelihood estimation for the univariate Gaussian"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Univariate Gaussian"
theorem: "Maximum likelihood estimation"

sources:
  - authors: "Bishop CM"
    year: 2006
    title: "Bayesian inference for the Gaussian"
    in: "Pattern Recognition for Machine Learning"
    pages: "pp. 93-94, eqs. 2.121, 2.122"
    url: "http://users.isr.ist.utl.pt/~wurmd/Livros/school/Bishop%20-%20Pattern%20Recognition%20And%20Machine%20Learning%20-%20Springer%20%202006.pdf"

proof_id: "P223"
shortcut: "ug-mle"
username: "JoramSoch"
---


**Theorem:** Let there be a [univariate Gaussian data set](/D/ug) $y = \left\lbrace y_1, \ldots, y_n \right\rbrace$:

$$ \label{eq:ug}
y_i \sim \mathcal{N}(\mu, \sigma^2), \quad i = 1, \ldots, n \; .
$$

Then, the [maximum likelihood estimates](/D/mle) for mean $\mu$ and variance $\sigma^2$ are given by

$$ \label{eq:ug-MLE}
\begin{split}
\hat{\mu} &= \frac{1}{n} \sum_{i=1}^n y_i \\
\hat{\sigma}^2 &= \frac{1}{n} \sum_{i=1}^n (y_i - \bar{y})^2 \; .
\end{split}
$$


**Proof:** The [likelihood function](/D/lf) for each observation is given by the [probability density function of the normal distribution](/P/norm-pdf)

$$ \label{eq:ug-yi}
p(y_i|\mu,\sigma^2) = \mathcal{N}(x; \mu, \sigma^2) = \frac{1}{\sqrt{2 \pi \sigma^2}} \cdot \exp \left[ -\frac{1}{2} \left( \frac{y_i-\mu}{\sigma} \right)^2 \right]
$$

and because observations are [independent](/D/ind), the likelihood function for all observations is the product of the individual ones:

$$ \label{eq:ug-LF-s1}
p(y|\mu,\sigma^2) = \prod_{i=1}^n p(y_i|\mu) = \sqrt{ \frac{1}{(2 \pi \sigma^2)^n} } \cdot \exp \left[ -\frac{1}{2} \sum_{i=1}^{n} \left( \frac{y_i-\mu}{\sigma} \right)^2 \right] \; .
$$

This can be developed into

$$ \label{eq:ug-LF-s2}
\begin{split}
p(y|\mu,\sigma^2) &= \left( \frac{1}{2 \pi \sigma^2} \right)^{n/2} \cdot \exp \left[ -\frac{1}{2} \sum_{i=1}^{n} \left( \frac{y_i^2 - 2 y_i \mu + \mu^2}{\sigma^2} \right) \right] \\
&= \left( \frac{1}{2 \pi \sigma^2} \right)^{n/2} \cdot \exp \left[ -\frac{1}{2 \sigma^2} \left( y^\mathrm{T} y - 2 n \bar{y} \mu + n \mu^2 \right) \right]
\end{split}
$$

where $\bar{y} = \frac{1}{n} \sum_{i=1}^{n} y_i$ is the mean of data points and $y^\mathrm{T} y = \sum_{i=1}^{n} y_i^2$ is the sum of squared data points.

Thus, the [log-likelihood function](/D/llf) is

$$ \label{eq:ug-LL}
\mathrm{LL}(\mu,\sigma^2) = \log p(y|\mu,\sigma^2) = -\frac{n}{2} \log (2 \pi \sigma^2) - \frac{1}{2 \sigma^2} \left( y^\mathrm{T} y - 2 n \bar{y} \mu + n \mu^2 \right) \; .
$$

<br>
The derivative of the log-likelihood function \eqref{eq:ug-LL} with respect to $\mu$ is

$$ \label{eq:dLL-dmu}
\frac{\mathrm{d}\mathrm{LL}(\mu,\sigma^2)}{\mathrm{d}\mu} = \frac{n \bar{y}}{\sigma^2} - \frac{n \mu}{\sigma^2} = \frac{n}{\sigma^2} (\bar{y}-\mu)
$$

and setting this derivative to zero gives the MLE for $\mu$:

$$ \label{eq:mu-MLE}
\begin{split}
\frac{\mathrm{d}\mathrm{LL}(\hat{\mu},\sigma^2)}{\mathrm{d}\mu} &= 0 \\
0 &= \frac{n}{\sigma^2} (\bar{y}-\hat{\mu}) \\
0 &= \bar{y}-\hat{\mu} \\
\hat{\mu} &= \bar{y} \\
\hat{\mu} &= \frac{1}{n} \sum_{i=1}^n y_i \; .
\end{split}
$$

<br>
The derivative of the log-likelihood function \eqref{eq:ug-LL} at $\hat{\mu}$ with respect to $\sigma^2$ is

$$ \label{eq:dLL-ds2}
\begin{split}
\frac{\mathrm{d}\mathrm{LL}(\hat{\mu},\sigma^2)}{\mathrm{d}\sigma^2} &= -\frac{n}{2} \frac{1}{\sigma^2} + \frac{1}{2 (\sigma^2)^2} \left( y^\mathrm{T} y - 2 n \bar{y} \hat{\mu} + n \hat{\mu}^2 \right) \\
&= -\frac{n}{2 \sigma^2} + \frac{1}{2 (\sigma^2)^2} \sum_{i=1}^n \left( y_i^2 - 2 y_i \hat{\mu} + \hat{\mu}^2 \right) \\
&= -\frac{n}{2 \sigma^2} + \frac{1}{2 (\sigma^2)^2} \sum_{i=1}^n (y_i - \hat{\mu})^2
\end{split}
$$

and setting this derivative to zero gives the MLE for $\sigma^2$:

$$ \label{eq:s2-MLE}
\begin{split}
\frac{\mathrm{d}\mathrm{LL}(\hat{\mu},\hat{\sigma}^2)}{\mathrm{d}\sigma^2} &= 0 \\
0 &= \frac{1}{2 (\hat{\sigma}^2)^2} \sum_{i=1}^n (y_i - \hat{\mu})^2 \\
\frac{n}{2 \hat{\sigma}^2} &= \frac{1}{2 (\hat{\sigma}^2)^2} \sum_{i=1}^n (y_i - \hat{\mu})^2 \\
\frac{2 (\hat{\sigma}^2)^2}{n} \cdot \frac{n}{2 \hat{\sigma}^2} &= \frac{2 (\hat{\sigma}^2)^2}{n} \cdot \frac{1}{2 (\hat{\sigma}^2)^2} \sum_{i=1}^n (y_i - \hat{\mu})^2 \\
\hat{\sigma}^2 &= \frac{1}{n} \sum_{i=1}^n (y_i - \hat{\mu})^2 \\
\hat{\sigma}^2 &= \frac{1}{n} \sum_{i=1}^n (y_i - \bar{y})^2 \\
\end{split}
$$

<br>
Together, \eqref{eq:mu-MLE} and \eqref{eq:s2-MLE} constitute the MLE for the univariate Gaussian.