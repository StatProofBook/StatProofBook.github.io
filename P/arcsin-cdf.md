---
layout: proof
mathjax: true

author: "syndexco (AI-assisted)"
affiliation: ""
e_mail: ""
date: 2026-10-19 15:50:00

title: "Cumulative distribution function of the arcsine distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Arcsine distribution"
theorem: "Cumulative distribution function"

sources:
  - authors: "Kyle Siegrist"
    year: "????"
    title: "The Arcsine Distribution"
    in: "Probability, Mathematical Statistics, and Stochastic Processes"
    pages: "retrieved on 2026-10-19"
    url: "https://www.randomservices.org/random/special/Arcsine.html"

proof_id: "P565"
shortcut: "arcsin-cdf"
username: "syndexco"
---


**Theorem:** Let $X$ have the standard [arcsine distribution](/D/arcsin), that is, the [beta distribution](/D/beta) with both [shape parameters](/D/para-shape) equal to $1/2$:

$$ \label{eq:arcsine-beta}
X \sim \mathrm{Bet}\!\left(\frac{1}{2},\frac{1}{2}\right) \; .
$$

Its [cumulative distribution function](/D/cdf), defined for every real $x$, is

$$ \label{eq:arcsine-cdf}
F_X(x) =
\begin{cases}
0, & x \leq 0, \\
\dfrac{2}{\pi}\arcsin\!\left(\sqrt{x}\right), & 0 < x < 1, \\
1, & x \geq 1 \; .
\end{cases}
$$


**Proof:** By the [beta density formula](/P/beta-pdf), the density is proportional to $[t(1-t)]^{-1/2}$ on $(0,1)$ and vanishes elsewhere. To determine its normalizing constant, substitute $t=\sin^2\theta$ in the [integral defining the beta function](/D/beta). For $0<\theta<\pi/2$, both sine and cosine are positive, so

$$ \label{eq:arcsine-normalization}
  \mathrm{B}\!\left(\frac{1}{2},\frac{1}{2}\right)
= \int_0^1 \frac{\mathrm{d}t}{\sqrt{t(1-t)}}
= \int_0^{\pi/2} 2 \, \mathrm{d}\theta
= \pi \; .
$$

The substitution applies first on compact subintervals; taking the endpoint limits gives the displayed improper integral. Consequently, the [probability density function](/D/pdf) is $f_X(t)=1/[\pi\sqrt{t(1-t)}]$ for $0<t<1$.

For $0<x<1$, the same substitution has upper limit $\theta=\arcsin(\sqrt{x})$. Therefore,

$$ \label{eq:arcsine-cdf-interior}
  F_X(x)
= \frac{1}{\pi}\int_0^x \frac{\mathrm{d}t}{\sqrt{t(1-t)}}
= \frac{2}{\pi}\int_0^{\arcsin(\sqrt{x})}\mathrm{d}\theta
= \frac{2}{\pi}\arcsin(\sqrt{x}) \; .
$$

Finally, $X$ is absolutely continuous and supported on $[0,1]$. Thus, it has no atoms at $0$ or $1$, giving $F_X(x)=0$ for $x\leq0$ and $F_X(x)=1$ for $x\geq1$. This proves \eqref{eq:arcsine-cdf}.