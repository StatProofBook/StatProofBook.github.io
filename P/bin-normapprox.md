---
layout: proof
mathjax: true

author: "AtticKnight (AI-assisted)"
affiliation: ""
e_mail: ""
date: 2026-11-23 08:05:00

title: "Normal approximation to the binomial distribution"
chapter: "Probability Distributions"
section: "Univariate discrete distributions"
topic: "Binomial distribution"
theorem: "Normal approximation"

sources:
  - authors: "Márton Balázs and Bálint Tóth"
    year: 2022
    title: "Stirling's Formula and DeMoivre-Laplace Central Limit Theorem"
    in: "University of Bristol and Budapest University of Technology and Economics"
    pages: "Theorems 1 and 2"
    url: "https://people.maths.bris.ac.uk/~mb13434/Stirling_DeMoivre_Laplace.pdf"

proof_id: "P578"
shortcut: "bin-normapprox"
username: "AtticKnight"
---


**Theorem:** Let $X_n$ have a [binomial distribution](/D/bin) with $n$ trials and fixed success probability $0<p<1$. Set $q=1-p$, $\sigma_n=\sqrt{npq}$ and $z_k=(k-np)/\sigma_n$. Write $\phi$ and $\Phi$ for the density and cumulative distribution function of the [standard normal distribution](/D/snorm). Then for every real $x$,

$$ \label{eq:bin-normal-cdf}
\lim_{n\to\infty}\Pr\!\left(\frac{X_n-np}{\sigma_n}\leq x\right)=\Phi(x).
$$

There is also a local approximation to the probability of an individual count. For every fixed $M>0$,

$$ \label{eq:bin-normal-local}
\max_{\substack{0\leq k\leq n,\;k\text{ integer}\\ |z_k|\leq M}}
\left|\frac{\sigma_n\Pr(X_n=k)}{\phi(z_k)}-1\right| \longrightarrow 0.
$$


**Proof:** Fix $M$ and consider counts with $|z_k|\leq M$. With $t=k/n$ we have $|t-p|\leq M\sqrt{pq/n}$. Thus $k$ and $n-k$ both grow at least as fast as a positive constant times $n$. Apply Stirling's formula $m!=\sqrt{2\pi m}(m/e)^m(1+O(m^{-1}))$ to the three factorials in the [binomial mass function](/P/bin-pmf). Collecting the powers of $p,q,t$ and $1-t$ gives

$$ \label{eq:bin-normal-stirling}
\begin{aligned}
\Pr(X_n=k)&=\frac{\exp\{-nD(t)\}}{\sqrt{2\pi n t(1-t)}}(1+O(n^{-1})),\\
D(t)&=t\log(t/p)+(1-t)\log((1-t)/q).
\end{aligned}
$$

The bound on the remainder holds uniformly over these counts. Direct differentiation gives $D(p)=D'(p)=0$ and $D''(t)=1/[t(1-t)]$. The third derivative is bounded in a neighborhood of $p$, so Taylor's formula yields

$$ \label{eq:bin-normal-exponent}
nD(t)=\frac{n(t-p)^2}{2pq}+O(n|t-p|^3)
=\frac{z_k^2}{2}+O(n^{-1/2}).
$$

Also $t(1-t)=pq+O(n^{-1/2})$. Substituting into \eqref{eq:bin-normal-stirling} gives $\sigma_n\Pr(X_n=k)=\phi(z_k)(1+O(n^{-1/2}))$, uniformly for $|z_k|\leq M$. This proves \eqref{eq:bin-normal-local}.

Let $Z_n=(X_n-np)/\sigma_n$. For fixed finite $b<c$, the lattice values $z_k$ in $[b,c]$ are spaced $1/\sigma_n$ apart. Summing the local approximation over these values therefore gives a Riemann sum,

$$ \label{eq:bin-normal-riemann}
\lim_{n\to\infty}\Pr(b\leq Z_n\leq c)
=\int_b^c \phi(z)\,\mathrm{d}z=\Phi(c)-\Phi(b).
$$

Finally, the [binomial mean](/P/bin-mean) and [variance](/P/bin-var) give $\mathrm{E}(Z_n^2)=1$. Hence $\Pr(Z_n<-M)\leq 1/M^2$. For $M>|x|$, apply \eqref{eq:bin-normal-riemann} on $[-M,x]$ and bound the omitted lower tail by $1/M^2$. As $M\to\infty$, both this bound and $\Phi(-M)$ tend to zero, proving the claimed limit.
