---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-11-11 16:54:00

title: "F-test for grand mean in two-way analysis of variance"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Analysis of variance"
theorem: "F-test for grand mean in two-way ANOVA"

sources:
  - authors: "Nandy, Siddhartha"
    year: 2018
    title: "Two-Way Analysis of Variance"
    in: "Stat 512: Applied Regression Analysis"
    pages: "Purdue University, Summer 2018, Ch. 19"
    url: "https://www.stat.purdue.edu/~snandy/stat512/topic7.pdf"
  - authors: "Olbricht, Gayla R."
    year: 2011
    title: "Two-Way ANOVA: Interaction"
    in: "Stat 512: Applied Regression Analysis"
    pages: "Purdue University, Spring 2011, Lect. 27"
    url: "https://www.stat.purdue.edu/~ghobbs/STAT_512/Lecture_Notes/ANOVA/Topic_27.pdf"

proof_id: "P374"
shortcut: "anova2-fgm"
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

$$ \label{eq:anova2-fgm}
F_M = \frac{n (\bar{y}_{\bullet \bullet \bullet})^2}{\frac{1}{n-ab} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (y_{ijk} - \bar{y}_{i j \bullet})^2}
$$

follows an [F-distribution](/D/f)

$$ \label{eq:anova2-fgm-h0}
F_M \sim \mathrm{F}\left( 1, n-ab \right)
$$

under the [null hypothesis](/D/h0) for the [grand mean](/D/anova2)

$$ \label{eq:anova2-h0}
\begin{split}
H_0: &\; \mu = 0 \\
H_1: &\; \mu \neq 0 \; .
\end{split}
$$


**Proof:** Applying [Cochran's theorem for two-analysis of variance](/P/anova2-cochran), we find that the following squared sums

$$ \label{eq:anova2-ss-dist}
\begin{split}
\frac{\mathrm{SS}_M}{\sigma^2} &= \frac{1}{\sigma^2} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (\bar{y}_{\bullet \bullet \bullet} - \mu)^2 = \frac{1}{\sigma^2} n (\bar{y}_{\bullet \bullet \bullet} - \mu)^2 \\
\frac{\mathrm{SS}_\mathrm{res}}{\sigma^2} &= \frac{1}{\sigma^2} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (y_{ijk} - \bar{y}_{i j \bullet})^2 = \frac{1}{\sigma^2} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (y_{ijk} - \bar{y}_{i j \bullet})^2
\end{split}
$$

are [independent](/D/ind) and [chi-squared distributed](/D/chi2):

$$ \label{eq:anova2-cochran-s1}
\begin{split}
\frac{\mathrm{SS}_M}{\sigma^2} &\sim \chi^2(1) \\
\frac{\mathrm{SS}_\mathrm{res}}{\sigma^2} &\sim \chi^2(n-ab) \; .
\end{split}
$$

Thus, the F-statistic from \eqref{eq:anova2-fgm} is equal to the ratio of two [independent](/D/ind) [chi-squared distributed](/D/chi2) [random variables](/D/rvar) divided by their degrees of freedom

$$ \label{eq:anova2-fgm-ess-tss}
\begin{split}
F_M &= \frac{(\mathrm{SS}_M/\sigma^2)/(1)}{(\mathrm{SS}_\mathrm{res}/\sigma^2)/(n-ab)} \\
&= \frac{\mathrm{SS}_M/(1)}{\mathrm{SS}_\mathrm{res}/(n-ab)} \\
&\overset{\eqref{eq:anova2-ss-dist}}{=} \frac{n (\bar{y}_{\bullet \bullet \bullet} - \mu)^2}{\frac{1}{n-ab} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (y_{ijk} - \bar{y}_{i j \bullet})^2} \\
&\overset{\eqref{eq:anova2-h0}}{=} \frac{n (\bar{y}_{\bullet \bullet \bullet})^2}{\frac{1}{n-ab} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (y_{ijk} - \bar{y}_{i j \bullet})^2}
\end{split}
$$

which, [by definition of the F-distribution](/D/f), is distributed as

$$ \label{eq:anova2-fia-qed}
F_M \sim \mathrm{F}(1, n-ab)
$$

under the [null hypothesis](/D/h0) for the grand mean.