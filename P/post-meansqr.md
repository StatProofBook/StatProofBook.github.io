---
layout: proof
mathjax: true

author: "Kenneth Petrykowski"
affiliation: "University of Warsaw"
e_mail: "kenneth.petrykowski@gmail.com"
date: 2026-10-18 22:15:00

title: "Posterior mean optimality under squared error loss"
chapter: "General Theorems"
section: "Bayesian statistics"
topic: "Probabilistic modeling"
theorem: "Posterior mean is optimal under squared error loss"

sources:
  - authors: "Gary Koop, Dale J. Poirier, Justin L. Tobias"
    year: 2007
    title: "Point estimation"
    in: "Bayesian Econometric Methods"
    pages: "Exercise 3.1, p. 31"

proof_id: "P561"
shortcut: "post-meansqr"
username: "kjpetrykowski"
---

**Theorem:** In a [joint Bayesian model](/D/fpm), draw a real parameter $\theta$ from a [prior](/D/prior) of total probability one, then draw data $X$ given $\theta$. Assume $\mathrm{E}(\theta^2)<\infty$. The mean of the [posterior distribution](/D/post) is

$$ \label{eq:posterior-mean}
m(X)=\mathrm{E}(\theta\mid X) \; .
$$

Let $\delta$ be a rule that assigns a real-valued estimate $\delta(x)$ to each possible observation $x$. Assume the rule is [measurable](/D/meas-fct), meaning that for every real cutoff $c$, the data values $x$ for which $\delta(x)\leq c$ form an event. Assume also that $\mathrm{E}[\delta(X)^2]<\infty$.

The rule's [posterior expected loss](/D/post-loss) is the average of its squared error [loss](/D/loss-fct) given $X$. For each such rule, the following identity holds [with probability one](/D/almost-sure), meaning that the exceptional data values together have probability zero under the [prior predictive distribution](/D/prior-pred) of $X$:

$$ \label{eq:identity}
\begin{split}
&\mathrm{E}[(\theta-\delta(X))^2\mid X] \\
&\qquad=\mathrm{Var}(\theta\mid X)+[m(X)-\delta(X)]^2 \; .
\end{split}
$$

Thus the posterior mean minimizes posterior expected loss with probability one. It also minimizes the [Bayes risk](/D/risk-fct), the squared error averaged over both $\theta$ and $X$:

$$ \label{eq:bayes-risk}
r(\delta)=\mathrm{E}[(\theta-\delta(X))^2]
$$

Equality $r(\delta)=r(m)$ holds exactly when $\delta(X)=m(X)$ with probability one.


**Proof:** First check that $m(X)$ has a finite second moment. By the [law of total expectation](/P/mean-tot), the nonnegative posterior second moment has average $\mathrm{E}(\theta^2)<\infty$, so it is finite with probability one. By the [variance identity](/P/var-mean),

$$ \label{eq:posterior-variance-bound}
0\leq\mathrm{Var}(\theta\mid X)
=\mathrm{E}(\theta^2\mid X)-m(X)^2 \; .
$$

Rearranging and averaging over the data gives

$$ \label{eq:finite-moment}
\begin{split}
m(X)^2&\leq\mathrm{E}(\theta^2\mid X),\\
\mathrm{E}[m(X)^2]&\leq\mathrm{E}[\mathrm{E}(\theta^2\mid X)]
=\mathrm{E}(\theta^2)<\infty \; .
\end{split}
$$

To obtain the conditional counterpart of the [squared-error property of the ordinary mean](/P/mean-mse), add and subtract $m(X)$ and expand the square:

$$ \label{eq:expand}
\begin{split}
\theta-\delta(X)&=[\theta-m(X)]+[m(X)-\delta(X)],\\
(\theta-\delta(X))^2
&=[\theta-m(X)]^2\\
&\quad+2[\theta-m(X)][m(X)-\delta(X)]\\
&\quad+[m(X)-\delta(X)]^2 \; .
\end{split}
$$

When we condition on $X$, both $m(X)$ and $\delta(X)$ are fixed. The first term has conditional expectation $\mathrm{Var}(\theta\mid X)$. For the middle term,

$$ \label{eq:centered}
\begin{split}
&\mathrm{E}[\theta-m(X)\mid X]
=\mathrm{E}(\theta\mid X)-m(X)=0,\\
&\mathrm{E}\bigl[2[\theta-m(X)][m(X)-\delta(X)]\mid X\bigr]\\
&\qquad=2[m(X)-\delta(X)]\cdot0=0 \; .
\end{split}
$$

The last term is fixed once $X$ is given. This proves \eqref{eq:identity}. Only $[m(X)-\delta(X)]^2$ depends on the chosen estimate. It is nonnegative and is zero exactly when $\delta(X)=m(X)$.

Taking expectations of \eqref{eq:identity} gives

$$ \label{eq:risk}
\begin{split}
r(\delta)
&=\mathrm{E}[\mathrm{Var}(\theta\mid X)]
 +\mathrm{E}([m(X)-\delta(X)]^2),\\
r(m)&=\mathrm{E}[\mathrm{Var}(\theta\mid X)],\\
r(\delta)-r(m)&=\mathrm{E}([m(X)-\delta(X)]^2)\geq0 \; .
\end{split}
$$

A nonnegative random variable has expectation zero only if it is zero with probability one. Thus equality of the risks is equivalent to $\delta(X)=m(X)$ with probability one.
