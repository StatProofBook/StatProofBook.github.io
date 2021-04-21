---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-02-04 15:12:00

title: "Log model evidence for the Poisson distribution with exposure values"
chapter: "Statistical Models"
section: "Poisson data"
topic: "Poisson distribution with exposure values"
theorem: "Log model evidence"

sources:

proof_id: "P43"
shortcut: "poissexp-lme"
username: "JoramSoch"
---


**Theorem:** Consider data $y = \left\lbrace y_1, \ldots, y_n \right\rbrace$ following a [Poisson distribution with exposure values](/D/poissexp):

$$ \label{eq:Poiss-exp}
y_i \sim \mathrm{Poiss}(\lambda x_i), \quad i = 1, \ldots, n \; .
$$

Moreover, assume a [gamma prior distribution](/P/poissexp-prior) over the model parameter $\lambda$:

$$ \label{eq:Poiss-exp-prior}
p(\lambda) = \mathrm{Gam}(\lambda; a_0, b_0) \; .
$$

Then, the [log model evidence](/D/lme) for this model is

$$ \label{eq:Poiss-exp-LME}
\begin{split}
\log p(y|m) = &\sum_{i=1}^n y_i \log(x_i) - \sum_{i=1}^n \log y_i ! + \\ 
&\log \Gamma(a_n) - \log \Gamma(a_0) + a_0 \log b_0 - a_n \log b_n \; .
\end{split}
$$

where the [posterior hyperparameters](/D/post) are given by

$$ \label{eq:Poiss-exp-post-par}
\begin{split}
a_n &= a_0 + n \bar{y} \\
a_n &= a_0 + n \bar{x} \; .
\end{split}
$$


**Proof:** With the [probability mass function of the Poisson distribution](/P/poiss-pmf), the [likelihood function](/D/lf) for each observation implied by \eqref{eq:Poiss-exp} is given by

$$ \label{eq:Poiss-exp-LF-s1}
p(y_i|\lambda) = \mathrm{Poiss}(y_i; \lambda x_i) = \frac{(\lambda x_i)^{y_i} \cdot \exp\left[-\lambda x_i\right]}{y_i !}
$$

and because observations are [independent](/D/ind), the likelihood function for all observations is the product of the individual ones:

$$ \label{eq:Poiss-exp-LF-s2}
p(y|\lambda) = \prod_{i=1}^n p(y_i|\lambda) = \prod_{i=1}^n \frac{(\lambda x_i)^{y_i} \cdot \exp\left[-\lambda x_i\right]}{y_i !} \; .
$$

Combining the likelihood function \eqref{eq:Poiss-exp-LF-s2} with the prior distribution \eqref{eq:Poiss-exp-prior}, the [joint likelihood](/D/jl) of the model is given by

$$ \label{eq:Poiss-exp-JL-s1}
\begin{split}
p(y,\lambda) &= p(y|\lambda) \, p(\lambda) \\
&= \prod_{i=1}^n \frac{(\lambda x_i)^{y_i} \cdot \exp\left[-\lambda x_i\right]}{y_i !} \cdot \frac{ {b_0}^{a_0}}{\Gamma(a_0)} \lambda^{a_0-1} \exp[-b_0 \lambda] \; .
\end{split}
$$

Resolving the product in the joint likelihood, we have

$$ \label{eq:Poiss-exp-JL-s2}
\begin{split}
p(y,\lambda) &= \prod_{i=1}^n \frac{ {x_i}^{y_i}}{y_i !} \prod_{i=1}^n \lambda^{y_i} \prod_{i=1}^n \exp\left[-\lambda x_i\right] \cdot \frac{ {b_0}^{a_0}}{\Gamma(a_0)} \lambda^{a_0-1} \exp[-b_0 \lambda] \\
&= \prod_{i=1}^n \left(\frac{ {x_i}^{y_i}}{y_i !}\right) \lambda^{\sum_{i=1}^n y_i} \exp\left[-\lambda \sum_{i=1}^n x_i\right] \cdot \frac{ {b_0}^{a_0}}{\Gamma(a_0)} \lambda^{a_0-1} \exp[-b_0 \lambda] \\
&= \prod_{i=1}^n \left(\frac{ {x_i}^{y_i}}{y_i !}\right) \lambda^{n \bar{y}} \exp\left[-n \bar{x} \lambda\right] \cdot \frac{ {b_0}^{a_0}}{\Gamma(a_0)} \lambda^{a_0-1} \exp[-b_0 \lambda] \\
&= \prod_{i=1}^n \left(\frac{ {x_i}^{y_i}}{y_i !}\right) \frac{ {b_0}^{a_0}}{\Gamma(a_0)}  \cdot \lambda^{a_0 + n \bar{y} - 1} \cdot \exp\left[-(b_0 + n \bar{x}) \lambda\right] \\
\end{split}
$$

where $\bar{y}$ and $\bar{x}$ are the [means](/D/mean-samp) of $y$ and $x$ respectively:

$$ \label{eq:xy-mean}
\begin{split}
\bar{y} &= \frac{1}{n} \sum_{i=1}^n y_i \\
\bar{x} &= \frac{1}{n} \sum_{i=1}^n x_i \; .
\end{split}
$$

Note that the [model evidence is the marginal density of the joint likelihood](/D/ml):

$$ \label{eq:Poiss-exp-ME}
p(y) = \int p(y,\lambda) \, \mathrm{d}\lambda \; .
$$

Setting $a_n = a_0 + n \bar{y}$ and $b_n = b_0 + n \bar{x}$, the joint likelihood can also be written as

$$ \label{eq:Poiss-exp-JL-s3}
p(y,\lambda) = \prod_{i=1}^n \left(\frac{ {x_i}^{y_i}}{y_i !}\right) \frac{ {b_0}^{a_0}}{\Gamma(a_0)} \frac{\Gamma(a_n)}{ {b_n}^{a_n}} \cdot \frac{ {b_n}^{a_n}}{\Gamma(a_n)} \lambda^{a_n-1} \exp\left[-b_n \lambda\right] \; .
$$

Using the [probability density function of the gamma distribution](/P/gam-pdf), $\lambda$ can now be integrated out easily

$$ \label{eq:Poiss-exp-ME-qed}
\begin{split}
\mathrm{p}(y) &= \int \prod_{i=1}^n \left(\frac{ {x_i}^{y_i}}{y_i !}\right) \frac{ {b_0}^{a_0}}{\Gamma(a_0)} \frac{\Gamma(a_n)}{ {b_n}^{a_n}} \cdot \frac{ {b_n}^{a_n}}{\Gamma(a_n)} \lambda^{a_n-1} \exp\left[-b_n \lambda\right] \, \mathrm{d}\lambda \\
&= \prod_{i=1}^n \left(\frac{ {x_i}^{y_i}}{y_i !}\right) \frac{\Gamma(a_n)}{\Gamma(a_0)} \frac{ {b_0}^{a_0}}{ {b_n}^{a_n}} \int \mathrm{Gam}(\lambda; a_n, b_n) \, \mathrm{d}\lambda \\
&= \prod_{i=1}^n \left(\frac{ {x_i}^{y_i}}{y_i !}\right) \frac{\Gamma(a_n)}{\Gamma(a_0)} \frac{ {b_0}^{a_0}}{ {b_n}^{a_n}} \; ,
\end{split}
$$

such that the [log model evidence](/D/lme) is shown to be

$$ \label{eq:Poiss-exp-LME-qed}
\begin{split}
\log p(y|m) = &\sum_{i=1}^n y_i \log(x_i) - \sum_{i=1}^n \log y_i ! + \\ 
&\log \Gamma(a_n) - \log \Gamma(a_0) + a_0 \log b_0 - a_n \log b_n \; .
\end{split}
$$