---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-02-04 14:11:00

title: "Conjugate prior distribution for the Poisson distribution with exposure values"
chapter: "Statistical Models"
section: "Poisson data"
topic: "Poisson distribution with exposure values"
theorem: "Conjugate prior distribution"

sources:

proof_id: "P41"
shortcut: "poissexp-prior"
username: "JoramSoch"
---


**Theorem:** Let $y = \left\lbrace y_1, \ldots, y_n \right\rbrace$ be a series of observed counts which are independently distributed according to a [Poisson distribution](/D/poiss.html) with common rate $\lambda$ and concurrent exposures $\left\lbrace x_1, \ldots, x_n \right\rbrace$:

$$ \label{eq:Poiss-exp}
y_i \sim \mathrm{Poiss}(\lambda x_i), \quad i = 1, \ldots, n \; .
$$

Then, the [conjugate prior](/D/conj-prior.html) for the model parameter $\lambda$ is a gamma distribution:

$$ \label{eq:Poiss-exp-prior}
p(\lambda) = \mathrm{Gam}(\lambda; a_0, b_0) \; .
$$


**Proof:** With the [probability mass function of the Poisson distribution](/P/poiss-pmf.html), the likelihood function for each observation implied by \eqref{eq:Poiss-exp} is given by

$$ \label{eq:Poiss-exp-LF-s1}
p(y_i|\lambda) = \mathrm{Poiss}(y_i; \lambda x_i) = \frac{(\lambda x_i)^{y_i} \cdot \exp\left[-\lambda x_i\right]}{y_i !}
$$

and because observations are independent, the [likelihood function](/D/lf.html) for all observations is the product of the individual ones:

$$ \label{eq:Poiss-exp-LF-s2}
p(y|\lambda) = \prod_{i=1}^n p(y_i|\lambda) = \prod_{i=1}^n \frac{(\lambda x_i)^{y_i} \cdot \exp\left[-\lambda x_i\right]}{y_i !} \; .
$$

Resolving the product in the likelihood function, we have

$$ \label{eq:Poiss-exp-LF-s3}
\begin{split}
p(y|\lambda) &= \prod_{i=1}^n \frac{ {x_i}^{y_i}}{y_i !} \cdot \prod_{i=1}^n \lambda^{y_i} \cdot \prod_{i=1}^n \exp\left[-\lambda x_i\right] \\
&= \prod_{i=1}^n \left(\frac{ {x_i}^{y_i}}{y_i !}\right) \cdot \lambda^{\sum_{i=1}^n y_i} \cdot \exp\left[-\lambda \sum_{i=1}^n x_i\right] \\
&= \prod_{i=1}^n \left(\frac{ {x_i}^{y_i}}{y_i !}\right) \cdot \lambda^{n \bar{y}} \cdot \exp\left[-n \bar{x} \lambda\right]
\end{split}
$$

where $\bar{y}$ and $\bar{x}$ are the means of $y$ and $x$ respectively:

$$ \label{eq:xy-mean}
\begin{split}
\bar{y} &= \frac{1}{n} \sum_{i=1}^n y_i \\
\bar{x} &= \frac{1}{n} \sum_{i=1}^n x_i \; .
\end{split}
$$

In other words, the likelihood function is proportional to a power of $\lambda$ times an exponential of $\lambda$:

$$ \label{eq:Poiss-exp-LF-prop}
p(y|\lambda) \propto \lambda^{n \bar{y}} \cdot \exp\left[-n \bar{x} \lambda\right] \; .
$$

The same is true for a gamma distribution over $\lambda$

$$ \label{eq:Poiss-exp-prior-s1}
p(\lambda) = \mathrm{Gam}(\lambda; a_0, b_0)
$$

the [probability density function of which](/P/gamma-pdf.html)

$$ \label{eq:Poiss-exp-prior-s2}
p(\lambda) = \frac{ {b_0}^{a_0}}{\Gamma(a_0)} \lambda^{a_0-1} \exp[-b_0 \lambda]
$$

exhibits the same proportionality

$$ \label{eq:Poiss-exp-prior-s3}
p(\lambda) \propto \lambda^{a_0-1} \cdot \exp[-b_0 \lambda]
$$

and is therefore conjugate relative to the likelihood.