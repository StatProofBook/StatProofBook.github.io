---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-11-06 13:41:00

title: "Two-way analysis of variance"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Analysis of variance"
definition: "Two-way ANOVA"

sources:
  - authors: "Bortz, Jürgen"
    year: 1977
    title: "Zwei- und mehrfaktorielle Varianzanalyse"
    in: "Lehrbuch der Statistik. Für Sozialwissenschaftler"
    pages: "ch. 12.2, pp. 538ff."
    url: "https://books.google.de/books?id=lNCyBgAAQBAJ"
  - authors: "ttd"
    year: 2021
    title: "Proof on SSAB/s2~chi2(I-1)(J-1) under the null hypothesis HAB: dij=0 for i=1,...,I and j=1,...,J"
    in: "StackExchange CrossValidated"
    pages: "retrieved on 2022-11-06"
    url: "https://stats.stackexchange.com/questions/545807/proof-on-ss-ab-sigma2-sim-chi2-i-1j-1-under-the-null-hypothesis"

def_id: "D182"
shortcut: "anova2"
username: "JoramSoch"
---


**Definition:** Let there be two factors $A$ and $B$ with levels $i = 1, \ldots, a$ and $j = 1, \ldots, b$ that are used to group measurements $y_{ijk} \in \mathbb{R}$ from distinct objects $k = 1, \ldots, n_{ij}$ into $a \cdot b$ categories $(i,j) \in \left\lbrace 1, \ldots, a \right\rbrace \times \left\lbrace 1, \ldots, b \right\rbrace$.

Then, in two-way analysis of variance (ANOVA), these measurements are assumed to come from [normal distributions](/D/norm)

$$ \label{eq:anova2-p1}
y_{ijk} \sim \mathcal{N}(\mu_{ij}, \sigma^2) \quad \text{for all} \quad i = 1, \ldots, a, \quad j = 1, \ldots, b, \quad \text{and} \quad k = 1, \dots, n_{ij}
$$

with

$$ \label{eq:anova2-p2}
\mu_{ij} = \mu + \alpha_i + \beta_j + \gamma_{ij}
$$

where

* $\mu$ is called the "grand mean";

* $\alpha_i$ is the additive "main effect" of the $i$-th level of factor $A$;

* $\beta_j$ is the additive "main effect" of the $j$-th level of factor $B$;

* $\gamma_{ij}$ is the non-additive "interaction effect" of category $(i,j)$;

* $\mu_{ij}$ is the [expected value](/D/mean) in category $(i,j)$; and

* $\sigma^2$ is common [variance](/D/var) across all categories.

Alternatively, the model may be written as

$$ \label{eq:anova2-alt}
\begin{split}
y_{ijk} &= \mu + \alpha_i + \beta_j + \gamma_{ij} + \varepsilon_{ijk} \\
\varepsilon_{ijk} &\sim \mathcal{N}(0, \sigma^2)
\end{split}
$$

where $\varepsilon_{ijk}$ is the [error term](/D/slr) corresponding to observation $k$ belonging to the $i$-th level of $A$ and the $j$-th level of $B$.

As the two-way ANOVA model is underdetermined, the parameters of the model are additionally subject to the constraints

$$ \label{eq:anova2-cons}
\begin{split}
\sum_{i=1}^{a} w_{ij} \alpha_i &= 0 \quad \text{for all} \quad j = 1, \ldots, b \\
\sum_{j=1}^{b} w_{ij} \beta_j &= 0 \quad \text{for all} \quad i = 1, \ldots, a \\
\sum_{i=1}^{a} w_{ij} \gamma_{ij} &= 0 \quad \text{for all} \quad j = 1, \ldots, b \\
\sum_{j=1}^{b} w_{ij} \gamma_{ij} &= 0 \quad \text{for all} \quad i = 1, \ldots, a
\end{split}
$$

where the weights are $w_{ij} = n_{ij}/n$ and the total sample size is $n = \sum_{i=1}^{a} \sum_{j=1}^{b} n_{ij}$.