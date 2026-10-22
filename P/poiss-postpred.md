---
layout: proof
mathjax: true

author: "Kenneth Petrykowski"
affiliation: "University of Warsaw"
e_mail: "kenneth.petrykowski@gmail.com"
date: 2026-10-17 21:51:05

title: "Negative binomial posterior prediction from a gamma Poisson model"
chapter: "Statistical Models"
section: "Count data"
topic: "Poisson distribution with exposure values"
theorem: "Posterior predictive distribution"

sources:
  - authors: "Gary Koop, Dale J. Poirier, Justin L. Tobias"
    year: 2007
    title: "Prediction"
    in: "Bayesian Econometric Methods"
    pages: "Exercise 7.2, pp. 73-74 (gamma shape-scale parameterization)"

proof_id: "P558"
shortcut: "poiss-postpred"
username: "kjpetrykowski"
---

**Theorem:** Fix observed data $y$. Suppose the event rate has posterior $\lambda\mid y\sim\mathrm{Gam}(a,b)$ in **shape-rate** form, meaning

$$ \label{eq:poiss-postpred-gamma}
p(\lambda\mid y)=\frac{b^a}{\Gamma(a)}\lambda^{a-1}\exp(-b\lambda),
\qquad \lambda>0,\quad a,b>0 \; .
$$

Let $t>0$ be a known future exposure. Assume $Y_{\ast}\mid\lambda,y\sim\mathrm{Poiss}(t\lambda)$, with the future observation conditionally independent of the observed data given $\lambda$. For each integer $k\geq0$,

$$ \label{eq:poiss-postpred-pmf}
\mathrm{Pr}(Y_{\ast}=k\mid y)
=\frac{\Gamma(a+k)}{\Gamma(a)k!}
 \left(\frac{b}{b+t}\right)^a
 \left(\frac{t}{b+t}\right)^k \; .
$$

Its predictive moments are

$$ \label{eq:poiss-postpred-moments}
\mathrm{E}(Y_{\ast}\mid y)=\frac{at}{b},\qquad
\mathrm{Var}(Y_{\ast}\mid y)=\frac{at}{b}+\frac{at^2}{b^2} \; .
$$

The rate $\lambda$ is measured in events per exposure unit. The gamma rate parameter $b$ has the same exposure units as $t$, so $b+t$ and $t/b$ are well defined. The shape $a$ is dimensionless.

Here “negative binomial” means the PMF on $k=0,1,2,\ldots$ in \eqref{eq:poiss-postpred-pmf}, with shape $a$ and probability parameter $b/(b+t)$. The shape may be any positive real number. The PMF, rather than its name alone, fixes which convention is intended. The gamma scale used in the source is $1/b$ in this shape-rate convention.

**Proof:** Conditional on $\lambda$, the future PMF is $\exp(-t\lambda)(t\lambda)^k/k!$. By the definition of a [posterior predictive distribution](/D/post-pred), average it over the gamma posterior:

$$ \label{eq:poiss-postpred-integral}
\begin{split}
\mathrm{Pr}(Y_{\ast}=k\mid y)
&=\int_0^\infty
 \frac{\exp(-t\lambda)(t\lambda)^k}{k!}\\
&\qquad{}\times\frac{b^a}{\Gamma(a)}\lambda^{a-1}\exp(-b\lambda)
 \,\mathrm{d}\lambda\\
&=\frac{b^at^k}{\Gamma(a)k!}
 \int_0^\infty \lambda^{a+k-1}\exp[-(b+t)\lambda]
 \,\mathrm{d}\lambda \; .
\end{split}
$$

For $s,c>0$, substituting $u=c\lambda$ in the defining gamma integral gives:

$$ \label{eq:poiss-postpred-gamma-integral}
\int_0^\infty\lambda^{s-1}\exp(-c\lambda)\,\mathrm{d}\lambda
=\frac{\Gamma(s)}{c^s} \; .
$$

Set $s=a+k$ and $c=b+t$. Equation \eqref{eq:poiss-postpred-integral} becomes $b^at^k\Gamma(a+k)/[\Gamma(a)k!(b+t)^{a+k}]$, which is \eqref{eq:poiss-postpred-pmf}. It is a normalized PMF because it mixes normalized Poisson PMFs against a normalized gamma density. Exchanging the nonnegative sum and integral preserves total probability one.

To obtain the posterior moments, multiply the gamma density by $\lambda^r$ and apply \eqref{eq:poiss-postpred-gamma-integral} with $s=a+r$ and $c=b$:

$$ \label{eq:poiss-postpred-rate-moments}
\begin{split}
\mathrm{E}(\lambda^r\mid y)
&=\frac{b^a}{\Gamma(a)}
 \int_0^\infty \lambda^{a+r-1}\exp(-b\lambda)\,\mathrm{d}\lambda\\
&=\frac{\Gamma(a+r)}{\Gamma(a)b^r},\qquad r=1,2 \; .
\end{split}
$$

Using the recurrence $\Gamma(z+1)=z\Gamma(z)$ gives $\mathrm{E}(\lambda\mid y)=a/b$ and $\mathrm{E}(\lambda^2\mid y)=a(a+1)/b^2$. The variance is the second moment minus the squared mean, so $\mathrm{Var}(\lambda\mid y)=a/b^2$. The [Poisson mean](/P/poiss-mean) and [variance](/P/poiss-var), together with [total expectation](/P/mean-tot) and [total variance](/P/var-tot), now give:

$$ \label{eq:poiss-postpred-total-variance}
\begin{split}
\mathrm{E}(Y_{\ast}\mid y)
&=\mathrm{E}[t\lambda\mid y]=\frac{at}{b},\\
\mathrm{Var}(Y_{\ast}\mid y)
&=\mathrm{E}[\mathrm{Var}(Y_{\ast}\mid\lambda,y)\mid y]
 +\mathrm{Var}[\mathrm{E}(Y_{\ast}\mid\lambda,y)\mid y]\\
&=\mathrm{E}(t\lambda\mid y)+\mathrm{Var}(t\lambda\mid y)
=\frac{at}{b}+\frac{at^2}{b^2} \; .
\end{split}
$$

This proves the PMF and both moments.

The predictive count has more variance than a Poisson count with the same mean. The term $at^2/b^2$ is the additional variance from posterior uncertainty about the event rate.
