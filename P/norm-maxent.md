---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-08-25 08:31:00

title: "Normal distribution maximizes differential entropy for fixed variance"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Normal distribution"
theorem: "Maximum entropy distribution"

sources:
  - authors: "Wikipedia"
    year: 2021
    title: "Differential entropy"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-08-25"
    url: "https://en.wikipedia.org/wiki/Differential_entropy#Maximization_in_the_normal_distribution"

proof_id: "P250"
shortcut: "norm-maxent"
username: "JoramSoch"
---


**Theorem:** The [normal distribution](/D/norm) maximizes [differential entropy](/D/dent) for a [random variable](/D/rvar) with fixed [variance](/D/var).


**Proof:** For a [random variable](/D/rvar) $X$ with set of possible values with [probability density function](/D/pdf) $f(x)$, the [differential entropy](/D/dent) is defined as:

$$ \label{eq:dent}
\mathrm{h}(X) = - \int_{\mathcal{X}} p(x) \log p(x) \, \mathrm{d}x
$$

Let $g(x)$ be the [probability density function](/D/pdf) of a [normal distribution](/D/norm) with [mean](/D/mean) $\mu$ and [variance](/D/var) $\sigma^2$ and let $f(x)$ be an arbitrary [probability density function](/D/pdf) with the same [variance](/D/var). Since [differential entropy](/D/dent) is [translation-invariant](/P/dent-inv), we can assume that $f(x)$ has the same mean as $g(x)$.

Consider the [Kullback-Leibler divergence](/D/kl) of distribution $f(x)$ from distribution $g(x)$ [which is non-negative](/P/kl-nonneg):

$$ \label{eq:kl-fg}
\begin{split}
0 \leq \mathrm{KL}[f||g] &= \int_{\mathcal{X}} f(x) \log \frac{f(x)}{g(x)} \, \mathrm{d}x \\
&= \int_{\mathcal{X}} f(x) \log f(x) \, \mathrm{d}x - \int_{\mathcal{X}} f(x) \log g(x) \, \mathrm{d}x \\
&\overset{\eqref{eq:dent}}{=} - \mathrm{h}[f(x)] - \int_{\mathcal{X}} f(x) \log g(x) \, \mathrm{d}x \; .
\end{split}
$$

By plugging the [probability density function of the normal distribution](/P/norm-pdf) into the second term, we obtain:

$$ \label{eq:int-fg-s1}
\begin{split}
\int_{\mathcal{X}} f(x) \log g(x) \, \mathrm{d}x &= \int_{\mathcal{X}} f(x) \log \left( \frac{1}{\sqrt{2 \pi} \sigma} \cdot \exp \left[ -\frac{1}{2} \left( \frac{x-\mu}{\sigma} \right)^2 \right] \right) \, \mathrm{d}x \\
&= \int_{\mathcal{X}} f(x) \log \left( \frac{1}{\sqrt{2 \pi \sigma^2}} \right) \, \mathrm{d}x + \int_{\mathcal{X}} f(x) \log \left( \exp \left[ -\frac{(x-\mu)^2}{2 \sigma^2} \right] \right) \, \mathrm{d}x \\
&= -\frac{1}{2} \log \left( 2 \pi \sigma^2 \right) \int_{\mathcal{X}} f(x) \, \mathrm{d}x - \frac{\log(e)}{2 \sigma^2} \int_{\mathcal{X}} f(x) (x-\mu)^2 \, \mathrm{d}x \; .
\end{split}
$$

Because the [entire integral over a probability density function is one](/D/pdf) and the [second central moment is equal to the variance](/P/momcent-2nd), we have:

$$ \label{eq:int-fg-s2}
\begin{split}
\int_{\mathcal{X}} f(x) \log g(x) \, \mathrm{d}x &= -\frac{1}{2} \log \left( 2 \pi \sigma^2 \right) - \frac{\log(e) \sigma^2}{2 \sigma^2} \\
&= -\frac{1}{2} \left[ \log \left( 2 \pi \sigma^2 \right) + \log(e) \right] \\
&= -\frac{1}{2} \log \left( 2 \pi \sigma^2 e \right) \; .
\end{split}
$$

This is actually the negative of the [differential entropy of the normal distribution](/P/norm-dent), such that:

$$ \label{eq:int-fg-s3}
\int_{\mathcal{X}} f(x) \log g(x) \, \mathrm{d}x = -\mathrm{h}[g(x)] \; .
$$

Combining \eqref{eq:kl-fg} with \eqref{eq:int-fg-s3}, we can show that

$$ \label{eq:norm-maxent}
\begin{split}
0 &\leq - \mathrm{h}[f(x)] - \left( -\mathrm{h}[g(x)] \right) \\
\mathrm{h}[g(x)] - \mathrm{h}[f(x)] &\geq 0
\end{split}
$$

which means that the [differential entropy](/D/dent) of the [normal distribution](/D/norm) $\mathcal{N}(\mu, \sigma^2)$ will be larger than or equal to any other [distribution](/D/dist) with the same [variance](/D/var) $\sigma^2$.