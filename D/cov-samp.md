---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-04-21 06:53:00

title: "Sample covariance"
chapter: "General Theorems"
section: "Probability theory"
topic: "Covariance"
definition: "Sample covariance"

sources:
  - authors: "Wikipedia"
    year: 2021
    title: "Covariance"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-05-20"
    url: "https://en.wikipedia.org/wiki/Covariance#Calculating_the_sample_covariance"

def_id: "D144"
shortcut: "cov-samp"
username: "ciaranmci"
---


**Definition:** Let $x = \left\lbrace x_1, \ldots, x_n \right\rbrace$ and $y = \left\lbrace y_1, \ldots, y_n \right\rbrace$ be [samples](/D/samp) from [random variables](/D/rvar) $X$ and $Y$. Then, the sample covariance of $x$ and $y$ is given by

$$ \label{eq:cov-samp}
\hat{\sigma}_{xy} = \frac{1}{n} \sum_{i=1}^{n} (x_i - \bar{x}) (y_i - \bar{y})
$$

and the unbiased sample covariance of $x$ and $y$ is given by

$$ \label{eq:cov-samp-unb}
s_{xy} = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x}) (y_i - \bar{y})
$$

where $\bar{x}$ and $\bar{y}$ are the [sample means](/D/mean-samp).