---
layout: proof
mathjax: true

author: "Lee Crossley"
affiliation: ""
e_mail: ""
date: 2026-11-21 22:12:02

title: "Linear transformation theorem for the multivariate t-distribution"
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


**Theorem:** Suppose $X$ has an $n$-dimensional [multivariate $t$-distribution](/D/mvt) with location $\mu$, positive-definite scale matrix $\Sigma$ and $\nu>0$ degrees of freedom. If $A$ is a real $m \times n$ matrix of rank $m$ and $b \in \mathbb{R}^m$, then

$$ \label{eq:mvt-ltt}
AX + b \sim t(A\mu + b, A \Sigma A^\mathrm{T}, \nu) \; .
$$

In particular, if $LL^\mathrm{T}=\Sigma$ with invertible $L \in \mathbb{R}^{n \times n}$, then $L^{-1}(X-\mu) \sim t(0, I_p, \nu)$.


**Proof:** Set $a=\nu/2$ and let $U$ be a [gamma random variable](/D/gam) with shape $a$ and rate $a$. Conditional on $U=u$, let $X$ be a [multivariate normal random vector](/D/mvn) from $\mathcal{N}(\mu, \Sigma/u)$. To check that this gives the required $t$-distribution, let $d = (x-\mu)^\mathrm{T} \Sigma^{-1} (x-\mu)$. Multiplying the [conditional](/D/dist-cond) [normal density](/D/mvn-pdf) by the [gamma density](/D/gam-pdf) and integrating yields

$$ \label{eq:mvt-pdf}
\begin{split}
   f_X(x)
&= \frac{a^a}{(2\pi)^{n/2} \, |\Sigma|^{1/2} \, \Gamma(a)} \int_0^\infty u^{a+n/2-1} \, e^{-(a+d/2)u} \, \mathrm{d}u \\
&= \frac{\Gamma((\nu+n)/2)}{\Gamma(\nu/2) \, (\nu\pi)^{n/2} \, |\Sigma|^{1/2}} \left( 1+\frac{d}{\nu} \right)^{-(\nu+n)/2} \; .
\end{split}
$$

This is the [multivariate $t$-density](/P/mvt-pdf). Conditional on the same $U=u$, the [linear transformation of the normal vector](/P/mvn-ltt) gives

$$ \label{eq:mvn-ltt}
AX + b \mid U = u \sim \mathcal{N}(A \mu + b, A \Sigma A^\mathrm{T}/u) \; .
$$

Full row rank ensures that $A \Sigma A^\mathrm{T}$ is positive-definite. Applying the same integral in dimension $m$ proves \eqref{eq:mvt-ltt}. Taking $A=L^{-1}$ and $b=-L^{-1}\mu$ gives the standard form mentioned in the theorem.