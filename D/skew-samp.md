---
layout: definition
mathjax: true

author: "Thomas J. Faulkenberry"
affiliation: "Tarleton State University"
e_mail: "faulkenberry@tarleton.edu"
date: 2023-10-30 12:00:00

title: "Sample skewness"
chapter: "General Theorems"
section: "Probability theory"
topic: "Skewness"
definition: "Sample skewness"

sources:
  - authors: "Joanes, D. N. and Gill, C. A."
    year: 1998
    title: "Comparing measures of sample skewness and kurtosis"
    in: "The Statistician"
    pages: "vol. 47, part 1, pp. 183-189"
    url: "https://www.jstor.org/stable/2988433"

def_id: "D190"
shortcut: "skew-samp"
username: "tomfaulkenberry"
---


**Definition:** Let $x = \left\lbrace x_1, \ldots, x_n \right\rbrace$ be a [sample](/D/samp) from a [random variable](/D/rvar) $X$. Then, the sample skewness of $x$ is given by

$$ \label{eq:skew-samp}
\hat{s} = \frac{\frac{1}{n}\sum_{i=1}^n (x_i-\bar{x})^3}{\left[\frac{1}{n}\sum_{i=1}^n(x_i-\bar{x})^2\right]^{3/2}} \; ,
$$

where $\bar{x}$ is the [sample mean](/D/mean-samp).
