---
layout: proof
mathjax: true

author: "Kenneth Petrykowski"
affiliation: "KU Leuven"
e_mail: "kenneth.petrykowski@gmail.com"
date: 2020-10-13 01:30:00

title: "Raw moments of the chi-squared distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Chi-squared distribution"
theorem: "Raw moments"

sources:
  - authors: "Robert V. Hogg, Joseph W. McKean, Allen T. Craig"
    year: 2018
    title: "The χ2-Distribution"
    in: "Introduction to Mathematical Statistics"
    pages: "Pearson, Boston, 2019, p. 179, eq. 3.3.8"
    url: "https://www.pearson.com/store/p/introduction-to-mathematical-statistics/P100000843744"

proof_id: "P175"
shortcut: "chi2-momraw"
username: "kjpetrykowski"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [chi-squared distribution](/D/chi2) with $k$ degrees of freedom:

$$ \label{eq:chi2}
X \sim \chi^{2}(k) \; .
$$

Then, if $m > -k/2$, the [raw moment](/D/mom-raw) $\mathrm{E}(X^{m})$ exists and is equal to:

$$ \label{eq:chi2-momraw}
\mathrm{E}(X^{m}) = 2^m \, \frac{\Gamma\left( \frac{k}{2}+m \right)}{\Gamma\left( \frac{k}{2} \right)} \; .
$$


**Proof:** Combining the [definition of the raw moment](/D/mom-raw) with the [probability density function of the chi-squared distribution](/P/chi2-pdf), we have:

$$ \label{eq:chi2-momraw-int}
\begin{split}
\mathrm{E}(X^{m}) &= \int_{0}^{\infty} x^m \frac{1}{2^{k/2} \Gamma\left( \frac{k}{2} \right)} \, x^{k/2-1} \, \exp \left[ -x/2 \right] \, \mathrm{d}x \\
&= \frac{1}{2^{k/2} \Gamma\left( \frac{k}{2} \right)} \int_{0}^{\infty} x^{(k/2)+m-1} \, \exp \left[ -x/2 \right] \, \mathrm{d}x \; .
\end{split}
$$

Now, we substitute $u = x/2$, such that $x = 2u$. As a result, we obtain:

$$ \label{eq:chi2-momraw-int-u}
\begin{split}
\mathrm{E}(X^{m}) &= \frac{1}{2^{k/2} \Gamma\left( \frac{k}{2} \right)} \int_{0}^{\infty} 2^{(k/2)+m-1} \, u^{(k/2)+m-1} \, \exp[-u] \, \mathrm{d}(2u) \\
&= \frac{2^{(k/2)+m}}{2^{k/2} \Gamma\left( \frac{k}{2} \right)} \int_{0}^{\infty} u^{(k/2)+m-1} \, \exp[-u] \, \mathrm{d}u \\
&= \frac{2^m}{\Gamma\left( \frac{k}{2} \right)} \int_{0}^{\infty} u^{(k/2)+m-1} \, \exp[-u] \, \mathrm{d}u \; .
\end{split}
$$

With the definition of the gamma function as

$$ \label{eq:gam-fct}
\Gamma(x) = \int_{0}^{\infty} t^{x-1} \, e^{-t} \, \mathrm{d}t, \; x > 0 \; ,
$$

this leads to the desired result when $m > -k/2$. Observe that, if $m$ is a non-negative integer, then $m > -k/2$ is always true. Therefore, all [moments](/D/mom) of a [chi-squared distribution](/D/chi2) exist and the $m$-th raw moment is given by the equation above.