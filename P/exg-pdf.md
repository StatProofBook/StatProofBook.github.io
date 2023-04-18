---
layout: proof
mathjax: true

author: "Thomas J. Faulkenberry"
affiliation: Tarleton State University
e_mail: faulkenberry@tarleton.edu
date: "2023-04-18 12:00:00"

title: "Probability density function of the ex-Gaussian distribution"
chapter: Probability Distributions
section: Univariate continuous distributions
topic: "ex-Gaussian distribution"
theorem: Probability density function

sources: 

proof_id: P402
shortcut: "exg-pdf"
username: tomfaulkenberry
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following an [ex-Gaussian distribution](/D/exg):

$$ \label{eq:exg}
X \sim \text{ex-Gaussian}(\mu, \sigma, \lambda) \; .
$$

Then the [probability density function](/D/pdf) of $X$ is 

$$ \label{eq:exg-pdf}
f_X(t) = \frac{\lambda}{\sqrt{2\pi}} \exp\left[\frac{\lambda^2\sigma^2}{2} - \lambda(t-\mu)\right] \cdot \int_{-\infty}^{\frac{t-\mu}{\sigma}-\lambda\sigma} \exp\left[-\frac{1}{2}y^2\right] dy \; .
$$


**Proof:** Suppose $X$ follows an [ex-Gaussian distribution](/D/exg). Then $X=A+B$, where $A$ and $B$ are [independent](/D/ind), $A$ is [normally distributed](/D/norm) with [mean](/P/norm-mean) $\mu$ and [variance](/P/norm-var) $\sigma^2$, and $B$ is [exponentially distributed](/D/exp) with rate $\lambda$. Then the [probability density function](/P/norm-pdf) for $A$ is given by

$$ \label{eq:norm-pdf}
f_A(t) = \frac{1}{\sigma\sqrt{2\pi}}\exp\left[-\frac{1}{2}\left(\frac{t-\mu}{\sigma}\right)^2\right] \; ,
$$

and the [probability density function](/P/exp-pdf) for $B$ is given by

$$ \label{eq:exp-pdf}
f_B(t) = \left\{
\begin{array}{rl}
\lambda\exp[-\lambda t] \;, & \text{if} \; t\geq 0\\
0 \;, & \text{if} \; t <0 \; .
\end{array}
\right.
$$

Then the [probability density function for the sum](/P/pdf-sumind) $X=A+B$ is given by taking the convolution of $f_A$ and $f_B$:

$$ \label{eq:convolution}
\begin{split}
f_X(t) &= \int_{-\infty}^{\infty} f_A(x)f_B(t-x)dx\\
&= \int_{-\infty}^{t} f_A(x)f_B(t-x)dx + \int_{t}^{\infty} f_A(x)f_B(t-x)dx \\
&= \int_{-\infty}^{t} f_A(x)f_B(t-x)dx \; ,
\end{split}
$$

which follows from the fact that $f_B(t-x) = 0$ for $x>t$. From here, we substitute the expressions \eqref{eq:norm-pdf} and \eqref{eq:exp-pdf} for the probability density functions $f_A$ and $f_B$ in \eqref{eq:convolution}:

$$ \label{eq:exg-pdf-s1}
\begin{split}
f_X(t) &= \int_{-\infty}^t \frac{1}{\sigma\sqrt{2\pi}}\exp\left[-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2\right]\cdot \lambda\exp[-\lambda(t-x)]dx\\
&= \frac{\lambda}{\sigma\sqrt{2\pi}}\int_{-\infty}^t \exp\left[-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2\right]\cdot \exp[-\lambda t+\lambda x]dx\\
&= \frac{\lambda}{\sigma\sqrt{2\pi}}\int_{-\infty}^t \exp\left[-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2\right]\cdot \exp[-\lambda t]\cdot \exp[\lambda x]dx\\
&= \frac{\lambda\exp[-\lambda t]}{\sigma\sqrt{2\pi}}\int_{-\infty}^t \exp\left[-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2+\lambda x\right]dx \; .
\end{split}
$$

We can further simplify the integrand with a substitution; to this end, let

$$ \label{eq:substitution}
y = g(x) = \frac{x-\mu}{\sigma} - \lambda\sigma
$$

This gives the following three identities:

$$ \label{eq:identity1}
\frac{dy}{dx} = \frac{1}{\sigma} \; , \; \text{or equivalently,} \; dx=\sigma dy \;,
$$

$$ \label{eq:identity2}
\frac{x-\mu}{\sigma} = y+\lambda\sigma \; ,
$$

and 

$$ \label{eq:identity3}
x=y\sigma + \lambda\sigma^2 + \mu \; .
$$

Substituting these identities into \eqref{eq:exg-pdf-s1} gives

$$ \label{eq:exg-pdf-s2}
\begin{split}
f_X(t) &= \frac{\lambda\exp[-\lambda t]}{\sigma\sqrt{2\pi}}\int_{-\infty}^{g(t)} \exp\left[-\frac{1}{2}(y+\lambda\sigma)^2+\lambda(y\sigma + \lambda\sigma^2+\mu)\right]\sigma dy\\
&= \frac{\lambda\sigma\exp[-\lambda t]}{\sigma\sqrt{2\pi}}\int_{-\infty}^{\frac{x-\mu}{\sigma}+\lambda\sigma} \exp\left[-\frac{1}{2}(y^2+2y\lambda\sigma + \lambda^2\sigma^2)+\lambda y\sigma + \lambda^2\sigma^2 + \lambda\mu\right] dy\\
&= \frac{\lambda\exp[-\lambda t]}{\sqrt{2\pi}}\int_{-\infty}^{\frac{x-\mu}{\sigma}+\lambda\sigma} \exp\left[-\frac{1}{2}y^2-y\lambda\sigma - \frac{\lambda^2\sigma^2}{2}+\lambda y\sigma + \lambda^2\sigma^2 + \lambda\mu\right] dy\\
&= \frac{\lambda\exp[-\lambda t]}{\sqrt{2\pi}}\int_{-\infty}^{\frac{x-\mu}{\sigma}+\lambda\sigma} \exp\left[-\frac{1}{2}y^2\right] \cdot \exp\left[\frac{\lambda^2\sigma^2}{2} + \lambda\mu\right] dy\\
&= \frac{\lambda\exp[-\lambda t]}{\sqrt{2\pi}}\cdot \exp\left[\frac{\lambda^2\sigma^2}{2} + \lambda\mu\right] \int_{-\infty}^{\frac{x-\mu}{\sigma}+\lambda\sigma} \exp\left[-\frac{1}{2}y^2\right] \cdot  dy\\
&= \frac{\lambda}{\sqrt{2\pi}}\cdot \exp\left[-\lambda t + \frac{\lambda^2\sigma^2}{2} + \lambda\mu\right] \int_{-\infty}^{\frac{x-\mu}{\sigma}+\lambda\sigma} \exp\left[-\frac{1}{2}y^2\right] \cdot  dy\\
&= \frac{\lambda}{\sqrt{2\pi}}\cdot \exp\left[\frac{\lambda^2\sigma^2}{2} - \lambda(t-\mu)\right] \int_{-\infty}^{\frac{x-\mu}{\sigma}+\lambda\sigma} \exp\left[-\frac{1}{2}y^2\right] \cdot  dy \; .
\end{split}
$$

This finishes the proof of \eqref{eq:exg-pdf}.