---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-10-15 12:04:00

title: "Relationship between gamma distribution and standard gamma distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Gamma distribution"
theorem: "Relationship to standard gamma distribution"

sources:

proof_id: "P177"
shortcut: "gam-sgam2"
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

Because $b$ is positive, $g(X)$ is strictly increasing and we can calculate the [probability density function of a strictly increasing function](/P/pdf-sifct) as

$$ \label{eq:pdf-sifct}
f_Y(y) = \left\{
\begin{array}{rl}
f_X(g^{-1}(y)) \, \frac{\mathrm{d}g^{-1}(y)}{\mathrm{d}y} \; , & \text{if} \; y \in \mathcal{Y} \\
0 \; , & \text{if} \; y \notin \mathcal{Y}
\end{array}
\right.
$$

where $\mathcal{Y} = \left\lbrace y = g(x): x \in \mathcal{X} \right\rbrace$. With the [probability density function of the gamma distribution](/P/gam-pdf), we have

$$ \label{eq:pdf-Y}
\begin{split}
f_Y(y) &= \frac{b^a}{\Gamma(a)} [g^{-1}(y)]^{a-1} \exp[-b \, g^{-1}(y)] \cdot \frac{\mathrm{d}g^{-1}(y)}{\mathrm{d}y} \\
&= \frac{b^a}{\Gamma(a)} \left(\frac{1}{b} y\right)^{a-1} \exp\left[-b \left(\frac{1}{b} y\right)\right] \cdot \frac{\mathrm{d}\left(\frac{1}{b} y\right)}{\mathrm{d}y} \\
&= \frac{b^a}{\Gamma(a)} \, \frac{1}{b^{a-1}} \, y^{a-1} \exp[-y] \cdot \frac{1}{b} \\
&= \frac{1}{\Gamma(a)} \, y^{a-1} \exp[-y]
\end{split}
$$

which is the [probability density function](/D/pdf) of the [standard gamma distribution](/D/sgam).