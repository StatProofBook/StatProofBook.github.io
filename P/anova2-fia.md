---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-11-11 16:09:00

title: "F-test for interaction in two-way analysis of variance"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Analysis of variance"
theorem: "F-test for interaction in two-way ANOVA"

sources:
  - authors: "Nandy, Siddhartha"
    year: 2018
    title: "Two-Way Analysis of Variance"
    in: "Stat 512: Applied Regression Analysis"
    pages: "Purdue University, Summer 2018, Ch. 19"
    url: "https://www.stat.purdue.edu/~snandy/stat512/topic7.pdf"
  - authors: "ttd"
    year: 2021
    title: "Proof on SSAB/s2~chi2(I-1)(J-1) under the null hypothesis HAB: dij=0 for i=1,...,I and j=1,...,J"
    in: "StackExchange CrossValidated"
    pages: "retrieved on 2022-11-10"
    url: "https://stats.stackexchange.com/questions/545807/proof-on-ss-ab-sigma2-sim-chi2-i-1j-1-under-the-null-hypothesis"

proof_id: "P373"
shortcut: "anova2-fia"
username: "JoramSoch"
---


**Theorem:** Assume the [two-way analysis of variance](/D/anova2) model

$$ \label{eq:anova2}
\begin{split}
y_{ijk} &= \mu + \alpha_i + \beta_j + \gamma_{ij} + \varepsilon_{ijk} \\
\varepsilon_{ijk} &\overset{\mathrm{i.i.d.}}{\sim} \mathcal{N}(0, \sigma^2), \; i = 1, \ldots, a, \; j = 1, \ldots, b, \; k = 1, \dots, n_{ij} \; .
\end{split}
$$

Then, the [test statistic](/D/tstat)

$$ \label{eq:anova2-fia}
F_{A \times B} = \frac{\frac{1}{(a-1)(b-1)} \sum_{i=1}^{a} \sum_{j=1}^{b} n_{ij} (\bar{y}_{i j \bullet} - \bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet j \bullet} + \bar{y}_{\bullet \bullet \bullet})^2}{\frac{1}{n-ab} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (y_{ijk} - \bar{y}_{i j \bullet})^2}
$$

follows an [F-distribution](/D/f)

$$ \label{eq:anova2-fia-h0}
F_{A \times B} \sim \mathrm{F}\left( (a-1)(b-1), n-ab \right)
$$

under the [null hypothesis](/D/h0) for the [interaction effect](/D/anova2) of factors A and B

$$ \label{eq:anova2-h0}
\begin{split}
H_0: &\; \gamma_{11} = \ldots = \gamma_{ab} = 0 \\
H_1: &\; \gamma_{ij} \neq 0 \quad \text{for at least one} \quad (i,j) \in \left\lbrace 1, \ldots, a \right\rbrace \times \left\lbrace 1, \ldots, b \right\rbrace \; .
\end{split}
$$


**Proof:** Applying [Cochran's theorem for two-analysis of variance](/P/anova2-cochran), we find that the following squared sums

$$ \label{eq:anova2-ss-dist}
\begin{split}
\frac{\mathrm{SS}_{A \times B}}{\sigma^2} &= \frac{1}{\sigma^2} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} ([\bar{y}_{i j \bullet} - \bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet j \bullet} + \bar{y}_{\bullet \bullet \bullet}] - \gamma_{ij})^2 \\
&= \frac{1}{\sigma^2} \sum_{i=1}^{a} \sum_{j=1}^{b} n_{ij} ([\bar{y}_{i j \bullet} - \bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet j \bullet} + \bar{y}_{\bullet \bullet \bullet}] - \gamma_{ij})^2 \\
\frac{\mathrm{SS}_\mathrm{res}}{\sigma^2} &= \frac{1}{\sigma^2} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (y_{ijk} - \bar{y}_{i j \bullet})^2 \\
&= \frac{1}{\sigma^2} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (y_{ijk} - \bar{y}_{i j \bullet})^2
\end{split}
$$

are [independent](/D/ind) and [chi-squared distributed](/D/chi2):

$$ \label{eq:anova2-cochran-s1}
\begin{split}
\frac{\mathrm{SS}_{A \times B}}{\sigma^2} &\sim \chi^2\left( (a-1)(b-1) \right) \\
\frac{\mathrm{SS}_\mathrm{res}}{\sigma^2} &\sim \chi^2(n-ab) \; .
\end{split}
$$

Thus, the F-statistic from \eqref{eq:anova2-fia} is equal to the ratio of two [independent](/D/ind) [chi-squared distributed](/D/chi2) [random variables](/D/rvar) divided by their degrees of freedom

$$ \label{eq:anova2-fia-ess-tss}
\begin{split}
F_{A \times B} &= \frac{(\mathrm{SS}_{A \times B}/\sigma^2)/\left( (a-1)(b-1) \right)}{(\mathrm{SS}_\mathrm{res}/\sigma^2)/(n-ab)} \\
&= \frac{\mathrm{SS}_{A \times B}/\left( (a-1)(b-1) \right)}{\mathrm{SS}_\mathrm{res}/(n-ab)} \\
&\overset{\eqref{eq:anova2-ss-dist}}{=} \frac{\frac{1}{(a-1)(b-1)} \sum_{i=1}^{a} \sum_{j=1}^{b} n_{ij} ([\bar{y}_{i j \bullet} - \bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet j \bullet} + \bar{y}_{\bullet \bullet \bullet}] - \gamma_{ij})^2}{\frac{1}{n-ab} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (y_{ijk} - \bar{y}_{i j \bullet})^2} \\
&\overset{\eqref{eq:anova2-fia-h0}}{=} \frac{\frac{1}{(a-1)(b-1)} \sum_{i=1}^{a} \sum_{j=1}^{b} n_{ij} (\bar{y}_{i j \bullet} - \bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet j \bullet} + \bar{y}_{\bullet \bullet \bullet})^2}{\frac{1}{n-ab} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (y_{ijk} - \bar{y}_{i j \bullet})^2}
\end{split}
$$

which, [by definition of the F-distribution](/D/f), is distributed as

$$ \label{eq:anova2-fia-qed}
F_{A \times B} \sim \mathrm{F}\left( (a-1)(b-1), n-ab \right)
$$

under the [null hypothesis](/D/h0) for an interaction of A and B.