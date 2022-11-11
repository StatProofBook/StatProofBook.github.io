---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-11-06 13:05:00

title: "F-test for main effect in one-way analysis of variance"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Analysis of variance"
theorem: "F-test for main effect in one-way ANOVA"

sources:
  - authors: "Denziloe"
    year: 2018
    title: "Derive the distribution of the ANOVA F-statistic under the alternative hypothesis"
    in: "StackExchange CrossValidated"
    pages: "retrieved on 2022-11-06"
    url: "https://stats.stackexchange.com/questions/355594/derive-the-distribution-of-the-anova-f-statistic-under-the-alternative-hypothesi"

proof_id: "P370"
shortcut: "anova1-f"
username: "JoramSoch"
---


**Theorem:** Assume the [one-way analysis of variance](/D/anova1) model

$$ \label{eq:anova1}
y_{ij} = \mu_i + \varepsilon_{ij}, \; \varepsilon_{ij} \overset{\mathrm{i.i.d.}}{\sim} \mathcal{N}(0, \sigma^2), \; i = 1, \ldots, k, \; j = 1, \dots, n_i \; ,
$$

and consider the [null](/D/h0) and [alternative](/D/h1) hypothesis

$$ \label{eq:anova1-h0}
\begin{split}
H_0: &\; \mu_1 = \ldots = \mu_K \\
H_1: &\; \mu_i \neq \mu_j \quad \text{for at least one} \quad i,j \in \left\lbrace 1, \ldots, k \right\rbrace, \; i \neq j \; .
\end{split}
$$

Then, the [test statistic](/D/tstat)

$$ \label{eq:anova1-f}
F = \frac{\frac{1}{k-1} \sum_{i=1}^{k} n_i (\bar{y}_i - \bar{y})^2}{\frac{1}{n-k} \sum_{i=1}^{k} \sum_{j=1}^{n_i} (y_{ij} - \bar{y}_i)^2}
$$

follows an [F-distribution](/D/f) under the null hypothesis:

$$ \label{eq:anova1-f-h0}
F \sim \mathrm{F}(k-1, n-k), \; \text{if} \; H_0 \; .
$$


**Proof:** Let $\mu$ be the common [mean](/D/mean) under the [null hypothesis](/D/h0) $\mu_1 = \ldots = \mu_K = \mu$. Under $H_0$, we have:

$$ \label{eq:yij-h0}
y_{ij} \sim \mathcal{N}(\mu, \sigma^2) \quad \text{for all} \quad i = 1, \ldots, k, \; j = 1, \ldots, n_i \; .
$$

Thus, the [random variable](/D/rvar) $U_{ij} = (y_{ij} - \mu)/\sigma$ [follows a standard normal distribution](/P/norm-snorm)

$$ \label{eq:Uij-h0}
U_{ij} = \frac{y_{ij} - \mu}{\sigma} \sim \mathcal{N}(0, 1) \; .
$$

Now consider the following sum:

$$ \label{eq:sum-Uij-s1}
\begin{split}
\sum_{i=1}^{k} \sum_{j=1}^{n_i} U_{ij}^2 &= \sum_{i=1}^{k} \sum_{j=1}^{n_i} \left( \frac{y_{ij} - \mu}{\sigma} \right)^2 \\
&= \frac{1}{\sigma^2} \sum_{i=1}^{k} \sum_{j=1}^{n_i} \left( (y_{ij} - \bar{y}_i) + (\bar{y}_i - \bar{y}) + (\bar{y} - \mu) \right)^2 \\
&= \frac{1}{\sigma^2} \sum_{i=1}^{k} \sum_{j=1}^{n_i} \left[ (y_{ij} - \bar{y}_i)^2 + (\bar{y}_i - \bar{y})^2 + (\bar{y} - \mu)^2 + 2 (y_{ij} - \bar{y}_i) (\bar{y}_i - \bar{y}) + 2 (y_{ij} - \bar{y}_i) (\bar{y} - \mu) + 2 (\bar{y}_i - \bar{y}) (\bar{y} - \mu) \right] \; .
\end{split}
$$

Because the following sum over $j$ is zero for all $i$

$$ \label{eq:sum-yij}
\begin{split}
\sum_{j=1}^{n_i} (y_{ij} - \bar{y}_i) &= \sum_{j=1}^{n_i} y_{ij} - n_i \bar{y}_i \\
&= \sum_{j=1}^{n_i} y_{ij}  - n_i \cdot \frac{1}{n_i} \sum_{j=1}^{n_i} y_{ij} \\
&= 0, \; i = 1, \ldots, k
\end{split}
$$

and the following sum over $i$ and $j$ is also zero

$$ \label{eq:sum-yib}
\begin{split}
\sum_{i=1}^{k} \sum_{j=1}^{n_i} (\bar{y}_i - \bar{y}) &= \sum_{i=1}^{k} n_i (\bar{y}_i - \bar{y}) \\
&= \sum_{i=1}^{k} n_i \bar{y}_i - \bar{y} \sum_{i=1}^{k} n_i \\
&= \sum_{i=1}^{k} n_i \cdot \frac{1}{n_i} \sum_{j=1}^{n_i} y_{ij} - n \cdot \frac{1}{n} \sum_{i=1}^{k} \sum_{j=1}^{n_i} y_{ij} \\
&= 0 \; ,
\end{split}
$$

where $n = \sum_{i=1}^{k} n_i$, the sum in \eqref{eq:sum-Uij-s1} reduces to

$$ \label{eq:sum-Uij-s2}
\begin{split}
\sum_{i=1}^{k} \sum_{j=1}^{n_i} U_{ij}^2 &= \sum_{i=1}^{k} \sum_{j=1}^{n_i} \left[ \left( \frac{y_{ij} - \bar{y}_i}{\sigma} \right)^2 + \left( \frac{\bar{y}_i - \bar{y}}{\sigma} \right)^2 + \left( \frac{\bar{y} - \mu}{\sigma} \right)^2 \right] \\
&= \sum_{i=1}^{k} \sum_{j=1}^{n_i} \left( \frac{y_{ij} - \bar{y}_i}{\sigma} \right)^2 + \sum_{i=1}^{k} \sum_{j=1}^{n_i} \left( \frac{\bar{y}_i - \bar{y}}{\sigma} \right)^2 + \sum_{i=1}^{k} \sum_{j=1}^{n_i} \left( \frac{\bar{y} - \mu}{\sigma} \right)^2 \; .
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

Let $U$ be the $n \times 1$ column vector of all observations

$$ \label{eq:U}
U = \left[ \begin{matrix} u_1 \\ \vdots \\ u_k \end{matrix} \right]
$$

where the group-wise $n_i \times 1$ column vectors are

$$ \label{yi}
u_1 = \left[ \begin{matrix} (y_{1,1}-\mu)/\sigma \\ \vdots \\ (y_{1,n_1}-\mu)/\sigma \end{matrix} \right], \quad \ldots, \quad u_k = \left[ \begin{matrix} (y_{k,1}-\mu)/\sigma \\ \vdots \\ (y_{k,n_k}-\mu)/\sigma \end{matrix} \right] \; .
$$

Then, we observe that the sum in \eqref{eq:sum-Uij-s2} can be represented in the form of \eqref{eq:cochran-p1} using the matrices

$$ \label{eq:sum-Uij-s3-Bj}
\begin{split}
B^{(1)} &= I_n - \mathrm{diag}\left( \frac{1}{n_1} J_{n_1}, \; \ldots, \; \frac{1}{n_K} J_{n_K} \right) \\
B^{(2)} &= \mathrm{diag}\left( \frac{1}{n_1} J_{n_1}, \; \ldots, \; \frac{1}{n_K} J_{n_K} \right) - \frac{1}{n} J_n \\
B^{(3)} &= \frac{1}{n} J_n
\end{split}
$$

where $J_n$ is an $n \times n$ matrix of ones and $\mathrm{diag}\left( A_1, \ldots, A_n \right)$ denotes a block-diagonal matrix composed of $A_1, \ldots, A_n$. The matrices in \eqref{eq:sum-Uij-s3-Bj} fulfill $B^{(1)} + B^{(2)} + B^{(3)} = I_n$ and their ranks are given by:

$$ \label{eq:sum-Uij-s3-Bj-rk}
\begin{split}
\mathrm{rank}\left( B^{(1)} \right) &= n-k \\
\mathrm{rank}\left( B^{(2)} \right) &= k-1 \\
\mathrm{rank}\left( B^{(3)} \right) &= 1 \; .
\end{split}
$$

Let's write down the [explained sum of squares](/D/ess) and the [residual sum of squares](/D/rss) for [one-way analysis of variance](/D/anova1) as

$$ \label{eq:ess-rss}
\begin{split}
\mathrm{ESS} &= \sum_{i=1}^{k} \sum_{j=1}^{n_i} \left( \bar{y}_i - \bar{y} \right)^2 \\
\mathrm{RSS} &= \sum_{i=1}^{k} \sum_{j=1}^{n_i} \left( y_{ij} - \bar{y}_i \right)^2 \; .
\end{split}
$$

Then, using \eqref{eq:sum-Uij-s2}, \eqref{eq:cochran-p1}, \eqref{eq:cochran-p2}, \eqref{eq:sum-Uij-s3-Bj} and \eqref{eq:sum-Uij-s3-Bj-rk}, we find that

$$ \label{eq:ess-rss-dist}
\begin{split}
\frac{\mathrm{ESS}}{\sigma^2} = \sum_{i=1}^{k} \sum_{j=1}^{n_i} \left( \frac{\bar{y}_i - \bar{y}}{\sigma} \right)^2 &= Q_2 = U^\mathrm{T} B^{(2)} U \sim \chi^2(k-1) \\
\frac{\mathrm{RSS}}{\sigma^2} = \sum_{i=1}^{k} \sum_{j=1}^{n_i} \left( \frac{y_{ij} - \bar{y}_i}{\sigma} \right)^2 &= Q_1 = U^\mathrm{T} B^{(1)} U \sim \chi^2(n-k) \; .
\end{split}
$$

Because $\mathrm{ESS}/\sigma^2$ and $\mathrm{RSS}/\sigma^2$ are also independent by \eqref{eq:cochran-p2}, the F-statistic from \eqref{eq:anova1-f} is equal to the ratio of two independent [chi-squared distributed](/D/chi2) [random variables](/D/rvar) divided by their degrees of freedom

$$ \label{eq:anova1-f-ess-tss}
\begin{split}
F &= \frac{(\mathrm{ESS}/\sigma^2)/(k-1)}{(\mathrm{RSS}/\sigma^2)/(n-k)} \\
&= \frac{\mathrm{ESS}/(k-1)}{\mathrm{RSS}/(n-k)} \\
&= \frac{\frac{1}{k-1} \sum_{i=1}^{k} \sum_{j=1}^{n_i} (\bar{y}_i - \bar{y})^2}{\frac{1}{n-k} \sum_{i=1}^{k} \sum_{j=1}^{n_i} (y_{ij} - \bar{y}_i)^2} \\
&= \frac{\frac{1}{k-1} \sum_{i=1}^{k} n_i (\bar{y}_i - \bar{y})^2}{\frac{1}{n-k} \sum_{i=1}^{k} \sum_{j=1}^{n_i} (y_{ij} - \bar{y}_i)^2}
\end{split}
$$

which, [by definition of the F-distribution](/D/f), is distributed as:

$$ \label{eq:anova1-f-qed}
F \sim \mathrm{F}(k-1, n-k), \; \text{if} \; H_0 \; .
$$
