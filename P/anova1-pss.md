---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-11-15 16:59:00

title: "Partition of sums of squares in one-way analysis of variance"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Analysis of variance"
theorem: "Sums of squares in one-way ANOVA"

sources:
  - authors: "Wikipedia"
    year: 2022
    title: "Analysis of variance"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2022-11-15"
    url: "https://en.wikipedia.org/wiki/Analysis_of_variance#Partitioning_of_the_sum_of_squares"

proof_id: "P376"
shortcut: "anova1-pss"
username: "JoramSoch"
---


**Theorem:** Given [one-way analysis of variance](/D/anova1),

$$ \label{eq:anova1}
y_{ij} = \mu_i + \varepsilon_{ij}, \; \varepsilon_{ij} \overset{\mathrm{i.i.d.}}{\sim} \mathcal{N}(0, \sigma^2)
$$

sums of squares can be partitioned as follows

$$ \label{eq:anova1-pss}
\mathrm{SS}_\mathrm{tot} = \mathrm{SS}_\mathrm{treat} + \mathrm{SS}_\mathrm{res}
$$

where $\mathrm{SS} _\mathrm{tot}$ is the [total sum of squares](/D/tss), $\mathrm{SS} _\mathrm{treat}$ is the [treatment sum of squares](/D/trss) (equivalent to [explained sum of squares](/D/ess)) and $\mathrm{SS} _\mathrm{res}$ is the [residual sum of squares](/D/rss).


**Proof:** The [total sum of squares](/D/tss) for [one-way ANOVA](/D/anova1) is given by

$$ \label{eq:anova1-tss}
\mathrm{SS}_\mathrm{tot} = \sum_{i=1}^{k} \sum_{j=1}^{n_i} (y_{ij} - \bar{y})^2
$$

where $\bar{y}$ is the mean across all values $y_{ij}$. This can be rewritten as

$$ \label{eq:anova1-pss-s1}
\begin{split}
\sum_{i=1}^{k} \sum_{j=1}^{n_i} (y_{ij} - \bar{y})^2 &= \sum_{i=1}^{k} \sum_{j=1}^{n_i} \left[ (y_{ij} - \bar{y}_i) + (\bar{y}_i - \bar{y}) \right]^2 \\
&= \sum_{i=1}^{k} \sum_{j=1}^{n_i} \left[ (y_{ij} - \bar{y}_i)^2 + (\bar{y}_i - \bar{y})^2 + 2 (y_{ij} - \bar{y}_i) (\bar{y}_i - \bar{y}) \right] \\
&= \sum_{i=1}^{k} \sum_{j=1}^{n_i} (y_{ij} - \bar{y}_i)^2 + \sum_{i=1}^{k} \sum_{j=1}^{n_i} (\bar{y}_i - \bar{y})^2 + 2 \sum_{i=1}^{k} (\bar{y}_i - \bar{y}) \sum_{j=1}^{n_i} (y_{ij} - \bar{y}_i) \; .
\end{split}
$$

Note that the following sum is zero

$$ \label{eq:anova1-pss-s2}
\sum_{j=1}^{n_i} (y_{ij} - \bar{y}_i) = \sum_{j=1}^{n_i} y_{ij} - n_i \cdot \bar{y}_i = \sum_{j=1}^{n_i} y_{ij} - n_i \cdot \frac{1}{n_i} \sum_{j=1}^{n_i} y_{ij} \; ,
$$

so that the sum in \eqref{eq:anova1-pss-s1} reduces to

$$ \label{eq:anova1-pss-s3}
\sum_{i=1}^{k} \sum_{j=1}^{n_i} (y_{ij} - \bar{y})^2 = \sum_{i=1}^{k} \sum_{j=1}^{n_i} (\bar{y}_i - \bar{y})^2 + \sum_{i=1}^{k} \sum_{j=1}^{n_i} (y_{ij} - \bar{y}_i)^2 \; .
$$

With the [treatment sum of squares](/D/trss) for [one-way ANOVA](/D/anova1)

$$ \label{eq:anova1-trss}
\mathrm{SS}_\mathrm{treat} = \sum_{i=1}^{k} \sum_{j=1}^{n_i} (\bar{y}_i - \bar{y})^2
$$

and the [residual sum of squares](/D/rss) for [one-way ANOVA](/D/anova1)

$$ \label{eq:anova1-rss}
\mathrm{SS}_\mathrm{res} = \sum_{i=1}^{k} \sum_{j=1}^{n_i} (y_{ij} - \bar{y}_i)^2 \; ,
$$

we finally have:

$$ \label{eq:anova1-pss-qed}
\mathrm{SS}_\mathrm{tot} = \mathrm{SS}_\mathrm{treat} + \mathrm{SS}_\mathrm{res} \; .
$$