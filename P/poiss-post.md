---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-04-21 08:48:00

title: "Posterior distribution for Poisson-distributed data"
chapter: "Statistical Models"
section: "Poisson data"
topic: "Poisson-distributed data"
theorem: "Posterior distribution"

sources:
  - authors: "Gelman A, Carlin JB, Stern HS, Dunson DB, Vehtari A, Rubin DB"
    year: 2014
    title: "Other standard single-parameter models"
    in: "Bayesian Data Analysis"
    pages: "3rd edition, ch. 2.6, p. 45, eq. 2.15"
    url: "http://www.stat.columbia.edu/~gelman/book/"

proof_id: "P226"
shortcut: "poiss-post"
username: "JoramSoch"
---


**Theorem:** Let there be a [Poisson-distributed data](/D/poiss-data) set $y = \left\lbrace y_1, \ldots, y_n \right\rbrace$:

$$ \label{eq:Poiss}
y_i \sim \mathrm{Poiss}(\lambda), \quad i = 1, \ldots, n \; .
$$

Moreover, assume a [gamma prior distribution](/P/poiss-prior) over the model parameter $\lambda$:

$$ \label{eq:Poiss-prior}
p(\lambda) = \mathrm{Gam}(\lambda; a_0, b_0) \; .
$$

Then, the [posterior distribution](/D/post) is also a [gamma distribution](/D/gam)

$$ \label{eq:Poiss-post}
p(\lambda|y) = \mathrm{Gam}(\lambda; a_n, b_n)
$$

and the [posterior hyperparameters](/D/post) are given by

$$ \label{eq:Poiss-post-par}
\begin{split}
a_n &= a_0 + n \bar{y} \\
b_n &= b_0 + n \; .
\end{split}
$$


**Proof:** With the [probability mass function of the Poisson distribution](/P/poiss-pmf), the [likelihood function](/D/lf) for each observation implied by \eqref{eq:Poiss} is given by

$$ \label{eq:Poiss-LF-s1}
p(y_i|\lambda) = \mathrm{Poiss}(y_i; \lambda) = \frac{\lambda^{y_i} \cdot \exp\left[-\lambda\right]}{y_i !}
$$

and because observations are [independent](/D/ind), the likelihood function for all observations is the product of the individual ones:

$$ \label{eq:Poiss-LF-s2}
p(y|\lambda) = \prod_{i=1}^n p(y_i|\lambda) = \prod_{i=1}^n \frac{\lambda^{y_i} \cdot \exp\left[-\lambda\right]}{y_i !} \; .
$$

Combining the likelihood function \eqref{eq:Poiss-LF-s2} with the prior distribution \eqref{eq:Poiss-prior}, the [joint likelihood](/D/jl) of the model is given by

$$ \label{eq:Poiss-JL-s1}
\begin{split}
p(y,\lambda) &= p(y|\lambda) \, p(\lambda) \\
&= \prod_{i=1}^n \frac{\lambda^{y_i} \cdot \exp\left[-\lambda\right]}{y_i !} \cdot \frac{ {b_0}^{a_0}}{\Gamma(a_0)} \lambda^{a_0-1} \exp[-b_0 \lambda] \; .
\end{split}
$$

Resolving the product in the joint likelihood, we have

$$ \label{eq:Poiss-JL-s2}
\begin{split}
p(y,\lambda) &= \prod_{i=1}^n \frac{1}{y_i !} \prod_{i=1}^n \lambda^{y_i} \prod_{i=1}^n \exp\left[-\lambda\right] \cdot \frac{ {b_0}^{a_0}}{\Gamma(a_0)} \lambda^{a_0-1} \exp[-b_0 \lambda] \\
&= \prod_{i=1}^n \left(\frac{1}{y_i !}\right) \lambda^{n \bar{y}} \exp\left[-n \lambda\right] \cdot \frac{ {b_0}^{a_0}}{\Gamma(a_0)} \lambda^{a_0-1} \exp[-b_0 \lambda] \\
&= \prod_{i=1}^n \left(\frac{1}{y_i !}\right) \cdot \frac{ {b_0}^{a_0}}{\Gamma(a_0)}  \cdot \lambda^{a_0 + n \bar{y} - 1} \cdot \exp\left[-(b_0 + n \lambda)\right] \\
\end{split}
$$

where $\bar{y}$ is the [mean](/D/mean-samp) of $y$:

$$ \label{eq:y-mean}
\bar{y} = \frac{1}{n} \sum_{i=1}^n y_i \; .
$$

Note that the [posterior distribution is proportional to the joint likelihood](/P/post-jl):

$$ \label{eq:Poiss-post-s1}
p(\lambda|y) \propto p(y,\lambda) \; .
$$

Setting $a_n = a_0 + n \bar{y}$ and $b_n = b_0 + n$, the posterior distribution is therefore proportional to

$$ \label{eq:Poiss-post-s2}
p(\lambda|y) \propto \lambda^{a_n-1} \cdot \exp\left[-b_n \lambda\right]
$$

which, when normalized to one, results in the [probability density function of the gamma distribution](/P/gam-pdf):

$$ \label{eq:Poiss-post-s3}
p(\lambda|y) = \frac{ {b_n}^{a_n}}{\Gamma(a_0)} \lambda^{a_n-1} \exp\left[-b_n \lambda\right] = \mathrm{Gam}(\lambda; a_n, b_n) \; .
$$