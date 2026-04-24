---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2026-04-21 15:01:45

title: "von Mises distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "von Mises distribution"
definition: "Definition"

sources:
  - authors: "Bishop CM"
    year: 2006
    title: "Probability Distributions"
    in: "Pattern Recognition for Machine Learning"
    pages: "Appendix B, p. 693, eq. B.77"
    url: "http://users.isr.ist.utl.pt/~wurmd/Livros/school/Bishop%20-%20Pattern%20Recognition%20And%20Machine%20Learning%20-%20Springer%20%202006.pdf"

def_id: "D231"
shortcut: "vm"
username: "JoramSoch"
---


**Definition:** Let $X$ be a [circular](/D/rvar-circ) [random variable](/D/rvar). Then, $X$ is said to follow a von Mises distribution with circular mean $\mu$ and reciprocal dispersion $\kappa$

$$ \label{eq:vm}
X \sim \mathrm{vM}(\mu, \kappa) \; ,
$$

if and only if its [probability density function](/D/pdf) is given by

$$ \label{eq:vm-pdf}
\mathrm{vM}(x; \mu, \kappa) = \frac{1}{2 \pi I_0(\kappa)} \cdot \exp \left[ \kappa \cos(x-\mu) \right]
$$

where $\mu \in \mathbb{R}$, $\kappa > 0$ and $I_0(\kappa)$ is the zeroth-order modified Bessel function of the first kind:

$$ \label{eq:vm-bessel}
I_0(\kappa) = \frac{1}{2\pi} \int_0^{2\pi} \exp \left[ \kappa \cos(x) \right] \, \mathrm{d}x \; .
$$