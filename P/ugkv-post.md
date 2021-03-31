---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-03-24 06:10:00

title: "Posterior distribution for the univariate Gaussian with known variance"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Univariate Gaussian with known variance"
theorem: "Posterior distribution"

sources:
  - authors: "Bishop, Christopher M."
    year: 2006
    title: "Bayesian inference for the Gaussian"
    in: "Pattern Recognition for Machine Learning"
    pages: "ch. 2.3.6, p. 98, eqs. 2.139-2.142"
    url: "http://users.isr.ist.utl.pt/~wurmd/Livros/school/Bishop%20-%20Pattern%20Recognition%20And%20Machine%20Learning%20-%20Springer%20%202006.pdf"

proof_id: "P212"
shortcut: "ugkv-post"
username: "JoramSoch"
---


**Theorem:** Let

$$ \label{eq:ugkv}
y = \left\lbrace y_1, \ldots, y_n \right\rbrace, \quad y_i \sim \mathcal{N}(\mu, \sigma^2), \quad i = 1, \ldots, n
$$

be a [univariate Gaussian data set](/D/ugkv) with unknown mean $\mu$ and known variance $\sigma^2$. Moreover, assume a [normal distribution](/P/ugkv-prior) over the model parameter $\mu$:

$$ \label{eq:UGkv-prior}
p(\mu) = \mathcal{N}(\mu; \mu_0, \lambda_0^{-1}) \; .
$$

Then, the [posterior distribution](/D/post) is also a [normal distribution](/D/norm)

$$ \label{eq:UGkv-post}
p(\mu|y) = \mathcal{N}(\mu; \mu_n, \lambda_n^{-1})
$$

and the [posterior hyperparameters](/D/post) are given by

$$ \label{eq:UGkv-post-par}
\begin{split}
\mu_n &= \frac{\lambda_0 \mu_0 + \tau n \bar{y}}{\lambda_0 + \tau n} \\
\lambda_n &= \lambda_0 + \tau n
\end{split}
$$

with the [sample mean](/D/mean-samp) $\bar{y}$ and the [inverse variance or precision](/D/prec) $\tau = 1/\sigma^2$.


**Proof:** According to [Bayes' theorem](/P/bayes-th), the [posterior distribution](/D/post) is given by

$$ \label{eq:UGkv-BT}
p(\mu|y) = \frac{p(y|\mu) \, p(\mu)}{p(y)} \; .
$$

Since $p(y)$ is just a normalization factor, the [posterior is proportional](/P/post-jl) to the numerator:

$$ \label{eq:UGkv-post-JL}
p(\mu|y) \propto p(y|\mu) \, p(\mu) = p(y,\mu) \; .
$$

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
Combining the [likelihood function](/D/lf) \eqref{eq:UGkv-LF-Bayes} with the [prior distribution](/D/prior) \eqref{eq:UGkv-prior}, the [joint likelihood](/D/jl) of the model is given by

$$ \label{eq:UGkv-JL-s1}
\begin{split}
p(y,\mu) = \; & p(y|\mu) \, p(\mu) \\
= \; & \left( \sqrt{\frac{\tau}{2 \pi}} \right)^n \cdot \exp\left[ -\frac{\tau}{2} \sum_{i=1}^{n} \left( y_i-\mu \right)^2 \right] \cdot \sqrt{\frac{\lambda_0}{2 \pi}} \cdot \exp\left[ -\frac{\lambda_0}{2} \left( \mu-\mu_0 \right)^2 \right] \; .
\end{split}
$$

Rearranging the terms, we then have:

$$ \label{eq:UGkv-JL-s2}
p(y,\mu) = \left( \frac{\tau}{2 \pi} \right)^{n/2} \cdot \sqrt{\frac{\lambda_0}{2 \pi}} \cdot \exp\left[ -\frac{\tau}{2} \sum_{i=1}^{n} \left( y_i-\mu \right)^2 - \frac{\lambda_0}{2} \left( \mu-\mu_0 \right)^2 \right] \; .
$$

[Expanding the products in the exponent](/P/ugkv-prior) gives

$$ \label{eq:UGkv-JL-s3}
\begin{split}
p(y,\mu) &= \left( \frac{\tau}{2 \pi} \right)^\frac{n}{2} \cdot \left( \frac{\lambda_0}{2 \pi} \right)^\frac{1}{2} \cdot \exp \left[ -\frac{1}{2} \left( \sum_{i=1}^n \tau (y_i-\mu)^2 + \lambda_0 (\mu-\mu_0)^2 \right) \right] \\
&= \left( \frac{\tau}{2 \pi} \right)^\frac{n}{2} \cdot \left( \frac{\lambda_0}{2 \pi} \right)^\frac{1}{2} \cdot \exp \left[ -\frac{1}{2} \left( \sum_{i=1}^n \tau (y_i^2 - 2 y_i \mu + \mu^2) + \lambda_0 (\mu^2 - 2 \mu \mu_0 + \mu_0^2) \right) \right] \\
&= \left( \frac{\tau}{2 \pi} \right)^\frac{n}{2} \cdot \left( \frac{\lambda_0}{2 \pi} \right)^\frac{1}{2} \cdot \exp \left[ -\frac{1}{2} \left( \tau (y^\mathrm{T} y - 2 n \bar{y} \mu + n \mu^2) + \lambda_0 (\mu^2 - 2 \mu \mu_0 + \mu_0^2) \right) \right] \\
&= \left( \frac{\tau}{2 \pi} \right)^\frac{n}{2} \cdot \left( \frac{\lambda_0}{2 \pi} \right)^\frac{1}{2} \cdot \exp \left[ -\frac{1}{2} \left( \mu^2 (\tau n + \lambda_0) - 2 \mu (\tau n \bar{y} + \lambda_0 \mu_0) + (\tau y^\mathrm{T} y + \lambda_0 \mu_0^2) \right) \right] \\
\end{split}
$$

where $\bar{y} = \frac{1}{n} \sum_{i=1}^{n} y_i$ and $y^\mathrm{T} y = \sum_{i=1}^{n} y_i^2$. Completing the square in $\mu$ then yields

$$ \label{eq:UGkv-JL-s4}
p(y,\mu) = \left( \frac{\tau}{2 \pi} \right)^\frac{n}{2} \cdot \left( \frac{\lambda_0}{2 \pi} \right)^\frac{1}{2} \cdot \exp \left[ -\frac{\lambda_n}{2} (\mu - \mu_n)^2 + f_n \right]
$$

with the [posterior hyperparameters](/D/post)

$$ \label{eq:UGkv-post-mu-par}
\begin{split}
\mu_n &= \frac{\lambda_0 \mu_0 + \tau n \bar{y}}{\lambda_0 + \tau n} \\
\lambda_n &= \lambda_0 + \tau n
\end{split}
$$

and the remaining independent term

$$ \label{eq:UGkv-JL-fn}
f_n = -\frac{1}{2} \left( \tau y^\mathrm{T} y + \lambda_0 \mu_0^2 - \lambda_n \mu_n^2 \right) \; .
$$

Ergo, the joint likelihood in \eqref{eq:UGkv-JL-s4} is proportional to

$$ \label{eq:UGkv-JL-s5}
p(y,\mu) \propto \exp \left[ -\frac{\lambda_n}{2} (\mu - \mu_n)^2 \right] \; ,
$$

such that the posterior distribution over $\mu$ is given by

$$ \label{eq:UGkv-post-mu}
p(\mu|y) = \mathcal{N}(\mu; \mu_n, \lambda_n^{-1}) \; .
$$

with the posterior hyperparameters given in \eqref{eq:UGkv-post-mu-par}.