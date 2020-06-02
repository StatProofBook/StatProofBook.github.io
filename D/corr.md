---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-06-02 20:34:00

title: "Correlation"
chapter: "General Theorems"
section: "Probability theory"
topic: "Correlation"
definition: "Definition"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Correlation and dependence"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-02-06"
    url: "https://en.wikipedia.org/wiki/Correlation_and_dependence#Pearson's_product-moment_coefficient"

def_id: "D71"
shortcut: "corr"
username: "JoramSoch"
---


**Definition:** The correlation of two [random variables](/D/rvar) $X$ and $Y$, also called Pearson product-moment correlation coefficient (PPMCC), is defined as the ratio of the [covariance](/D/cov) of $X$ and $Y$ relative to the product of their [standard deviations](/D/std):

$$ \label{eq:corr}
\mathrm{Corr}(X,Y) = \frac{\sigma_{XY}}{\sigma_X \sigma_Y} = \frac{\mathrm{Cov}(X,Y)}{\sqrt{\mathrm{Var}(X)} \sqrt{\mathrm{Var}(Y)}} = \frac{\mathrm{E}\left[ (X-\mathrm{E}[X]) (Y-\mathrm{E}[Y]) \right]}{\sqrt{\mathrm{E}\left[ (X-\mathrm{E}[X])^2 \right]} \sqrt{\mathrm{E}\left[ (Y-\mathrm{E}[Y])^2 \right]}} \; .
$$