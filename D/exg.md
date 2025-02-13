---
layout: definition
mathjax: true

author: "Thomas J. Faulkenberry"
affiliation: "Tarleton State University"
e_mail: "faulkenberry@tarleton.edu"
date: 2023-04-18 12:00:00

title: "ex-Gaussian distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "ex-Gaussian distribution"
definition: "Definition"

sources:
  - authors: "Luce, R. D."
    year: 1986
    title: "Response Times: Their Role in Inferring Elementary Mental Organization"
    pages: "35-36"
    url: "https://global.oup.com/academic/product/response-times-9780195036428"

def_id: "D187"
shortcut: "exg"
username: "tomfaulkenberry"
---


**Definition:** Let $A$ be a [random variable](/D/rvar) that is [normally distributed](/D/norm) with mean $\mu$ and variance $\sigma^2$, and let $B$ be a random variable that is [exponentially distributed](/D/exp) with rate $\lambda$. Suppose further that $A$ and $B$ are [independent](/D/ind). Then the sum $X=A+B$ is said to have an exponentially-modified Gaussian (i.e., ex-Gaussian) distribution, with parameters $\mu$, $\sigma$, and $\lambda$; that is,

$$ \label{eq:exg}
X \sim \mathrm{ex-Gaussian}(\mu, \sigma, \lambda) \; ,
$$

where $\mu \in \mathbb{R}$, $\sigma>0$, and $\lambda > 0$.

