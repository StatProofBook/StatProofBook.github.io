---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-11-16 16:01:00

title: "Partition of sums of squares in two-way analysis of variance"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Analysis of variance"
theorem: "Sums of squares in two-way ANOVA"

sources:
  - authors: "Nandy, Siddhartha"
    year: 2018
    title: "Two-Way Analysis of Variance"
    in: "Stat 512: Applied Regression Analysis"
    pages: "Purdue University, Summer 2018, Ch. 19"
    url: "https://www.stat.purdue.edu/~snandy/stat512/topic7.pdf"
  - authors: "Wikipedia"
    year: 2022
    title: "Analysis of variance"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2022-11-15"
    url: "https://en.wikipedia.org/wiki/Analysis_of_variance#Partitioning_of_the_sum_of_squares"

proof_id: "P379"
shortcut: "anova2-pss"
username: "JoramSoch"
---


**Theorem:** Given [two-way analysis of variance](/D/anova2),

$$ \label{eq:anova2}
y_{ijk} = \mu + \alpha_i + \beta_j + \gamma_{ij} + \varepsilon_{ijk}, \; \varepsilon_{ijk} \overset{\mathrm{i.i.d.}}{\sim} \mathcal{N}(0, \sigma^2)
$$

sums of squares can be partitioned as follows

$$ \label{eq:anova2-pss}
\mathrm{SS}_\mathrm{tot} = \mathrm{SS}_{A} + \mathrm{SS}_{B} + \mathrm{SS}_{A \times B} + \mathrm{SS}_\mathrm{res}
$$

where $\mathrm{SS} _\mathrm{tot}$ is the [total sum of squares](/D/tss), $\mathrm{SS} _{A}$, $\mathrm{SS} _{B}$ and $\mathrm{SS} _{A \times B}$ are [treatment](/D/trss) and [interaction sum of squares](/D/iass) (summing into the [explained sum of squares](/D/ess)) and $\mathrm{SS} _\mathrm{res}$ is the [residual sum of squares](/D/rss).


**Proof:** The [total sum of squares](/D/tss) for [two-way ANOVA](/D/anova2) is given by

$$ \label{eq:anova2-tss}
\mathrm{SS}_\mathrm{tot} = \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (y_{ijk} - \bar{y}_{\bullet \bullet \bullet})^2
$$

where $\bar{y} _{\bullet \bullet \bullet}$ is the mean across all values $y_{ijk}$. This can be rewritten as

$$ \label{eq:anova2-pss-s1}
\begin{split}
\sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (y_{ijk} - \bar{y}_{\bullet \bullet \bullet})^2 = \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} & \left[ (y_{ijk} - \bar{y}_{i j \bullet}) + (\bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet \bullet \bullet}) + (\bar{y}_{\bullet j \bullet} - \bar{y}_{\bullet \bullet \bullet}) + \right. \\
\\ & \left. (\bar{y}_{i j \bullet} - \bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet j \bullet} + \bar{y}_{\bullet \bullet \bullet}) \right]^2 \\
\end{split}
$$

It [can be shown](/P/anova2-cochran) that the following sums are all zero:

$$ \label{eq:anova2-pss-s2}
\begin{split}
\sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (y_{ijk} - \bar{y}_{i j \bullet}) &= 0 \\
\sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (\bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet \bullet \bullet}) &= 0 \\
\sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (\bar{y}_{\bullet j \bullet} - \bar{y}_{\bullet \bullet \bullet}) &= 0 \\
\sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (\bar{y}_{i j \bullet} - \bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet j \bullet} + \bar{y}_{\bullet \bullet \bullet}) &= 0 \; .
\end{split}
$$

This means that the sum in \eqref{eq:anova2-pss-s1} reduces to

$$ \label{eq:anova2-pss-s3}
\begin{split}
\sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (y_{ijk} - \bar{y}_{\bullet \bullet \bullet})^2 = \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} & \left[ (y_{ijk} - \bar{y}_{i j \bullet})^2 + (\bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet \bullet \bullet})^2 + (\bar{y}_{\bullet j \bullet} - \bar{y}_{\bullet \bullet \bullet})^2 + \right. \\
\\ & \left. (\bar{y}_{i j \bullet} - \bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet j \bullet} + \bar{y}_{\bullet \bullet \bullet})^2 \right] \\
= \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} & (y_{ijk} - \bar{y}_{i j \bullet})^2 + \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (\bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet \bullet \bullet})^2 + \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (\bar{y}_{\bullet j \bullet} - \bar{y}_{\bullet \bullet \bullet})^2 \\
\sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} & (\bar{y}_{i j \bullet} - \bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet j \bullet} + \bar{y}_{\bullet \bullet \bullet})^2 \; .
\end{split}
$$

With the [treatment sums of squares](/D/trss)

$$ \label{eq:anova2-trss}
\begin{split}
\mathrm{SS}_A &= \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (\bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet \bullet \bullet})^2 \\
\mathrm{SS}_B &= \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (\bar{y}_{\bullet j \bullet} - \bar{y}_{\bullet \bullet \bullet})^2 \; ,
\end{split}
$$

the [interaction sum of squares](/D/iass)

$$ \label{eq:anova2-iass}
\mathrm{SS}_\mathrm{A \times B} = \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (\bar{y}_{i j \bullet} - \bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet j \bullet} + \bar{y}_{\bullet \bullet \bullet})^2
$$

and the [residual sum of squares](/D/rss) for [two-way ANOVA](/D/anova2)

$$ \label{eq:anova2-rss}
\mathrm{SS}_\mathrm{res} = \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (y_{ijk} - \bar{y}_{i j \bullet})^2 \; ,
$$

we finally have:

$$ \label{eq:anova2-pss-qed}
\mathrm{SS}_\mathrm{tot} = \mathrm{SS}_{A} + \mathrm{SS}_{B} + \mathrm{SS}_{A \times B} + \mathrm{SS}_\mathrm{res} \; .
$$