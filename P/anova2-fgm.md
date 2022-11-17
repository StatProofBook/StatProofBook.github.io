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


**Proof:** Denote sample sizes as

$$ \label{eq:samp-size}
\begin{split}
n_{ij} &- \text{number of samples in category} \; (i,j) \\
n_{i \bullet} &= \sum_{j=1}^{b} n_{ij} \\
n_{\bullet j} &= \sum_{i=1}^{a} n_{ij} \\
n &= \sum_{i=1}^{a} \sum_{j=1}^{b} n_{ij}
\end{split}
$$

and denote sample means as

$$ \label{eq:mean-samp}
\begin{split}
\bar{y}_{\bullet \bullet \bullet} &= \frac{1}{n} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} y_{ijk} \\
\bar{y}_{i \bullet \bullet} &= \frac{1}{n_{i \bullet}} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} y_{ijk} \\
\bar{y}_{\bullet j \bullet} &= \frac{1}{n_{\bullet j}} \sum_{i=1}^{a} \sum_{k=1}^{n_{ij}} y_{ijk} \\
\bar{y}_{i j \bullet} &= \frac{1}{n_{ij}} \sum_{k=1}^{n_{ij}} y_{ijk} \; .
\end{split}
$$

Assume that $\mu$ zero, according to $H_0$ given by \eqref{eq:anova2-h0}. Under this null hypothesis, we have:

$$ \label{eq:yijk-h0}
y_{ijk} \sim \mathcal{N}(\alpha_i + \beta_j + \gamma_{ij}, \sigma^2) \quad \text{for all} \quad i, j, k \; .
$$

Thus, the [random variable](/D/rvar) $U_{ijk} = (y_{ijk} - \alpha_i - \beta_j - \gamma_{ij})/\sigma$ [follows a standard normal distribution](/P/norm-snorm)

$$ \label{eq:Uijk-h0}
U_{ijk} = \frac{y_{ijk} - \alpha_i - \beta_j - \gamma_{ij}}{\sigma} \sim \mathcal{N}(0, 1) \; .
$$

Now consider the following sum

$$ \label{eq:sum-Uijk-s1}
\sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} U_{ijk}^2 = \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} \left( \frac{y_{ijk} - \alpha_i - \beta_j - \gamma_{ij}}{\sigma} \right)^2 \\
$$

which can be rewritten as follows:

$$ \label{eq:sum-Uijk-s2}
\begin{split}
\sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} U_{ijk}^2 = \frac{1}{\sigma^2} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} & \left[ (y_{ijk} - \alpha_i - \beta_j - \gamma_{ij}) - \right. \\
&\left. [\bar{y}_{\bullet \bullet \bullet} + (\bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet \bullet \bullet}) + (\bar{y}_{\bullet j \bullet} - \bar{y}_{\bullet \bullet \bullet}) + (\bar{y}_{i j \bullet} - \bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet j \bullet} + \bar{y}_{\bullet \bullet \bullet})] \right. + \\
&\left. [\bar{y}_{\bullet \bullet \bullet} + (\bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet \bullet \bullet}) + (\bar{y}_{\bullet j \bullet} - \bar{y}_{\bullet \bullet \bullet}) + (\bar{y}_{i j \bullet} - \bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet j \bullet} + \bar{y}_{\bullet \bullet \bullet})] \right]^2 \\
= \frac{1}{\sigma^2}\sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} & \left[ (y_{ijk} - [\bar{y}_{\bullet \bullet \bullet} + (\bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet \bullet \bullet}) + (\bar{y}_{\bullet j \bullet} - \bar{y}_{\bullet \bullet \bullet}) + (\bar{y}_{i j \bullet} - \bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet j \bullet} + \bar{y}_{\bullet \bullet \bullet})]) + \right. \\
&\left. (\bar{y}_{\bullet \bullet \bullet}) + ([\bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet \bullet \bullet}] - \alpha_i) + ([\bar{y}_{\bullet j \bullet} - \bar{y}_{\bullet \bullet \bullet}] - \beta_j) \right. + \\
&\left. ([\bar{y}_{i j \bullet} - \bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet j \bullet} + \bar{y}_{\bullet \bullet \bullet}] - \gamma_{ij}) \right]^2 \\
= \frac{1}{\sigma^2}\sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} & \left[ (y_{ijk} - \bar{y}_{i j \bullet}) + (\bar{y}_{\bullet \bullet \bullet}) + (\bar{y}_{i j \bullet} - \bar{y}_{\bullet \bullet \bullet} - \alpha_i - \beta_j - \gamma_{ij}) \right]^2
\end{split}
$$

Because the following sum over $k$ is zero for all $(i,j)$

$$ \label{eq:sum-yijk}
\begin{split}
\sum_{k=1}^{n_{ij}} (y_{ijk} - \bar{y}_{i j \bullet}) &= \sum_{k=1}^{n_{ij}} y_{ijk} - n_{ij} \bar{y}_{ij \bullet} \\
&= \sum_{k=1}^{n_{ij}} y_{ijk}  - n_{ij} \cdot \frac{1}{n_{ij}} \sum_{k=1}^{n_{ij}} y_{ijk} \\
&= 0, \; (i,j) \in \left\lbrace 1, \ldots, a \right\rbrace \times \left\lbrace 1, \ldots, b \right\rbrace \; ,
\end{split}
$$

the following sum over $(i,j,k)$ and is also zero

$$ \label{eq:sum-yib}
\begin{split}
\sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (\bar{y}_{i j \bullet} - \bar{y}_{\bullet \bullet \bullet}) &= \sum_{i=1}^{a} \sum_{j=1}^{b} n_{ij} \bar{y}_{i j \bullet} - \bar{y}_{\bullet \bullet \bullet} \sum_{i=1}^{a} \sum_{j=1}^{b} n_{ij} \\
&= \sum_{i=1}^{a} \sum_{j=1}^{b} n_{ij} \cdot \frac{1}{n_{ij}} \sum_{k=1}^{n_{ij}} y_{ijk} - n \cdot \frac{1}{n} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} y_{ijk} \\
&= 0
\end{split}
$$

and the term $\bar{y}_{\bullet \bullet \bullet}$ does not depend on $i$, $j$ and $k$

$$ \label{eq:yb-const}
\bar{y}_{\bullet \bullet \bullet} = \text{const.} \; ,
$$

non-square products in \eqref{eq:sum-Uijk-s2} disappear and the sum reduces to

$$ \label{eq:sum-Uijk-s3}
\begin{split}
\sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} U_{ijk}^2 = \frac{1}{\sigma^2} & \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} \left[ (y_{ijk} - \bar{y}_{i j \bullet})^2 + (\bar{y}_{\bullet \bullet \bullet})^2 + (\bar{y}_{i j \bullet} - \bar{y}_{\bullet \bullet \bullet} - \alpha_i - \beta_j - \gamma_{ij})^2 + \right] \\
= \frac{1}{\sigma^2} & \left[ \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} \right. (y_{ijk} - \bar{y}_{i j \bullet})^2 + \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (\bar{y}_{\bullet \bullet \bullet})^2 + \\
& \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} \left. (\bar{y}_{i j \bullet} - \bar{y}_{\bullet \bullet \bullet} - \alpha_i - \beta_j - \gamma_{ij})^2 \right]
\end{split}
$$

[Cochran's theorem](/P/snorm-cochran) states that, if a sum of squared [standard normal](/D/snorm) [random variables](/D/rvar) can be written as a sum of squared forms

$$ \label{eq:cochran-p1}
\begin{split}
\sum_{i=1}^{n} U_i^2 = \sum_{j=1}^{m} Q_j \quad &\text{where} \quad Q_j = U^\mathrm{T} B^{(j)} U \\
&\text{with} \quad \sum_{j=1}^{m} B^{(j)} = I_n \\
&\text{and} \quad r_j = \mathrm{rank}(B^{(j)}) \; ,
\end{split}
$$

then the terms $Q_j$ are [independent](/D/ind) and each term $Q_j$ follows a [chi-squared distribution](/D/chi2) with $r_j$ degrees of freedom:

$$ \label{eq:cochran-p2}
Q_j \sim \chi^2(r_j), \; j = 1, \ldots, m \; .
$$

First, we define the $n \times 1$ vector $U$:

$$ \label{eq:U}
U = \left[ \begin{matrix} u_{1 \bullet} \\ \vdots \\ u_{a \bullet} \end{matrix} \right] \quad \text{where} \quad u_{i \bullet} = \left[ \begin{matrix} u_{i1} \\ \vdots \\ u_{ib} \end{matrix} \right] \quad \text{where} \quad u_{ij} = \left[ \begin{matrix} (y_{i,j,1} - \alpha_i - \beta_j - \gamma_{ij})/\sigma \\ \vdots \\ (y_{i,j,n_{ij}} - \mu - \alpha_i - \beta_j)/\sigma \end{matrix} \right] \; .
$$

Next, we specify the $n \times n$ matrices $B$

$$ \label{eq:B}
\begin{split}
B^{(1)} &= I_n - \mathrm{diag}\left[ \mathrm{diag}\left( \frac{1}{n_{11}} J_{n_{11}}, \; \ldots, \; \frac{1}{n_{1b}} J_{n_{1b}} \right), \; \ldots, \; \mathrm{diag}\left( \frac{1}{n_{a1}} J_{n_{a1}}, \; \ldots, \; \frac{1}{n_{ab}} J_{n_{ab}} \right) \right] \\
B^{(2)} &= \frac{1}{n} J_n \\
B^{(3)} &= \mathrm{diag}\left[ \mathrm{diag}\left( \frac{1}{n_{11}} J_{n_{11}}, \; \ldots, \; \frac{1}{n_{1b}} J_{n_{1b}} \right), \; \ldots, \; \mathrm{diag}\left( \frac{1}{n_{a1}} J_{n_{a1}}, \; \ldots, \; \frac{1}{n_{ab}} J_{n_{ab}} \right) \right] - \frac{1}{n} J_n
\end{split}
$$

where $J_n$ is an $n \times n$ matrix of ones, $J_{n,m}$ is an $n \times m$ matrix of ones and $\mathrm{diag}\left( A_1, \ldots, A_n \right)$ denotes a block-diagonal matrix composed of $A_1, \ldots, A_n$. We observe that those matrices satisfy

$$ \label{eq:U-Q-B}
\sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} U_{ijk]^2 = Q_1 + Q_2 + Q_3 = U^\mathrm{T} B^{(1)} U + U^\mathrm{T} B^{(2)} U + U^\mathrm{T} B^{(3)} U
$$

as well as

$$ \label{eq:B-In}
B^{(1)} + B^{(2)} + B^{(3)} = I_n
$$

and their ranks are

$$ \label{eq:B-rk}
\begin{split}
\mathrm{rank}\left( B^{(1)} \right) &= n - a \cdot b \\
\mathrm{rank}\left( B^{(2)} \right) &= 1 \\
\mathrm{rank}\left( B^{(3)} \right) &= n - (n-ab) - 1 = a \cdot b - 1 \; .
\end{split}
$$

Let's write down the [explained sum of squares](/D/ess) and the [residual sum of squares](/D/rss) for [two-way analysis of variance](/D/anova2) as

$$ \label{eq:ess-rss}
\begin{split}
\mathrm{ESS} &= \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (\bar{y}_{\bullet \bullet \bullet})^2 \\
\mathrm{RSS} &= \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (y_{ijk} - \bar{y}_{i j \bullet})^2 \; .
\end{split}
$$

Then, using \eqref{eq:sum-Uijk-s3}, \eqref{eq:cochran-p1}, \eqref{eq:cochran-p2}, \eqref{eq:B} and \eqref{eq:B-rk}, we find that

$$ \label{eq:ess-rss-dist}
\begin{split}
\frac{\mathrm{ESS}}{\sigma^2} = \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} \left( \frac{\bar{y}_{\bullet \bullet \bullet}}{\sigma} \right)^2 &= Q_2 = U^\mathrm{T} B^{(2)} U \sim \chi^2(1) \\
\frac{\mathrm{RSS}}{\sigma^2} = \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} \left( \frac{y_{ijk} - \bar{y}_{i j \bullet}}{\sigma} \right)^2 &= Q_1 = U^\mathrm{T} B^{(1)} U \sim \chi^2(n-ab) \; .
\end{split}
$$

Because $\mathrm{ESS}/\sigma^2$ and $\mathrm{RSS}/\sigma^2$ are also independent by \eqref{eq:cochran-p2}, the F-statistic from \eqref{eq:anova2-fgm} is equal to the ratio of two independent [chi-squared distributed](/D/chi2) [random variables](/D/rvar) divided by their degrees of freedom

$$ \label{eq:anova2-fgm-ess-tss}
\begin{split}
F_M &= \frac{(\mathrm{ESS}/\sigma^2)/(1)}{(\mathrm{RSS}/\sigma^2)/(n-ab)} \\
&= \frac{\mathrm{ESS}/(1)}{\mathrm{RSS}/(n-ab)} \\
&= \frac{\sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (\bar{y}_{\bullet \bullet \bullet})^2}{\frac{1}{n-ab} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (y_{ijk} - \bar{y}_{i j \bullet})^2} \\
&= \frac{(\bar{y}_{\bullet \bullet \bullet})^2 \sum_{i=1}^{a} \sum_{j=1}^{b} n_{ij}}{\frac{1}{n-ab} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (y_{ijk} - \bar{y}_{i j \bullet})^2} \\
&= \frac{n (\bar{y}_{\bullet \bullet \bullet})^2}{\frac{1}{n-ab} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (y_{ijk} - \bar{y}_{i j \bullet})^2}
\end{split}
$$

which, [by definition of the F-distribution](/D/f), is distributed as

$$ \label{eq:anova2-fia-qed}
F_M \sim \mathrm{F}(1, n-ab)
$$

under the [null hypothesis](/D/h0) for the grand mean.