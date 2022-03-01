---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-03-01 07:48:00

title: "Deviance information criterion"
chapter: "Model Selection"
section: "Classical information criteria"
topic: "Deviance information criterion"
definition: "Deviance"

sources:
  - authors: "Spiegelhalter DJ, Best NG, Carlin BP, Van Der Linde A"
    year: 2002
    title: "Bayesian measures of model complexity and fit"
    in: "Journal of the Royal Statistical Society, Series B: Statistical Methodology"
    pages: "vol. 64, iss. 4, pp. 583-639"
    url: "https://rss.onlinelibrary.wiley.com/doi/10.1111/1467-9868.00353"
    doi: "10.1111/1467-9868.00353"
  - authors: "Soch J, Allefeld C"
    year: 2018
    title: "MACS – a new SPM toolbox for model assessment, comparison and selection"
    in: "Journal of Neuroscience Methods"
    pages: "vol. 306, pp. 19-31, eqs. 10-12"
    url: "https://www.sciencedirect.com/science/article/pii/S0165027018301468"
    doi: "10.1016/j.jneumeth.2018.05.017"
  - authors: "Wikipedia"
    year: 2022
    title: "Deviance information criterion"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2022-03-01"
    url: "https://en.wikipedia.org/wiki/Deviance_information_criterion#Definition"

def_id: "D172"
shortcut: "dev"
username: "JoramSoch"
---


**Definition:** Let there be a [generative model](/D/gm) $m$ describing measured data $y$ using model parameters $\theta$. Then, the deviance of $m$ is a function of $\theta$ which multiplies the [log-likelihood function](/D/llf) with $-2$:

$$ \label{eq:dev}
D(\theta) = -2 \log p(y|\theta,m) \; .
$$

The deviance function serves the definition of the [deviance information criterion](/D/dic).