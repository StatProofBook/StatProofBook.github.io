---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-08-25 21:11:00

title: "Extreme points of the probability density function of the normal distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Normal distribution"
theorem: "Extreme points"

sources:
  - authors: "Wikipedia"
    year: 2021
    title: "Normal distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-08-25"
    url: "https://en.wikipedia.org/wiki/Normal_distribution#Symmetries_and_derivatives"

proof_id: "P251"
shortcut: "norm-extr"
username: "JoramSoch"
---


**Theorem:** The [probability density function](/D/pdf) of the [normal distribution](/D/norm) with mean $\mu$ and variance $\sigma^2$ has a maximum at $x = \mu$ and no other extrema. Consequently, the [normal distribution](/D/norm) is a [unimodal probability distribution](/D/dist-uni).


**Proof:** The [probability density function of the normal distribution](/P/norm-pdf) is:

$$ \label{eq:norm-pdf}
f_X(x) = \frac{1}{\sqrt{2 \pi} \sigma} \cdot \exp \left[ -\frac{1}{2} \left( \frac{x-\mu}{\sigma} \right)^2 \right] \; .
$$

The [first two deriatives of this function](/P/norm-mode) are:

$$ \label{eq:norm-pdf-der1}
f'_X(x) = \frac{\mathrm{d}f_X(x)}{\mathrm{d}x} = \frac{1}{\sqrt{2 \pi} \sigma^3} \cdot (-x + \mu) \cdot \exp \left[ -\frac{1}{2} \left( \frac{x-\mu}{\sigma} \right)^2 \right]
$$

$$ \label{eq:norm-pdf-der2}
f''_X(x) = \frac{\mathrm{d}^2f_X(x)}{\mathrm{d}x^2} = -\frac{1}{\sqrt{2 \pi} \sigma^3} \cdot \exp \left[ -\frac{1}{2} \left( \frac{x-\mu}{\sigma} \right)^2 \right] + \frac{1}{\sqrt{2 \pi} \sigma^5} \cdot (-x + \mu)^2 \cdot \exp \left[ -\frac{1}{2} \left( \frac{x-\mu}{\sigma} \right)^2 \right] \; .
$$

The first derivative is zero, if and only if

$$ \label{eq:norm-pdf-der1-zero}
-x + \mu = 0 \quad \Leftrightarrow \quad x = \mu \; .
$$

Since the second derivative is negative at this value

$$ \label{eq:norm-pdf-der2-extr}
f''_X(\mu) = -\frac{1}{\sqrt{2 \pi} \sigma^3} < 0 \; ,
$$

there is a maximum at $x = \mu$. From \eqref{eq:norm-pdf-der1}, it can be seen that $f'_X(x)$ is positive for $x < \mu$ and negative for $x > \mu$. Thus, there are no further extrema and $\mathcal{N}(\mu, \sigma^2)$ is [unimodal](/P/norm-mode).