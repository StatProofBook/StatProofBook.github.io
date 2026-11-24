---
layout: proof
mathjax: true

author: "Ljx000888"
affiliation: ""
e_mail: ""
date: 2026-11-24 23:26:00

title: "Exact confidence interval for a binomial proportion"
chapter: "Statistical Models"
section: "Count data"
topic: "Binomial observations"
theorem: "Exact confidence interval"

sources:
  - authors: "Clopper, C. J. and Pearson, E. S."
    year: 1934
    title: "The use of confidence or fiducial limits illustrated in the case of the binomial"
    in: "Biometrika"
    pages: "26(4), 404–413"
    doi: "10.1093/biomet/26.4.404"

proof_id: "P574"
shortcut: "bin-ci"
username: "Ljx000888"
---

**Theorem:** Let $X$ count the successes in $n \geq 1$ independent trials with common success probability $p$, so $X$ has a [binomial distribution](/D/bin). Write $a=\alpha/2$ for $0<\alpha<1$, and let $Q_q(r,s)$ denote the $q$-quantile of the [beta distribution](/D/beta) with shape parameters $r,s$. For $X=x$, the equal-tailed Clopper–Pearson [confidence interval](/D/ci) is $[L(x),U(x)]$, where

$$ \label{eq:bin-ci-limits}
\begin{aligned}
L(x)&=\begin{cases}
0, & x=0,\\
Q_a(x,n-x+1), & 1\leq x\leq n,
\end{cases}
&
U(x)&=\begin{cases}
Q_{1-a}(x+1,n-x), & 0\leq x<n,\\
1, & x=n.
\end{cases}
\end{aligned}
$$

Its coverage satisfies $\Pr_p\{L(X)\leq p\leq U(X)\}\geq 1-\alpha$ for every $p\in[0,1]$.

**Proof:** For $1\leq k\leq n$, write $T_k(p)=\Pr_p(X\geq k)$. Differentiating the finite binomial sum gives

$$ \label{eq:bin-ci-tail}
\frac{\mathrm d}{\mathrm dp}\sum_{j=k}^{n}\binom nj p^j(1-p)^{n-j}
= n\binom{n-1}{k-1}p^{k-1}(1-p)^{n-k}.
$$

Indeed, the positive derivative term at index $j$ cancels the negative term at index $j-1$ for $j>k$. The right-hand side is the beta density with parameters $(k,n-k+1)$. Since $T_k(0)=0$, $T_k(p)$ equals the corresponding beta distribution function at $p$. It increases strictly from zero to one.

For $x>0$, invert the upper-tail equation $T_x(L(x))=a$. For $x<n$, invert the lower-tail equation $\Pr_{U(x)}(X\leq x)=1-T_{x+1}(U(x))=a$. These inversions give the two beta quantiles in \eqref{eq:bin-ci-limits}. At $x=0$ only the upper limit needs inversion, giving $U(0)=1-a^{1/n}$; at $x=n$ only the lower limit needs inversion, giving $L(n)=a^{1/n}$.

For $0<x<n$, $T_{x+1}(L(x))\leq T_x(L(x))=a<1-a=T_{x+1}(U(x))$, so the lower endpoint is below the upper endpoint.

To check coverage, fix $0<p<1$. If $L(x)>p$, then $\Pr_p(X\geq x)<a$, and conversely. Since the tail decreases with $x$, these counts, if any, form an upper tail starting at some $k$. Their total probability is exactly $\Pr_p(X\geq k)<a$. Likewise, the counts for which $U(x)<p$ form a lower tail of total probability at most $a$, since $\Pr_p(X\leq x)$ increases with $x$. The probability of missing $p$ is therefore at most $2a=\alpha$. At $p=0$ and $p=1$ the count equals $0$ and $n$, respectively, with probability one, and the interval includes the true endpoint in each case.
