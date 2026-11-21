---
layout: proof
mathjax: true

author: "Lee Crossley"
affiliation: ""
e_mail: ""
date: 2026-11-21 22:12:01

title: "Expected log-determinant of a Wishart random matrix"
chapter: "Probability Distributions"
section: "Matrix-variate continuous distributions"
topic: "Wishart distribution"
theorem: "Expected log-determinant"

sources:
  - authors: "Bishop, Christopher M."
    year: 2006
    title: "Pattern Recognition and Machine Learning"
    in: "Springer"
    pages: "Appendix B, p. 693, equations B.78–B.81"
    url: "https://www.microsoft.com/en-us/research/wp-content/uploads/2006/01/Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf"

proof_id: "P568"
shortcut: "wish-logdetmean"
username: "leecrossley"
---


**Theorem.** Let $S$ have the $p \times p$ [Wishart distribution](/D/wish) with positive-definite scale $V$ and real degrees of freedom $\nu>p-1$. With $\psi(x)=\frac{\mathrm{d}}{\mathrm{d}x}\log\Gamma(x)$, its expected log-determinant is

$$ \label{eq:wish-logdetmean}
\mathrm{E}[\log |S|]=\log |V|+p\log 2+
\sum_{j=1}^{p}\psi\!\left(\frac{\nu+1-j}{2}\right).
$$

**Proof.** Write $c(\nu,V)$ for the normalizing denominator of the Wishart density on positive-definite matrices. In terms of the multivariate gamma function it is

$$
c(\nu,V)=2^{p\nu/2}|V|^{\nu/2}\Gamma_p(\nu/2),
\qquad
\Gamma_p(a)=\pi^{p(p-1)/4}\prod_{j=1}^{p}\Gamma\!\left(a+\frac{1-j}{2}\right).
$$

The density is $|S|^{(\nu-p-1)/2}\exp[-\operatorname{tr}(V^{-1}S)/2]/c(\nu,V)$. Multiplication by $|S|^t$ increases the determinant exponent by $t$ and leaves the trace term fixed. When $\nu+2t>p-1$, integrating this new density kernel gives

$$
M(t)=\mathrm{E}\!\left[e^{t\log|S|}\right]
=\frac{c(\nu+2t,V)}{c(\nu,V)}
=2^{pt}|V|^t\frac{\Gamma_p(\nu/2+t)}{\Gamma_p(\nu/2)}.
$$

The interval of admissible $t$ contains zero in its interior, so this moment-generating function is differentiable there and $M'(0)=\mathrm{E}[\log|S|]$. Since $M(0)=1$, the derivative of $\log M$ at zero has the same value. Differentiating the product formula for $\Gamma_p$ gives the sum of digamma functions in \eqref{eq:wish-logdetmean}.
