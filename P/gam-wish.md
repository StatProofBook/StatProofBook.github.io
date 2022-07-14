---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-07-14 07:45:00

title: "Gamma distribution is a special case of Wishart distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Gamma distribution"
theorem: "Special case of Wishart distribution"

sources:

proof_id: "P328"
shortcut: "gam-wish"
username: "JoramSoch"
---


**Theorem:** The [gamma distribution](/D/gam) is a special case of the [Wishart distribution](/D/wish) where the number of columns of the [random matrix](/D/rmat) is $p = 1$.


**Proof:** Let $X$ be a $p \times p$ positive-definite symmetric matrix, such that $X$ follows a [Wishart distribution](/D/wish):

$$ \label{eq:wish}
Y \sim \mathcal{W}(V, n) \; .
$$

Then, $Y$ [is described by the probability density function](/P/wish-pdf)

$$ \label{eq:wish-pdf}
\begin{split}
p(Y) = \frac{1}{\Gamma_p \left( \frac{n}{2} \right)} \cdot \frac{1}{\sqrt{2^{n p} |V|^n}} \cdot |X|^{(n-p-1)/2} \cdot \exp\left[ -\frac{1}{2} \mathrm{tr}\left( V^{-1} X \right) \right]
\end{split}
$$

where $\lvert A \rvert$ is a matrix determinant, $A^{-1}$ is a matrix inverse and $\Gamma_p(x)$ is the multivariate gamma function of order $p$. If $p = 1$, then $\Gamma_p(x) = \Gamma(x)$ is the ordinary gamma function, $x = X$ and $v = V$ are real numbers. Thus, the [probability density function](/D/pdf) of $x$ can be developed as

$$ \label{eq:gam-pdf-s1}
\begin{split}
p(x) &= \frac{1}{\Gamma\left( \frac{n}{2} \right)} \cdot \frac{1}{\sqrt{2^n \, v^n}} \cdot x^{(n-2)/2} \cdot \exp\left[ -\frac{1}{2} \mathrm{tr}\left( v^{-1} x \right) \right] \\
&= \frac{(2v)^{-n/2}}{\Gamma\left( \frac{n}{2} \right)} \cdot x^{n/2-1} \cdot \exp\left[ -\frac{1}{2v} x \right] \\
\end{split}
$$

Finally, substituting $a = \frac{n}{2}$ and $b = \frac{1}{2v}$, we get

$$ \label{eq:gam-pdf-s2}
p(x) = \frac{b^a}{\Gamma(a)} \, x^{a-1} \, \exp[-b x]
$$

which is the [probability density function of the gamma distribution](/P/gam-pdf).