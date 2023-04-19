---
layout: proof
mathjax: true

author: "Thomas J. Faulkenberry"
affiliation: Tarleton State University
e_mail: faulkenberry@tarleton.edu
date: "2023-04-19 12:00:00"

title: "Moment-generating function of the exponential distribution"
chapter: Probability Distributions
section: Univariate continuous distributions
topic: Exponential distribution
theorem: Moment generating function

sources: 

proof_id: P403
shortcut: "exp-mgf"
username: tomfaulkenberry
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following an [exponential distribution](/D/exp):

$$ \label{eq:exp}
X \sim \mathrm{Exp}(\lambda) \; .
$$

Then the [moment generating function](/D/mgf) of $X$ is 

$$ \label{eq:exp-mgf}
M_X(t) = \frac{\lambda}{\lambda - t} \; ,
$$

which is well-defined for $t < \lambda$.

**Proof:** Suppose $X$ follows an [exponential distribution](/D/exp) with rate $\lambda$; that is, $X\sim \mathrm{Exp}(\lambda)$. Then the [probability density function](/P/exp-pdf) is given by 

$$ \label{eq:exp-pdf}
f_X(x) = \lambda e^{-\lambda x}
$$

and the [moment-generating function](/D/mgf) is defined as

$$ \label{eq:mgf}
M_X(t) = \mathrm{E} \left[ e^{tX} \right] \; .
$$

Using the definition of [expected value for continuous random variables](/D/mean), the moment-generating function of $X$ is thus

$$ \label{eq:exp-mgf-s1}
\begin{split}
M_X(t) &= \int_0^{\infty} e^{tx} \cdot f_X(x) dx\\
&= \int_0^{\infty} e^{tx}\cdot \lambda e^{-\lambda x} dx\\
&= \int_0^{\infty} \lambda e^{x(t-\lambda)} dx\\
&= \frac{\lambda}{t-\lambda} e^{x(t-\lambda)} \Big|_{x = 0}^{x = \infty}\\
&= \lim_{x\rightarrow \infty} \left[ \frac{\lambda}{t-\lambda} e^{x(t-\lambda)} - \frac{\lambda}{t-\lambda}\right]\\
&= \frac{\lambda}{t-\lambda} \left[ \lim_{x\rightarrow \infty} e^{x(t-\lambda)} -1 \right] \; .
\end{split}
$$

Note that $t$ cannot be equal to $\lambda$, else $M_X(t)$ is undefined. Further, if $t > \lambda$, then $\lim_{x\rightarrow \infty} e^{x(t-\lambda)} = \infty$, which implies that $M_X(t)$ diverges for $t \geq \lambda$. So, we must restrict the domain of $M_X(t)$ to $t<\lambda$. Assuming this, we can further simplify \eqref{eq:exp-mgf-s1}:

$$ \label{eq:exp-mgf-s2}
\begin{split}
M_X(t) &= \frac{\lambda}{t-\lambda} \left[ \lim_{x\rightarrow \infty} e^{x(t-\lambda)} -1 \right] \\
&= \frac{\lambda}{t-\lambda} \left[ 0 - 1 \right] \\
&= \frac{\lambda}{\lambda - t} \; .
\end{split}
$$

This completes the proof of \eqref{eq:exp-mgf}.
