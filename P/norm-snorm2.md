---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-10-15 11:42:00

title: "Relationship between normal distribution and standard normal distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Normal distribution"
theorem: "Relationship to standard normal distribution"

sources:

proof_id: "P176"
shortcut: "norm-snorm2"
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

Because $\sigma$ is positive, $g(X)$ is strictly increasing and we can calculate the [probability density function of a strictly increasing function](/P/pdf-sifct) as

$$ \label{eq:pdf-sifct}
f_Y(y) = \left\{
\begin{array}{rl}
f_X(g^{-1}(y)) \, \frac{\mathrm{d}g^{-1}(y)}{\mathrm{d}y} \; , & \text{if} \; y \in \mathcal{Y} \\
0 \; , & \text{if} \; y \notin \mathcal{Y}
\end{array}
\right.
$$

where $\mathcal{Y} = \left\lbrace y = g(x): x \in \mathcal{X} \right\rbrace$. With the [probability density function of the normal distribution](/P/norm-pdf), we have

$$ \label{eq:pdf-Z}
\begin{split}
f_Z(z) &= \frac{1}{\sqrt{2 \pi} \sigma} \cdot \exp \left[ -\frac{1}{2} \left( \frac{g^{-1}(z)-\mu}{\sigma} \right)^2 \right] \cdot \frac{\mathrm{d}g^{-1}(z)}{\mathrm{d}z} \\
&= \frac{1}{\sqrt{2 \pi} \sigma} \cdot \exp \left[ -\frac{1}{2} \left( \frac{(\sigma z + \mu)-\mu}{\sigma} \right)^2 \right] \cdot \frac{\mathrm{d}(\sigma z + \mu)}{\mathrm{d}z} \\
&= \frac{1}{\sqrt{2 \pi} \sigma} \cdot \exp \left[ -\frac{1}{2} z^2 \right] \cdot \sigma \\
&= \frac{1}{\sqrt{2 \pi}} \cdot \exp \left[ -\frac{1}{2} z^2 \right]
\end{split}
$$

which is the [probability density function](/D/pdf) of the [standard normal distribution](/D/snorm).