---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2026-04-23 16:52:11

title: "Maximum likelihood estimation for univariate von Mises data"
chapter: "Statistical Models"
section: "Periodic data"
topic: "Univariate von Mises"
theorem: "Maximum likelihood estimation"

sources:
  - authors: "Bishop CM"
    year: 2006
    title: "Periodic variables"
    in: "Pattern Recognition for Machine Learning"
    pages: "sect. 2.3.8, pp. 108-110, eqs. 2.181-2.186"
    url: "http://users.isr.ist.utl.pt/~wurmd/Livros/school/Bishop%20-%20Pattern%20Recognition%20And%20Machine%20Learning%20-%20Springer%20%202006.pdf"

proof_id: "P537"
shortcut: "vm-mle"
username: "JoramSoch"
---


**Theorem:** Let there be a [univariate von Mises data set](/D/vm-data) $y = \left\lbrace y_1, \ldots, y_n \right\rbrace$:

$$ \label{eq:vm}
y_i \sim \mathrm{vM}(\mu, \kappa), \quad i = 1, \ldots, n \; .
$$

Then, the [maximum likelihood estimates](/D/mle) for circular mean $\mu$ and reciprocal dispersion $\kappa$ are given by

$$ \label{eq:vm-mle}
\begin{split}
\hat{\mu}    &= \arctan \left( \frac{\sum_{i=1}^n \sin y_i}{\sum_{i=1}^n \cos y_i} \right) \\
\hat{\kappa} &= A^{-1}\left( \frac{1}{n} \sum_{i=1}^n \cos(y_i-\hat{\mu}) \right)
\end{split}
$$

where $A^{-1}$ is the inverse function of

$$ \label{eq:A}
A(\kappa) = \frac{I_1(\kappa)}{I_0(\kappa)}
$$

with the [zeroth- and first-order modified Bessel function of the first kind](/D/vm):

$$ \label{eq:I0-I1}
\begin{split}
I_0(\kappa) &= \frac{1}{2\pi} \int_0^{2\pi} \exp \left[ \kappa \cos(x) \right] \, \mathrm{d}x \\ \text{and} \quad
I_1(\kappa) &= \frac{\mathrm{d}}{\mathrm{d}\kappa} I_0(\kappa)
\end{split}
$$


**Proof:** The [likelihood function](/D/lf) for each observation is given by the [probability density function of the von Mises distribution](/P/vm-pdf)

$$ \label{eq:vm-yi}
p(y_i|\mu,\kappa) = \mathrm{vM}(y_i; \mu, \kappa) = \frac{1}{\sqrt{2 \pi} I_0(\kappa)} \cdot \exp \left[ \kappa \cos(y_i-\mu) \right]
$$

and because observations are [independent](/D/ind), the likelihood function for all observations is the product of the individual ones:

$$ \label{eq:vm-LF}
p(y|\mu,\kappa) = \prod_{i=1}^n p(y_i|\mu, \kappa) = \left( \frac{1}{\sqrt{2 \pi} I_0(\kappa)} \right)^n \cdot \exp \left[ \kappa \sum_{i=1}^n \cos(y_i-\mu) \right] \; .
$$

Thus, the [log-likelihood function](/D/llf) is

$$ \label{eq:vm-LL}
\mathrm{LL}(\mu,\kappa) = \ln p(y|\mu,\kappa) = - n \ln(2 \pi) - n \ln I_0(\kappa) + \kappa \sum_{i=1}^n \cos(y_i-\mu) \; .
$$

We will use the following trigonometric identities:

$$ \label{eq:sin-cos}
\begin{split}
\frac{\sin x}{\cos x} &= \tan x \\
\cos(x-y) &= \cos x \cos y + \sin x \sin y \; .
\end{split}
$$

The derivative of the log-likelihood function \eqref{eq:vm-LL} with respect to $\mu$ is

$$ \label{eq:dLL-dmu}
\frac{\mathrm{d}\mathrm{LL}(\mu,\kappa)}{\mathrm{d}\mu} = - \kappa \sum_{i=1}^n \sin(y_i-\mu)
$$

and setting this derivative to zero gives the MLE for $\mu$:

$$ \label{eq:mu-mle}
\begin{split}
\frac{\mathrm{d}\mathrm{LL}(\hat{\mu},\kappa)}{\mathrm{d}\mu} &= 0 \\
0 &= - \kappa \sum_{i=1}^n \sin(y_i-\hat{\mu}) \\
0 &\overset{\eqref{eq:sin-cos}}{=} - \kappa \sum_{i=1}^n \left[ \cos \hat{\mu} \sin y_i - \cos y_i \sin \hat{\mu} \right] \\
0 &= - \kappa \cos \hat{\mu} \sum_{i=1}^n \sin y_i + \kappa \sin \hat{\mu} \sum_{i=1}^n \cos y_i \\
\kappa \cos \hat{\mu} \sum_{i=1}^n \sin y_i &= \kappa \sin \hat{\mu} \sum_{i=1}^n \cos y_i \\
\frac{\sin \hat{\mu}}{\cos \hat{\mu}} &= \frac{\sum_{i=1}^n \sin y_i}{\sum_{i=1}^n \cos y_i} \\
\tan \hat{\mu} &\overset{\eqref{eq:sin-cos}}{=} \frac{\sum_{i=1}^n \sin y_i}{\sum_{i=1}^n \cos y_i} \\
\hat{\mu} &= \arctan \left( \frac{\sum_{i=1}^n \sin y_i}{\sum_{i=1}^n \cos y_i} \right) \; .
\end{split}
$$

The derivative of the log-likelihood function \eqref{eq:vm-LL} at $\hat{\mu}$ with respect to $\kappa$ is

$$ \label{eq:dLL-dkappa}
\begin{split}
   \frac{\mathrm{d}\mathrm{LL}(\hat{\mu},\kappa)}{\mathrm{d}\kappa}
&= - n \frac{\mathrm{d} \ln I_0(\kappa)}{\mathrm{d}\kappa} + \sum_{i=1}^n \cos(y_i-\hat{\mu}) \\
&\overset{\eqref{eq:I0-I1}}{=} - n \frac{I_1(\kappa)}{I_0(\kappa)} + \sum_{i=1}^n \cos(y_i-\hat{\mu})
\end{split}
$$

and setting this derivative to zero gives the MLE for $\kappa$:

$$ \label{eq:kappa-mle}
\begin{split}
\frac{\mathrm{d}\mathrm{LL}(\hat{\mu},\hat{\kappa})}{\mathrm{d}\kappa} &= 0 \\
0 &= - n \frac{I_1(\hat{\kappa})}{I_0(\hat{\kappa})} + \sum_{i=1}^n \cos(y_i-\hat{\mu}) \\
\frac{I_1(\hat{\kappa})}{I_0(\hat{\kappa})} &= \frac{1}{n} \sum_{i=1}^n \cos(y_i-\hat{\mu}) \\
A(\hat{\kappa}) &\overset{\eqref{eq:A}}{=} \frac{1}{n} \sum_{i=1}^n \cos(y_i-\hat{\mu}) \\
\hat{\kappa} &= A^{-1}\left( \frac{1}{n} \sum_{i=1}^n \cos(y_i-\hat{\mu}) \right) \; .
\end{split}
$$

Together, \eqref{eq:mu-mle} and \eqref{eq:kappa-mle} constitute the MLE for the univariate von Mises.