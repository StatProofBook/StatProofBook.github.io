---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-05-26 23:14:00

title: "Relationship between gamma distribution and standard gamma distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Gamma distribution"
theorem: "Relationship to standard gamma distribution"

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


**Proof:** Note that $Y$ is a function of $X$

$$ \label{eq:Y-X}
Y = g(X) = b X
$$

with the inverse function

$$ \label{eq:X-Y}
X = g^{-1}(Y) = \frac{1}{b} Y \; .
$$

Because $b$ is positive, $g(X)$ is strictly increasing and we can calculate the [cumulative distribution function of a strictly increasing function](/P/cdf-sifct) as

$$ \label{eq:cdf-sifct}
F_Y(y) = \left\{
\begin{array}{rl}
0 \; , & \text{if} \; y < \mathrm{min}(\mathcal{Y}) \\
F_X(g^{-1}(y)) \; , & \text{if} \; y \in \mathcal{Y} \\
1 \; , & \text{if} \; y > \mathrm{max}(\mathcal{Y}) \; .
\end{array}
\right.
$$

The [cumulative distribution function of the gamma-distributed](/P/gam-cdf) $X$ is

$$ \label{eq:gam-cdf}
F_X(x) = \int_{-\infty}^{x} \frac{b^a}{\Gamma(a)} t^{a-1} \exp[-b t] \, \mathrm{d}t \; .
$$

Applying \eqref{eq:cdf-sifct} to \eqref{eq:gam-cdf}, we have:

$$ \label{eq:Y-cdf-s1}
\begin{split}
F_Y(y) &\overset{\eqref{eq:cdf-sifct}}{=} F_X(g^{-1}(y)) \\
&\overset{\eqref{eq:gam-cdf}}{=} \int_{-\infty}^{y/b} \frac{b^a}{\Gamma(a)} t^{a-1} \exp[-b t] \, \mathrm{d}t \; .
\end{split}
$$

Substituting $s = b t$, such that $t = s/b$, we obtain

$$ \label{eq:Z-cdf-s2}
\begin{split}
F_Y(y) &= \int_{-b \infty}^{b (y/b)} \frac{b^a}{\Gamma(a)} \left(\frac{s}{b}\right)^{a-1} \exp\left[-b \left(\frac{s}{b}\right)\right] \, \mathrm{d}\left(\frac{s}{b}\right) \\
&= \int_{-\infty}^{y} \frac{b^a}{\Gamma(a)} \, \frac{1}{b^{a-1} \, b} \, s^{a-1} \exp[-s] \, \mathrm{d}s \\
&= \int_{-\infty}^{y} \frac{1}{\Gamma(a)} s^{a-1} \exp[-s] \, \mathrm{d}s
\end{split}
$$

which is the [cumulative distribution function](/D/cdf) of the [standard gamma distribution](/D/sgam).