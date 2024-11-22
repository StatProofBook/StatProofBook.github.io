---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-11-06 15:55:00

title: "Ordinary least squares for two-way analysis of variance"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Analysis of variance"
theorem: "Ordinary least squares for two-way ANOVA"

sources:
  - authors: "Olbricht, Gayla R."
    year: 2011
    title: "Two-Way ANOVA: Interaction"
    in: "Stat 512: Applied Regression Analysis"
    pages: "Purdue University, Spring 2011, Lect. 27"
    url: "https://www.stat.purdue.edu/~ghobbs/STAT_512/Lecture_Notes/ANOVA/Topic_27.pdf"

proof_id: "P371"
shortcut: "anova2-ols"
username: "JoramSoch"
---


**Theorem:** Given the [two-way analysis of variance](/D/anova2) assumption

$$ \label{eq:anova2}
\begin{split}
y_{ijk} &= \mu + \alpha_i + \beta_j + \gamma_{ij} + \varepsilon_{ijk} \\
\varepsilon_{ijk} &\overset{\mathrm{i.i.d.}}{\sim} \mathcal{N}(0, \sigma^2), \; i = 1, \ldots, a, \; j = 1, \ldots, b, \; k = 1, \dots, n_{ij} \; ,
\end{split}
$$

the parameters minimizing the [residual sum of squares](/D/rss) and satisfying the [constraints for the model parameters](/D/anova2) are given by

$$ \label{eq:anova2-ols}
\begin{split}
\hat{\mu} &= \bar{y}_{\bullet \bullet \bullet} \\
\hat{\alpha}_i &= \bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet \bullet \bullet} \\
\hat{\beta}_j &= \bar{y}_{\bullet j \bullet} - \bar{y}_{\bullet \bullet \bullet} \\
\hat{\gamma}_{ij} &= \bar{y}_{i j \bullet} - \bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet j \bullet} + \bar{y}_{\bullet \bullet \bullet}
\end{split}
$$

where $\bar{y} _{\bullet \bullet \bullet}$, $\bar{y} _{i \bullet \bullet}$, $\bar{y} _{\bullet j \bullet}$ and $\bar{y} _{i j \bullet}$ are the following [sample means](/D/mean-samp):

$$ \label{eq:mean-samp}
\begin{split}
\bar{y}_{\bullet \bullet \bullet} &= \frac{1}{n} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} y_{ijk} \\
\bar{y}_{i \bullet \bullet} &= \frac{1}{n_{i \bullet}} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} y_{ijk} \\
\bar{y}_{\bullet j \bullet} &= \frac{1}{n_{\bullet j}} \sum_{i=1}^{a} \sum_{k=1}^{n_{ij}} y_{ijk} \\
\bar{y}_{i j \bullet} &= \frac{1}{n_{ij}} \sum_{k=1}^{n_{ij}} y_{ijk}
\end{split}
$$

with the [sample size](/D/samp-size) numbers

$$ \label{eq:samp-size}
\begin{split}
n_{ij} &- \text{number of samples in category} \; (i,j) \\
n_{i \bullet} &= \sum_{j=1}^{b} n_{ij} \\
n_{\bullet j} &= \sum_{i=1}^{a} n_{ij} \\
n &= \sum_{i=1}^{a} \sum_{j=1}^{b} n_{ij} \; .
\end{split}
$$


**Proof:** In two-way ANOVA, model parameters [are subject to the constraints](/D/anova2)

$$ \label{eq:anova2-cons}
\begin{split}
\sum_{i=1}^{a} w_{ij} \alpha_i &= 0 \quad \text{for all} \quad j = 1, \ldots, b \\
\sum_{j=1}^{b} w_{ij} \beta_j &= 0 \quad \text{for all} \quad i = 1, \ldots, a \\
\sum_{i=1}^{a} w_{ij} \gamma_{ij} &= 0 \quad \text{for all} \quad j = 1, \ldots, b \\
\sum_{j=1}^{b} w_{ij} \gamma_{ij} &= 0 \quad \text{for all} \quad i = 1, \ldots, a
\end{split}
$$

where $w_{ij} = n_{ij}/n$. The [residual sum of squares](/D/rss) for this model is

$$ \label{eq:rss}
\mathrm{RSS}(\mu,\alpha,\beta,\gamma) = \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} \varepsilon_{ijk}^2 = \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (y_{ij} - \mu - \alpha_i - \beta_j - \gamma_{ij})^2
$$

and the derivatives of $\mathrm{RSS}$ with respect to $\mu$, $\alpha$, $\beta$ and $\gamma$ are

$$ \label{eq:rss-der-mu}
\begin{split}
\frac{\mathrm{d}\mathrm{RSS}}{\mathrm{d}\mu} &= \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} \frac{\mathrm{d}}{\mathrm{d}\mu} (y_{ijk} - \mu - \alpha_i - \beta_j - \gamma_{ij})^2 \\
&= \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} -2 (y_{ijk} - \mu - \alpha_i - \beta_j - \gamma_{ij}) \\
&= \sum_{i=1}^{a} \sum_{j=1}^{b} \left( 2 n_{ij} \mu + 2 n_{ij} (\alpha_i + \beta_j + \gamma_{ij}) - 2 \sum_{k=1}^{n_{ij}} y_{ijk} \right) \\
&= 2 n \mu + 2 \left( \sum_{i=1}^{a} n_{i \bullet} \alpha_i + \sum_{j=1}^{b} n_{\bullet j} \beta_j + \sum_{i=1}^{a} \sum_{j=1}^{b} n_{ij} \gamma_{ij} \right) - 2 \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} y_{ijk}
\end{split}
$$

$$ \label{eq:rss-der-alpha}
\begin{split}
\frac{\mathrm{d}\mathrm{RSS}}{\mathrm{d}\alpha_i} &= \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} \frac{\mathrm{d}}{\mathrm{d}\alpha_i} (y_{ijk} - \mu - \alpha_i - \beta_j - \gamma_{ij})^2 \\
&= \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} -2 (y_{ijk} - \mu - \alpha_i - \beta_j - \gamma_{ij}) \\
&= 2 n_{i \bullet} \mu + 2 n_{i \bullet} \alpha_i + 2 \left( \sum_{j=1}^{b} n_{ij} \beta_j + \sum_{j=1}^{b} n_{ij} \gamma_{ij} \right) - 2 \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} y_{ijk}
\end{split}
$$

$$ \label{eq:rss-der-beta}
\begin{split}
\frac{\mathrm{d}\mathrm{RSS}}{\mathrm{d}\beta_j} &= \sum_{i=1}^{a} \sum_{k=1}^{n_{ij}} \frac{\mathrm{d}}{\mathrm{d}\beta_j} (y_{ijk} - \mu - \alpha_i - \beta_j - \gamma_{ij})^2 \\
&= \sum_{i=1}^{a} \sum_{k=1}^{n_{ij}} -2 (y_{ijk} - \mu - \alpha_i - \beta_j - \gamma_{ij}) \\
&= 2 n_{\bullet j} \mu + 2 n_{\bullet j} \beta_j + 2 \left( \sum_{i=1}^{a} n_{ij} \alpha_i + \sum_{i=1}^{a} n_{ij} \gamma_{ij} \right) - 2 \sum_{i=1}^{a} \sum_{k=1}^{n_{ij}} y_{ijk}
\end{split}
$$

$$ \label{eq:rss-der-gamma}
\begin{split}
\frac{\mathrm{d}\mathrm{RSS}}{\mathrm{d}\gamma_{ij}} &= \sum_{k=1}^{n_{ij}} \frac{\mathrm{d}}{\mathrm{d}\gamma_{ij}} (y_{ijk} - \mu - \alpha_i - \beta_j - \gamma_{ij})^2 \\
&= \sum_{k=1}^{n_{ij}} -2 (y_{ijk} - \mu - \alpha_i - \beta_j - \gamma_{ij}) \\
&= 2 n_{ij} (\mu + \alpha_i + \beta_j + \gamma_{ij}) - 2 \sum_{k=1}^{n_{ij}} y_{ijk} \; .
\end{split}
$$

Setting these derivatives to zero, we obtain the estimates of $\mu$, $\alpha_i$, $\beta_j$ and $\gamma_{ij}$:

$$ \label{eq:rss-der-mu-zero}
\begin{split}
0 &= 2 n \hat{\mu} + 2 \left( \sum_{i=1}^{a} n_{i \bullet} \alpha_i + \sum_{j=1}^{b} n_{\bullet j} \beta_j + \sum_{i=1}^{a} \sum_{j=1}^{b} n_{ij} \gamma_{ij} \right) - 2 \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} y_{ijk} \\
\hat{\mu} &= \frac{1}{n} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} y_{ijk} -  \sum_{i=1}^{a} \frac{n_{i \bullet}}{n} \alpha_i - \sum_{j=1}^{b} \frac{n_{\bullet j}}{n} \beta_j - \sum_{i=1}^{a} \sum_{j=1}^{b} \frac{n_{ij}}{n} \gamma_{ij} \\
&\overset{\eqref{eq:samp-size}}{=} \frac{1}{n} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} y_{ijk} - \sum_{j=1}^{b} \sum_{i=1}^{a} \frac{n_{ij}}{n} \alpha_i - \sum_{i=1}^{a} \sum_{j=1}^{b} \frac{n_{ij}}{n} \beta_j - \sum_{i=1}^{a} \sum_{j=1}^{b} \frac{n_{ij}}{n} \gamma_{ij} \\
&\overset{\eqref{eq:anova2-cons}}{=} \frac{1}{n} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} y_{ijk} \\
&\overset{\eqref{eq:mean-samp}}{=} \bar{y}_{\bullet \bullet \bullet}
\end{split}
$$

$$ \label{eq:rss-der-alpha-zero}
\begin{split}
0 &= 2 n_{i \bullet} \hat{\mu} + 2 n_{i \bullet} \hat{\alpha}_i + 2 \left( \sum_{j=1}^{b} n_{ij} \beta_j + \sum_{j=1}^{b} n_{ij} \gamma_{ij} \right) - 2 \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} y_{ijk} \\
\hat{\alpha}_i &= \frac{1}{n_{i \bullet}} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} y_{ijk} - \hat{\mu} - \sum_{j=1}^{b} \frac{n_{ij}}{n_{i \bullet}} \beta_j - \sum_{j=1}^{b} \frac{n_{ij}}{n_{i \bullet}} \gamma_{ij} \\
&= \frac{1}{n_{i \bullet}} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} y_{ijk} - \hat{\mu} - \frac{n}{n_{i \bullet}} \sum_{j=1}^{b} \frac{n_{ij}}{n} \beta_j - \frac{n}{n_{i \bullet}} \sum_{j=1}^{b} \frac{n_{ij}}{n} \gamma_{ij} \\
&\overset{\eqref{eq:anova2-cons}}{=} \frac{1}{n_{i \bullet}} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} y_{ijk} - \frac{1}{n} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} y_{ijk} \\
&\overset{\eqref{eq:mean-samp}}{=} \bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet \bullet \bullet}
\end{split}
$$

$$ \label{eq:rss-der-beta-zero}
\begin{split}
0 &= 2 n_{\bullet j} \hat{\mu} + 2 n_{\bullet j} \hat{\beta}_j + 2 \left( \sum_{i=1}^{a} n_{ij} \alpha_i + \sum_{i=1}^{a} n_{ij} \gamma_{ij} \right) - 2 \sum_{i=1}^{a} \sum_{k=1}^{n_{ij}} y_{ijk} \\
\hat{\beta}_j &= \frac{1}{n_{\bullet j}} \sum_{i=1}^{a} \sum_{k=1}^{n_{ij}} y_{ijk} - \hat{\mu} - \sum_{i=1}^{a} \frac{n_{ij}}{n_{\bullet j}} \alpha_i - \sum_{i=1}^{a} \frac{n_{ij}}{n_{\bullet j}} \gamma_{ij} \\
&= \frac{1}{n_{\bullet j}} \sum_{i=1}^{a} \sum_{k=1}^{n_{ij}} y_{ijk} - \hat{\mu} - \frac{n}{n_{\bullet j}} \sum_{i=1}^{a} \frac{n_{ij}}{n} \alpha_i - \frac{n}{n_{\bullet j}} \sum_{i=1}^{a} \frac{n_{ij}}{n} \gamma_{ij} \\
&\overset{\eqref{eq:anova2-cons}}{=} \frac{1}{n_{\bullet j}} \sum_{i=1}^{a} \sum_{k=1}^{n_{ij}} y_{ijk} - \frac{1}{n} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} y_{ijk} \\
&\overset{\eqref{eq:mean-samp}}{=} \bar{y}_{\bullet j \bullet} - \bar{y}_{\bullet \bullet \bullet}
\end{split}
$$

$$ \label{eq:rss-der-gamma-zero}
\begin{split}
0 &= 2 n_{ij} (\hat{\mu} + \hat{\alpha}_i + \hat{\beta}_j + \hat{\gamma_{ij}}) - 2 \sum_{k=1}^{n_{ij}} y_{ijk} \\
\hat{\gamma_{ij}} &= \frac{1}{n_{ij}} \sum_{k=1}^{n_{ij}} y_{ijk} - \hat{\alpha}_i - \hat{\beta}_j - \hat{\mu} \\
&= \frac{1}{n_{ij}} \sum_{k=1}^{n_{ij}} y_{ijk} - \frac{1}{n_{i \bullet}} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} y_{ijk} - \frac{1}{n_{\bullet j}} \sum_{i=1}^{a} \sum_{k=1}^{n_{ij}} y_{ijk} + \frac{1}{n} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} y_{ijk} \\
&\overset{\eqref{eq:mean-samp}}{=} \bar{y}_{i j \bullet} - \bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet j \bullet} + \bar{y}_{\bullet \bullet \bullet} \; .
\end{split}
$$