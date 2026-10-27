---
layout: proof
mathjax: true

author: "Kenneth Petrykowski"
affiliation: "University of Warsaw"
e_mail: "kenneth.petrykowski@gmail.com"
date: 2026-10-17 21:51:05

title: "Posterior predictive distribution of future data point based on observed Poisson data with exposures"
chapter: "Statistical Models"
section: "Count data"
topic: "Poisson distribution with exposure values"
theorem: "Posterior predictive distribution"

sources:
  - authors: "Gary Koop, Dale J. Poirier, Justin L. Tobias"
    year: 2007
    title: "Prediction"
    in: "Bayesian Econometric Methods"
    pages: "Exercise 7.2, pp. 73-74"

proof_id: "P558"
shortcut: "poissexp-postpred"
username: "kjpetrykowski"
---


**Theorem:** Let $y$ be a [Poisson data set with exposure values](/D/poissexp). Suppose the event rate $\lambda$ has [posterior distribution](/D/post) $\lambda \mid y \sim \mathrm{Gam}(a,b)$, i.e. a [gamma distribution](/D/gam) with [density function](/D/pdf)

$$ \label{eq:poiss-postpred-gamma}
p(\lambda \mid y) = \frac{b^a}{\Gamma(a)}\lambda^{a-1}\exp(-b\lambda),
\qquad \lambda>0, \quad a,b>0 \; .
$$

Let $t>0$ be a known future exposure and assume that a future observation satisfies $Y \mid \lambda,y \sim \mathrm{Poiss}(t\lambda)$. Then, for each integer $k \geq 0$, we have the [probability mass function](/D/pmf) (PMF)

$$ \label{eq:poiss-postpred-pmf}
  \mathrm{Pr}(Y=k \mid y)
= \frac{\Gamma(a+k)}{\Gamma(a)k!}
  \left(\frac{b}{b+t}\right)^a
  \left(\frac{t}{b+t}\right)^k
$$

and the predictive [moments](/D/mom) of the future [observation](/D/data) are

$$ \label{eq:poiss-postpred-moments}
\mathrm{E}(Y \mid y) = \frac{at}{b}, \qquad
\mathrm{Var}(Y \mid y) = \frac{at}{b}+\frac{at^2}{b^2} \; .
$$

The [Poisson rate parameter](/D/poissexp) $\lambda$ is measured in events per exposure unit. The [gamma rate](/D/gam) $b$ has the same exposure units as $t$, so $b+t$ and $t/b$ are well-defined. The [gamma shape](/D/gam) $a$ is dimensionless.

The distribution of $Y$ given $y$ is thus a [negative binomial](/D/negbin), with PMF on $k=0,1,2,\ldots$ in \eqref{eq:poiss-postpred-pmf} parametrized by [shape](/D/para-shape) $a$ and [probability parameter](/D/bin) $b/(b+t)$. The shape may be any positive real number.


**Proof:** Conditional on $\lambda$, the future [PMF is](/P/poiss-pdf) $\exp(-t\lambda)(t\lambda)^k/k!$. By the definition of a [posterior predictive distribution](/D/post-pred), we take the [expectation](/D/mean) over the gamma posterior:

$$ \label{eq:poiss-postpred-integral}
\begin{split}
   \mathrm{Pr}(Y=k \mid y)
&= \int_0^\infty \frac{\exp(-t\lambda)(t\lambda)^k}{k!} \cdot \frac{b^a}{\Gamma(a)}\lambda^{a-1}\exp(-b\lambda) \, \mathrm{d}\lambda \\
&= \frac{b^a t^k}{\Gamma(a)k!} \int_0^\infty \lambda^{a+k-1}\exp[-(b+t)\lambda] \, \mathrm{d}\lambda \; .
\end{split}
$$

For $s,c>0$, substituting $u=c\lambda$ in the [defining gamma integral](/D/gam) gives:

$$ \label{eq:poiss-postpred-gamma-integral}
  \int_0^\infty \lambda^{s-1} \exp(-c\lambda) \, \mathrm{d}\lambda
= \frac{\Gamma(s)}{c^s} \; .
$$

Set $s=a+k$ and $c=b+t$. Then, equation \eqref{eq:poiss-postpred-integral} becomes

$$ \label{eq:poiss-postpred-integral-dev}
  \mathrm{Pr}(Y=k \mid y)
= \frac{b^a t^k \Gamma(a+k)}{\Gamma(a) k! (b+t)^{a+k}}
$$


which is equivalent to \eqref{eq:poiss-postpred-pmf}. It is a [normalized PMF](/D/pmf), because it mixes normalized [Poisson mass functions](/P/poiss-pmf) with a normalized [gamma density function](/P/gam-pdf). Exchanging the non-negative sum and integral preserves total probability one.

To obtain the posterior moments, multiply the gamma density \eqref{eq:poiss-postpred-gamma} by $\lambda^r$ and apply \eqref{eq:poiss-postpred-gamma-integral} with $s=a+r$ and $c=b$:

$$ \label{eq:poiss-postpred-rate-moments}
\begin{split}
   \mathrm{E}(\lambda^r \mid y)
&= \frac{b^a}{\Gamma(a)} \int_0^\infty \lambda^{a+r-1} \exp(-b\lambda) \, \mathrm{d}\lambda \\
&= \frac{\Gamma(a+r)}{\Gamma(a) b^r}, \qquad r=1,2 \; .
\end{split}
$$

Using the recurrence relation $\Gamma(z+1)=z\Gamma(z)$ gives $\mathrm{E}(\lambda \mid y)=a/b$ and $\mathrm{E}(\lambda^2 \mid y)=a(a+1)/b^2$. The [variance is the second moment minus the squared mean](/P/var-mean), so $\mathrm{Var}(\lambda \mid y)=a/b^2$. The [Poisson mean](/P/poiss-mean) and [variance](/P/poiss-var), together with the [laws of total expectation](/P/mean-tot) and [total variance](/P/var-tot), now give:

$$ \label{eq:poiss-postpred-total-variance}
\begin{split}
   \mathrm{E}(Y \mid y)
&= \mathrm{E}[t\lambda \mid y] = \frac{at}{b} \; , \\
   \mathrm{Var}(Y \mid y)
&= \mathrm{E}[\mathrm{Var}(Y \mid \lambda,y) \mid y] + \mathrm{Var}[\mathrm{E}(Y \mid \lambda,y) \mid y] \\
&= \mathrm{E}(t\lambda \mid y) + \mathrm{Var}(t\lambda \mid y)
 = \frac{at}{b}+\frac{at^2}{b^2} \; .
\end{split}
$$

This proves the PMF and both moments. The predictive count $Y$ has more variance than a [Poisson count](/D/poiss) with the same mean. The term $at^2/b^2$ is the additional variance which comes from the [posterior uncertainty](/D/post) about the event rate.