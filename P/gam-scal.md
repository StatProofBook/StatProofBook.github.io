---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2023-11-24 13:08:34

title: "Scaling of a random variable following the gamma distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Gamma distribution"
theorem: "Scaling of a gamma random variable"

sources:

proof_id: "P426"
shortcut: "gam-scal"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [gamma distribution](/D/gam) with shape $a$ and rate $b$:

$$ \label{eq:gam}
X \sim \mathrm{Gam}(a,b) \; .
$$

Then, the quantity $Y = c X$ will also be gamma-distributed with shape $a$ and rate $b/c$:

$$ \label{eq:gam-scal}
Y = c X \sim \mathrm{Gam}\left( a, \frac{b}{c} \right) \; .
$$


**Proof:**  Note that $Y$ is a function of $X$

$$ \label{eq:Y-X}
Y = g(X) = c X
$$

with the inverse function

$$ \label{eq:X-Y}
X = g^{-1}(Y) = \frac{1}{c} Y \; .
$$

Because the parameters of a gamma distribution [are positive](/D/gam), $c$ must also be positive. Thus, $g(X)$ is strictly increasing and we can calculate the [probability density function of a strictly increasing function](/P/pdf-sifct) as

$$ \label{eq:pdf-sifct}
f_Y(y) = \left\{
\begin{array}{rl}
f_X(g^{-1}(y)) \, \frac{\mathrm{d}g^{-1}(y)}{\mathrm{d}y} \; , & \text{if} \; y \in \mathcal{Y} \\
0 \; , & \text{if} \; y \notin \mathcal{Y}
\end{array}
\right.
$$

The [probability density function of the gamma-distributed](/P/gam-pdf) $X$ is

$$ \label{eq:gam-pdf}
f_X(x) = \frac{b^a}{\Gamma(a)} x^{a-1} \exp[-b x] \; .
$$

Applying \eqref{eq:pdf-sifct} to \eqref{eq:gam-pdf}, we have:

$$ \label{eq:Y-pdf}
\begin{split}
f_Y(y) &= \frac{b^a}{\Gamma(a)} [g^{-1}(y)]^{a-1} \exp[-b g^{-1}(y)] \, \frac{\mathrm{d}g^{-1}(y)}{\mathrm{d}y} \\
&= \frac{b^a}{\Gamma(a)} \left( \frac{1}{c} y \right)^{a-1} \exp\left[-b \left( \frac{1}{c} y \right) \right] \, \frac{\mathrm{d}\left( \frac{1}{c} y \right)}{\mathrm{d}y} \\
&= \frac{b^a}{\Gamma(a)} \left( \frac{1}{c} \right)^{a} \left( \frac{1}{c} \right)^{-1} y^{a-1} \exp\left[- \frac{b}{c} y \right] \, \frac{1}{c} \\
&= \frac{(b/c)^a}{\Gamma(a)} y^{a-1} \exp\left[- \frac{b}{c} y \right]
\end{split}
$$

which is the [probability density function](/D/pdf) of a [gamma distribution](/D/gam) with shape $a$ and rate $b/c$.