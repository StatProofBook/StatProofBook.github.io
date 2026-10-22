---
layout: proof
mathjax: true

author: "Kenneth Petrykowski"
affiliation: "University of Warsaw"
e_mail: "kenneth.petrykowski@gmail.com"
date: 2026-10-19 20:30:00

title: "Moments and pointwise consistency of the empirical distribution function"
chapter: "General Theorems"
section: "Probability theory"
topic: "Cumulative distribution function"
theorem: "Empirical distribution moments and pointwise consistency"

sources:
  - authors: "John A. Rice"
    year: 2007
    title: "The empirical cumulative distribution function"
    in: "Mathematical Statistics and Data Analysis"
    pages: "Third edition, Section 10.2.1, pp. 378-380"

proof_id: "P562"
shortcut: "ecdf-momcons"
username: "kjpetrykowski"
---

**Theorem:** Let $X\_1,X\_2,\ldots$ be an infinite sequence of independent and identically distributed real observations. For each integer $n\geq1$, use its first $n$ observations. Their common [cumulative distribution function](/D/cdf) is $F(x)=\mathrm{Pr}(X\_i\leq x)$, $x\in\mathbb{R}$. Define the empirical distribution function by

$$ \label{eq:ecdf-momcons-definition}
F_n(x)=\frac{1}{n}\sum_{i=1}^n I_i(x),\qquad
I_i(x)=\mathbf{1}\{X_i\leq x\} \; .
$$

The indicator $I\_i(x)$ is 1 when $X\_i\leq x$ and 0 otherwise. For every fixed real $x$,

$$ \label{eq:ecdf-momcons-moments}
\mathrm{E}[F_n(x)]=F(x),\qquad
\mathrm{Var}[F_n(x)]=\frac{F(x)[1-F(x)]}{n} \; .
$$

For each $\varepsilon>0$,

$$ \label{eq:ecdf-momcons-bound}
\mathrm{Pr}\{\lvert F_n(x)-F(x)\rvert\geq\varepsilon\}
\leq\frac{F(x)[1-F(x)]}{n\varepsilon^2}
\leq\frac{1}{4n\varepsilon^2}
\longrightarrow0 \; .
$$

Thus $F\_n(x)$ converges in probability to $F(x)$ at each fixed $x$. The value of $x$ is fixed before taking the probability or the limit. We do not assume that $F$ is continuous. Both $F\_n(x)$ and $F(x)$ are dimensionless probabilities, even when the observations and threshold have physical units.

**Proof:** For a fixed threshold, $I\_i(x)$ is a Bernoulli variable with success probability $F(x)$. The indicators are independent because each depends on a different independent observation. Since $I\_i(x)^2=I\_i(x)$,

$$ \label{eq:ecdf-momcons-indicator}
\mathrm{E}[I_i(x)]=F(x),\qquad
\mathrm{Var}[I_i(x)]=F(x)-F(x)^2 \; .
$$

Linearity of expectation gives:

$$ \label{eq:ecdf-momcons-mean}
\mathrm{E}[F_n(x)]=\frac{1}{n}\sum_{i=1}^n\mathrm{E}[I_i(x)]
=\frac{nF(x)}{n}=F(x) \; .
$$

Because the indicators are independent, the cross-covariance terms in the variance of the sum are zero:

$$ \label{eq:ecdf-momcons-variance}
\begin{split}
\mathrm{Var}[F_n(x)]
&=\frac{1}{n^2}\sum_{i=1}^n\mathrm{Var}[I_i(x)]\\
&=\frac{nF(x)[1-F(x)]}{n^2}
=\frac{F(x)[1-F(x)]}{n} \; .
\end{split}
$$

[Chebyshev's inequality](/P/cheb-ineq) applied to the unbiased variable $F\_n(x)$ gives the first bound in \eqref{eq:ecdf-momcons-bound}. The identity $q(1-q)=1/4-(q-1/2)^2\leq1/4$ for $q\in[0,1]$ gives the second. For fixed $\varepsilon>0$, the resulting upper bound tends to zero as $n$ grows. This is exactly convergence in probability.

If $F(x)=0$ or $F(x)=1$, the indicators are constant almost surely and the sampling variance is exactly zero. No division by $F(x)[1-F(x)]$ was used, so these cases are included.

Pointwise convergence proves the claim separately for each fixed threshold. However, a bound on the largest error over all thresholds requires an additional theorem.
