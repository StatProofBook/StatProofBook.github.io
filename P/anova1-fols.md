---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-11-15 17:35:00

title: "F-statistic in terms of ordinary least squares estimates in one-way analysis of variance"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Analysis of variance"
theorem: "F-statistic in terms of OLS estimates"

sources:

proof_id: "P377"
shortcut: "anova1-fols"
username: "JoramSoch"
---


**Theorem:** Given the [one-way analysis of variance](/D/anova1) assumption

$$ \label{eq:anova1}
y_{ij} = \mu_i + \varepsilon_{ij}, \; \varepsilon_{ij} \overset{\mathrm{i.i.d.}}{\sim} \mathcal{N}(0, \sigma^2),
$$

1) the [F-statistic for the main effect](/P/anova1-f) can be expressed in terms of [ordinary least squares parameter estimates](/P/anova1-ols) as

$$ \label{eq:anova1-fols-v1}
F = \frac{\frac{1}{k-1} \sum_{i=1}^{k} n_i (\hat{\mu}_i - \bar{y})^2}{\frac{1}{n-k} \sum_{i=1}^{k} \sum_{j=1}^{n_i} (y_{ij} - \hat{\mu}_i)^2}
$$

2) or, when using the [reparametrized version of one-way ANOVA](/P/anova1-repara), the F-statistic can be expressed as

$$ \label{eq:anova1-fols-v2}
F = \frac{\frac{1}{k-1} \sum_{i=1}^{k} n_i \hat{\delta}_i^2}{\frac{1}{n-k} \sum_{i=1}^{k} \sum_{j=1}^{n_i} (y_{ij} - \hat{\mu} - \hat{\delta}_i)^2} \; .
$$


**Theorem:** The [F-statistic for the main effect in one-way ANOVA](/P/anova1-f) is given in terms of the [sample means](/D/mean-samp) as

$$ \label{eq:anova1-f}
F = \frac{\frac{1}{k-1} \sum_{i=1}^{k} n_i (\bar{y}_i - \bar{y})^2}{\frac{1}{n-k} \sum_{i=1}^{k} \sum_{j=1}^{n_i} (y_{ij} - \bar{y}_i)^2}
$$

where $\bar{y} _i$ is the average of all values $y_{ij}$ from category $i$ and $\bar{y}$ is the grand mean of all values $y_{ij}$ from all categories $i = 1, \ldots, k$.

1) The [ordinary least squares estimates for one-way ANOVA](/P/anova1-ols) are

$$ \label{eq:anova1-ols}
\hat{\mu}_i = \bar{y}_i \; ,
$$

such that

$$ \label{eq:anova1-fols-v1-qed}
F = \frac{\frac{1}{k-1} \sum_{i=1}^{k} n_i (\hat{\mu}_i - \bar{y})^2}{\frac{1}{n-k} \sum_{i=1}^{k} \sum_{j=1}^{n_i} (y_{ij} - \hat{\mu}_i)^2} \; .
$$

2) The [OLS estimates for reparametrized one-way ANOVA](/P/anova1-repara) are

$$ \label{eq:anova1-repara-ols}
\begin{split}
\hat{\mu} &= \bar{y} \\
\hat{\delta}_i &= \bar{y}_i - \bar{y} \; ,
\end{split}
$$

such that

$$ \label{eq:anova1-fols-v2-qed}
F = \frac{\frac{1}{k-1} \sum_{i=1}^{k} n_i \hat{\delta}_i^2}{\frac{1}{n-k} \sum_{i=1}^{k} \sum_{j=1}^{n_i} (y_{ij} - \hat{\mu} - \hat{\delta}_i)^2} \; .
$$