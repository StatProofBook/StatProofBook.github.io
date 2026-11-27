---
layout: proof
mathjax: true

author: "Emptybiu"
affiliation: ""
e_mail: ""
date: 2026-11-21 00:00:00

title: "Differential entropy of the arcsine distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Arcsine distribution"
theorem: "Differential entropy"

sources:
  - authors: "SciPy Developers"
    year: "????"
    title: "Arcsine Distribution"
    in: "SciPy User Guide"
    pages: "retrieved on 2026-11-21"
    url: "https://docs.scipy.org/doc/scipy/tutorial/stats/continuous_arcsine.html"
  - authors: "Kyle Siegrist"
    year: "????"
    title: "The Arcsine Distribution"
    in: "Probability, Mathematical Statistics, and Stochastic Processes"
    pages: "retrieved on 2026-11-21"
    url: "https://www.randomservices.org/random/special/Arcsine.html"

proof_id: "P571"
shortcut: "arcsin-dent"
username: "Emptybiu"
---


**Theorem:** Let $X$ have the standard [arcsine distribution](/D/arcsin), with [density](/P/arcsin-pdf) $f_X(x)=1/(\pi\sqrt{x(1-x)})$ on $0<x<1$ and zero outside this interval. Its [differential entropy](/D/dent) in nats is

$$ \label{eq:arcsine-entropy}
h(X) = -\int_0^1 f_X(x) \log f_X(x) \, \mathrm{d}x
     = \log\!\left(\frac{\pi}{4}\right) \; .
$$


**Proof:** The [arcsine CDF proof](/P/arcsin-cdf) gives the density above as a special case of the [beta density](/P/beta-pdf). Throughout, $\log$ denotes the natural logarithm. Set $x = \sin^2 t$ for $0 < t < \pi/2$. On this open interval, both sine and cosine are positive. Consequently, $f_X(x) \, \mathrm{d}x = (2/\pi) \, \mathrm{d}t$ and $-\log f_X(x) = \log\pi + \log\sin t + \log\cos t$.

First, apply this substitution on compact subintervals of $(0,1)$. As $t \downarrow 0$, the ratio $(\sin t)/t$ tends to $1$, so $\log \sin t - \log t$ stays bounded. The absolute value of $\log t$ is integrable near zero, and $\log \sin t$ is bounded near $\pi/2$. The substitution $t \mapsto \pi/2 - t$ gives the corresponding bounds for $\log \cos t$. Thus, the transformed integrand is absolutely integrable, justifying both endpoint limits and giving

$$ \label{eq:arcsine-entropy-integral}
h(X) = \log\pi + \frac{2}{\pi} \int_0^{\pi/2} \left( \log \sin t + \log \cos t \right) \, \mathrm{d}t \; .
$$

Write $I = \int_0^{\pi/2} \log \sin t \, \mathrm{d}t$. The same reflection shows that the log-cosine integral is also $I$. Since $2 \sin t \cos t = \sin(2t)$, the substitution $u = 2t$ gives

$$ \label{eq:arcsine-log-sine}
2I = \frac{1}{2}\int_0^\pi \log \sin u \, \mathrm{d}u - \frac{\pi}{2} \log 2
   = I - \frac{\pi}{2} \log 2 \; ,
$$

where the second equality follows from $\sin(\pi-u) = \sin u$. Therefore $I = -(\pi/2) \log 2$, and \eqref{eq:arcsine-entropy-integral} yields $h(X) = \log\pi - 2 \log 2 = \log(\pi/4)$, proving \eqref{eq:arcsine-entropy}.