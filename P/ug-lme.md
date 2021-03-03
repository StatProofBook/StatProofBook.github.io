---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-03-03 10:25:00

title: "Log model evidence for the univariate Gaussian"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Univariate Gaussian"
theorem: "Log model evidence"

sources:
  - authors: "Bishop CM"
    year: 2006
    title: "Bayesian linear regression"
    in: "Pattern Recognition for Machine Learning"
    pages: "pp. 152-161, ex. 3.23, eq. 3.118"
    url: "http://users.isr.ist.utl.pt/~wurmd/Livros/school/Bishop%20-%20Pattern%20Recognition%20And%20Machine%20Learning%20-%20Springer%20%202006.pdf"

proof_id: "P203"
shortcut: "ug-lme"
username: "JoramSoch"
---


**Theorem:** Let

$$ \label{eq:ug}
m: \; y = \left\lbrace y_1, \ldots, y_n \right\rbrace, \quad y_i \sim \mathcal{N}(\mu, \sigma^2), \quad i = 1, \ldots, n
$$

be a [univariate Gaussian data set](/D/ug) with unknown mean $\mu$ and unknown variance $\sigma^2$. Moreover, assume a [normal-gamma prior distribution](/P/ug-prior) over the model parameters $\mu$ and $\tau = 1/\sigma^2$:

$$ \label{eq:UG-NG-prior}
p(\mu,\tau) = \mathcal{N}(\mu; \mu_0, (\tau \lambda_0)^{-1}) \cdot \mathrm{Gam}(\tau; a_0, b_0) \; .
$$

Then, the [log model evidence](/D/lme) for this model is

$$ \label{eq:UG-NG-LME}
\log p(y|m) = - \frac{n}{2} \log (2 \pi)  + \frac{1}{2} \log \frac{\lambda_0}{\lambda_n} + \log \Gamma(a_n) - \log \Gamma(a_0) + a_0 \log b_0 - a_n \log b_n
$$

where the [posterior hyperparameters](/D/post) are given by

$$ \label{eq:UG-NG-post-par}
\begin{split}
\mu_n &= \frac{\lambda_0 \mu_0 + n \bar{y}}{\lambda_0 + n} \\
\lambda_n &= \lambda_0 + n \\
a_n &= a_0 + \frac{n}{2} \\
b_n &= b_0 + \frac{1}{2} (y^\mathrm{T} y + \lambda_0 \mu_0^2 - \lambda_n \mu_n^2) \; .
\end{split}
$$


**Proof:** According to the [law of marginal probability](/D/prob-marg), the [model evidence](/D/ml) for this model is:

$$ \label{eq:UG-NG-ME-s1}
p(y|m) = \iint p(y|\mu,\tau) \, p(\mu,\tau) \, \mathrm{d}\mu \, \mathrm{d}\tau \; .
$$

According to the [law of conditional probability](/D/prob-cond), the integrand is equivalent to the [joint likelihood](/D/jl):

$$ \label{eq:UG-NG-ME-s2}
p(y|m) = \iint p(y,\mu,\tau) \, \mathrm{d}\mu \, \mathrm{d}\tau \; .
$$

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
When [deriving the posterior distribution](/P/ug-post) $p(\mu,\tau|y)$, the joint likelihood $p(y,\mu,\tau)$ is obtained as

$$ \label{eq:UG-NG-LME-s1}
\begin{split}
p(y,\mu,\tau) = \; & \sqrt{\frac{\tau^{n+1} \lambda_0}{(2 \pi)^{n+1}}} \, \frac{ {b_0}^{a_0}}{\Gamma(a_0)} \, \tau^{a_0-1} \exp[-b_0 \tau] \cdot \\
& \exp\left[ -\frac{\tau \lambda_n}{2} \left( \mu - \mu_n \right)^2 -\frac{\tau}{2} \left( y^\mathrm{T} y + \lambda_0 \mu_0^2 - \lambda_n \mu_n^2 \right) \right] \; .
\end{split}
$$

Using the [probability density function of the normal distribution](/P/norm-pdf), we can rewrite this as

$$ \label{eq:UG-NG-LME-s2}
\begin{split}
p(y,\mu,\tau) = \; & \sqrt{\frac{\tau^{n}}{(2 \pi)^{n}}} \sqrt{\frac{\tau \lambda_0}{2 \pi}} \sqrt{\frac{2 \pi}{\tau \lambda_n}} \, \frac{ {b_0}^{a_0}}{\Gamma(a_0)} \, \tau^{a_0-1} \exp[-b_0 \tau] \cdot \\
& \mathcal{N}(\mu; \mu_n, (\tau \lambda_n)^{-1}) \, \exp\left[ -\frac{\tau}{2} \left( y^\mathrm{T} y + \lambda_0 \mu_0^2 - \lambda_n \mu_n^2 \right) \right] \; .
\end{split}
$$

Now, $\mu$ can be integrated out easily:

$$ \label{eq:UG-NG-LME-s3}
\begin{split}
\int p(y,\mu,\tau) \, \mathrm{d}\mu = \; & \sqrt{\frac{1}{(2 \pi)^{n}}} \sqrt{\frac{\lambda_0}{\lambda_n}} \, \frac{ {b_0}^{a_0}}{\Gamma(a_0)} \, \tau^{a_0+n/2-1} \exp[-b_0 \tau] \cdot \\
& \exp\left[ -\frac{\tau}{2} \left( y^\mathrm{T} y + \lambda_0 \mu_0^2 - \lambda_n \mu_n^2 \right) \right] \; .
\end{split}
$$

Using the [probability density function of the gamma distribution](/P/gam-pdf), we can rewrite this as

$$ \label{eq:UG-NG-LME-s4}
\int p(y,\mu,\tau) \, \mathrm{d}\mu = \sqrt{\frac{1}{(2 \pi)^{n}}} \sqrt{\frac{\lambda_0}{\lambda_n}} \, \frac{ {b_0}^{a_0}}{\Gamma(a_0)} \, \frac{\Gamma(a_n)}{ {b_n}^{a_n}} \, \mathrm{Gam}(\tau; a_n, b_n) \; .
$$

Finally, $\tau$ can also be integrated out:

$$ \label{eq:UG-NG-LME-s5}
\iint p(y,\mu,\tau) \, \mathrm{d}\mu \, \mathrm{d}\tau = \sqrt{\frac{1}{(2 \pi)^{n}}} \sqrt{\frac{\lambda_0}{\lambda_n}} \, \frac{\Gamma(a_n)}{\Gamma(a_0)} \, \frac{ {b_0}^{a_0}}{ {b_n}^{a_n}} \; .
$$

Thus, the [log model evidence](/D/lme) of this model is given by

$$ \label{eq:UG-NG-LME-s6}
\log p(y|m) = - \frac{n}{2} \log (2 \pi)  + \frac{1}{2} \log \frac{\lambda_0}{\lambda_n} + \log \Gamma(a_n) - \log \Gamma(a_0) + a_0 \log b_0 - a_n \log b_n \; .
$$