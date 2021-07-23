---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-03-24 07:49:00

title: "Accuracy and complexity for the univariate Gaussian with known variance"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Univariate Gaussian with known variance"
theorem: "Accuracy and complexity"

sources:

proof_id: "P214"
shortcut: "ugkv-anc"
username: "JoramSoch"
---


**Theorem:** Let

$$ \label{eq:ugkv}
y = \left\lbrace y_1, \ldots, y_n \right\rbrace, \quad y_i \sim \mathcal{N}(\mu, \sigma^2), \quad i = 1, \ldots, n
$$

be a [univariate Gaussian data set](/D/ugkv) with unknown mean $\mu$ and known variance $\sigma^2$. Moreover, assume a [statistical model](/D/fpm) imposing a [normal distribution](/P/ugkv-prior) as the [prior distribution](/D/prior) on the model parameter $\mu$:

$$ \label{eq:m}
m: \; y_i \sim \mathcal{N}(\mu, \sigma^2), \; \mu \sim \mathcal{N}(\mu_0, \lambda_0^{-1}) \; .
$$

Then, [accuracy and complexity](/P/lme-anc) of this model are

$$ \label{eq:UGkv-anc}
\begin{split}
\mathrm{Acc}(m) &= \frac{n}{2} \log\left( \frac{\tau}{2 \pi} \right) - \frac{1}{2} \left[ \tau y^\mathrm{T} y - 2 \, \tau n \bar{y} \mu_n + \tau n \mu_n^2 + \frac{\tau n}{\lambda_n} \right] \\
\mathrm{Com}(m) &= \frac{1}{2} \left[ \frac{\lambda_0}{\lambda_n} + \lambda_0 (\mu_0 - \mu_n)^2 - 1 + \log\left( \frac{\lambda_0}{\lambda_n} \right) \right]
\end{split}
$$

where $\mu_n$ and $\lambda_n$ are the [posterior hyperparameters for the univariate Gaussian with known variance](/P/ugkv-post), $\tau = 1/\sigma^2$ is the [inverse variance or precision](/D/prec) and $\bar{y}$ is the [sample mean](/D/mean-samp).


**Proof:** Model [accuracy and complexity are defined as](/P/lme-anc)

$$ \label{eq:lme-anc}
\begin{split}
\mathrm{LME}(m) &= \mathrm{Acc}(m) - \mathrm{Com}(m) \\
\mathrm{Acc}(m) &= \left\langle \log p(y|\mu,m) \right\rangle_{p(\mu|y,m)} \\
\mathrm{Com}(m) &= \mathrm{KL} \left[ p(\mu|y,m) \, || \, p(\mu|m) \right] \; .
\end{split}
$$

<br>
The accuracy term is the [expectation](/D/mean) of the [log-likelihood function](/D/llf) $\log p(y|\mu)$ with respect to the [posterior distribution](/D/post) $p(\mu|y)$. With the [log-likelihood function for the univariate Gaussian with known variance](/P/ugkv-mle) and the [posterior distribution for the univariate Gaussian with known variance](/P/ugkv-post), the model accuracy of $m$ evaluates to:

$$ \label{eq:UGkv-Acc}
\begin{split}
\mathrm{Acc}(m) &= \left\langle \log p(y|\mu) \right\rangle_{p(\mu|y)} \\
&= \left\langle \frac{n}{2} \log\left( \frac{\tau}{2 \pi} \right) - \frac{\tau}{2} \left( y^\mathrm{T} y - 2 n \bar{y} \mu + n \mu^2 \right) \right\rangle_{\mathcal{N}(\mu_n, \lambda_n^{-1})} \\
&= \frac{n}{2} \log\left( \frac{\tau}{2 \pi} \right) - \frac{1}{2} \left[ \tau y^\mathrm{T} y - 2 \tau n \bar{y} \mu_n + \tau n \mu_n^2 + \frac{\tau n}{\lambda_n} \right] \; .
\end{split}
$$

<br>
The complexity penalty is the [Kullback-Leibler divergence](/D/kl) of the [posterior distribution](/D/post) $p(\mu|y)$ from the [prior distribution](/D/prior) $p(\mu)$. With the [prior distribution](/P/ugkv-prior) given by \eqref{eq:m}, the [posterior distribution for the univariate Gaussian with known variance](/P/ugkv-post) and the [Kullback-Leibler divergence of the normal distribution](/P/norm-kl), the model complexity of $m$ evaluates to:

$$ \label{eq:UGkv-Com}
\begin{split}
\mathrm{Com}(m) &= \mathrm{KL} \left[ p(\mu|y) \, || \, p(\mu) \right] \\
&= \mathrm{KL} \left[ \mathcal{N}(\mu_n, \lambda_n^{-1}) \, || \, \mathcal{N}(\mu_0, \lambda_0^{-1}) \right] \\
&= \frac{1}{2} \left[ \frac{\lambda_0}{\lambda_n} + \lambda_0 (\mu_0 - \mu_n)^2 - 1 + \log\left( \frac{\lambda_0}{\lambda_n} \right) \right] \; .
\end{split}
$$

A control calculation confirms that

$$ \label{eq:UGkv-anc-lme}
\mathrm{Acc}(m) - \mathrm{Com}(m) = \mathrm{LME}(m)
$$

where $\mathrm{LME}(m)$ is the [log model evidence for the univariate Gaussian with known variance](/P/ugkv-lme).