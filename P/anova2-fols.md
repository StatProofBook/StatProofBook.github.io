---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-11-16 16:34:00

title: "F-statistics in terms of ordinary least squares estimates in two-way analysis of variance"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Analysis of variance"
theorem: "F-statistics in terms of OLS estimates"

sources:

proof_id: "P380"
shortcut: "anova2-fols"
username: "JoramSoch"
---


**Theorem:** Given the [two-way analysis of variance](/D/anova2) assumption

$$ \label{eq:anova2}
y_{ijk} = \mu + \alpha_i + \beta_j + \gamma_{ij} + \varepsilon_{ijk}, \; \varepsilon_{ijk} \overset{\mathrm{i.i.d.}}{\sim} \mathcal{N}(0, \sigma^2) \; ,
$$

the F-statistics for the [grand mean](/P/anova2-fgm), the [main effects](/P/anova2-fme) and the [interaction](/P/anova2-fia) can be expressed in terms of [ordinary least squares parameter estimates](/P/anova2-ols) as

$$ \label{eq:anova2-fols}
\begin{split}
F_M &= \frac{n \hat{\mu}^2}{\frac{1}{n-ab} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (y_{ijk} - \hat{y}_{ijk})^2} \\
F_A &= \frac{\frac{1}{a-1} \sum_{i=1}^{a} n_{i \bullet} \hat{\alpha}_i^2}{\frac{1}{n-ab} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (y_{ijk} - \hat{y}_{ijk})^2} \\
F_B &= \frac{\frac{1}{b-1} \sum_{j=1}^{b} n_{\bullet j} \hat{\beta}_j^2}{\frac{1}{n-ab} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (y_{ijk} - \hat{y}_{ijk})^2} \\
F_{A \times B} &= \frac{\frac{1}{(a-1)(b-1)} \sum_{i=1}^{a} \sum_{j=1}^{b} n_{ij} \hat{\gamma}_{ij}^2}{\frac{1}{n-ab} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (y_{ijk} - \hat{y}_{ijk})^2}
\end{split}
$$

where the predicted values $\hat{y}_{ijk}$ are given by

$$ \label{eq:y-est}
\hat{y}_{ijk} = \hat{\mu} + \hat{\alpha}_i + \hat{\beta}_j + \hat{\gamma}_{ij} \; .
$$


**Theorem:** The F-statistics for the [grand mean](/P/anova2-fgm), the [main effects](/P/anova2-fme) and the [interaction](/P/anova2-fia) in [two-way ANOVA](/D/anova2) are calculated as

$$ \label{eq:anova2-f}
\begin{split}
F_M &= \frac{n (\bar{y}_{\bullet \bullet \bullet})^2}{\frac{1}{n-ab} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (y_{ijk} - \bar{y}_{i j \bullet})^2} \\
F_A &= \frac{\frac{1}{a-1} \sum_{i=1}^{a} n_{i \bullet} (\bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet \bullet \bullet})^2}{\frac{1}{n-ab} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (y_{ijk} - \bar{y}_{i j \bullet})^2} \\
F_B &= \frac{\frac{1}{b-1} \sum_{j=1}^{b} n_{\bullet j} (\bar{y}_{\bullet j \bullet} - \bar{y}_{\bullet \bullet \bullet})^2}{\frac{1}{n-ab} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (y_{ijk} - \bar{y}_{i j \bullet})^2} \\
F_{A \times B} &= \frac{\frac{1}{(a-1)(b-1)} \sum_{i=1}^{a} \sum_{j=1}^{b} n_{ij} (\bar{y}_{i j \bullet} - \bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet j \bullet} + \bar{y}_{\bullet \bullet \bullet})^2}{\frac{1}{n-ab} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (y_{ijk} - \bar{y}_{i j \bullet})^2}
\end{split}
$$

and the [ordinary least squares estimates for two-way ANOVA](/P/anova2-ols) are

$$ \label{eq:anova2-ols}
\begin{split}
\hat{\mu} &= \bar{y}_{\bullet \bullet \bullet} \\
\hat{\alpha}_i &= \bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet \bullet \bullet} \\
\hat{\beta}_j &= \bar{y}_{\bullet j \bullet} - \bar{y}_{\bullet \bullet \bullet} \\
\hat{\gamma}_{ij} &= \bar{y}_{i j \bullet} - \bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet j \bullet} + \bar{y}_{\bullet \bullet \bullet}
\end{split}
$$

where the the [sample means](/D/mean-samp) are given by

$$ \label{eq:mean-samp}
\begin{split}
\bar{y}_{\bullet \bullet \bullet} &= \frac{1}{n} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} y_{ijk} \\
\bar{y}_{i \bullet \bullet} &= \frac{1}{n_{i \bullet}} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} y_{ijk} \\
\bar{y}_{\bullet j \bullet} &= \frac{1}{n_{\bullet j}} \sum_{i=1}^{a} \sum_{k=1}^{n_{ij}} y_{ijk} \\
\bar{y}_{i j \bullet} &= \frac{1}{n_{ij}} \sum_{k=1}^{n_{ij}} y_{ijk} \; .
\end{split}
$$

We first note that the predicted values can be evaluated as

$$ \label{eq:y-est-qed}
\begin{split}
\hat{y}_{ijk} &= \hat{\mu} + \hat{\alpha}_i + \hat{\beta}_j + \hat{\gamma}_{ij} \\
&= \bar{y}_{\bullet \bullet \bullet} + (\bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet \bullet \bullet}) + (\bar{y}_{\bullet j \bullet} - \bar{y}_{\bullet \bullet \bullet}) + (\bar{y}_{i j \bullet} - \bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet j \bullet} + \bar{y}_{\bullet \bullet \bullet}) \\
&= \bar{y}_{i \bullet \bullet} + \bar{y}_{\bullet j \bullet} + \bar{y}_{i j \bullet} - \bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet j \bullet} \\
&= \bar{y}_{i j \bullet} \; .
\end{split}
$$

Substituting this \eqref{eq:y-est-qed} and the OLS estimates \eqref{eq:anova2-ols} into the F-formulas \eqref{eq:anova2-f}, we obtain:

$$ \label{eq:anova2-fols-qed}
\begin{split}
F_M &= \frac{n \hat{\mu}^2}{\frac{1}{n-ab} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (y_{ijk} - \hat{y}_{ijk})^2} \\
F_A &= \frac{\frac{1}{a-1} \sum_{i=1}^{a} n_{i \bullet} \hat{\alpha}_i^2}{\frac{1}{n-ab} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (y_{ijk} - \hat{y}_{ijk})^2} \\
F_B &= \frac{\frac{1}{b-1} \sum_{j=1}^{b} n_{\bullet j} \hat{\beta}_j^2}{\frac{1}{n-ab} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (y_{ijk} - \hat{y}_{ijk})^2} \\
F_{A \times B} &= \frac{\frac{1}{(a-1)(b-1)} \sum_{i=1}^{a} \sum_{j=1}^{b} n_{ij} \hat{\gamma}_{ij}^2}{\frac{1}{n-ab} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (y_{ijk} - \hat{y}_{ijk})^2} \; .
\end{split}
$$