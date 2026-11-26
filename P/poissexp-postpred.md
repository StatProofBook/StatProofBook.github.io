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

**Theorem:** For fixed observed [Poisson data with known exposures](/D/poissexp) $y$, suppose the event rate $\lambda$ has [posterior distribution](/D/post)

$$ \label{eq:posterior}
\lambda\mid y\sim\mathrm{Gam}(a,b),\qquad a,b>0 \; .
$$

Here $a$ is the shape and $b$ is the rate, so the corresponding scale is $1/b$. Writing $\Gamma$ for the [gamma function](/D/gam), the [gamma density](/D/gam) is

$$ \label{eq:poiss-postpred-gamma}
p(\lambda\mid y)=\frac{b^a}{\Gamma(a)}\lambda^{a-1}e^{-b\lambda},
\qquad\lambda>0 \; .
$$

Let $t>0$ be a known future exposure. The event rate $\lambda$ is measured per unit exposure, so $t\lambda$ is a mean count and $b$ has the same units as $t$. We treat all known exposures as fixed and omit them from the conditioning notation. Given $\lambda$, assume a future count $Y$ is independent of the observed data and has distribution $\mathrm{Poiss}(t\lambda)$. For $k=0,1,2,\ldots$, its [posterior predictive mass function](/D/post-pred) is

$$ \label{eq:poiss-postpred-pmf}
\mathrm{Pr}(Y=k\mid y)
=\frac{\Gamma(a+k)}{\Gamma(a)k!}
  \left(\frac{b}{b+t}\right)^a
  \left(\frac{t}{b+t}\right)^k \; .
$$

This is the negative binomial mass function with shape $a$ (any positive real number). Here $p=b/(b+t)$ is the probability parameter, so the two powers in \eqref{eq:poiss-postpred-pmf} are $p^a$ and $(1-p)^k$. The predictive mean and variance are

$$ \label{eq:poiss-postpred-moments}
\mathrm{E}(Y\mid y)=\frac{at}{b},\qquad
\mathrm{Var}(Y\mid y)=\frac{at}{b}+\frac{at^2}{b^2} \; .
$$


**Proof:** Multiply the [conditional Poisson mass function](/P/poiss-pmf) by the posterior gamma density and integrate over the unknown rate:

$$ \label{eq:poiss-postpred-integral}
\begin{split}
\mathrm{Pr}(Y=k\mid y)
&=\int_0^\infty
  \frac{e^{-t\lambda}(t\lambda)^k}{k!}
  \frac{b^a}{\Gamma(a)}\lambda^{a-1}e^{-b\lambda}
  \,\mathrm{d}\lambda\\
&=\frac{b^at^k}{\Gamma(a)k!}
  \int_0^\infty\lambda^{a+k-1}e^{-(b+t)\lambda}
  \,\mathrm{d}\lambda \; .
\end{split}
$$

For positive $s,c$, substitute $u=c\lambda$. Then $\lambda=u/c$ and $\mathrm{d}\lambda=\mathrm{d}u/c$, so the [gamma integral](/D/gam) gives

$$ \label{eq:poiss-postpred-gamma-integral}
\begin{split}
\int_0^\infty\lambda^{s-1}e^{-c\lambda}\,\mathrm{d}\lambda
&=\frac{1}{c^s}\int_0^\infty u^{s-1}e^{-u}\,\mathrm{d}u\\
&=\frac{\Gamma(s)}{c^s} \; .
\end{split}
$$

Apply this with $s=a+k$ and $c=b+t$:

$$ \label{eq:poiss-postpred-integral-dev}
\begin{split}
\mathrm{Pr}(Y=k\mid y)
&=\frac{b^at^k\Gamma(a+k)}{\Gamma(a)k!(b+t)^{a+k}}\\
&=\frac{\Gamma(a+k)}{\Gamma(a)k!}
  \left(\frac{b}{b+t}\right)^a
  \left(\frac{t}{b+t}\right)^k \; .
\end{split}
$$

To see why the probabilities sum to one, sum over $k$ in \eqref{eq:poiss-postpred-integral}. All terms are nonnegative, so we can interchange the sum and integral:

$$ \label{eq:normalization}
\begin{split}
\sum_{k=0}^\infty\mathrm{Pr}(Y=k\mid y)
&=\int_0^\infty
  \left[\sum_{k=0}^\infty\mathrm{Pr}(Y=k\mid\lambda)\right]
  p(\lambda\mid y)\,\mathrm{d}\lambda\\
&=\int_0^\infty p(\lambda\mid y)\,\mathrm{d}\lambda=1 \; .
\end{split}
$$

For the predictive moments, first calculate the posterior moments of $\lambda$. Multiplication by $\lambda^r$ and \eqref{eq:poiss-postpred-gamma-integral} give

$$ \label{eq:poiss-postpred-rate-moments}
\begin{split}
\mathrm{E}(\lambda^r\mid y)
&=\frac{b^a}{\Gamma(a)}
  \int_0^\infty\lambda^{a+r-1}e^{-b\lambda}\,\mathrm{d}\lambda\\
&=\frac{\Gamma(a+r)}{\Gamma(a)b^r},\qquad r=1,2 \; .
\end{split}
$$

Using $\Gamma(a+1)=a\Gamma(a)$ and $\Gamma(a+2)=(a+1)a\Gamma(a)$,

$$ \label{eq:gamma-moments-expanded}
\begin{split}
\mathrm{E}(\lambda\mid y)
&=\frac{a\Gamma(a)}{\Gamma(a)b}=\frac{a}{b},\\
\mathrm{E}(\lambda^2\mid y)
&=\frac{a(a+1)\Gamma(a)}{\Gamma(a)b^2}=\frac{a(a+1)}{b^2},\\
\mathrm{Var}(\lambda\mid y)
&=\frac{a(a+1)}{b^2}-\left(\frac{a}{b}\right)^2
=\frac{a}{b^2} \; .
\end{split}
$$

The [conditional Poisson mean](/P/poiss-mean) and [variance](/P/poiss-var) both equal $t\lambda$. By the [second-moment identity](/P/var-mean), the conditional second moment is $t\lambda+t^2\lambda^2$. Averaging this nonnegative quantity over the posterior gives

$$ \label{eq:poiss-postpred-second-moment}
\begin{split}
\mathrm{E}(Y^2\mid y)
&=\mathrm{E}[t\lambda+t^2\lambda^2\mid y]\\
&=\frac{at}{b}+\frac{a(a+1)t^2}{b^2}<\infty \; .
\end{split}
$$

The predictive variance is therefore finite. Apply the [law of total expectation](/P/mean-tot) and the [law of total variance](/P/var-tot):

$$ \label{eq:poiss-postpred-total-variance}
\begin{split}
\mathrm{E}(Y\mid y)
&=\mathrm{E}[\mathrm{E}(Y\mid\lambda,y)\mid y]
=t\,\mathrm{E}(\lambda\mid y)=\frac{at}{b},\\
\mathrm{Var}(Y\mid y)
&=\mathrm{E}[\mathrm{Var}(Y\mid\lambda,y)\mid y]\\
&\quad+\mathrm{Var}[\mathrm{E}(Y\mid\lambda,y)\mid y]\\
&=t\,\mathrm{E}(\lambda\mid y)+t^2\mathrm{Var}(\lambda\mid y)\\
&=\frac{at}{b}+\frac{at^2}{b^2} \; .
\end{split}
$$

The extra variance term $at^2/b^2$ comes from uncertainty about the event rate $\lambda$.
