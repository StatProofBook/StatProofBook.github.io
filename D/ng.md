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


**Definition**: Let $X$ be an $n \times 1$ random vector and let $Y$ be a positive random variable. Then, $X$ and $Y$ are said to follow a normal-gamma distribution

$$ \label{eq:ng}
X,Y \sim \mathrm{NG}(\mu, \Lambda, a, b) \; ,
$$

if and only if their joint probability density function is given by

$$ \label{eq:ng-pdf}
f_{X,Y}(x,y) = \mathcal{N}(x; \mu, (y \Lambda)^{-1}) \cdot \mathrm{Gam}(y; a, b)
$$

where $\mathrm{N}(x; \mu, \Sigma)$ is the [probability density function of the multivariate normal distribution](/P/mvn-pdf.html) with mean $\mu$ and covariance $\Sigma$ and $\mathrm{Gam}(x; a, b)$ is the [probability density function of the gamma distribution](/P/gam-pdf.html) with shape $a$ and rate $b$.