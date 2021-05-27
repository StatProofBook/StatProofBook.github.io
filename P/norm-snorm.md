---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-05-26 23:01:00

title: "Relationship between normal distribution and standard normal distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Normal distribution"
theorem: "Relationship to standard normal distribution"

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


**Proof:** Note that $Z$ is a function of $X$

$$ \label{eq:Z-X}
Z = g(X) = \frac{X-\mu}{\sigma}
$$

with the inverse function

$$ \label{eq:X-Z}
X = g^{-1}(Z) = \sigma Z + \mu \; .
$$

Because $\sigma$ is positive, $g(X)$ is strictly increasing and we can calculate the [cumulative distribution function of a strictly increasing function](/P/cdf-sifct) as

$$ \label{eq:cdf-sifct}
F_Y(y) = \left\{
\begin{array}{rl}
0 \; , & \text{if} \; y < \mathrm{min}(\mathcal{Y}) \\
F_X(g^{-1}(y)) \; , & \text{if} \; y \in \mathcal{Y} \\
1 \; , & \text{if} \; y > \mathrm{max}(\mathcal{Y}) \; .
\end{array}
\right.
$$

The [cumulative distribution function of the normally distributed](/P/norm-cdf) $X$ is

$$ \label{eq:norm-cdf}
F_X(x) = \int_{-\infty}^{x} \frac{1}{\sqrt{2 \pi} \sigma} \cdot \exp \left[ -\frac{1}{2} \left( \frac{t-\mu}{\sigma} \right)^2 \right] \, \mathrm{d}t \; .
$$

Applying \eqref{eq:cdf-sifct} to \eqref{eq:norm-cdf}, we have:

$$ \label{eq:Z-cdf-s1}
\begin{split}
F_Z(z) &\overset{\eqref{eq:cdf-sifct}}{=} F_X(g^{-1}(z)) \\
&\overset{\eqref{eq:norm-cdf}}{=} \int_{-\infty}^{\sigma z + \mu} \frac{1}{\sqrt{2 \pi} \sigma} \cdot \exp \left[ -\frac{1}{2} \left( \frac{t-\mu}{\sigma} \right)^2 \right] \, \mathrm{d}t \; .
\end{split}
$$

Substituting $s = (t - \mu)/\sigma$, such that $t = \sigma s + \mu$, we obtain

$$ \label{eq:Z-cdf-s2}
\begin{split}
F_Z(z) &= \int_{(-\infty - \mu)/\sigma}^{([\sigma z + \mu] - \mu)/\sigma} \frac{1}{\sqrt{2 \pi} \sigma} \cdot \exp \left[ -\frac{1}{2} \left( \frac{(\sigma s + \mu)-\mu}{\sigma} \right)^2 \right] \, \mathrm{d}(\sigma s + \mu) \\
&= \int_{-\infty}^{z} \frac{\sigma}{\sqrt{2 \pi} \sigma} \cdot \exp \left[ -\frac{1}{2} s^2 \right] \, \mathrm{d}s \\
&= \int_{-\infty}^{z} \frac{1}{\sqrt{2 \pi}} \cdot \exp \left[ -\frac{1}{2} s^2 \right] \, \mathrm{d}s
\end{split}
$$

which is the [cumulative distribution function](/D/cdf) of the [standard normal distribution](/D/snorm).