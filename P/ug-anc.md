---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-07-14 08:26:00

title: "Accuracy and complexity for the univariate Gaussian"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Univariate Gaussian"
theorem: "Accuracy and complexity"

sources:

proof_id: "P240"
shortcut: "ug-anc"
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

Then, [accuracy and complexity](/P/lme-anc) of this model are

$$ \label{eq:UG-NG-AnC}
\begin{split}
\mathrm{Acc}(m) &= - \frac{1}{2} \frac{a_n}{b_n} \left( y^\mathrm{T} y - 2 n \bar{y} \mu_n + n \mu_n^2 \right) - \frac{1}{2} n \lambda_n^{-1} + \frac{n}{2} \left(\psi(a_n) - \log(b_n)\right) - \frac{n}{2} \log (2 \pi) \\
\mathrm{Com}(m) &= \frac{1}{2} \frac{a_n}{b_n} \left[ \lambda_0 (\mu_0 - \mu_n)^2 - 2 (b_n - b_0) \right] + \frac{1}{2} \frac{\lambda_0}{\lambda_n} - \frac{1}{2} \log \frac{\lambda_0}{\lambda_n} - \frac{1}{2} \\
&+ a_0 \cdot \log \frac{b_n}{b_0} - \log \frac{\Gamma(a_n)}{\Gamma(a_0)} + (a_n - a_0) \cdot \psi(a_n)
\end{split}
$$

where $\mu_n$ and $\lambda_n$ as well as $a_n$ and $b_n$ are the [posterior hyperparameters for the univariate Gaussian](/P/ug-post) and $\bar{y}$ is the [sample mean](/D/mean-samp).


**Proof:** Model [accuracy and complexity are defined as](/P/lme-anc)

$$ \label{eq:lme-anc}
\begin{split}
\mathrm{LME}(m) &= \mathrm{Acc}(m) - \mathrm{Com}(m) \\
\mathrm{Acc}(m) &= \left\langle \log p(y|\mu,m) \right\rangle_{p(\mu|y,m)} \\
\mathrm{Com}(m) &= \mathrm{KL} \left[ p(\mu|y,m) \, || \, p(\mu|m) \right] \; .
\end{split}
$$

<br>
The accuracy term is the [expectation](/D/mean) of the [log-likelihood function](/D/llf) $\log p(y|\mu,\tau)$ with respect to the [posterior distribution](/D/post) $p(\mu,\tau|y)$. With the [log-likelihood function for the univariate Gaussian](/P/ug-mle) and the [posterior distribution for the univariate Gaussian](/P/ug-post), the model accuracy of $m$ evaluates to:

$$ \label{eq:UG-NG-Acc}
\begin{split}
\mathrm{Acc}(m) &= \left\langle \log p(y|\mu,\tau) \right\rangle_{p(\mu,\tau|y)} \\
&= \left\langle \left\langle \log p(y|\mu,\tau) \right\rangle_{p(\mu|\tau,y)} \right\rangle_{p(\tau|y)} \\
&= \left\langle \left\langle \frac{n}{2} \log (\tau) - \frac{n}{2} \log (2 \pi) - \frac{\tau}{2} \left( y^\mathrm{T} y - 2 n \bar{y} \mu + n \mu^2 \right) \right\rangle_{\mathcal{N}(\mu_n, (\tau \lambda_n)^{-1})} \right\rangle_{\mathrm{Gam}(a_n, b_n)} \\
&= \left\langle \frac{n}{2} \log (\tau) - \frac{n}{2} \log (2 \pi) - \frac{\tau}{2} \left( y^\mathrm{T} y - 2 n \bar{y} \mu_n + n \mu_n^2 \right) - \frac{1}{2} n \lambda_n^{-1} \right\rangle_{\mathrm{Gam}(a_n, b_n)} \\
&= \frac{n}{2} \left(\psi(a_n) - \log(b_n)\right) - \frac{n}{2} \log (2 \pi) - \frac{1}{2} \frac{a_n}{b_n} \left( y^\mathrm{T} y - 2 n \bar{y} \mu_n + n \mu_n^2 \right) - \frac{1}{2} n \lambda_n^{-1} \\
&= - \frac{1}{2} \frac{a_n}{b_n} \left( y^\mathrm{T} y - 2 n \bar{y} \mu_n + n \mu_n^2 \right) - \frac{1}{2} n \lambda_n^{-1} + \frac{n}{2} \left(\psi(a_n) - \log(b_n)\right) - \frac{n}{2} \log (2 \pi) \\
\end{split}
$$

<br>
The complexity penalty is the [Kullback-Leibler divergence](/D/kl) of the [posterior distribution](/D/post) $p(\mu,\tau|y)$ from the [prior distribution](/D/prior) $p(\mu,\tau)$. With the [prior distribution](/P/ug-prior) given by \eqref{eq:UG-NG-prior}, the [posterior distribution for the univariate Gaussian](/P/ug-post) and the [Kullback-Leibler divergence of the normal-gamma distribution](/P/ng-kl), the model complexity of $m$ evaluates to:

$$ \label{eq:UG-NG-Com}
\begin{split}
\mathrm{Com}(m) &= \mathrm{KL} \left[ p(\mu,\tau|y) \, || \, p(\mu,\tau) \right] \\
&= \mathrm{KL} \left[ \mathrm{NG}(\mu_n, \lambda_n^{-1}, a_n, b_n) \, || \,  \mathrm{NG}(\mu_0, \lambda_0^{-1}, a_0, b_0) \right] \\
&= \frac{1}{2} \frac{a_n}{b_n} \left[ \lambda_0 (\mu_0 - \mu_n)^2 \right] + \frac{1}{2} \frac{\lambda_0}{\lambda_n} - \frac{1}{2} \log \frac{\lambda_0}{\lambda_n} - \frac{1}{2} \\
&+ a_0 \cdot \log \frac{b_n}{b_0} - \log \frac{\Gamma(a_n)}{\Gamma(a_0)} + (a_n - a_0) \cdot \psi(a_n) - (b_n - b_0) \cdot \frac{a_n}{b_n} \\
&= \frac{1}{2} \frac{a_n}{b_n} \left[ \lambda_0 (\mu_0 - \mu_n)^2 - 2 (b_n - b_0) \right] + \frac{1}{2} \frac{\lambda_0}{\lambda_n} - \frac{1}{2} \log \frac{\lambda_0}{\lambda_n} - \frac{1}{2} \\
&+ a_0 \cdot \log \frac{b_n}{b_0} - \log \frac{\Gamma(a_n)}{\Gamma(a_0)} + (a_n - a_0) \cdot \psi(a_n) \; .
\end{split}
$$

A control calculation confirms that

$$ \label{eq:UG-NG-AnC-LME}
\mathrm{Acc}(m) - \mathrm{Com}(m) = \mathrm{LME}(m)
$$

where $\mathrm{LME}(m)$ is the [log model evidence for the univariate Gaussian](/P/ug-lme).