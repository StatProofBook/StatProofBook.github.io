---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-11-06 11:18:00

title: "Ordinary least squares for one-way analysis of variance"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Analysis of variance"
theorem: "Ordinary least squares for one-way ANOVA"

sources:

proof_id: "P369"
shortcut: "anova1-ols"
username: "JoramSoch"
---


**Theorem:** Given the [one-way analysis of variance](/D/anova1) assumption

$$ \label{eq:anova1}
y_{ij} = \mu_i + \varepsilon_{ij}, \; \varepsilon_{ij} \overset{\mathrm{i.i.d.}}{\sim} \mathcal{N}(0, \sigma^2), \; i = 1, \ldots, k, \; j = 1, \dots, n_i \; ,
$$

the parameters minimizing the [residual sum of squares](/D/rss) are given by

$$ \label{eq:anova1-ols}
\hat{\mu}_i = \bar{y}_i
$$

where $\bar{y}_i$ is the [sample mean](/D/mean-samp) of all observations in [group](/D/anova1) $i$:

$$ \label{eq:mean-samp}
\hat{\mu}_i = \bar{y}_i = \frac{1}{n_i} \sum_{j=1}^{n_i} y_{ij} \; .
$$


**Proof:** The [residual sum of squares](/D/rss) for this model is

$$ \label{eq:rss}
\mathrm{RSS}(\mu) = \sum_{i=1}^{k} \sum_{j=1}^{n_i} \varepsilon_{ij}^2 = \sum_{i=1}^{k} \sum_{j=1}^{n_i} (y_{ij} - \mu_i)^2
$$

and the derivatives of $\mathrm{RSS}$ with respect to $\mu_i$ are

$$ \label{eq:rss-der}
\begin{split}
\frac{\mathrm{d}\mathrm{RSS}(\mu)}{\mathrm{d}\mu_i} &= \sum_{j=1}^{n_i} \frac{\mathrm{d}}{\mathrm{d}\mu_i} (y_{ij} - \mu_i)^2 \\
&= \sum_{j=1}^{n_i} 2 (y_{ij} - \mu_i) (-1) \\
&= 2 \sum_{j=1}^{n_i} (\mu_i - y_{ij}) \\
&= 2 n_i \mu_i - 2 \sum_{j=1}^{n_i} y_{ij} \quad \text{for} \quad i = 1, \ldots, k \; .
\end{split}
$$

Setting these derivatives to zero, we obtain the estimates of $\mu_i$:

$$ \label{eq:rss-der-zero}
\begin{split}
0 &= 2 n_i \hat{\mu}_i - 2 \sum_{j=1}^{n_i} y_{ij} \\
\hat{\mu}_i &= \frac{1}{n_i} \sum_{j=1}^{n_i} y_{ij} \quad \text{for} \quad i = 1, \ldots, k \; .
\end{split}
$$