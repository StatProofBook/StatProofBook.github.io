---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-12-15 22:55:00

title: "F-test for main effect in two-way analysis of variance"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Analysis of variance"
theorem: "F-test for main effect in two-way ANOVA"

sources:
  - authors: "ttd"
    year: 2021
    title: "Proof on SSAB/s2~chi2(I-1)(J-1) under the null hypothesis HAB: dij=0 for i=1,...,I and j=1,...,J"
    in: "StackExchange CrossValidated"
    pages: "retrieved on 2022-11-10"
    url: "https://stats.stackexchange.com/questions/545807/proof-on-ss-ab-sigma2-sim-chi2-i-1j-1-under-the-null-hypothesis"
  - authors: "JohnK"
    year: 2014
    title: "In a two-way ANOVA, how can the F-statistic for one factor have a central distribution if the null is false for the other factor?"
    in: "StackExchange CrossValidated"
    pages: "retrieved on 2022-11-10"
    url: "https://stats.stackexchange.com/questions/124166/in-a-two-way-anova-how-can-the-f-statistic-for-one-factor-have-a-central-distri"

proof_id: "P372"
shortcut: "anova2-fme"
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

$$ \label{eq:anova2-fme-A}
F_A = \frac{\frac{1}{a-1} \sum_{i=1}^{a} n_{i \bullet} (\bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet \bullet \bullet})^2}{\frac{1}{n-ab} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (y_{ijk} - \bar{y}_{i j \bullet})^2}
$$

follows an [F-distribution](/D/f)

$$ \label{eq:anova2-fme-h0-A}
F_A \sim \mathrm{F}(a-1, n-ab)
$$

under the [null hypothesis](/D/h0) for the [main effect](/D/anova2) of factor A

$$ \label{eq:anova2-h0-A}
\begin{split}
H_0: &\; \alpha_1 = \ldots = \alpha_a = 0 \\
H_1: &\; \alpha_i \neq 0 \quad \text{for at least one} \quad i \in \left\lbrace 1, \ldots, a \right\rbrace
\end{split}
$$

and the [test statistic](/D/tstat)

$$ \label{eq:anova2-fme-B}
F_B = \frac{\frac{1}{b-1} \sum_{j=1}^{b} n_{\bullet j} (\bar{y}_{\bullet j \bullet} - \bar{y}_{\bullet \bullet \bullet})^2}{\frac{1}{n-ab} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (y_{ijk} - \bar{y}_{i j \bullet})^2}
$$

follows an [F-distribution](/D/f)

$$ \label{eq:anova2-fme-h0-B}
F_B \sim \mathrm{F}(b-1, n-ab)
$$

under the [null hypothesis](/D/h0) for the [main effect](/D/anova2) of factor B

$$ \label{eq:anova2-h0-B}
\begin{split}
H_0: &\; \beta_1 = \ldots = \beta_b = 0 \\
H_1: &\; \beta_j \neq 0 \quad \text{for at least one} \quad j \in \left\lbrace 1, \ldots, b \right\rbrace \; .
\end{split}
$$


**Proof:** Applying [Cochran's theorem for two-analysis of variance](/P/anova2-cochran), we find that the following squared sums

$$ \label{eq:anova2-ss-dist}
\begin{split}
\frac{\mathrm{SS}_A}{\sigma^2} &= \frac{1}{\sigma^2} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} ([\bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet \bullet \bullet}] - \alpha_i)^2 = \frac{1}{\sigma^2} \sum_{i=1}^{a} n_{i \bullet} ([\bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet \bullet \bullet}] - \alpha_i)^2 \\
\frac{\mathrm{SS}_B}{\sigma^2} &= \frac{1}{\sigma^2} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} ([\bar{y}_{\bullet j \bullet} - \bar{y}_{\bullet \bullet \bullet}] - \beta_j)^2 = \frac{1}{\sigma^2} \sum_{j=1}^{b} n_{\bullet j} ([\bar{y}_{\bullet j \bullet} - \bar{y}_{\bullet \bullet \bullet}] - \beta_j)^2 \\
\frac{\mathrm{SS}_\mathrm{res}}{\sigma^2} &= \frac{1}{\sigma^2} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (y_{ijk} - \bar{y}_{i j \bullet})^2 = \frac{1}{\sigma^2} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (y_{ijk} - \bar{y}_{i j \bullet})^2
\end{split}
$$

are [independent](/D/ind) and [chi-squared distributed](/D/chi2):

$$ \label{eq:anova2-cochran-s1}
\begin{split}
\frac{\mathrm{SS}_A}{\sigma^2} &\sim \chi^2(a-1) \\
\frac{\mathrm{SS}_B}{\sigma^2} &\sim \chi^2(b-1) \\
\frac{\mathrm{SS}_\mathrm{res}}{\sigma^2} &\sim \chi^2(n-ab) \; .
\end{split}
$$

1) Thus, the F-statistic from \eqref{eq:anova2-fme-A} is equal to the ratio of two [independent](/D/ind) [chi-squared distributed](/D/chi2) [random variables](/D/rvar) divided by their degrees of freedom

$$ \label{eq:anova2-fme-A-ss}
\begin{split}
F_A &= \frac{(\mathrm{SS}_A/\sigma^2)/(a-1)}{(\mathrm{SS}_\mathrm{res}/\sigma^2)/(n-ab)} \\
&= \frac{\mathrm{SS}_A/(a-1)}{\mathrm{SS}_\mathrm{res}/(n-ab)} \\
&\overset{\eqref{eq:anova2-ss-dist}}{=} \frac{\frac{1}{a-1} \sum_{i=1}^{a} n_{i \bullet} ([\bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet \bullet \bullet}] - \alpha_i)^2}{\frac{1}{n-ab} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (y_{ijk} - \bar{y}_{i j \bullet})^2} \\
&\overset{\eqref{eq:anova2-fme-h0-A}}{=} \frac{\frac{1}{a-1} \sum_{i=1}^{a} n_{i \bullet} (\bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet \bullet \bullet})^2}{\frac{1}{n-ab} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (y_{ijk} - \bar{y}_{i j \bullet})^2}
\end{split}
$$

which, [by definition of the F-distribution](/D/f), is distributed as

$$ \label{eq:anova2-fme-A-qed}
F_A \sim \mathrm{F}(a-1, n-ab)
$$

under the [null hypothesis](/D/h0) for main effect of $A$.

2) Similarly, the F-statistic from \eqref{eq:anova2-fme-B} is equal to the ratio of two independent [chi-squared distributed](/D/chi2) [random variables](/D/rvar) divided by their degrees of freedom

$$ \label{eq:anova2-fme-B-ss}
\begin{split}
F_B &= \frac{(\mathrm{SS}_B/\sigma^2)/(b-1)}{(\mathrm{SS}_\mathrm{res}/\sigma^2)/(n-ab)} \\
&= \frac{\mathrm{SS}_B/(b-1)}{\mathrm{SS}_\mathrm{res}/(n-ab)} \\
&\overset{\eqref{eq:anova2-ss-dist}}{=} \frac{\frac{1}{b-1} \sum_{j=1}^{b} n_{\bullet j} ([\bar{y}_{\bullet j \bullet} - \bar{y}_{\bullet \bullet \bullet}] - \beta_j)^2}{\frac{1}{n-ab} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (y_{ijk} - \bar{y}_{i j \bullet})^2} \\
&\overset{\eqref{eq:anova2-fme-h0-B}}{=} \frac{\frac{1}{b-1} \sum_{j=1}^{b} n_{\bullet j} (\bar{y}_{\bullet j \bullet} - \bar{y}_{\bullet \bullet \bullet})^2}{\frac{1}{n-ab} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (y_{ijk} - \bar{y}_{i j \bullet})^2}
\end{split}
$$

which, [by definition of the F-distribution](/D/f), is distributed as

$$ \label{eq:anova2-fme-B-qed}
F_B \sim \mathrm{F}(b-1, n-ab)
$$

under the [null hypothesis](/D/h0) for main effect of $B$.