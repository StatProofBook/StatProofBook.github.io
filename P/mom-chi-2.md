---

layout: proof
mathjax: true

author: "Kenneth Petrykowski"
affiliation: "Ku Leuven"
e_mail: "kenneth.petrykowski@gmail.com"
date: 2020-10-13 01:30:00

title: "M-th moment of chi square distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Chi-square distribution"
theorem: "M-th moment of chi square distribution"

sources:
 - authors: "Robert V. Hogg, Joseph W. McKean, Allen T. Craig"
   year: 2018
   title: "The χ2-Distribution"
   in: "Introduction to Mathematical Statistics"
   pages: "Pearson, Boston, 2019, p. 179, eq. 3.3.8"
   url: "https://www.pearson.com/store/p/introduction-to-mathematical-statistics/P100000843744"



proof_id: "P172"
shortcut: "mom-chi-2"
username: "kjpetrykowski"
---


**Theorem:** Let $X$ have a $\chi^{2}(k)$ distribution. If $m > -k/2$, then $E(X^{m})$ exists and is equal to:
$$ \label{eq:chi-2-mom}
{ {E}(X^{m}) =\frac {2^{m} \Gamma (\frac{k}{2} +m)}{\Gamma(\frac{k}{2})}\;,}$$  if  $m  >  -k/2$. \

**Proof:** Observe that:

$$ \label{eq:chi-2-mom-int}
{ {E}(X^{m}) = \int_{0}^{\infty} {\frac {1}{\Gamma (\frac{k}{2}) 2^{k/2}}}\;x^{(k/2)+m-1}e^{-x/2}dx\;}. 
$$

Now set a new variable $u$ that $u=x/2$. As a result, we obtain:

$$ \label{eq:chi-2-mom-int-u}
{ {E}(X^{m}) = \int_{0}^{\infty} {\frac {1}{\Gamma (\frac{k}{2}) 2^{(k/2)-1}}}\;2^{(k/2)+m-1}u^{(k/2)+m-1}e^{-u}du\;}. 
$$

This leads to the desired result when $m$ $> -\frac{k}{2}$ \
Observe that if $m$ is a nonnegative integer, then $m$ $> -\frac{k}{2}$ is always true. Therefore,
all moments of a chi-square distribution exist and the m-th moment is given by this foregoing equation.