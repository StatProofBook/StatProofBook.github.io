---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-11-06 10:23:00

title: "One-way analysis of variance"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Analysis of variance"
definition: "One-way ANOVA"

sources:
  - authors: "Bortz, Jürgen"
    year: 1977
    title: "Einfaktorielle Varianzanalyse"
    in: "Lehrbuch der Statistik. Für Sozialwissenschaftler"
    pages: "ch. 12.1, pp. 528ff."
    url: "https://books.google.de/books?id=lNCyBgAAQBAJ"
  - authors: "Denziloe"
    year: 2018
    title: "Derive the distribution of the ANOVA F-statistic under the alternative hypothesis"
    in: "StackExchange CrossValidated"
    pages: "retrieved on 2022-11-06"
    url: "https://stats.stackexchange.com/questions/355594/derive-the-distribution-of-the-anova-f-statistic-under-the-alternative-hypothesi"

def_id: "D181"
shortcut: "anova1"
username: "JoramSoch"
---


**Definition:** Consider measurements $y_{ij} \in \mathbb{R}$ from disctinct objects $j = 1, \ldots, n_i$ in separate groups $i = 1, \ldots, k$.

Then, in one-way analysis of variance (ANOVA), these measurements are assumed to come from [normal distributions](/D/norm)

$$ \label{eq:anova1}
y_{ij} \sim \mathcal{N}(\mu_i, \sigma^2) \quad \text{for all} \quad i = 1, \ldots, k \quad \text{and} \quad j = 1, \dots, n_i
$$

where

* $\mu_i$ is the [expected value](/D/mean) in group $i$ and

* $\sigma^2$ is the common [variance](/D/var) across groups.

Alternatively, the model may be written as

$$ \label{eq:anova1-alt}
\begin{split}
y_{ij} &= \mu_i + \varepsilon_{ij} \\
\varepsilon_{ij} &\overset{\mathrm{i.i.d.}}{\sim} \mathcal{N}(0, \sigma^2)
\end{split}
$$

where $\varepsilon_{ij}$ is the [error term](/D/slr) belonging to observation $j$ in category $i$ and $\varepsilon_{ij}$ are the [independent and identically distributed](/D/iid).