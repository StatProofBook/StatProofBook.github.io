---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-05-26 23:01:00

title: "Relation between normal distribution and standard normal distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Normal distribution"
theorem: "Relation to standard normal distribution"

sources:

proof_id: "P111"
shortcut: "norm-snorm"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [normal distribution](/D/norm) with mean $\mu$ and variance $\sigma^2$:

$$ \label{eq:X-norm}
X \sim \mathcal{N}(\mu, \sigma^2) \; .
$$

Then, the quantity $Z = (X-\mu)/\sigma$ will have a [standard normal distribution](/D/snorm) with mean $0$ and variance $1$:

$$ \label{eq:Z-snorm}
Z = \frac{X-\mu}{\sigma} \sim \mathcal{N}(0, 1) \; .
$$


**Proof:** Rearranging to get $X$ in terms of $Z$, we have

$$ \label{eq:X-Z}
X = \sigma Z + \mu \; .
$$

The [cumulative distribution function of the normally distributed](/P/norm-cdf) $X$ is

$$ \label{eq:norm-cdf}
F_X(t) = \int_{-\infty}^{t} \frac{1}{\sqrt{2 \pi} \sigma} \cdot \exp \left[ -\frac{1}{2} \left( \frac{x-\mu}{\sigma} \right)^2 \right] \, \mathrm{d}x \; .
$$

Substituting \eqref{eq:X-Z} into \eqref{eq:norm-cdf}, we obtain

$$ \label{eq:snorm-cdf}
\begin{split}
F_Z(t) &= \int_{-\infty}^{t} \frac{1}{\sqrt{2 \pi} \sigma} \cdot \exp \left[ -\frac{1}{2} \left( \frac{(\sigma z + \mu)-\mu}{\sigma} \right)^2 \right] \, \mathrm{d}(\sigma z + \mu) \\
&= \int_{-\infty}^{t} \frac{\sigma}{\sqrt{2 \pi} \sigma} \cdot \exp \left[ -\frac{1}{2} z^2 \right] \, \mathrm{d}z \\
&= \int_{-\infty}^{t} \frac{1}{\sqrt{2 \pi}} \cdot \exp \left[ -\frac{1}{2} z^2 \right] \, \mathrm{d}z
\end{split}
$$

which is the [cumulative distribution function](/D/cdf) of the [standard normal distribution](/D/snorm).