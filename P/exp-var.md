---
layout: proof
mathjax: true

author: "Maja Pavlovic"
affiliation: "Queen Mary University London"
e_mail: "m.pavlovic@se22.qmul.ac.uk"
date: 2023-01-23 09:02:00

title: "Variance of the exponential distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Exponential distribution"
theorem: "Variance"

sources:
  - authors: "Taboga, Marco"
    year: 2023
    title: "Exponential distribution"
    in: "Lectures on probability theory and mathematical statistics"
    pages: "retrieved on 2023-01-23"
    url: "https://www.statlect.com/probability-distributions/exponential-distribution"
  - authors: "Wikipedia"
    year: 2023
    title: "Variance"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2023-01-23"
    url: "https://en.wikipedia.org/wiki/Variance#Definition"

proof_id: "P401"
shortcut: "exp-var"
username: "majapavlo"
---

**Theorem:** Let $X$ be a [random variable](/D/rvar) following an [exponential distribution](/D/exp):

$$
X \sim \mathrm{Exp}(\lambda) .
$$

Then, the [variance](/D/var) of $X$ is

$$ \label{eq:exp-var}
\mathrm{Var}(X) = \frac{1}{\lambda^2} \; .
$$


**Proof:** The [variance](/D/var) of a random variable is defined as

$$ \label{eq:var}
\mathrm{Var}(X) = \mathrm{E}\left[ (X-\mathrm{E}(X))^2 \right] 
$$

which, [partitioned into expected values](/P/var-mean), reads:

$$ \label{eq:var2}
\mathrm{Var}(X) = \mathrm{E}\left[ X^2 \right] - \mathrm{E}\left[ X \right]^2 \; .
$$

The [expected value of the exponential distribution](/P/exp-mean) is: 

$$ \label{eq:exp-mean-ref}
\mathrm{E}[X] = \frac{1}{\lambda}
$$

The second moment $\mathrm{E}[X^2]$ can be derived as follows:

$$ \label{eq:second-moment-s1}
\begin{split}
\mathrm{E} [X^2] &= \int_{- \infty}^{+\infty} x^2 \cdot f_\mathrm{X}(x) \, \mathrm{d}x \\ 
&= \int_{0}^{+\infty} x^2 \cdot \lambda \exp(-\lambda x) \, \mathrm{d}x \\ 
&= \lambda \int_{0}^{+\infty} x^2 \cdot \exp(-\lambda x) \, \mathrm{d}x \\
\end{split}
$$

Using the following anti-derivative

$$ \label{eq:second-moment-s2}
\begin{split}
\int x^2 \cdot \exp(-\lambda x) \, \mathrm{d}x = \left[ - \frac{1}{\lambda}x^2 \cdot \mathrm{exp}(-\lambda x) \right]_{0}^{+\infty}  - \int 2x \left( - \frac{1}{\lambda}x \cdot \mathrm{exp}(-\lambda x) \right) \\
&= \left[ - \frac{1}{\lambda}x^2 \cdot \mathrm{exp}(-\lambda x) \right]_{0}^{+\infty}  - \left\[ \left[ \frac{1}{\lambda^2}2x \cdot \mathrm{exp}(-\lambda x) \right]_{0}^{+\infty} - \int 2 \left (\frac{1}{\lambda^2} \cdot \mathrm{exp}(-\lambda x)\right ) \right] \\
&= \left[ - \frac{x^2}{\lambda} \cdot \mathrm{exp}(-\lambda x) \right]_{0}^{+\infty}  - \left[ \left[ \frac{2x}{\lambda^2} \cdot \mathrm{exp}(-\lambda x) \right]_{0}^{+\infty} - \left[ - \frac{2}{\lambda^3} \cdot \mathrm{exp}(-\lambda x) \right]_{0}^{+\infty} \right] \\
&= \left[ \left( - \frac{x^2}{\lambda} - \frac{2x}{\lambda^2} - \frac{2}{\lambda^3} \right) \exp(-\lambda x)  \right]_{0}^{+\infty}\; .
\end{split}
$$

the second moment becomes

$$ \label{eq:second-moment-s3}
\begin{split}
\mathrm{E} [X^2] &= \lambda \left[ \left( - \frac{x^2}{\lambda} - \frac{2x}{\lambda^2} - \frac{2}{\lambda^3} \right) \exp(-\lambda x) \right]_{0}^{+\infty} \\
&= \lambda \left[ \lim_{x \to \infty} \left( - \frac{x^2}{\lambda} - \frac{2x}{\lambda^2} - \frac{2}{\lambda^3} \right) \exp(-\lambda x) - \left( 0 - 0 - \frac{2}{\lambda^3} \right) \exp(-\lambda \cdot 0) \right] \\
&= \lambda \left[ 0 + \frac{2}{\lambda^3} \right] \\
&= \frac{2}{\lambda^2} \; .
\end{split}
$$

Plugging \eqref{eq:second-moment-s3} and \eqref{eq:exp-mean-ref} into \eqref{eq:var2}, we have:

$$ \label{eq:exp-var-2}
\begin{split}
\mathrm{Var}(X) &= \mathrm{E}\left[ X^2 \right] - \mathrm{E}\left[ X \right]^2  \\
&= \frac{2}{\lambda^2} - \left ( \frac{1}{\lambda} \right)^2 \\
&= \frac{2}{\lambda^2} - \frac{1}{\lambda^2} \\
&= \frac{1}{\lambda^2} \; .
\end{split}
$$