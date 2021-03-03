---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-03-03 09:53:00

title: "Posterior distribution for the univariate Gaussian"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Univariate Gaussian"
theorem: "Posterior distribution"

sources:
  - authors: "Bishop CM"
    year: 2006
    title: "Bayesian inference for the Gaussian"
    in: "Pattern Recognition for Machine Learning"
    pages: "pp. 97-102, eq. 2.154"
    url: "http://users.isr.ist.utl.pt/~wurmd/Livros/school/Bishop%20-%20Pattern%20Recognition%20And%20Machine%20Learning%20-%20Springer%20%202006.pdf"

proof_id: "P202"
shortcut: "ug-post"
username: "JoramSoch"
---


**Theorem:** Let

$$ \label{eq:ug}
y = \left\lbrace y_1, \ldots, y_n \right\rbrace, \quad y_i \sim \mathcal{N}(\mu, \sigma^2), \quad i = 1, \ldots, n
$$

be a [univariate Gaussian data set](/D/ug) with unknown mean $\mu$ and unknown variance $\sigma^2$. Moreover, assume a [normal-gamma prior distribution](/P/ug-prior) over the model parameters $\mu$ and $\tau = 1/\sigma^2$:

$$ \label{eq:UG-NG-prior}
p(\mu,\tau) = \mathcal{N}(\mu; \mu_0, (\tau \lambda_0)^{-1}) \cdot \mathrm{Gam}(\tau; a_0, b_0) \; .
$$

Then, the [posterior distribution](/D/post) is also a [normal-gamma distribution](/D/ng)

$$ \label{eq:UG-NG-post}
p(\mu,\tau|y) = \mathcal{N}(\mu; \mu_n, (\tau \lambda_n)^{-1}) \cdot \mathrm{Gam}(\tau; a_n, b_n)
$$

and the [posterior hyperparameters](/D/post) are given by

$$ \label{eq:UG-NG-post-par}
\begin{split}
\mu_n &= \frac{\lambda_0 \mu_0 + n \bar{y}}{\lambda_0 + n} \\
\lambda_n &= \lambda_0 + n \\
a_n &= a_0 + \frac{n}{2} \\
b_n &= b_0 + \frac{1}{2} (y^\mathrm{T} y + \lambda_0 \mu_0^2 - \lambda_n \mu_n^2) \; .
\end{split}
$$


**Proof:** According to [Bayes' theorem](/P/bayes-th), the [posterior distribution](/D/post) is given by

$$ \label{eq:UG-NG-BT}
p(\mu,\tau|y) = \frac{p(y|\mu,\tau) \, p(\mu,\tau)}{p(y)} \; .
$$

Since $p(y)$ is just a normalization factor, the [posterior is proportional](/P/post-jl) to the numerator:

$$ \label{eq:UG-NG-post-JL}
p(\mu,\tau|y) \propto p(y|\mu,\tau) \, p(\mu,\tau) = p(y,\mu,\tau) \; .
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
Combining the [likelihood function](/D/lf) \eqref{eq:UG-LF-Bayes} with the [prior distribution](/D/prior) \eqref{eq:UG-NG-prior}, the [joint likelihood](/D/jl) of the model is given by

$$ \label{eq:UG-NG-JL-s1}
\begin{split}
p(y,\mu,\tau) = \; & p(y|\mu,\tau) \, p(\mu,\tau) \\
= \; & \left( \sqrt{\frac{\tau}{2 \pi}} \right)^n \cdot \exp\left[ -\frac{\tau}{2} \sum_{i=1}^{n} \left( y_i-\mu \right)^2 \right] \cdot \\
& \sqrt{\frac{\tau \lambda_0}{2 \pi}} \cdot \exp\left[ -\frac{\tau \lambda_0}{2} \left( \mu-\mu_0 \right)^2 \right] \cdot \\
& \frac{ {b_0}^{a_0} }{\Gamma(a_0)} \, \tau^{a_0-1} \exp[-b_0 \tau] \; .
\end{split}
$$

Collecting identical variables gives:

$$ \label{eq:UG-NG-JL-s2}
\begin{split}
p(y,\mu,\tau) = \; & \sqrt{\frac{\tau^{n+1} \lambda_0}{(2 \pi)^{n+1}}} \, \frac{ {b_0}^{a_0}}{\Gamma(a_0)} \, \tau^{a_0-1} \exp[-b_0 \tau] \cdot \\
& \exp\left[ -\frac{\tau}{2} \left( \sum_{i=1}^{n} \left( y_i-\mu \right)^2 + \lambda_0 \left( \mu-\mu_0 \right)^2 \right) \right] \; .
\end{split}
$$

[Expanding the products in the exponent](/P/ug-prior) gives

$$ \label{eq:UG-NG-JL-s3}
\begin{split}
p(y,\mu,\tau) = \; & \sqrt{\frac{\tau^{n+1} \lambda_0}{(2 \pi)^{n+1}}} \, \frac{ {b_0}^{a_0}}{\Gamma(a_0)} \, \tau^{a_0-1} \exp[-b_0 \tau] \cdot \\
& \exp\left[ -\frac{\tau}{2} \left( (y^\mathrm{T} y - 2 \mu n \bar{y} + n \mu^2) + \lambda_0 (\mu^2 - 2 \mu \mu_0 + \mu_0^2) \right) \right]
\end{split}
$$

where $\bar{y} = \frac{1}{n} \sum_{i=1}^{n} y_i$ and $y^\mathrm{T} y = \sum_{i=1}^{n} y_i^2$, such that

$$ \label{eq:UG-NG-JL-s4}
\begin{split}
p(y,\mu,\tau) = \; & \sqrt{\frac{\tau^{n+1} \lambda_0}{(2 \pi)^{n+1}}} \, \frac{ {b_0}^{a_0}}{\Gamma(a_0)} \, \tau^{a_0-1} \exp[-b_0 \tau] \cdot \\
& \exp\left[ -\frac{\tau}{2} \left( \mu^2 (\lambda_0 + n) - 2 \mu (\lambda_0 \mu_0 + n \bar{y}) + (y^\mathrm{T} y + \lambda_0 \mu_0^2) \right) \right]
\end{split}
$$

Completing the square over $\mu$, we finally have

$$ \label{eq:UG-NG-JL-s5}
\begin{split}
p(y,\mu,\tau) = \; & \sqrt{\frac{\tau^{n+1} \lambda_0}{(2 \pi)^{n+1}}} \, \frac{ {b_0}^{a_0}}{\Gamma(a_0)} \, \tau^{a_0-1} \exp[-b_0 \tau] \cdot \\
& \exp\left[ -\frac{\tau \lambda_n}{2} \left( \mu - \mu_n \right)^2 -\frac{\tau}{2} \left( y^\mathrm{T} y + \lambda_0 \mu_0^2 - \lambda_n \mu_n^2 \right) \right]
\end{split}
$$

with the [posterior hyperparameters](/D/post)

$$ \label{eq:UG-NG-post-mu-par}
\begin{split}
\mu_n &= \frac{\lambda_0 \mu_0 + n \bar{y}}{\lambda_0 + n} \\
\lambda_n &= \lambda_0 + n \; .
\end{split}
$$

Ergo, the joint likelihood is proportional to

$$ \label{eq:UG-NG-JL-s6}
p(y,\mu,\tau) \propto \tau^{1/2} \cdot \exp\left[ -\frac{\tau \lambda_n}{2} \left( \mu - \mu_n \right)^2 \right] \cdot \tau^{a_n-1} \cdot \exp\left[ -b_n \tau \right]
$$

with the [posterior hyperparameters](/D/post)

$$ \label{eq:UG-NG-post-tau-par}
\begin{split}
a_n &= a_0 + \frac{n}{2} \\
b_n &= b_0 + \frac{1}{2} \left( y^\mathrm{T} y + \lambda_0 \mu_0^2 - \lambda_n \mu_n^2 \right) \; .
\end{split}
$$

From the term in \eqref{eq:UG-NG-JL-s5}, we can isolate the posterior distribution over $\mu$ given $\tau$:

$$ \label{eq:UG-NG-post-mu}
p(\mu|\tau,y) = \mathcal{N}(\mu; \mu_n, (\tau \lambda_n)^{-1}) \; .
$$

From the remaining term, we can isolate the posterior distribution over $\tau$:

$$ \label{eq:UG-NG-post-tau}
p(\tau|y) = \mathrm{Gam}(\tau; a_n, b_n) \; .
$$

Together, \eqref{eq:UG-NG-post-mu} and \eqref{eq:UG-NG-post-tau} constitute the [joint](/D/prob-joint) [posterior distribution](/D/post) of $\mu$ and $\tau$.