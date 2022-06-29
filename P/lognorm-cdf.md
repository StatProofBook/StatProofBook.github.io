---
layout: proof
mathjax: true

author: "Maja Pavlovic"
affiliation: ""
e_mail: "mpavlovic@uw.co.uk"
date: 2022-06-29 22:20:00

title: "Cumulative distribution function of the log-normal distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Log-normal distribution"
theorem: "Cumulative distribution function"

sources:
  - authors: "skdhfgeq2134"
    year: 2015
    title: "How to derive the cdf of a lognormal distribution from its pdf"
    in: "StackExchange"
    pages: "retrieved on 2022-06-29"
    url: "https://stats.stackexchange.com/questions/151398/how-to-derive-the-cdf-of-a-lognormal-distribution-from-its-pdf/151404#151404"
  - authors: "JoramSoch"
    year: 2020
    title: "Cumulative distribution function of the normal distribution"
    in: "The Book of Statistical Proofs"
    pages: "retrieved on 2022-06-29"
    url: "https://statproofbook.github.io/P/norm-cdf"

# proof_id: 
shortcut: "lognorm-cdf"
username: "majapavlo"
---




**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [log-normal distribution](/D/lognorm):

$$ \label{eq:norm}
X \sim \ln \mathcal{N}(\mu, \sigma^2) \; .
$$

Then, the [cumulative distribution function](/D/lognorm-cdf) of $X$ is

$$ \label{eq:lognorm-cdf}
F_X(x) = \frac{1}{2} \left[ 1 + \mathrm{erf}\left( \frac{\ln x-\mu}{\sqrt{2} \sigma} \right) \right]
$$

where $\mathrm{erf}(x)$ is the error function defined as

$$ \label{eq:erf}
\mathrm{erf}(x) = \frac{2}{\sqrt{\pi}} \int_{0}^{x} \exp(-t^2) \, \mathrm{d}t \; .
$$


**Proof:** The [probability density function of the log-normal distribution](/P/lognorm-pdf) is:

$$ \label{eq:lognorm-pdf}
f_X(x) = \frac{1}{x \sigma \sqrt{2 \pi}} \cdot \exp \left[ - \left( \frac{\ln x-\mu}{\sqrt{2} \sigma} \right)^2 \right] \; .
$$

Thus, the [cumulative distribution function](/D/lognorm-cdf) is:

$$ \label{eq:lognorm-cdf-s1}
\begin{split}
F_X(x) &= \int_{-\infty}^{x} \mathcal{\ln N}(z; \mu, \sigma^2) \, \mathrm{d}z \\
&= \int_{-\infty}^{x} \frac{1}{x\sigma \sqrt{2 \pi}} \cdot \exp \left[ -\left( \frac{\ln z-\mu}{\sqrt{2} \sigma} \right)^2 \right] \, \mathrm{d}z \\
&= \frac{1}{x\sigma \sqrt{2 \pi}} \int_{-\infty}^{x} \exp \left[ -\left( \frac{\ln z-\mu}{\sqrt{2} \sigma} \right)^2 \right] \, \mathrm{d}z \; .
\end{split}
$$

Substituting $t = (\ln z-\mu)/(\sqrt{2} \sigma)$, i.e. $z = \sqrt{2} \sigma t + \mu$, this becomes:

$$ \label{eq:lognorm-cdf-s2}
\begin{split}
F_X(x) &= \frac{1}{x\sigma \sqrt{2 \pi}} \int_{(-\infty-\mu)/(\sqrt{2} \sigma)}^{(\ln x-\mu)/(\sqrt{2} \sigma)} \exp(-t^2) \, \mathrm{d}\left( \sqrt{2} \sigma t + \mu \right) \\
&=\frac{\sqrt{2} \sigma}{x\sigma \sqrt{2 \pi}} \int_{-\infty}^{\frac{\ln x-\mu}{\sqrt{2} \sigma}} \exp(-t^2) \, \mathrm{d}t \\
&= \frac{1}{\sqrt{\pi}} \int_{-\infty}^{\frac{\ln x-\mu}{\sqrt{2} \sigma}} \exp(-t^2) \, \mathrm{d}t \\
&= \frac{1}{\sqrt{\pi}} \int_{-\infty}^{0} \exp(-t^2) \, \mathrm{d}t + \frac{1}{\sqrt{\pi}} \int_{0}^{\frac{\ln x-\mu}{\sqrt{2} \sigma}} \exp(-t^2) \, \mathrm{d}t \\
&= \frac{1}{\sqrt{\pi}} \int_{0}^{\infty} \exp(-t^2) \, \mathrm{d}t + \frac{1}{\sqrt{\pi}} \int_{0}^{\frac{\ln x-\mu}{\sqrt{2} \sigma}} \exp(-t^2) \, \mathrm{d}t \; .
\end{split}
$$

Applying \eqref{eq:erf} to \eqref{eq:lognorm-cdf-s2}, we have:

$$ \label{eq:lognorm-cdf-s3}
\begin{split}
F_X(x) &= \frac{1}{2} \lim_{x \to \infty} \mathrm{erf}(x) + \frac{1}{2} \, \mathrm{erf}\left( \frac{\ln x-\mu}{\sqrt{2} \sigma} \right) \\
&= \frac{1}{2} + \frac{1}{2} \, \mathrm{erf}\left( \frac{\ln x-\mu}{\sqrt{2} \sigma} \right) \\
&= \frac{1}{2} \left[ 1 + \mathrm{erf}\left( \frac{\ln x-\mu}{\sqrt{2} \sigma} \right) \right] \; .
\end{split}
$$