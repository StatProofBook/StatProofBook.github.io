---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-03-20 01:33:00

title: "Cumulative distribution function of the normal distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Normal distribution"
theorem: "Cumulative distribution function"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Normal distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-03-20"
    url: "https://en.wikipedia.org/wiki/Normal_distribution#Cumulative_distribution_function"
  - authors: "Wikipedia"
    year: 2020
    title: "Error function"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-03-20"
    url: "https://en.wikipedia.org/wiki/Error_function"

proof_id: "P85"
shortcut: "norm-cdf"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [normal distributions](/D/norm):

$$ \label{eq:norm}
X \sim \mathcal{N}(\mu, \sigma^2) \; .
$$

Then, the [cumulative distribution function](/D/cdf) of $X$ is

$$ \label{eq:norm-cdf}
F_X(x) = \frac{1}{2} \left[ 1 + \mathrm{erf}\left( \frac{x-\mu}{\sqrt{2} \sigma} \right) \right]
$$

where $\mathrm{erf}(x)$ is the error function defined as

$$ \label{eq:erf}
\mathrm{erf}(x) = \frac{2}{\sqrt{\pi}} \int_{0}^{x} \exp(-t^2) \, \mathrm{d}t \; .
$$


**Proof:** The [probability density function of the normal distribution](/P/norm-pdf) is:

$$ \label{eq:norm-pdf}
f_X(x) = \frac{1}{\sqrt{2 \pi} \sigma} \cdot \exp \left[ -\frac{1}{2} \left( \frac{x-\mu}{\sigma} \right)^2 \right] \; .
$$

Thus, the [cumulative distribution function](/D/cdf) is:

$$ \label{eq:norm-cdf-s1}
\begin{split}
F_X(x) &= \int_{-\infty}^{x} \mathcal{N}(z; \mu, \sigma^2) \, \mathrm{d}z \\
&= \int_{-\infty}^{x} \frac{1}{\sqrt{2 \pi} \sigma} \cdot \exp \left[ -\frac{1}{2} \left( \frac{z-\mu}{\sigma} \right)^2 \right] \, \mathrm{d}z \\
&= \frac{1}{\sqrt{2 \pi} \sigma} \int_{-\infty}^{x} \exp \left[ -\left( \frac{z-\mu}{\sqrt{2} \sigma} \right)^2 \right] \, \mathrm{d}z \; .
\end{split}
$$

Substituting $t = (z-\mu)/(\sqrt{2} \sigma)$, i.e. $z = \sqrt{2} \sigma t + \mu$, this becomes:

$$ \label{eq:norm-cdf-s2}
\begin{split}
F_X(x) &= \frac{1}{\sqrt{2 \pi} \sigma} \int_{(-\infty-\mu)/(\sqrt{2} \sigma)}^{(x-\mu)/(\sqrt{2} \sigma)} \exp(-t^2) \, \mathrm{d}\left( \sqrt{2} \sigma t + \mu \right) \\
&= \frac{\sqrt{2} \sigma}{\sqrt{2 \pi} \sigma} \int_{-\infty}^{\frac{x-\mu}{\sqrt{2} \sigma}} \exp(-t^2) \, \mathrm{d}t \\
&= \frac{1}{\sqrt{\pi}} \int_{-\infty}^{\frac{x-\mu}{\sqrt{2} \sigma}} \exp(-t^2) \, \mathrm{d}t \\
&= \frac{1}{\sqrt{\pi}} \int_{-\infty}^{0} \exp(-t^2) \, \mathrm{d}t + \frac{1}{\sqrt{\pi}} \int_{0}^{\frac{x-\mu}{\sqrt{2} \sigma}} \exp(-t^2) \, \mathrm{d}t \\
&= \frac{1}{\sqrt{\pi}} \int_{0}^{\infty} \exp(-t^2) \, \mathrm{d}t + \frac{1}{\sqrt{\pi}} \int_{0}^{\frac{x-\mu}{\sqrt{2} \sigma}} \exp(-t^2) \, \mathrm{d}t \; .
\end{split}
$$

Applying \eqref{eq:erf} to \eqref{eq:norm-cdf-s2}, we have:

$$ \label{eq:norm-cdf-s3}
\begin{split}
F_X(x) &= \frac{1}{2} \lim_{x \to \infty} \mathrm{erf}(x) + \frac{1}{2} \, \mathrm{erf}\left( \frac{x-\mu}{\sqrt{2} \sigma} \right) \\
&= \frac{1}{2} + \frac{1}{2} \, \mathrm{erf}\left( \frac{x-\mu}{\sqrt{2} \sigma} \right) \\
&= \frac{1}{2} \left[ 1 + \mathrm{erf}\left( \frac{x-\mu}{\sqrt{2} \sigma} \right) \right] \; .
\end{split}
$$