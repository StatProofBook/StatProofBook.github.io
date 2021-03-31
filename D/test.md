---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-03-19 14:36:00

title: "Statistical hypothesis test"
chapter: "General Theorems"
section: "Frequentist statistics"
topic: "Hypothesis testing"
definition: "Statistical test"

sources:
  - authors: "Wikipedia"
    year: 2021
    title: "Statistical hypothesis testing"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-03-19"
    url: "https://en.wikipedia.org/wiki/Statistical_hypothesis_testing#The_testing_process"

def_id: "D130"
shortcut: "test"
username: "JoramSoch"
---


**Definition:** Let $y$ be a set of [measured data](/D/data). Then, a statistical hypothesis test consists of the following:

* an assumption about the [distribution](/D/dist) of the data, often expressed in terms of a [statistical model](/D/gm) $m$;

* a [null hypothesis](/D/h0) $H_0$ and an [alternative hypothesis](/D/h1) $H_1$ which make specific statements about the distribution of the data; 

* a [test statistic](/D/tstat) $T(Y)$ which is a function of the data and whose distribution under the [null hypothesis](/D/h0) is known;

* a [significance level](/D/alpha) $\alpha$ which imposes an upper bound on the [probability](/D/prob) of rejecting $H_0$, given that $H_0$ is true.

Procedurally, the statistical hypothesis test works as follows:

* Given the null hypothesis $H_0$ and the significance level $\alpha$, a [critical value](/D/cval) $t_\mathrm{crit}$ is determined which partitions the set of possible values of $T(Y)$ into "acceptance region" and "rejection region".

* Then, the observed [test statistic](/D/tstat) $t_\mathrm{obs} = T(y)$ is calculated from the actually measured data $y$. If it is in the rejection region, $H_0$ is rejected in favor of $H_1$. Otherwise, the test fails to reject $H_0$.