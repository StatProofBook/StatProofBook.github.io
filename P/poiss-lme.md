---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-04-21 09:09:00

title: "Log model evidence for Poisson-distributed data"
chapter: "Statistical Models"
section: "Poisson data"
topic: "Poisson-distributed data"
theorem: "Log model evidence"

sources:

proof_id: "P227"
shortcut: "poiss-lme"
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

Then, the [log model evidence](/D/lme) for this model is

$$ \label{eq:Poiss-LME}
\log p(y|m) = - \sum_{i=1}^n \log y_i ! + \log \Gamma(a_n) - \log \Gamma(a_0) + a_0 \log b_0 - a_n \log b_n \; .
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

Note that the [model evidence is the marginal density of the joint likelihood](/D/ml):

$$ \label{eq:Poiss-ME}
p(y) = \int p(y,\lambda) \, \mathrm{d}\lambda \; .
$$

Setting $a_n = a_0 + n \bar{y}$ and $b_n = b_0 + n$, the joint likelihood can also be written as

$$ \label{eq:Poiss-JL-s3}
p(y,\lambda) = \prod_{i=1}^n \left(\frac{1}{y_i !}\right) \frac{ {b_0}^{a_0}}{\Gamma(a_0)} \frac{\Gamma(a_n)}{ {b_n}^{a_n}} \cdot \frac{ {b_n}^{a_n}}{\Gamma(a_n)} \lambda^{a_n-1} \exp\left[-b_n \lambda\right] \; .
$$

Using the [probability density function of the gamma distribution](/P/gam-pdf), $\lambda$ can now be integrated out easily

$$ \label{eq:Poiss-ME-qed}
\begin{split}
\mathrm{p}(y) &= \int \prod_{i=1}^n \left(\frac{1}{y_i !}\right) \frac{ {b_0}^{a_0}}{\Gamma(a_0)} \frac{\Gamma(a_n)}{ {b_n}^{a_n}} \cdot \frac{ {b_n}^{a_n}}{\Gamma(a_n)} \lambda^{a_n-1} \exp\left[-b_n \lambda\right] \, \mathrm{d}\lambda \\
&= \prod_{i=1}^n \left(\frac{1}{y_i !}\right) \frac{\Gamma(a_n)}{\Gamma(a_0)} \frac{ {b_0}^{a_0}}{ {b_n}^{a_n}} \int \mathrm{Gam}(\lambda; a_n, b_n) \, \mathrm{d}\lambda \\
&= \prod_{i=1}^n \left(\frac{1}{y_i !}\right) \frac{\Gamma(a_n)}{\Gamma(a_0)} \frac{ {b_0}^{a_0}}{ {b_n}^{a_n}} \; ,
\end{split}
$$

such that the [log model evidence](/D/lme) is shown to be

$$ \label{eq:Poiss-LME-qed}
\log p(y|m) = - \sum_{i=1}^n \log y_i ! + \log \Gamma(a_n) - \log \Gamma(a_0) + a_0 \log b_0 - a_n \log b_n \; .
$$