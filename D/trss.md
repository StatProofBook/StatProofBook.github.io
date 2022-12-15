---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-12-14 13:01:00

title: "Treatment sum of squares"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Analysis of variance"
definition: "Treatment sum of squares"

sources:
  - authors: "Wikipedia"
    year: 2022
    title: "Analysis of variance"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2022-11-15"
    url: "https://en.wikipedia.org/wiki/Analysis_of_variance#Partitioning_of_the_sum_of_squares"

def_id: "D183"
shortcut: "trss"
username: "JoramSoch"
---


**Definition:** Let there be an analysis of variance (ANOVA) model with [one](/D/anova1), [two](/D/anova2) or [multiple](/D/anovan) factors influencing the measured data $y$ (here, using the [reparametrized version](/P/anova1-repara) of [one-way ANOVA](/D/anova1)):

$$ \label{eq:anova}
y_{ij} = \mu + \delta_i + \varepsilon_{ij}, \; \varepsilon_{ij} \overset{\mathrm{i.i.d.}}{\sim} \mathcal{N}(0, \sigma^2) \; .
$$

Then, the treatment sum of squares is defined as the [explained sum of squares] (ESS) for each main effect, i.e. as the sum of squared deviations of the average for each level of the factor, from the average across all observations:

$$ \label{eq:trss}
\mathrm{SS}_\mathrm{treat} = \sum_{i=1}^{k} \sum_{j=1}^{n_i} (\bar{y}_i - \bar{y})^2 \; .
$$

Here, $\bar{y}_i$ is the mean for the $i$-th level of the factor (out of $k$ levels), computed from $n_i$ values $y_{ij}$, and $\bar{y}$ is the mean across all values $y_{ij}$.