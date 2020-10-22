---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-01-09 15:04:00

title: "Mean of the normal distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Normal distribution"
theorem: "Mean"

sources:
  - authors: "Papadopoulos, Alecos"
    year: 2013
    title: "How to derive the mean and variance of Gaussian random variable?"
    in: "StackExchange Mathematics"
    pages: "retrieved on 2020-01-09"
    url: "https://math.stackexchange.com/questions/518281/how-to-derive-the-mean-and-variance-of-a-gaussian-random-variable"

proof_id: "P15"
shortcut: "norm-mean"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [normal distribution](/D/norm):

$$ \label{eq:norm}
X \sim \mathcal{N}(\mu, \sigma^2) \; .
$$

Then, the [mean or expected value](/D/mean) of $X$ is

$$ \label{eq:norm-mean}
\mathrm{E}(X) = \mu \; .
$$


**Proof:** The [expected value](/D/mean) is the probability-weighted average over all possible values:

$$ \label{eq:mean}
\mathrm{E}(X) = \int_{\mathcal{X}} x \cdot f_X(x) \, \mathrm{d}x \; .
$$

With the [probability density function of the normal distribution](/P/norm-pdf), this reads:

$$ \label{eq:norm-mean-s1}
\begin{split}
\mathrm{E}(X) &= \int_{-\infty}^{+\infty} x \cdot \frac{1}{\sqrt{2 \pi} \sigma} \cdot \exp \left[ -\frac{1}{2} \left( \frac{x-\mu}{\sigma} \right)^2 \right] \, \mathrm{d}x \\
&= \frac{1}{\sqrt{2 \pi} \sigma} \int_{-\infty}^{+\infty} x \cdot \exp \left[ -\frac{1}{2} \left( \frac{x-\mu}{\sigma} \right)^2 \right] \, \mathrm{d}x \; .
\end{split}
$$

Substituting $z = x -\mu$, we have:

$$ \label{eq:norm-mean-s2}
\begin{split}
\mathrm{E}(X) &= \frac{1}{\sqrt{2 \pi} \sigma} \int_{-\infty-\mu}^{+\infty-\mu} (z + \mu) \cdot \exp \left[ -\frac{1}{2} \left( \frac{z}{\sigma} \right)^2 \right] \, \mathrm{d}(z + \mu) \\
&= \frac{1}{\sqrt{2 \pi} \sigma} \int_{-\infty}^{+\infty} (z + \mu) \cdot \exp \left[ -\frac{1}{2} \left( \frac{z}{\sigma} \right)^2 \right] \, \mathrm{d}z \\
&= \frac{1}{\sqrt{2 \pi} \sigma} \left( \int_{-\infty}^{+\infty} z \cdot \exp \left[ -\frac{1}{2} \left( \frac{z}{\sigma} \right)^2 \right] \, \mathrm{d}z + \mu \int_{-\infty}^{+\infty} \exp \left[ -\frac{1}{2} \left( \frac{z}{\sigma} \right)^2 \right] \, \mathrm{d}z \right) \\
&= \frac{1}{\sqrt{2 \pi} \sigma} \left( \int_{-\infty}^{+\infty} z \cdot \exp \left[ -\frac{1}{2 \sigma^2} \cdot z^2 \right] \, \mathrm{d}z + \mu \int_{-\infty}^{+\infty} \exp \left[ -\frac{1}{2 \sigma^2} \cdot z^2 \right] \, \mathrm{d}z \right) \; .
\end{split}
$$

The general antiderivatives are

$$ \label{eq:exp-erf-anti-der}
\begin{split}
\int x \cdot \exp \left[ -a x^2 \right] \mathrm{d}x &= -\frac{1}{2a} \cdot \exp \left[ -a x^2 \right] \\
\int \exp \left[ -a x^2 \right] \mathrm{d}x &= \frac{1}{2} \sqrt{\frac{\pi}{a}} \cdot \mathrm{erf} \left[ \sqrt{a} x \right]
\end{split}
$$

where $\mathrm{erf}(x)$ is the error function. Using this, the integrals can be calculated as:

$$ \label{eq:norm-mean-s3}
\begin{split}
\mathrm{E}(X) &= \frac{1}{\sqrt{2 \pi} \sigma} \left( \left[ -\sigma^2 \cdot \exp \left[ -\frac{1}{2 \sigma^2} \cdot z^2 \right] \right]_{-\infty}^{+\infty} + \mu \left[ \sqrt{\frac{\pi}{2}} \sigma \cdot \mathrm{erf} \left[ \frac{1}{\sqrt{2} \sigma} z \right] \right]_{-\infty}^{+\infty} \right) \\
&= \frac{1}{\sqrt{2 \pi} \sigma} \left( \left[ \lim_{z \to \infty} \left( -\sigma^2 \cdot \exp \left[ -\frac{1}{2 \sigma^2} \cdot z^2 \right] \right) - \lim_{z \to -\infty} \left( -\sigma^2 \cdot \exp \left[ -\frac{1}{2 \sigma^2} \cdot z^2 \right] \right) \right] \right. \\
&\hphantom{\sqrt{2 \pi}\sigma \;} + \mu \left. \left[ \lim_{z \to \infty} \left( \sqrt{\frac{\pi}{2}} \sigma \cdot \mathrm{erf} \left[ \frac{1}{\sqrt{2} \sigma} z \right] \right) - \lim_{z \to -\infty} \left( \sqrt{\frac{\pi}{2}} \sigma \cdot \mathrm{erf} \left[ \frac{1}{\sqrt{2} \sigma} z \right] \right) \right] \right) \\
&= \frac{1}{\sqrt{2 \pi} \sigma} \left( [0 - 0] + \mu \left[ \sqrt{\frac{\pi}{2}} \sigma - \left(- \sqrt{\frac{\pi}{2}} \sigma \right) \right] \right) \\
&= \frac{1}{\sqrt{2 \pi} \sigma} \cdot \mu \cdot 2 \sqrt{\frac{\pi}{2}} \sigma \\
&= \mu \; .
\end{split}
$$
