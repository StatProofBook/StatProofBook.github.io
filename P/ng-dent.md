---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-07-08 10:51:00

title: "Differential entropy of the normal-gamma distribution"
chapter: "Probability Distributions"
section: "Multivariate continuous distributions"
topic: "Normal-gamma distribution"
theorem: "Differential entropy"

sources:

proof_id: "P238"
shortcut: "ng-dent"
username: "JoramSoch"
---


**Theorem:** Let $X$ be an $n$-dimensional [random vector](/D/rvec) and let $Y$ be a positive [random variable](/D/rvar). Assume that $X$ and $Y$ are [jointly normal-gamma distributed](/D/ng):

$$ \label{eq:NG}
X,Y \sim \mathrm{NG}(\mu, \Lambda^{-1}, a, b)
$$

Then, the [differential entropy](/D/dent) of $(X,Y)$ in nats is

$$ \label{eq:NG-dent}
\begin{split}
   \mathrm{h}(X,Y)
&= \frac{n}{2} \ln(2\pi) - \frac{1}{2} \ln|\Lambda| + \frac{1}{2} n \\
&+ a + \ln \Gamma(a) - \frac{n-2+2a}{2} \psi(a) + \frac{n-2}{2} \ln b \; .
\end{split}
$$


**Proof:** The [probabibility density function of the normal-gamma distribution](/P/ng-pdf) is

$$ \label{eq:NG-pdf}
  p(x,y)
= p(x|y) \cdot p(y)
= \mathcal{N}(x; \mu, (y \Lambda)^{-1}) \cdot \mathrm{Gam}(y; a, b) \; .
$$

The [differential entropy of the multivariate normal distribution](/P/mvn-dent) is

$$ \label{eq:mvn-dent}
\mathrm{h}(X) = \frac{n}{2} \ln(2\pi) + \frac{1}{2} \ln|\Sigma| + \frac{1}{2} n
$$

and the [differential entropy of the univariate gamma distribution](/P/gam-dent) is

$$ \label{eq:gam-dent}
\mathrm{h}(Y) = a + \ln \Gamma(a) + (1-a) \cdot \psi(a) - \ln b
$$

where $\Gamma(x)$ is the gamma function and $\psi(x)$ is the digamma function.

The [differential entropy of a continuous random variable](/D/dent) in nats is given by

$$ \label{eq:dent}
\mathrm{h}(Z) = - \int_{\mathcal{Z}} p(z) \ln p(z) \, \mathrm{d}z
$$

which, applied to the [normal-gamma distribution](/D/ng) over $X$ and $Y$, yields

$$ \label{eq:NG-dent0}
\mathrm{h}(X,Y) = - \int_{0}^{\infty} \int_{\mathbb{R}^n} p(x,y) \, \ln p(x,y) \, \mathrm{d}x \, \mathrm{d}y \; .
$$

Using the [law of conditional probability](/D/prob-cond), this can be evaluated as follows:

$$ \label{eq:NG-dent1}
\begin{split}
   \mathrm{h}(X,Y)
&= - \int_{0}^{\infty} \int_{\mathbb{R}^n} p(x|y) \, p(y) \, \ln p(x|y) \, p(y) \, \mathrm{d}x \, \mathrm{d}y \\
&= - \int_{0}^{\infty} \int_{\mathbb{R}^n} p(x|y)\, p(y) \, \ln p(x|y) \, \mathrm{d}x \, \mathrm{d}y - \int_{0}^{\infty} \int_{\mathbb{R}^n} p(x|y)\, p(y) \, \ln p(y) \, \mathrm{d}x \, \mathrm{d}y \\
&= \int_{0}^{\infty} p(y) \int_{\mathbb{R}^n} p(x|y) \, \ln p(x|y) \, \mathrm{d}x \, \mathrm{d}y + \int_{0}^{\infty} p(y) \, \ln p(y) \int_{\mathbb{R}^n} p(x|y) \, \mathrm{d}x \, \mathrm{d}y \\
&= \left\langle \mathrm{h}(X|Y) \right\rangle_{p(y)} + \mathrm{h}(Y) \; .
\end{split}
$$

In other words, the differential entropy of the normal-gamma distribution over $X$ and $Y$ is equal to the sum of a multivariate normal entropy regarding $X$ conditional on $Y$, expected over $Y$, and a univariate gamma entropy regarding $Y$.

From equations \eqref{eq:NG-pdf} and \eqref{eq:mvn-dent}, the first term becomes

$$ \label{eq:exp-mvn-dent-s1}
\begin{split}
   \left\langle \mathrm{h}(X|Y) \right\rangle_{p(y)}
&= \left\langle \frac{n}{2} \ln(2\pi) + \frac{1}{2} \ln|(y \Lambda)^{-1}| + \frac{1}{2} n \right\rangle_{p(y)} \\
&= \left\langle \frac{n}{2} \ln(2\pi) - \frac{1}{2} \ln|(y \Lambda)| + \frac{1}{2} n \right\rangle_{p(y)} \\
&= \left\langle \frac{n}{2} \ln(2\pi) - \frac{1}{2} \ln(y^n |\Lambda|) + \frac{1}{2} n \right\rangle_{p(y)} \\
&= \frac{n}{2} \ln(2\pi) - \frac{1}{2} \ln|\Lambda| + \frac{1}{2} n - \left\langle \frac{n}{2} \ln y \right\rangle_{p(y)} \\
\end{split}
$$

and using [the relation](/P/gam-logmean) $Y \sim \mathrm{Gam}(a,b) \Rightarrow \left\langle \ln Y \right\rangle = \psi(a) - \ln(b)$, we have

$$ \label{eq:exp-mvn-dent-s2}
\begin{split}
\left\langle \mathrm{h}(X|Y) \right\rangle_{p(y)} = \frac{n}{2} \ln(2\pi) - \frac{1}{2} \ln|\Lambda| + \frac{1}{2} n - \frac{n}{2} \psi(a) + \frac{n}{2} \ln b \; .
\end{split}
$$

By plugging \eqref{eq:exp-mvn-dent-s2} and \eqref{eq:gam-dent} into \eqref{eq:NG-dent1}, one arrives at the differential entropy given by \eqref{eq:NG-dent}.