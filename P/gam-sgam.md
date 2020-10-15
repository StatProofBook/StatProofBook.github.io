---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-05-26 23:14:00

title: "Relation between gamma distribution and standard gamma distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Gamma distribution"
theorem: "Relation to standard gamma distribution"

sources:

proof_id: "P112"
shortcut: "gam-sgam"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [gamma distribution](/D/gam) with shape $a$ and rate $b$:

$$ \label{eq:X-gam}
X \sim \mathrm{Gam}(a,b) \; .
$$

Then, the quantity $Y = b X$ will have a [standard gamma distribution](/D/sgam) with shape $a$ and rate $1$:

$$ \label{eq:Y-snorm}
Y = b X \sim \mathrm{Gam}(a,1) \; .
$$


**Proof:** Rearranging to get $X$ in terms of $Y$, we have

$$ \label{eq:X-Y}
X = \frac{1}{b} Y \; .
$$

The [cumulative distribution function of the gamma-distributed](/P/gam-cdf) $X$ is

$$ \label{eq:gam-cdf}
F_X(t) = \int_{-\infty}^{t} \frac{b^a}{\Gamma(a)} x^{a-1} \exp[-b x] \, \mathrm{d}x \; .
$$

Substituting \eqref{eq:X-Y} into \eqref{eq:gam-cdf}, we obtain

$$ \label{eq:sgam-cdf}
\begin{split}
F_Z(t) &= \int_{-\infty}^{t} \frac{b^a}{\Gamma(a)} \left(\frac{1}{b} y\right)^{a-1} \exp\left[-b \left(\frac{1}{b} y\right)\right] \, \mathrm{d}\left(\frac{1}{b} y\right) \\
&= \int_{-\infty}^{t} \frac{b^a}{b} \left(\frac{1}{b}\right)^{a-1} \cdot \frac{1}{\Gamma(a)} y^{a-1} \exp[-y] \, \mathrm{d}y \\
&= \int_{-\infty}^{t} \frac{1}{\Gamma(a)} y^{a-1} \exp[-y] \, \mathrm{d}y
\end{split}
$$

which is the [cumulative distribution function](/D/cdf) of the [standard gamma distribution](/D/sgam).