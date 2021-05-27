---
layout: proof
mathjax: true

author: "Kenneth Petrykowski"
affiliation: "KU Leuven"
e_mail: "kenneth.petrykowski@gmail.com"
date: 2020-10-13 01:30:00

title: "Moments of the chi-squared distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Chi-squared distribution"
theorem: "Moments"

sources:
  - authors: "Robert V. Hogg, Joseph W. McKean, Allen T. Craig"
    year: 2018
    title: "The χ2-Distribution"
    in: "Introduction to Mathematical Statistics"
    pages: "Pearson, Boston, 2019, p. 179, eq. 3.3.8"
    url: "https://www.pearson.com/store/p/introduction-to-mathematical-statistics/P100000843744"

proof_id: "P175"
shortcut: "chi2-mom"
username: "kjpetrykowski"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [chi-squared distribution](/D/chi2):

$$ \label{eq:chi2}
X \sim \chi^{2}(k) \; .
$$

If $m > -k/2$, then $E(X^{m})$ exists and is equal to:

$$ \label{eq:chi2-mom}
\mathrm{E}(X^{m}) = \frac{2^{m} \Gamma\left( \frac{k}{2}+m \right)}{\Gamma\left( \frac{k}{2} \right)} \; .
$$


**Proof:** Combining the [definition of the $m$-th raw moment](/D/mom-raw) with the [probability density function of the chi-squared distribution](/P/chi2-pdf), we have:

$$ \label{eq:chi2-mom-int}
\mathrm{E}(X^{m}) = \int_{0}^{\infty} \frac{1}{\Gamma\left( \frac{k}{2} \right) 2^{k/2}} \, x^{(k/2)+m-1} \, e^{-x/2} \mathrm{d}x \; . 
$$

Now define a new variable $u = x/2$. As a result, we obtain:

$$ \label{eq:chi-2-mom-int-u}
\mathrm{E}(X^{m}) = \int_{0}^{\infty} \frac{1}{\Gamma\left( \frac{k}{2} \right) 2^{(k/2)-1}} \, 2^{(k/2)+m-1} \, u^{(k/2)+m-1} \, e^{-u} \mathrm{d}u \; .
$$

This leads to the desired result when $m > -k/2$. Observe that, if $m$ is a nonnegative integer, then $m > -k/2$ is always true. Therefore, all [moments](/D/mom) of a [chi-squared distribution](/D/chi2) exist and the $m$-th raw moment is given by the foregoing equation.