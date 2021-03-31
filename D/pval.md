---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-03-19 14:58:00

title: "p-value"
chapter: "General Theorems"
section: "Frequentist statistics"
topic: "Hypothesis testing"
definition: "p-value"

sources:
  - authors: "Wikipedia"
    year: 2021
    title: "Statistical hypothesis testing"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-03-19"
    url: "https://en.wikipedia.org/wiki/Statistical_hypothesis_testing#Definition_of_terms"

def_id: "D135"
shortcut: "pval"
username: "JoramSoch"
---


**Definition:** Let there be a [statistical test](/D/test) of the [null hypothesis](/D/h0) $H_0$ and the [alternative hypothesis](/D/h1) $H_1$ using the [test statistic](/D/tstat) $T(Y)$. Let $y$ be the [measured data](/D/data) and let $t_\mathrm{obs} = T(y)$ be the observed test statistic computed from $y$. Moreover, assume that $F_T(t)$ is the [cumulative distribution function](/D/cdf) (CDF) of the distribution of $T(Y)$ under $H_0$.

Then, the p-value is the probability of obtaining a test statistic more extreme than or as extreme as $t_\mathrm{obs}$, given that the null hypothesis $H_0$ is true:

* $p = F_T^{-1}(t_\mathrm{obs})$, if $H_1$ is a left-sided [one-tailed hypothesis](/D/hyp-tail);

* $p = 1 - F_T^{-1}(t_\mathrm{obs})$, if $H_1$ is a right-sided [one-tailed hypothesis](/D/hyp-tail);

* $p = 2 \cdot \min \left( \left[ F_T^{-1}(t_\mathrm{obs}), \, 1 - F_T^{-1}(t_\mathrm{obs}) \right] \right)$, if $H_1$ is a [two-tailed hypothesis](/D/hyp-tail).