---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-03-21 21:44:00

title: "Total sum of squares"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Multiple linear regression"
definition: "Total sum of squares"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Total sum of squares"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-03-21"
    url: "https://en.wikipedia.org/wiki/Total_sum_of_squares"

def_id: "D37"
shortcut: "tss"
username: "JoramSoch"
---


**Definition:** Let there be a [multiple linear regression with independent observations](/D/mlr) using measured data $y$ and design matrix $X$:

$$ \label{eq:mlr}
y = X\beta + \varepsilon, \; \varepsilon_i \overset{\mathrm{i.i.d.}}{\sim} \mathcal{N}(0, \sigma^2) \; .
$$

Then, the total sum of squares (TSS) is defined as the sum of squared deviations of the measured signal from the average signal:

$$ \label{eq:tss}
\mathrm{TSS} = \sum_{i=1}^n (y_i - \bar{y})^2 \quad \text{where} \quad \bar{y} = \frac{1}{n} \sum_{i=1}^n y_i \; .
$$