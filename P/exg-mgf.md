---
layout: proof
mathjax: true

author: "Thomas J. Faulkenberry"
affiliation: "Tarleton State University"
e_mail: "faulkenberry@tarleton.edu"
date: 2023-04-19 12:00:00

title: "Moment-generating function of the ex-Gaussian distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "ex-Gaussian distribution"
theorem: "Moment-generating function"

sources:

proof_id: "P404"
shortcut: "exg-mgf"
username: "tomfaulkenberry"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following an [ex-Gaussian distribution](/D/exg):

$$ \label{eq:exg}
X \sim \mathrm{ex-Gaussian}(\mu, \sigma, \lambda) \; .
$$

Then, the [moment generating function](/D/mgf) of $X$ is 

$$ \label{eq:exg-mgf}
M_X(t) = \left( \frac{\lambda}{\lambda-t} \right) \exp \left[ \mu t + \frac{1}{2}\sigma^2t^2 \right] \; .
$$


**Proof:** Suppose $X$ follows an [ex-Gaussian distribution](/D/exg). Then, $X=A+B$ where $A$ and $B$ are [independent](/D/ind), $A$ is [normally distributed](/D/norm) with [mean](/P/norm-mean) $\mu$ and [variance](/P/norm-var) $\sigma^2$, and $B$ is [exponentially distributed](/D/exp) with rate $\lambda$. Then the [moment generating function](/P/norm-mgf) for $A$ is given by

$$ \label{eq:norm-mgf}
M_A(t) = \exp \left[ \mu t + \frac{1}{2}\sigma^2t^2 \right]
$$ 

and the [moment generating function](/P/exp-mgf) for $B$ is given by

$$ \label{eq:exp-mgf}
M_B(t) = \frac{\lambda}{\lambda - t} \; .
$$

By definition, $X$ is a linear combination of independent random variables $A$ and $B$, so the [moment generating function](/P/mgf-lincomb) of $X$ is the product of $M_A(t)$ and $M_B(t)$. That is,

$$ \label{eq:exg-mgf-s1}
\begin{split}
M_X(t) &= M_A(t)\cdot M_B(t)\\
&= \exp\left[ \mu t + \frac{1}{2}\sigma^2t^2 \right] \cdot \left( \frac{\lambda}{\lambda-t} \right)\\
&= \left( \frac{\lambda}{\lambda-t} \right) \exp\left[ \mu t + \frac{1}{2}\sigma^2t^2 \right] \; .
\end{split}
$$

This finishes the proof of \eqref{eq:exg-mgf}.