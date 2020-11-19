---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-11-19 07:31:00

title: "Quantile function of the gamma distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Gamma distribution"
theorem: "Quantile function"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Incomplete gamma function"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-11-19"
    url: "https://en.wikipedia.org/wiki/Incomplete_gamma_function#Definition"

proof_id: "P194"
shortcut: "gam-qf"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [gamma distribution](/D/gam):

$$ \label{eq:gam}
X \sim \mathrm{Gam}(a,b) \; .
$$

Then, the [quantile function](/D/qf) of $X$ is

$$ \label{eq:gam-qf}
Q_X(p) = \left\{
\begin{array}{rl}
-\infty \; , & \text{if} \; p = 0 \\
\gamma^{-1}(a, \Gamma(a) \cdot p)/b \; , & \text{if} \; p > 0
\end{array}
\right.
$$

where $\gamma^{-1}(s, y)$ is the inverse of the lower incomplete gamma function $\gamma(s, x)$


**Proof:** The [cumulative distribution function of the gamma distribution](/P/gam-cdf) is:

$$ \label{eq:gam-cdf}
F_X(x) = \left\{
\begin{array}{rl}
0 \; , & \text{if} \; x < 0 \\
\frac{\gamma(a,bx)}{\Gamma(a)} \; , & \text{if} \; x \geq 0 \; .
\end{array}
\right.
$$

The quantile function $Q_X(p)$ [is defined as](/D/qf) the smallest $x$, such that $F_X(x) = p$:

$$ \label{eq:qf}
Q_X(p) = \min \left\lbrace x \in \mathbb{R} \, \vert \, F_X(x) = p \right\rbrace \; .
$$

Thus, we have $Q_X(p) = -\infty$, if $p = 0$. When $p > 0$, [it holds that](/P/qf-cdf)

$$ \label{eq:gam-qf-s1}
Q_X(p) = F_X^{-1}(x) \; .
$$

This can be derived by rearranging equation \eqref{eq:gam-cdf}:

$$ \label{eq:gam-qf-s2}
\begin{split}
p &= \frac{\gamma(a,bx)}{\Gamma(a)} \\
\Gamma(a) \cdot p &= \gamma(a,bx) \\
\gamma^{-1}(a, \Gamma(a) \cdot p) &= bx \\
x &= \frac{\gamma^{-1}(a, \Gamma(a) \cdot p)}{b} \; .
\end{split}
$$