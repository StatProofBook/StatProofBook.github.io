---
layout: proof
mathjax: true

author: "Thomas J. Faulkenberry"
affiliation: "Tarleton State University"
e_mail: "faulkenberry@tarleton.edu"
date: 2020-09-13 12:00:00

title: "Moment-generating function of the Wald distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Wald distribution"
theorem: "Moment-generating function"

sources:
  - authors: "Siegrist, K."
    year: 2020
    title: "The Wald Distribution"
    in: "Random: Probability, Mathematical Statistics, Stochastic Processes"
    pages: "retrieved on 2020-09-13"
    url: "https://www.randomservices.org/random/special/Wald.html"
  - authors: "National Institute of Standards and Technology"
    year: 2020
    title: "NIST Digital Library of Mathematical Functions"
    pages: "retrieved on 2020-09-13"
    url: "https://dlmf.nist.gov"

proof_id: "P168"
shortcut: "wald-mgf"
username: "tomfaulkenberry"
---


**Theorem:** Let $X$ be a positive [random variable](/D/rvar) following a [Wald distribution](/D/wald):

$$ \label{eq:wald}
X \sim \mathrm{Wald}(\gamma, \alpha) \; .
$$

Then, the [moment-generating function](/D/mgf) of $X$ is

$$ \label{eq:wald-mgf}
M_X(t) = \exp \left[ \alpha\gamma-\sqrt{\alpha^2(\gamma^2-2t)}\right] \; .
$$


**Proof:** The [probability density function of the Wald distribution](/P/wald-pdf) is

$$ \label{eq:wald-pdf}
f_X(x) = \frac{\alpha}{\sqrt{2\pi x^3}}\exp\left(-\frac{(\alpha-\gamma x)^2}{2x}\right)
$$

and the [moment-generating function](/D/mgf) is defined as

$$ \label{eq:mgf-var}
M_X(t) = \mathrm{E} \left[ e^{tX} \right] \; .
$$

Using the definition of [expected value for continuous random variables](/D/mean), the moment-generating function of $X$ therefore is

$$ \label{eq:wald-mgf-s1}
\begin{split}
M_X(t) &= \int_0^{\infty} e^{tx} \cdot \frac{\alpha}{\sqrt{2\pi x^3}}\cdot \exp\left[-\frac{(\alpha-\gamma x)^2}{2x}\right]dx \\
&= \frac{\alpha}{\sqrt{2\pi}}\int_0^{\infty} x^{-3/2}\cdot \exp\left[tx - \frac{(\alpha-\gamma x)^2}{2x}\right]dx \; .
\end{split}
$$

To evaluate this integral, we will need two identities about [modified Bessel functions of the second kind](https://dlmf.nist.gov/10.25), denoted $K_{p}$. The function $K_{p}$ (for $p\in \mathbb{R}$) is one of the two linearly independent solutions of the differential equation

$$ \label{eq:bessel-de}
x^2\frac{d^2y}{dx^2} + x\frac{dy}{dx}-(x^2+p^2)y=0 \; .
$$

The [first of these identities](https://dlmf.nist.gov/10.39.2) gives an explicit solution for $K_{-1/2}$:

$$ \label{eq:bessel-fact1}
K_{-1/2}(x) = \sqrt{\frac{\pi}{2x}} e^{-x} \; .
$$

The [second of these identities](https://dlmf.nist.gov/10.32.10) gives an integral representation of $K_p$:

$$ \label{eq:bessel-fact2}
K_p(\sqrt{ab}) = \frac{1}{2}\left(\frac{a}{b}\right)^{p/2} \int_0^{\infty}x^{p-1}\cdot \exp\left[-\frac{1}{2}\left(ax + \frac{b}{x}\right)\right]dx \; .
$$

Starting from \eqref{eq:wald-mgf-s1}, we can expand the binomial term and rearrange the moment generating function into the following form:

$$ \label{eq:wald-mgf-s2}
\begin{split}
M_X(t) &= \frac{\alpha}{\sqrt{2\pi}} \int_0^{\infty} x^{-3/2}\cdot \exp\left[ tx - \frac{\alpha^2}{2x} + \alpha\gamma - \frac{\gamma^2x}{2}\right]dx \\
       &= \frac{\alpha}{\sqrt{2\pi}}\cdot e^{\alpha \gamma} \int_0^{\infty} x^{-3/2}\cdot \exp\left[\left(t-\frac{\gamma^2}{2}\right)x - \frac{\alpha^2}{2x}\right]dx \\
       &= \frac{\alpha}{\sqrt{2\pi}}\cdot e^{\alpha \gamma} \int_0^{\infty} x^{-3/2}\cdot \exp \left[-\frac{1}{2}\left(\gamma^2-2t\right)x - \frac{1}{2}\cdot \frac{\alpha^2}{x}\right]dx \; .
\end{split}
$$

The integral now has the form of the integral in \eqref{eq:bessel-fact2} with $p=-1/2$, $a=\gamma^2-2t$, and $b=\alpha^2$. This allows us to write the moment-generating function in terms of the modified Bessel function $K_{-1/2}$:

$$ \label{eq:wald-mgf-s3}
M_X(t) = \frac{\alpha}{\sqrt{2\pi}}\cdot e^{\alpha \gamma}\cdot 2\left(\frac{\gamma^2-2t}{\alpha^2}\right)^{1/4}\cdot K_{-1/2}\left(\sqrt{\alpha^2(\gamma^2-2t)}\right).
$$

Combining with \eqref{eq:bessel-fact1} and simplifying gives

$$ \label{eq:wald-mgf-s4}
\begin{split}
M_X(t) &= \frac{\alpha}{\sqrt{2\pi}}\cdot e^{\alpha \gamma}\cdot 2\left(\frac{\gamma^2-2t}{\alpha^2}\right)^{1/4} \cdot \sqrt{\frac{\pi}{2\sqrt{\alpha^2(\gamma^2-2t)}}}\cdot \exp\left[-\sqrt{\alpha^2(\gamma^2-2t)}\right] \\
       &= \frac{\alpha}{\sqrt{2}\cdot \sqrt{\pi}}\cdot e^{\alpha \gamma}\cdot 2 \cdot \frac{(\gamma^2-2t)^{1/4}}{\sqrt{\alpha}}\cdot \frac{\sqrt{\pi}}{\sqrt{2}\cdot \sqrt{\alpha}\cdot (\gamma^2-2t)^{1/4}}\cdot \exp\left[-\sqrt{\alpha^2(\gamma^2-2t)}\right] \\
       &= e^{\alpha \gamma} \cdot \exp\left[-\sqrt{\alpha^2(\gamma^2-2t)}\right] \\
       &= \exp\left[\alpha \gamma-\sqrt{\alpha^2(\gamma^2-2t)}\right] \; .
\end{split}
$$

This finishes the proof of \eqref{eq:wald-mgf}.