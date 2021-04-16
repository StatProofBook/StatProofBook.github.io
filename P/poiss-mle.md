---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-01-20 21:53:00

title: "Maximum likelihood estimation for Poisson-distributed data"
chapter: "Statistical Models"
section: "Poisson data"
topic: "Poisson-distributed data"
theorem: "Maximum likelihood estimation"

sources:

proof_id: "P27"
shortcut: "poiss-mle"
username: "JoramSoch"
---


**Theorem:** Let there be a [Poisson-distributed data](/D/poiss-data) set $y = \left\lbrace y_1, \ldots, y_n \right\rbrace$:

$$ \label{eq:Poiss}
y_i \sim \mathrm{Poiss}(\lambda), \quad i = 1, \ldots, n \; .
$$

Then, the [maximum likelihood estimate](/D/mle) for the rate parameter $\lambda$ is given by

$$ \label{eq:Poiss-MLE}
\hat{\lambda} = \bar{y}
$$

where $\bar{y}$ is the [sample mean](/D/mean-samp)

$$ \label{eq:y-mean}
\bar{y} = \frac{1}{n} \sum_{i=1}^n y_i \; .
$$


**Proof:** The [likelihood function](/D/lf) for each observation is given by the [probability mass function of the Poisson distribution](/P/poiss-pmf)

$$ \label{eq:Poiss-yi}
p(y_i|\lambda) = \mathrm{Poiss}(y_i; \lambda) = \frac{\lambda^{y_i} \cdot \exp(-\lambda)}{y_i !}
$$

and because observations are [independent](/D/ind), the likelihood function for all observations is the product of the individual ones:

$$ \label{eq:Poiss-LF}
p(y|\lambda) = \prod_{i=1}^n p(y_i|\lambda) = \prod_{i=1}^n \frac{\lambda^{y_i} \cdot \exp(-\lambda)}{y_i !} \; .
$$

Thus, the [log-likelihood function](/D/llf) is

$$ \label{eq:Poiss-LL}
\mathrm{LL}(\lambda) = \log p(y|\lambda) = \log \left[ \prod_{i=1}^n \frac{\lambda^{y_i} \cdot \exp(-\lambda)}{y_i !} \right]
$$

which can be developed into

$$ \label{eq:Poiss-LL-der}
\begin{split}
\mathrm{LL}(\lambda) &= \sum_{i=1}^n \log \left[ \frac{\lambda^{y_i} \cdot \exp(-\lambda)}{y_i !} \right] \\
&= \sum_{i=1}^n \left[ y_i \cdot \log(\lambda) - \lambda - \log(y_i !) \right] \\
&= - \sum_{i=1}^n \lambda + \sum_{i=1}^n y_i \cdot \log(\lambda) - \sum_{i=1}^n \log(y_i !) \\
&= - n \lambda + \log(\lambda) \sum_{i=1}^n y_i - \sum_{i=1}^n \log(y_i !) \\
\end{split}
$$

The derivatives of the log-likelihood with respect to $\lambda$ are

$$ \label{eq:Poiss-dLLdl-d2LLdl2}
\begin{split}
\frac{\mathrm{d}\mathrm{LL}(\lambda)}{\mathrm{d}\lambda} &= \frac{1}{\lambda} \sum_{i=1}^n y_i - n \\
\frac{\mathrm{d}^2\mathrm{LL}(\lambda)}{\mathrm{d}\lambda^2} &= -\frac{1}{\lambda^2} \sum_{i=1}^n y_i \; . \\
\end{split}
$$

Setting the first derivative to zero, we obtain:

$$ \label{eq:Poiss-dLLdl}
\begin{split}
\frac{\mathrm{d}\mathrm{LL}(\hat{\lambda})}{\mathrm{d}\lambda} &= 0 \\
0 &= \frac{1}{\hat{\lambda}} \sum_{i=1}^n y_i - n \\
\hat{\lambda} &= \frac{1}{n} \sum_{i=1}^n y_i = \bar{y} \; .
\end{split}
$$

Plugging this value into the second derivative, we confirm:

$$ \label{eq:Poiss-d2LLdl2}
\begin{split}
\frac{\mathrm{d}^2\mathrm{LL}(\hat{\lambda})}{\mathrm{d}\lambda^2} &= -\frac{1}{\bar{y}^2} \sum_{i=1}^n y_i \\
&= -\frac{n \cdot \bar{y}}{\bar{y}^2} \\
&= -\frac{n}{\bar{y}} < 0 \; .
\end{split}
$$

This demonstrates that the estimate $\hat{\lambda} = \bar{y}$ maximizes the likelihood $p(y \vert \lambda)$.