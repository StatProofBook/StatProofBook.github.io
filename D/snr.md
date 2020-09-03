---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-02-25 12:01:00

title: "Signal-to-noise ratio"
chapter: "Model Selection"
section: "Goodness-of-fit measures"
topic: "Signal-to-noise ratio"
definition: "Definition"

sources:
  - authors: "Soch J, Allefeld C"
    year: 2018
    title: "MACS – a new SPM toolbox for model assessment, comparison and selection"
    in: "Journal of Neuroscience Methods"
    pages: "vol. 306, pp. 19-31, eq. 6"
    url: "https://www.sciencedirect.com/science/article/pii/S0165027018301468"
    doi: "10.1016/j.jneumeth.2018.05.017"

def_id: "D22"
shortcut: "snr"
username: "JoramSoch"
---


**Definition:** Let there be a [linear regression model](/D/mlr) with [independent](/D/ind) observations

$$ \label{eq:mlr}
y = X\beta + \varepsilon, \; \varepsilon_i \overset{\mathrm{i.i.d.}}{\sim} \mathcal{N}(0, \sigma^2)
$$

with measured data $y$, known design matrix $X$ as well as unknown regression coefficients $\beta$ and noise variance $\sigma^2$.

Given estimated [regression coefficients](/P/mlr-mle) $\hat{\beta}$ and [residual variance](/D/resvar) $\hat{\sigma}^2$, the signal-to-noise ratio (SNR) is defined as the ratio of estimated signal variance to estimated noise variance:

$$ \label{eq:SNR}
\mathrm{SNR} = \frac{\mathrm{Var}(X\hat{\beta})}{\hat{\sigma}^2} \; .
$$