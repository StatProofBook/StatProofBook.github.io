---
layout: definition
mathjax: true

author: "Kenneth Petrykowski"
affiliation: "KU Leuven"
e_mail: "kenneth.petrykowski@gmail.com"
date: 2020-10-13 01:20:00

title: "Chi-squared distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Chi-squared distribution"
definition: "Definition"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Chi-square distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-10-12"
    url: "https://en.wikipedia.org/wiki/Chi-square_distribution#Definitions"
  - authors: "Robert V. Hogg, Joseph W. McKean, Allen T. Craig"
    year: 2018
    title: "The Chi-Squared-Distribution"
    in: "Introduction to Mathematical Statistics"
    pages: "Pearson, Boston, 2019, p. 178, eq. 3.3.7"
    url: "https://www.pearson.com/store/p/introduction-to-mathematical-statistics/P100000843744"

def_id: "D100"
shortcut: "chi2"
username: "kjpetrykowski"
---


**Definition:** Let $X_{1}, ..., X_{k}$ be [independent](/D/ind) [random variables](/D/rvar) where each of them is following a [standard normal distribution](/D/snorm):

$$ \label{eq:snorm}
X_{i} \sim \mathcal{N}(0,1) \quad \text{for} \quad i = 1, \ldots, n \; .
$$

Then, the sum of their squares follows a chi-squared distribution with $k$ degrees of freedom:

$$\label{eq:chi2}
Y = \sum_{i=1}^{k} X_{i}^{2} \sim \chi^{2}(k) \quad \text{where} \quad k > 0 \; .
$$

The [probability density function of the chi-squared distribution](/P/chi2-pdf) with $k$ degress of freedom is

$$ \label{eq:chi2-pdf}
\chi^{2}(x; k) = \frac{1}{2^{k/2}\Gamma (k/2)} \, x^{k/2-1} \, e^{-x/2}
$$

where $k > 0$ and the density is zero if $x \leq 0$.