---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-12-14 13:14:00

title: "Interaction sum of squares"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Analysis of variance"
definition: "Interaction sum of squares"

sources:
  - authors: "Nandy, Siddhartha"
    year: 2018
    title: "Two-Way Analysis of Variance"
    in: "Stat 512: Applied Regression Analysis"
    pages: "Purdue University, Summer 2018, Ch. 19"
    url: "https://www.stat.purdue.edu/~snandy/stat512/topic7.pdf"

def_id: "D184"
shortcut: "iass"
username: "JoramSoch"
---


**Definition:** Let there be an analysis of variance (ANOVA) model with [two](/D/anova2) or [more](/D/anovan) factors influencing the measured data $y$ (here, using the [standard formulation](/P/anova2-pss) of [two-way ANOVA](/D/anova2)):

$$ \label{eq:anova}
y_{ijk} = \mu + \alpha_i + \beta_j + \gamma_{ij} + \varepsilon_{ijk}, \; \varepsilon_{ijk} \overset{\mathrm{i.i.d.}}{\sim} \mathcal{N}(0, \sigma^2) \; .
$$

Then, the interaction sum of squares is defined as the [explained sum of squares](/D/ess) (ESS) for each interaction, i.e. as the sum of squared deviations of the average for each cell from the average across all observations, controlling for the [treatment sums of squares](/D/trss) of the corresponding factors:

$$ \label{eq:iass}
\begin{split}
\mathrm{SS}_\mathrm{A \times B} &= \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} ([\bar{y}_{i j \bullet} - \bar{y}_{\bullet \bullet \bullet}] - [\bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet \bullet \bullet}] - [\bar{y}_{\bullet j \bullet} - \bar{y}_{\bullet \bullet \bullet}])^2 \\
&= \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (\bar{y}_{i j \bullet} - \bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet j \bullet} + \bar{y}_{\bullet \bullet \bullet})^2 \; .
\end{split}
$$

Here, $\bar{y}\_{i j \bullet}$ is the mean for the $(i,j)$-th cell (out of $a \times b$ cells), computed from $n\_{ij}$ values $y\_{ijk}$, $\bar{y}\_{i \bullet \bullet}$ and $\bar{y}\_{\bullet j \bullet}$ are the level means for the two factors and and $\bar{y}\_{\bullet \bullet \bullet}$ is the mean across all values $y\_{ijk}$.