---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2025-05-21 14:24:00

title: "Multivariate normal distribution maximizes differential entropy for fixed covariance"
chapter: "Probability Distributions"
section: "Multivariate continuous distributions"
topic: "Multivariate normal distribution"
theorem: "Maximum entropy distribution"

sources:
  - authors: "Wikipedia"
    year: 2025
    title: "Maximum entropy probability distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2025-05-23"
    url: "https://en.wikipedia.org/wiki/Maximum_entropy_probability_distribution#Other_examples"

proof_id: "P500"
shortcut: "mvn-maxent"
username: "JoramSoch"
---


**Theorem:** The [multivariate normal distribution](/D/mvn) maximizes [differential entropy](/D/dent) for a [random vector](/D/rvec) with fixed [covariance matrix](/D/covmat).


**Proof:** For a [random vector](/D/rvar) $X$ with set of possible values $\mathcal{X}$ and [probability density function](/D/pdf) $p(x)$, the [differential entropy](/D/dent) is defined as:

$$ \label{eq:dent}
\mathrm{h}(X) = - \int_{\mathcal{X}} p(x) \log p(x) \, \mathrm{d}x \; .
$$

Let $g(x)$ be the [probability density function](/D/pdf) of a [multivariate normal distribution](/D/norm) with [mean](/D/mean) $\mu$ and [covariance](/D/covmat) $\Sigma$ and let $f(x)$ be an arbitrary [probability density function](/D/pdf) with the same [covariance](/D/covmat). Since [differential entropy](/D/dent) is [translation-invariant](/P/dent-inv), we can assume that $f(x)$ has the same mean as $g(x)$.

Consider the [Kullback-Leibler divergence](/D/kl) of distribution $f(x)$ from distribution $g(x)$ [which is non-negative](/P/kl-nonneg):

$$ \label{eq:kl-fg}
\begin{split}
0 \leq \mathrm{KL}[f||g] &= \int_{\mathcal{X}} f(x) \log \frac{f(x)}{g(x)} \, \mathrm{d}x \\
&= \int_{\mathcal{X}} f(x) \log f(x) \, \mathrm{d}x - \int_{\mathcal{X}} f(x) \log g(x) \, \mathrm{d}x \\
&\overset{\eqref{eq:dent}}{=} - \mathrm{h}[f(x)] - \int_{\mathcal{X}} f(x) \log g(x) \, \mathrm{d}x \; .
\end{split}
$$

By plugging the [probability density function of the multivariate normal distribution](/P/mvn-pdf) into the second term, we obtain:

$$ \label{eq:int-fg-s1}
\begin{split}
\int_{\mathcal{X}} f(x) \log g(x) \, \mathrm{d}x &= \int_{\mathcal{X}} f(x) \log \left( \frac{1}{\sqrt{(2 \pi)^n |\Sigma|}} \cdot \exp \left[ -\frac{1}{2} (x-\mu)^\mathrm{T} \Sigma^{-1} (x-\mu) \right] \right) \, \mathrm{d}x \\
&= \int_{\mathcal{X}} f(x) \log \left( \frac{1}{\sqrt{(2 \pi)^n |\Sigma|}} \right) \, \mathrm{d}x + \int_{\mathcal{X}} f(x) \log \left( \exp \left[ -\frac{1}{2} (x-\mu)^\mathrm{T} \Sigma^{-1} (x-\mu) \right] \right) \, \mathrm{d}x \\
&= \left( - \frac{n}{2} \log (2 \pi) - \frac{1}{2} \log |\Sigma| \right) \int_{\mathcal{X}} f(x) \, \mathrm{d}x - \frac{1}{2} \int_{\mathcal{X}} f(x) \left[ (x-\mu)^\mathrm{T} \Sigma^{-1} (x-\mu) \right] \, \mathrm{d}x \; .
\end{split}
$$

Because the [entire integral over a probability density function is one](/D/pdf) and with the [definition of the expected value](/D/mean), this becomes:

$$ \label{eq:int-fg-s2}
\int_{\mathcal{X}} f(x) \log g(x) \, \mathrm{d}x = - \frac{n}{2} \log (2 \pi) - \frac{1}{2} \log |\Sigma| - \frac{1}{2} \left\langle (x-\mu)^\mathrm{T} \Sigma^{-1} (x-\mu) \right\rangle_{f(x)} \; .
$$

Using the [expectation of a trace](/D/mean-tr) and the [definition of the covariance matrix](/D/covmat), the second term can be developed as follows:

$$ \label{eq:int-fg-s3}
\begin{split}
   \left\langle (x-\mu)^\mathrm{T} \Sigma^{-1} (x-\mu) \right\rangle_{f(x)}
&= \left\langle \mathrm{tr} \left[ (x-\mu)^\mathrm{T} \Sigma^{-1} (x-\mu) \right] \right\rangle_{f(x)} \\
&= \left\langle \mathrm{tr} \left[ \Sigma^{-1} (x-\mu) (x-\mu)^\mathrm{T} \right] \right\rangle_{f(x)} \\
&= \mathrm{tr} \left[ \Sigma^{-1} \left\langle (x-\mu) (x-\mu)^\mathrm{T} \right\rangle_{f(x)} \right] \\
&= \mathrm{tr} \left[ \Sigma^{-1} \Sigma \right] \\
&= \mathrm{tr} \left[ I_n \right] \\
&= n \; .
\end{split}
$$

Thus, the second term in \eqref{eq:kl-fg} is equal to

$$ \label{eq:int-fg-s4}
\int_{\mathcal{X}} f(x) \log g(x) \, \mathrm{d}x = - \frac{n}{2} \log (2 \pi) - \frac{1}{2} \log |\Sigma| - \frac{n}{2} \; .
$$

This is actually the negative of the [differential entropy of the multivariate normal distribution](/P/norm-dent), such that:

$$ \label{eq:int-fg-s5}
\int_{\mathcal{X}} f(x) \log g(x) \, \mathrm{d}x = -\mathrm{h}[\mathcal{N}(\mu,\Sigma)] = -\mathrm{h}[g(x)] \; .
$$

Combining \eqref{eq:kl-fg} with \eqref{eq:int-fg-s5}, we can show that

$$ \label{eq:mvn-maxent}
\begin{split}
               0 &\leq \mathrm{KL}[f||g] \\
               0 &\leq - \mathrm{h}[f(x)] - \left( -\mathrm{h}[g(x)] \right) \\
\mathrm{h}[g(x)] &\geq \mathrm{h}[f(x)]
\end{split}
$$

which means that the [differential entropy](/D/dent) of the [multivariate normal distribution](/D/mvn) $\mathcal{N}(\mu, \Sigma)$ will be larger than or equal to any other [distribution](/D/dist) with the same [covariance matrix](/D/covmat) $\Sigma$.