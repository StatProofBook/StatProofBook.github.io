---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-03-27 23:41:00

title: "Mean squared error"
chapter: "General Theorems"
section: "Estimation theory"
topic: "Point estimates"
definition: "Mean squared error"

sources:
  - authors: "Wikipedia"
    year: 2022
    title: "Estimator"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2022-03-27"
    url: "https://en.wikipedia.org/wiki/Estimator#Mean_squared_error"

def_id: "D173"
shortcut: "mse"
username: "JoramSoch"
---


**Definition:** Let $\hat{\theta}$ be an [estimator](/D/est) of an unknown [parameter](/D/para) $\hat{\theta}$ based on measured [data](/D/data) $y$. Then, the mean squared error is defined as the [expected value](/D/mean) of the squared difference between the estimated value and the true value of the parameter:

$$ \label{eq:mse}
\mathrm{MSE} = \mathrm{E}_{\hat{\theta}}\left[ \left( \hat{\theta} - \theta \right)^2 \right] \; .
$$

where $\mathrm{E}_{\hat{\theta}}\left[ \cdot \right]$ is expectation calculated over all possible [samples](/D/samp) $y$ leading to values of $\hat{\theta}$.