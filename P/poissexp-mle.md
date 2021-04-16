---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-04-16 11:42:00

title: "Maximum likelihood estimation for the Poisson distribution with exposure values"
chapter: "Statistical Models"
section: "Poisson data"
topic: "Poisson distribution with exposure values"
theorem: "Maximum likelihood estimation"

sources:

proof_id: "P224"
shortcut: "poissexp-mle"
username: "JoramSoch"
---


**Theorem:** Consider data $y = \left\lbrace y_1, \ldots, y_n \right\rbrace$ following a [Poisson distribution with exposure values](/D/poissexp):

$$ \label{eq:Poiss-exp}
y_i \sim \mathrm{Poiss}(\lambda x_i), \quad i = 1, \ldots, n \; .
$$

Then, the [maximum likelihood estimate](/D/mle) for the rate parameter $\lambda$ is given by

$$ \label{eq:Poiss-exp-MLE}
\hat{\lambda} = \frac{\bar{y}}{\bar{x}}
$$

where $\bar{y}$ and $\bar{x}$ are the [sample means](/D/mean-sample)

$$ \label{eq:xy-mean}
\begin{split}
\bar{y} &= \frac{1}{n} \sum_{i=1}^n y_i \\
\bar{x} &= \frac{1}{n} \sum_{i=1}^n x_i \; .
\end{split}
$$


**Proof:** With the [probability mass function of the Poisson distribution](/P/poiss-pmf), the [likelihood function](/D/lf) for each observation implied by \eqref{eq:Poiss-exp} is given by

$$ \label{eq:Poiss-exp-LF-s1}
p(y_i|\lambda) = \mathrm{Poiss}(y_i; \lambda x_i) = \frac{(\lambda x_i)^{y_i} \cdot \exp[-\lambda x_i]}{y_i !}
$$

and because observations are [independent](/D/ind), the likelihood function for all observations is the product of the individual ones:

$$ \label{eq:Poiss-exp-LF-s2}
p(y|\lambda) = \prod_{i=1}^n p(y_i|\lambda) = \prod_{i=1}^n \frac{(\lambda x_i)^{y_i} \cdot \exp[-\lambda x_i]}{y_i !} \; .
$$

Thus, the [log-likelihood function](/D/llf) is

$$ \label{eq:Poiss-LL}
\mathrm{LL}(\lambda) = \log p(y|\lambda) = \log \left[ \prod_{i=1}^n \frac{(\lambda x_i)^{y_i} \cdot \exp[-\lambda x_i]}{y_i !} \right]
$$

which can be developed into

$$ \label{eq:Poiss-LL-der}
\begin{split}
\mathrm{LL}(\lambda) &= \sum_{i=1}^n \log \left[ \frac{(\lambda x_i)^{y_i} \cdot \exp[-\lambda x_i]}{y_i !} \right] \\
&= \sum_{i=1}^n \left[ y_i \cdot \log(\lambda x_i) - \lambda x_i - \log(y_i !) \right] \\
&= - \sum_{i=1}^n \lambda x_i + \sum_{i=1}^n y_i \cdot \left[ \log(\lambda) + \log(x_i) \right] - \sum_{i=1}^n \log(y_i !) \\
&= - \lambda \sum_{i=1}^n x_i + \log(\lambda) \sum_{i=1}^n y_i + \sum_{i=1}^n y_i \log(x_i) - \sum_{i=1}^n \log(y_i !) \\
&= - n \bar{x} \lambda + n \bar{y} \log(\lambda) + \sum_{i=1}^n y_i \log(x_i) - \sum_{i=1}^n \log(y_i !) \\
\end{split}
$$

where $\bar{x}$ and $\bar{y}$ are the sample means from equation \eqref{eq:xy-mean}.

<br>
The derivatives of the log-likelihood with respect to $\lambda$ are

$$ \label{eq:Poiss-dLLdl-d2LLdl2}
\begin{split}
\frac{\mathrm{d}\mathrm{LL}(\lambda)}{\mathrm{d}\lambda} &= - n \bar{x} + \frac{n \bar{y}}{\lambda} \\
\frac{\mathrm{d}^2\mathrm{LL}(\lambda)}{\mathrm{d}\lambda^2} &= -\frac{n \bar{y}}{\lambda^2} \; . \\
\end{split}
$$

Setting the first derivative to zero, we obtain:

$$ \label{eq:Poiss-dLLdl}
\begin{split}
\frac{\mathrm{d}\mathrm{LL}(\hat{\lambda})}{\mathrm{d}\lambda} &= 0 \\
0 &= - n \bar{x} + \frac{n \bar{y}}{\hat{\lambda}} \\
\hat{\lambda} &= \frac{n \bar{y}}{n \bar{x}} = \frac{\bar{y}}{\bar{x}} \; .
\end{split}
$$

Plugging this value into the second derivative, we confirm:

$$ \label{eq:Poiss-d2LLdl2}
\begin{split}
\frac{\mathrm{d}^2\mathrm{LL}(\hat{\lambda})}{\mathrm{d}\lambda^2} &= -\frac{n \bar{y}}{\hat{\lambda}^2} \\
&= -\frac{n \cdot \bar{y}}{(\bar{y}/\bar{x})^2} \\
&= -\frac{n \cdot \bar{x}^2}{\bar{y}} < 0 \; .
\end{split}
$$

This demonstrates that the estimate $\hat{\lambda} = \bar{y}/\bar{x}$ maximizes the likelihood $p(y \vert \lambda)$.