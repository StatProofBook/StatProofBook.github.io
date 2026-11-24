---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-03-22 17:15:00

title: "Wishart distribution"
chapter: "Probability Distributions"
section: "Matrix-variate continuous distributions"
topic: "Wishart distribution"
definition: "Definition"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Wishart distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-03-22"
    url: "https://en.wikipedia.org/wiki/Wishart_distribution#Definition"
  - authors: "Bishop, Christopher M."
    year: 2006
    title: "Pattern Recognition and Machine Learning"
    in: "Springer"
    pages: "Appendix B, p. 693, equations B.78 and B.79"
    url: "https://www.microsoft.com/en-us/research/wp-content/uploads/2006/01/Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf"

def_id: "D43"
shortcut: "wish"
username: "JoramSoch"
---


**Definition:** Let $Y$ be an $n \times p$ matrix following a [matrix-normal distribution](/D/matn) with mean zero, independence across rows and covariance across columns $V$:

$$ \label{eq:matn}
Y \sim \mathcal{MN}(0, I_n, V) \; .
$$

Define the scatter matrix $X$ as the product of the transpose of $Y$ with itself:

$$ \label{eq:scat-mat}
X = Y^T Y = \sum_{i=1}^n y_i^\mathrm{T} y_i \; .
$$

Then, the matrix $X$ is said to follow a Wishart distribution with scale matrix $V$ and [degrees of freedom](/D/dof) $n$

$$ \label{eq:wish}
X \sim \mathcal{W}(V, n)
$$

where $n > p - 1$ and $V$ is a positive-definite symmetric covariance matrix.

The scatter construction uses an integer number of rows. For every real $n>p-1$, the nonsingular Wishart distribution with scale $V$ has the following density on the symmetric positive-definite $p\times p$ matrices.

$$ \label{eq:wish-real-density}
f(X)=\frac{|X|^{(n-p-1)/2}\exp\!\left[-\operatorname{tr}(V^{-1}X)/2\right]}{2^{np/2}|V|^{n/2}\Gamma_p(n/2)}.
$$

Here $\Gamma_p(a)=\pi^{p(p-1)/4}\prod_{j=1}^{p}\Gamma(a+(1-j)/2)$ is the multivariate gamma function. For integer $n\geq p$, this density gives the law of the scatter matrix above.
