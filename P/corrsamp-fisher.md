---
layout: proof
mathjax: true

author: "AtticKnight (AI-assisted)"
affiliation: ""
e_mail: ""
date: 2026-11-25 11:48:00

title: "Fisher transformation of the sample correlation coefficient"
chapter: "General Theorems"
section: "Probability theory"
topic: "Correlation"
theorem: "Fisher transformation"

sources:
  - authors: "Fisher, R. A."
    year: 1921
    title: "On the probable error of a coefficient of correlation deduced from a small sample"
    in: "Metron"
    pages: "1, 3–32, transformation (V)"
    url: "https://digital.library.adelaide.edu.au/items/002ad8fb-c23c-407b-8a89-f036d8da6030"

proof_id: "P580"
shortcut: "corrsamp-fisher"
username: "AtticKnight"
---


**Theorem:** Let $r_n$ be the [sample correlation coefficient](/D/corr-samp) from $n\geq3$ independent observations of a nonsingular [bivariate normal distribution](/D/bvn) with population correlation $\rho\in(-1,1)$. For $h(r)=\tfrac12\log((1+r)/(1-r))$,

$$ \label{eq:corrsamp-fisher}
\sqrt n\bigl(h(r_n)-h(\rho)\bigr)\ \xrightarrow{\mathrm d}\ \mathcal N(0,1).
$$

The limiting normal law has variance one for every $\rho\in(-1,1)$. For $n>3$, using $\sqrt{n-3}$ in place of $\sqrt n$ gives the same limit because their ratio tends to one.


**Proof:** Subtract the two population means and divide by the corresponding positive standard deviations. This [preserves the sample correlation](/P/corrsamp-inv). Write $X_i,Y_i$ for the standardized coordinates, so their variances are one and $\mathrm E[X_iY_i]=\rho$. Their centered sample second moments with divisor $n$ are

$$ \label{eq:corrsamp-fisher-mom}
a_n=\overline{X^2}-\bar X^2,\qquad
b_n=\overline{Y^2}-\bar Y^2,\qquad
c_n=\overline{XY}-\bar X\bar Y.
$$

Here each bar averages over the $n$ pairs. Finite fourth moments and [Chebyshev's inequality](/P/cheb-ineq) make the deviations of the three uncentered second moments from $(1,1,\rho)$ of order $O_p(n^{-1/2})$. The sample means are themselves $O_p(n^{-1/2})$, so the centering corrections in \eqref{eq:corrsamp-fisher-mom} are $O_p(n^{-1})$.

Now $r_n=c_n/\sqrt{a_nb_n}$. At $(a,b,c)=(1,1,\rho)$ the gradient of $c/\sqrt{ab}$ is $(-\rho/2,-\rho/2,1)$. Its second derivatives are bounded in a neighborhood of this point, which contains the sample moments with probability tending to one. Hence Taylor expansion yields

$$ \label{eq:corrsamp-fisher-lin}
r_n-\rho=\frac1n\sum_{i=1}^n
\left(X_iY_i-\frac{\rho}{2}(X_i^2+Y_i^2)\right)+O_p(n^{-1}).
$$

To compute the limiting variance, set $A_i=(X_i+Y_i)/\sqrt{2(1+\rho)}$ and $B_i=(X_i-Y_i)/\sqrt{2(1-\rho)}$. These variables are jointly normal with unit variances and zero covariance, hence independent [standard normals](/D/snorm). Expanding their squares gives

$$ \label{eq:corrsamp-fisher-rot}
X_iY_i-\frac{\rho}{2}(X_i^2+Y_i^2)
=(1-\rho^2)\,\frac{A_i^2-B_i^2}{2}.
$$

Each squared standard normal has mean one and variance two. The differences $(A_i^2-B_i^2)/2$ therefore form an independent and identically distributed sequence with mean zero and variance one. Applying the [classical central limit theorem](/P/clt-iid) in \eqref{eq:corrsamp-fisher-lin} gives $\sqrt n(r_n-\rho)/(1-\rho^2)\xrightarrow{\mathrm d}\mathcal N(0,1)$. The sample correlation lies in $(-1,1)$ almost surely because a nonsingular normal sample of size at least three is almost surely noncollinear. Finally $h'(\rho)=1/(1-\rho^2)$. Taylor expansion of $h$ at this interior point, using $r_n-\rho=O_p(n^{-1/2})$, gives \eqref{eq:corrsamp-fisher}.
