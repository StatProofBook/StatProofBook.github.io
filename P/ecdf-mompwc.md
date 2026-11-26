---
layout: proof
mathjax: true

author: "Kenneth Petrykowski"
affiliation: "University of Warsaw"
e_mail: "kenneth.petrykowski@gmail.com"
date: 2026-10-19 20:30:00

title: "Moments and point-wise consistency of the empirical cumulative distribution function"
chapter: "General Theorems"
section: "Probability theory"
topic: "Cumulative distribution function"
theorem: "Moments and point-wise consistency of the empirical CDF"

sources:
  - authors: "John A. Rice"
    year: 2007
    title: "The empirical cumulative distribution function"
    in: "Mathematical Statistics and Data Analysis"
    pages: "Third edition, Section 10.2.1, pp. 378-380"

proof_id: "P562"
shortcut: "ecdf-mompwc"
username: "kjpetrykowski"
---

**Theorem:** Let $X\_1,X\_2,\ldots$ be [independent and identically distributed](/D/iid) real random variables with common [cumulative distribution function](/D/cdf) $F(x)=\mathrm{Pr}(X\_i\leq x)$. For each $n\geq1$, the [empirical cumulative distribution function](/D/ecdf) at a threshold $x$ is the fraction of the first $n$ observations at most $x$. In the sum below the [indicator](/D/ind-fct) counts 1 when $X\_i\leq x$ and 0 otherwise:

$$ \label{eq:ecdf-momcons-definition}
F_n(x)=\frac{1}{n}\sum_{i=1}^n\mathbf{1}_{\lbrace X_i\leq x\rbrace},
\qquad x\in\mathbb{R} \; .
$$

For every fixed $x\in\mathbb{R}$,

$$ \label{eq:ecdf-momcons-moments}
\mathrm{E}[F_n(x)]=F(x),\qquad
\mathrm{Var}[F_n(x)]=\frac{F(x)[1-F(x)]}{n} \; .
$$

Moreover, for every $\varepsilon>0$,

$$ \label{eq:ecdf-momcons-bound}
\begin{split}
\mathrm{Pr}(|F_n(x)-F(x)|\geq\varepsilon)
&\leq\frac{F(x)[1-F(x)]}{n\varepsilon^2}\\
&\leq\frac{1}{4n\varepsilon^2}\longrightarrow0
\quad(n\to\infty) \; .
\end{split}
$$

Consequently, $F\_n(x)$ [converges in probability](/D/conv-prob) to $F(x)$ at each fixed $x$. No continuity assumption on $F$ is needed.


**Proof:** Fix a threshold $x$ and write

$$ \label{eq:indicators}
I_i=\mathbf{1}_{\lbrace X_i\leq x\rbrace} \; .
$$

Each $I\_i$ is a Bernoulli random variable with success probability $F(x)$. Since $I\_i^2=I\_i$,

$$ \label{eq:ecdf-momcons-indicator}
\begin{split}
\mathrm{E}(I_i)&=1\cdot F(x)+0\cdot[1-F(x)]=F(x),\\
\mathrm{Var}(I_i)&=\mathrm{E}(I_i^2)-[\mathrm{E}(I_i)]^2\\
&=F(x)-F(x)^2=F(x)[1-F(x)] \; .
\end{split}
$$

By [linearity of expectation](/P/mean-lin),

$$ \label{eq:ecdf-momcons-mean}
\begin{split}
\mathrm{E}[F_n(x)]
&=\frac{1}{n}\sum_{i=1}^n\mathrm{E}(I_i)\\
&=\frac{nF(x)}{n}=F(x) \; .
\end{split}
$$

The indicators are independent because each depends on a different independent observation. Their covariances are therefore zero. Applying the [two-variable variance-of-a-sum identity](/P/var-sum) repeatedly gives

$$ \label{eq:ecdf-momcons-variance}
\begin{split}
\mathrm{Var}[F_n(x)]
&=\frac{1}{n^2}\sum_{i=1}^n\mathrm{Var}(I_i)\\
&=\frac{nF(x)[1-F(x)]}{n^2}
=\frac{F(x)[1-F(x)]}{n} \; .
\end{split}
$$

If $F(x)=0$ or $F(x)=1$, each indicator equals $F(x)$ with probability one. Hence $F\_n(x)=F(x)$ with probability one, and the error probability in \eqref{eq:ecdf-momcons-bound} is zero for every $\varepsilon>0$. This proves the bound and convergence in these cases.

Otherwise, $0<F(x)<1$, so the standard deviation $\sigma\_n(x)=\sqrt{\mathrm{Var}[F\_n(x)]}$ is positive. For any $\varepsilon>0$, apply [Chebyshev's inequality](/P/cheb-ineq) with $k=\varepsilon/\sigma\_n(x)$, so that its threshold $k\sigma\_n(x)$ equals $\varepsilon$. Using the mean and variance just calculated gives

$$ \label{eq:chebyshev-substitution}
\begin{split}
\mathrm{Pr}(|F_n(x)-F(x)|\geq\varepsilon)
&=\mathrm{Pr}(|F_n(x)-\mathrm{E}[F_n(x)]|\geq\varepsilon)\\
&\leq\frac{\mathrm{Var}[F_n(x)]}{\varepsilon^2}\\
&=\frac{F(x)[1-F(x)]}{n\varepsilon^2} \; .
\end{split}
$$

For every $q\in[0,1]$,

$$ \label{eq:bernoulli-variance-bound}
q(1-q)=\frac14-\left(q-\frac12\right)^2\leq\frac14 \; .
$$

Substituting $q=F(x)$ gives the second bound in \eqref{eq:ecdf-momcons-bound}. For each fixed $x$ and every $\varepsilon>0$, this bound tends to zero as $n$ increases. Thus $F\_n(x)$ converges in probability to $F(x)$.
