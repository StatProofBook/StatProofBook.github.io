---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-03-24 06:45:00

title: "Log model evidence for the univariate Gaussian with known variance"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Univariate Gaussian with known variance"
theorem: "Log model evidence"

sources:

proof_id: "P213"
shortcut: "ugkv-lme"
username: "JoramSoch"
---


**Theorem:** Let

$$ \label{eq:ug}
m: \; y = \left\lbrace y_1, \ldots, y_n \right\rbrace, \quad y_i \sim \mathcal{N}(\mu, \sigma^2), \quad i = 1, \ldots, n
$$

be a [univariate Gaussian data set](/D/ugkv) with unknown mean $\mu$ and known variance $\sigma^2$. Moreover, assume a [normal distribution](/P/ugkv-prior) over the model parameter $\mu$:

$$ \label{eq:UGkv-prior}
p(\mu) = \mathcal{N}(\mu; \mu_0, \lambda_0^{-1}) \; .
$$

Then, the [log model evidence](/D/lme) for this model is

$$ \label{eq:UGkv-LME}
\log p(y|m) = \frac{n}{2} \log\left( \frac{\tau}{2 \pi} \right) + \frac{1}{2} \log\left( \frac{\lambda_0}{\lambda_n} \right) - \frac{1}{2} \left( \tau y^T y + \lambda_0 \mu_0^2 - \lambda_n \mu_n^2 \right) \; .
$$

where the [posterior hyperparameters](/D/post) are given by

$$ \label{eq:UGkv-post-par}
\begin{split}
\mu_n &= \frac{\lambda_0 \mu_0 + \tau n \bar{y}}{\lambda_0 + \tau n} \\
\lambda_n &= \lambda_0 + \tau n
\end{split}
$$

with the [sample mean](/D/mean-samp) $\bar{y}$ and the [inverse variance or precision](/D/prec) $\tau = 1/\sigma^2$.


**Proof:** According to the [law of marginal probability](/D/prob-marg), the [model evidence](/D/ml) for this model is:

$$ \label{eq:UGkv-ME-s1}
p(y|m) = \int p(y|\mu) \, p(\mu) \, \mathrm{d}\mu \; .
$$

According to the [law of conditional probability](/D/prob-cond), the integrand is equivalent to the [joint likelihood](/D/jl):

$$ \label{eq:UGkv-ME-s2}
p(y|m) = \int p(y,\mu) \, \mathrm{d}\mu \; .
$$

Equation \eqref{eq:ug} implies the following [likelihood function](/D/lf)

$$ \label{eq:UG-LF-class}
\begin{split}
p(y|\mu,\sigma^2) &= \prod_{i=1}^{n} \mathcal{N}(y_i; \mu, \sigma^2) \\
&= \prod_{i=1}^{n} \frac{1}{\sqrt{2 \pi} \sigma} \cdot \exp\left[ -\frac{1}{2} \left( \frac{y_i-\mu}{\sigma} \right)^2 \right] \\
&= \left( \sqrt{\frac{1}{2 \pi \sigma^2}} \right)^n \cdot \exp\left[ -\frac{1}{2 \sigma^2} \sum_{i=1}^{n} \left( y_i-\mu \right)^2 \right]
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
When [deriving the posterior distribution](/P/ugkv-post) $p(\mu|y)$, the joint likelihood $p(y,\mu)$ is obtained as

$$ \label{eq:UGkv-LME-s1}
p(y,\mu) = \left( \frac{\tau}{2 \pi} \right)^\frac{n}{2} \cdot \sqrt{\frac{\lambda_0}{2 \pi}} \cdot \exp \left[ -\frac{\lambda_n}{2} (\mu - \mu_n)^2 -\frac{1}{2} \left( \tau y^\mathrm{T} y + \lambda_0 \mu_0^2 - \lambda_n \mu_n^2 \right) \right] \; .
$$

Using the [probability density function of the normal distribution](/P/norm-pdf), we can rewrite this as

$$ \label{eq:UGkv-LME-s2}
p(y,\mu) =  \left( \frac{\tau}{2 \pi} \right)^\frac{n}{2} \cdot \sqrt{\frac{\lambda_0}{2 \pi}} \cdot \sqrt{\frac{2 \pi}{\lambda_n}} \cdot \mathcal{N}(\mu; \lambda_n^{-1}) \cdot \exp \left[ -\frac{1}{2} \left( \tau y^\mathrm{T} y + \lambda_0 \mu_0^2 - \lambda_n \mu_n^2 \right) \right] \; .
$$

Now, $\mu$ can be integrated out using the [properties of the probability density function](/D/pdf):

$$ \label{eq:UGkv-LME-s3}
p(y|m) = \int p(y,\mu) \, \mathrm{d}\mu = \left( \frac{\tau}{2 \pi} \right)^\frac{n}{2} \cdot \sqrt{\frac{\lambda_0}{\lambda_n}} \cdot \exp \left[ -\frac{1}{2} \left( \tau y^\mathrm{T} y + \lambda_0 \mu_0^2 - \lambda_n \mu_n^2 \right) \right] \; .
$$

Thus, the [log model evidence](/D/lme) of this model is given by

$$ \label{eq:UGkv-LME-s4}
\log p(y|m) = \frac{n}{2} \log\left( \frac{\tau}{2 \pi} \right) + \frac{1}{2} \log\left( \frac{\lambda_0}{\lambda_n} \right) - \frac{1}{2} \left( \tau y^T y + \lambda_0 \mu_0^2 - \lambda_n \mu_n^2 \right) \; .
$$