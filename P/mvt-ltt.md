---
layout: proof
mathjax: true

author: "Lee Crossley"
affiliation: ""
e_mail: ""
date: 2026-11-21 22:12:02

title: "Linear transformation of a multivariate t-distributed random vector"
chapter: "Probability Distributions"
section: "Multivariate continuous distributions"
topic: "Multivariate t-distribution"
theorem: "Linear transformation"

sources:
  - authors: "Taboga, Marco"
    year: 2021
    title: "Multivariate Student's t distribution"
    in: "Lectures on probability theory and mathematical statistics"
    pages: "Online appendix"
    url: "https://www.statlect.com/probability-distributions/multivariate-student-t-distribution"

proof_id: "P569"
shortcut: "mvt-ltt"
username: "leecrossley"
---


**Theorem.** Suppose $X$ has the $p$-dimensional [multivariate $t$-distribution](/D/mvt) with location $\mu$, positive-definite scale matrix $\Sigma$ and $\nu>0$ degrees of freedom. If $A$ is a real $m\times p$ matrix of rank $m$ and $b\in\mathbb R^m$, then

$$ \label{eq:mvt-ltt}
AX+b\sim t(A\mu+b,A\Sigma A^\mathrm{T},\nu).
$$

In particular, if $LL^\mathrm{T}=\Sigma$ with $L$ invertible, then $L^{-1}(X-\mu)\sim t(0,I_p,\nu)$.

**Proof.** Set $a=\nu/2$. Draw a [gamma](/D/gam) random variable $U$ with shape $a$ and rate $a$. Conditional on $U=u$, draw $X$ from the normal distribution $\mathcal N(\mu,\Sigma/u)$. To check that this gives the required $t$-distribution, put $d=(x-\mu)^\mathrm{T}\Sigma^{-1}(x-\mu)$. Multiplying the conditional density by the gamma density and integrating yields

$$
\begin{aligned}
f_X(x)
&=\frac{a^a}{(2\pi)^{p/2}|\Sigma|^{1/2}\Gamma(a)}
  \int_0^\infty u^{a+p/2-1}e^{-(a+d/2)u}\,\mathrm{d}u\\
&=\frac{\Gamma((\nu+p)/2)}{\Gamma(\nu/2)(\nu\pi)^{p/2}|\Sigma|^{1/2}}
  \left(1+\frac{d}{\nu}\right)^{-(\nu+p)/2}.
\end{aligned}
$$

This is the [multivariate $t$ density](/P/mvt-pdf). Conditional on the same $U=u$, the [linear transformation of the normal vector](/P/mvn-ltt) gives

$$
AX+b\mid U=u\sim\mathcal N(A\mu+b,A\Sigma A^\mathrm{T}/u).
$$

Full row rank ensures $A\Sigma A^\mathrm{T}$ is positive definite. Applying the same integral in dimension $m$ proves \eqref{eq:mvt-ltt}. Taking $A=L^{-1}$ and $b=-L^{-1}\mu$ gives the standard form.
