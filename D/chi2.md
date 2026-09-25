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


**Definition:** Let $Z_1, \ldots, Z_k$ be [independent](/D/ind) [random variables](/D/rvar) where each of them is following a [standard normal distribution](/D/snorm):

$$ \label{eq:snorm}
Z_i \sim \mathcal{N}(0,1) \quad \text{for} \quad i = 1, \ldots, n \; .
$$

Define the random variable $X$ as the sum of all squared $Z_i$:

$$ \label{eq:X}
X = \sum_{i=1}^{k} Z_i^2 \; .
$$

Then, the variable $X$ is said to follow a chi-squared distribution with $k$ [degrees of freedom](/D/dof):

$$ \label{eq:wish}
X \sim \chi^{2}(k)
$$

where $k > 0$.