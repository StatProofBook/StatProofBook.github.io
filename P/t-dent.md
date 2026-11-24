---
layout: proof
mathjax: true

author: "Artemis Data Desk"
affiliation: ""
e_mail: ""
date: 2026-11-24 15:00:00

title: "Differential entropy of the t-distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "t-distribution"
theorem: "Differential entropy"

sources:
  - authors: "Cook, John D."
    year: 2022
    title: "Entropy of a Student t distribution"
    in: "John D. Cook Consulting"
    pages: "November 15"
    url: "https://www.johndcook.com/blog/2022/11/15/t-entropy/"
  - authors: "Askey, R. A. and Roy, R."
    year: 2010
    title: "Gamma Function"
    in: "NIST Digital Library of Mathematical Functions"
    pages: "equations 5.2.2, 5.12.1 and 5.12.3"
    url: "https://dlmf.nist.gov/5.12"

proof_id: "P573"
shortcut: "t-dent"
username: "theyounganimation-rgb"
---


**Theorem.** If $X$ has a standard [t-distribution](/D/t) with $\nu>0$ degrees of freedom, its [differential entropy](/D/dent) in nats is

$$ \label{eq:t-dent}
\mathrm{h}(X)
= \ln\!\left[\sqrt{\nu}\,\mathrm{B}\!\left(\tfrac12,\tfrac{\nu}{2}\right)\right]
+ \frac{\nu+1}{2}
  \left[\psi\!\left(\tfrac{\nu+1}{2}\right)-\psi\!\left(\tfrac{\nu}{2}\right)\right] .
$$

Here $\mathrm{B}$ is the beta function and $\psi(z)=(\ln\Gamma(z))'$ is the digamma function.


**Proof.** Put $a=(\nu+1)/2$ and $Y=X/\sqrt{\nu}$. The [density of $X$](/P/t-pdf) gives $Y$ density $(1+y^2)^{-a}/I(a)$, where, for any $s>1/2$,

$$ \label{eq:t-dent-beta}
I(s)=\int_{-\infty}^{\infty}(1+y^2)^{-s}\,\mathrm{d}y
=\int_0^\infty u^{-1/2}(1+u)^{-s}\,\mathrm{d}u
=\mathrm{B}\!\left(\tfrac12,s-\tfrac12\right).
$$

The second equality uses symmetry and $u=y^2$. Fix $s_0$ with $1/2<s_0<a$. For $s$ in a neighborhood of $a$ with $s>s_0$, the absolute derivative of the first integrand is bounded by $(1+y^2)^{-s_0}\ln(1+y^2)$. This is integrable, so differentiating under the integral gives

$$ \label{eq:t-dent-expectation}
\mathrm{E}\!\left[\ln(1+Y^2)\right]
=-\frac{I'(a)}{I(a)}
=\psi(a)-\psi(a-\tfrac12).
$$

The last equality follows by taking the logarithmic derivative of $I(s)=\Gamma(1/2)\Gamma(s-1/2)/\Gamma(s)$. Finally, the density of $X$ is $f_\nu(x)=(1+x^2/\nu)^{-a}/(\sqrt{\nu}\,I(a))$. Hence

$$ \label{eq:t-dent-density}
\mathrm{h}(X)=-\mathrm{E}\!\left[\ln f_\nu(X)\right]
=\ln\!\left(\sqrt{\nu}\,I(a)\right)+a\,\mathrm{E}\!\left[\ln(1+Y^2)\right] .
$$

Substitution of $\eqref{eq:t-dent-beta}$ and $\eqref{eq:t-dent-expectation}$ into $\eqref{eq:t-dent-density}$ gives $\eqref{eq:t-dent}$. $\blacksquare$
