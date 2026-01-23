---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-01-27 14:28:00

title: "Normal-gamma distribution"
chapter: "Probability Distributions"
section: "Multivariate continuous distributions"
topic: "Normal-gamma distribution"
definition: "Definition"

sources:
  - authors: "Koch KR"
    year: 2007
    title: "Normal-Gamma Distribution"
    in: "Introduction to Bayesian Statistics"
    pages: "ch. 2.5.3, pp. 55-56, eq. 2.212"
    url: "https://www.springer.com/gp/book/9783540727231"
    doi: "10.1007/978-3-540-72726-2"

def_id: "D5"
shortcut: "ng"
username: "JoramSoch"
---


**Definition:** Let $X$ be an $n$-dimensional [random vector](/D/rvec) and let $Y$ be a positive [random variable](/D/rvar). Then, $X$ and $Y$ are said to follow a normal-gamma distribution

$$ \label{eq:ng}
X,Y \sim \mathrm{NG}(\mu, \Lambda, a, b) \; ,
$$

if the distribution of $X$ conditional on $Y$ is a [multivariate normal distribution](/D/mvn) with mean vector $\mu$ and covariance matrix $(y \Lambda)^{-1}$ and $Y$ follows a [gamma distribution](/D/gam) with shape parameter $a$ and rate parameter $b$:

$$ \label{eq:mvn-gam}
\begin{split}
X \vert Y &\sim \mathcal{N}(\mu, (Y \Lambda)^{-1}) \\
Y &\sim \mathrm{Gam}(a, b) \; .
\end{split}
$$

The $n \times n$ matrix $\Lambda$ is referred to as the [precision matrix](/D/precmat) of the normal-gamma distribution.