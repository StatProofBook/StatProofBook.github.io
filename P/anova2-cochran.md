---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-11-16 15:15:00

title: "Application of Cochran's theorem to two-way analysis of variance"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Analysis of variance"
theorem: "Cochran's theorem for two-way ANOVA"

sources:
  - authors: "Nandy, Siddhartha"
    year: 2018
    title: "Two-Way Analysis of Variance"
    in: "Stat 512: Applied Regression Analysis"
    pages: "Purdue University, Summer 2018, Ch. 19"
    url: "https://www.stat.purdue.edu/~snandy/stat512/topic7.pdf"

proof_id: "P378"
shortcut: "anova2-cochran"
username: "JoramSoch"
---


**Theorem:** Assume the [two-way analysis of variance](/D/anova2) model

$$ \label{eq:anova2}
\begin{split}
y_{ijk} &= \mu + \alpha_i + \beta_j + \gamma_{ij} + \varepsilon_{ijk} \\
\varepsilon_{ijk} &\overset{\mathrm{i.i.d.}}{\sim} \mathcal{N}(0, \sigma^2), \; i = 1, \ldots, a, \; j = 1, \ldots, b, \; k = 1, \dots, n_{ij}
\end{split}
$$

under the well-known [constraints for the model parameters](/D/anova2)

$$ \label{eq:anova2-constr}
\begin{split}
\sum_{i=1}^{a} \frac{n_{ij}}{n} \alpha_i &= 0 \quad \text{for all} \quad j = 1, \ldots, b \\
\sum_{j=1}^{b} \frac{n_{ij}}{n} \beta_j &= 0 \quad \text{for all} \quad i = 1, \ldots, a \\
\sum_{i=1}^{a} \frac{n_{ij}}{n} \gamma_{ij} &= 0 \quad \text{for all} \quad j = 1, \ldots, b \\
\sum_{j=1}^{b} \frac{n_{ij}}{n} \gamma_{ij} &= 0 \quad \text{for all} \quad i = 1, \ldots, a \; .
\end{split}
$$

Then, the following [sums of squares](/P/anova2-pss) are [chi-square distributed](/D/chi2)

$$ \label{eq:anova2-cochran}
\begin{split}
\frac{1}{\sigma^2} n (\bar{y}_{\bullet \bullet \bullet} - \mu)^2 = \frac{\mathrm{SS}_M}{\sigma^2} &\sim \chi^2(1) \\
\frac{1}{\sigma^2} \sum_{i=1}^{a} n_{i \bullet} ([\bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet \bullet \bullet}] - \alpha_i)^2 = \frac{\mathrm{SS}_A}{\sigma^2} &\sim \chi^2(a-1) \\
\frac{1}{\sigma^2} \sum_{j=1}^{b} n_{\bullet j} ([\bar{y}_{\bullet j \bullet} - \bar{y}_{\bullet \bullet \bullet}] - \beta_j)^2 = \frac{\mathrm{SS}_B}{\sigma^2} &\sim \chi^2(b-1) \\
\frac{1}{\sigma^2} \sum_{i=1}^{a} \sum_{j=1}^{b} n_{ij} ([\bar{y}_{i j \bullet} - \bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet j \bullet} + \bar{y}_{\bullet \bullet \bullet}] - \gamma_{ij})^2 = \frac{\mathrm{SS}_{A \times B}}{\sigma^2} &\sim \chi^2\left( (a-1)(b-1) \right) \\
\frac{1}{\sigma^2} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (y_{ijk} - \bar{y}_{i j \bullet})^2 = \frac{\mathrm{SS}_\mathrm{res}}{\sigma^2} &\sim \chi^2(n-ab) \; .
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

According to the model given by \eqref{eq:anova2}, the observations are distributed as:

$$ \label{eq:yijk-h0}
y_{ijk} \sim \mathcal{N}(\mu + \alpha_i + \beta_j + \gamma_{ij}, \sigma^2) \quad \text{for all} \quad i, j, k \; .
$$

Thus, the [random variable](/D/rvar) $U_{ijk} = (y_{ijk} - \mu - \alpha_i - \beta_j - \gamma_{ij})/\sigma$ [follows a standard normal distribution](/P/norm-snorm)

$$ \label{eq:Uijk-h0}
U_{ijk} = \frac{y_{ijk} - \mu - \alpha_i - \beta_j - \gamma_{ij}}{\sigma} \sim \mathcal{N}(0, 1) \; .
$$

Now consider the following sum

$$ \label{eq:sum-Uijk-s1}
\sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} U_{ijk}^2 = \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} \left( \frac{y_{ijk} - \mu - \alpha_i - \beta_j - \gamma_{ij}}{\sigma} \right)^2 \\
$$

which can be rewritten as follows:

$$ \label{eq:sum-Uijk-s2}
\begin{split}
\sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} U_{ijk}^2 = \frac{1}{\sigma^2} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} & \left[ (y_{ijk} - \mu - \alpha_i - \beta_j - \gamma_{ij}) - \right. \\
&\left. [\bar{y}_{\bullet \bullet \bullet} + (\bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet \bullet \bullet}) + (\bar{y}_{\bullet j \bullet} - \bar{y}_{\bullet \bullet \bullet}) + (\bar{y}_{i j \bullet} - \bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet j \bullet} + \bar{y}_{\bullet \bullet \bullet})] \right. + \\
&\left. [\bar{y}_{\bullet \bullet \bullet} + (\bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet \bullet \bullet}) + (\bar{y}_{\bullet j \bullet} - \bar{y}_{\bullet \bullet \bullet}) + (\bar{y}_{i j \bullet} - \bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet j \bullet} + \bar{y}_{\bullet \bullet \bullet})] \right]^2 \\
= \frac{1}{\sigma^2} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} & \left[ (y_{ijk} - [\bar{y}_{\bullet \bullet \bullet} + (\bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet \bullet \bullet}) + (\bar{y}_{\bullet j \bullet} - \bar{y}_{\bullet \bullet \bullet}) + (\bar{y}_{i j \bullet} - \bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet j \bullet} + \bar{y}_{\bullet \bullet \bullet})]) + \right. \\
&\left. (\bar{y}_{\bullet \bullet \bullet} - \mu) + ([\bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet \bullet \bullet}] - \alpha_i) + ([\bar{y}_{\bullet j \bullet} - \bar{y}_{\bullet \bullet \bullet}] - \beta_j) \right. + \\
&\left. ([\bar{y}_{i j \bullet} - \bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet j \bullet} + \bar{y}_{\bullet \bullet \bullet}] - \gamma_{ij}) \right]^2 \\
= \frac{1}{\sigma^2} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} & \left[ (y_{ijk} - \bar{y}_{i j \bullet}) + (\bar{y}_{\bullet \bullet \bullet} - \mu) + ([\bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet \bullet \bullet}] - \alpha_i) + \right. \\
&\left. ([\bar{y}_{\bullet j \bullet} - \bar{y}_{\bullet \bullet \bullet}] - \beta_j) + ([\bar{y}_{i j \bullet} - \bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet j \bullet} + \bar{y}_{\bullet \bullet \bullet}] - \gamma_{ij}) \right]^2
\end{split}
$$

Note that the following sums are all zero

$$ \label{eq:sum-Uijk-s3a}
\begin{split}
\sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (y_{ijk} - \bar{y}_{i j \bullet}) &= \sum_{i=1}^{a} \sum_{j=1}^{b} \left[ \sum_{k=1}^{n_{ij}} y_{ijk} - n_{ij} \cdot \bar{y}_{i j \bullet} \right] \\
&\overset{\eqref{eq:mean-samp}}{=} \sum_{i=1}^{a} \sum_{j=1}^{b} \left[ \sum_{k=1}^{n_{ij}} y_{ijk} - n_{ij} \cdot \frac{1}{n_{ij}} \sum_{k=1}^{n_{ij}} y_{ijk} \right] \\
&= \sum_{i=1}^{a} \sum_{j=1}^{b} 0 = 0
\end{split}
$$

$$ \label{eq:sum-Uijk-s3b}
\begin{split}
\sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} ([\bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet \bullet \bullet}] - \alpha_i) &= \sum_{i=1}^{a} n_{i \bullet} \cdot (\bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet \bullet \bullet} - \alpha_i) \\
&= \sum_{i=1}^{a} n_{i \bullet} \cdot \bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet \bullet \bullet} \sum_{i=1}^{a} n_{i \bullet} - \sum_{i=1}^{a} n_{i \bullet} \alpha_i \\
&\overset{\eqref{eq:mean-samp}}{=} \sum_{i=1}^{a} n_{i \bullet} \cdot \frac{1}{n_{i \bullet}} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} y_{ijk} - n \cdot \frac{1}{n} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} y_{ijk} - \sum_{i=1}^{a} n_{i \bullet} \alpha_i \\
&= - \sum_{i=1}^{a} n_{i \bullet} \alpha_i \overset{\eqref{eq:samp-size}}{=} - n \sum_{i=1}^{a} \sum_{j=1}^{b} \frac{n_{ij}}{n} \alpha_i \overset{\eqref{eq:anova2-constr}}{=} 0
\end{split}
$$

$$ \label{eq:sum-Uijk-s3c}
\begin{split}
\sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} ([\bar{y}_{\bullet j \bullet} - \bar{y}_{\bullet \bullet \bullet}] - \beta_j) &= \sum_{j=1}^{b} n_{\bullet j} \cdot (\bar{y}_{\bullet j \bullet} - \bar{y}_{\bullet \bullet \bullet} - \beta_j) \\
&= \sum_{j=1}^{b} n_{\bullet j} \cdot \bar{y}_{\bullet j \bullet} - \bar{y}_{\bullet \bullet \bullet} \sum_{j=1}^{b} n_{\bullet j} - \sum_{j=1}^{b} n_{\bullet j} \beta_j \\
&\overset{\eqref{eq:mean-samp}}{=} \sum_{j=1}^{b} n_{\bullet j} \cdot \frac{1}{n_{\bullet j}} \sum_{i=1}^{a} \sum_{k=1}^{n_{ij}} y_{ijk} - n \cdot \frac{1}{n} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} y_{ijk} - \sum_{j=1}^{b} n_{\bullet j} \beta_j \\
&= - \sum_{j=1}^{b} n_{\bullet j} \beta_j \overset{\eqref{eq:samp-size}}{=} - n \sum_{j=1}^{b} \sum_{i=1}^{a} \frac{n_{ij}}{n} \beta_j \overset{\eqref{eq:anova2-constr}}{=} 0
\end{split}
$$

$$ \label{eq:sum-Uijk-s3d}
\begin{split}
&\hphantom{=} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} ([\bar{y}_{i j \bullet} - \bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet j \bullet} + \bar{y}_{\bullet \bullet \bullet}] - \gamma_{ij}) \\
&= \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} \left[ (\bar{y}_{i j \bullet} - \bar{y}_{\bullet \bullet \bullet}) - (\bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet \bullet \bullet}) - (\bar{y}_{\bullet j \bullet} - \bar{y}_{\bullet \bullet \bullet}) - \gamma_{ij} \right] \\
&= \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (\bar{y}_{i j \bullet} - \bar{y}_{\bullet \bullet \bullet} - \gamma_{ij}) - \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (\bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet \bullet \bullet}) - \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (\bar{y}_{\bullet j \bullet} - \bar{y}_{\bullet \bullet \bullet}) \\
&\overset{\eqref{eq:sum-Uijk-s3c}}{=} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (\bar{y}_{i j \bullet} - \bar{y}_{\bullet \bullet \bullet} - \gamma_{ij}) - \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (\bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet \bullet \bullet}) \\
&\overset{\eqref{eq:sum-Uijk-s3b}}{=} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (\bar{y}_{i j \bullet} - \bar{y}_{\bullet \bullet \bullet} - \gamma_{ij}) \\
&= \sum_{i=1}^{a} \sum_{j=1}^{b} n_{ij} \bar{y}_{i j \bullet} - \bar{y}_{\bullet \bullet \bullet} \sum_{i=1}^{a} \sum_{j=1}^{b} n_{ij} - \sum_{i=1}^{a} \sum_{j=1}^{b} n_{ij} \gamma_{ij} \\
&\overset{\eqref{eq:mean-samp}}{=} \sum_{i=1}^{a} \sum_{j=1}^{b} n_{ij} \cdot \frac{1}{n_{ij}} \sum_{k=1}^{n_{ij}} y_{ijk} - n \cdot \frac{1}{n} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} y_{ijk} - \sum_{i=1}^{a} \sum_{j=1}^{b} n_{ij} \gamma_{ij} \\
&= - \frac{1}{n} \sum_{i=1}^{a} \sum_{j=1}^{b} \frac{n_{ij}}{n} \gamma_{ij} \overset{\eqref{eq:anova2-constr}}{=} 0 \; .
\end{split}
$$

Note further that $\bar{y}_{\bullet \bullet \bullet}$ and $\mu$ are not dependent on $i$, $j$ and $k$:

$$ \label{eq:yb-mu-const}
\bar{y}_{\bullet \bullet \bullet} = \text{const.} \quad \text{and} \quad \mu = \text{const.} \; .
$$

Thus, all the non-square products in \eqref{eq:sum-Uijk-s2} disappear and the sum reduces to

$$ \label{eq:sum-Uijk-s4}
\begin{split}
\sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} U_{ijk}^2 = \frac{1}{\sigma^2} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} & \left[ (y_{ijk} - \bar{y}_{i j \bullet})^2 + (\bar{y}_{\bullet \bullet \bullet} - \mu)^2 + ([\bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet \bullet \bullet}] - \alpha_i)^2 + \right. \\
&\left. ([\bar{y}_{\bullet j \bullet} - \bar{y}_{\bullet \bullet \bullet}] - \beta_j)^2 + ([\bar{y}_{i j \bullet} - \bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet j \bullet} + \bar{y}_{\bullet \bullet \bullet}] - \gamma_{ij})^2 \right] \\
= \frac{1}{\sigma^2} \left[ \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} \right. & (y_{ijk} - \bar{y}_{i j \bullet})^2 + \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (\bar{y}_{\bullet \bullet \bullet} - \mu)^2 + \\
\sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} &\left. ([\bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet \bullet \bullet}] - \alpha_i)^2 + \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} ([\bar{y}_{\bullet j \bullet} - \bar{y}_{\bullet \bullet \bullet}] - \beta_j)^2 + \right. \\
\sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} &\left. ([\bar{y}_{i j \bullet} - \bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet j \bullet} + \bar{y}_{\bullet \bullet \bullet}] - \gamma_{ij})^2 \right]
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
U = \left[ \begin{matrix} u_{1 \bullet} \\ \vdots \\ u_{a \bullet} \end{matrix} \right] \quad \text{where} \quad u_{i \bullet} = \left[ \begin{matrix} u_{i1} \\ \vdots \\ u_{ib} \end{matrix} \right] \quad \text{where} \quad u_{ij} = \left[ \begin{matrix} (y_{i,j,1} - \mu - \alpha_i - \beta_j - \gamma_{ij})/\sigma \\ \vdots \\ (y_{i,j,n_{ij}} - \mu - \alpha_i - \beta_j - \gamma_{ij})/\sigma \end{matrix} \right] \; .
$$

Next, we specify the $n \times n$ matrices $B$

$$ \label{eq:B}
\begin{split}
B^{(1)} &= I_n - \mathrm{diag}\left[ \mathrm{diag}\left( \frac{1}{n_{11}} J_{n_{11}}, \; \ldots, \; \frac{1}{n_{1b}} J_{n_{1b}} \right), \; \ldots, \; \mathrm{diag}\left( \frac{1}{n_{a1}} J_{n_{a1}}, \; \ldots, \; \frac{1}{n_{ab}} J_{n_{ab}} \right) \right] \\
B^{(2)} &= \frac{1}{n} J_n \\
B^{(3)} &= \mathrm{diag}\left( \frac{1}{n_{1 \bullet}} J_{n_{1 \bullet}}, \; \ldots, \; \frac{1}{n_{a \bullet}} J_{n_{a \bullet}} \right) - \frac{1}{n} J_n \\
B^{(4)} &= M_B - \frac{1}{n} J_n \\
B^{(5)} &= \mathrm{diag}\left[ \mathrm{diag}\left( \frac{1}{n_{11}} J_{n_{11}}, \; \ldots, \; \frac{1}{n_{1b}} J_{n_{1b}} \right), \; \ldots, \; \mathrm{diag}\left( \frac{1}{n_{a1}} J_{n_{a1}}, \; \ldots, \; \frac{1}{n_{ab}} J_{n_{ab}} \right) \right] \\
&- \mathrm{diag}\left( \frac{1}{n_{1 \bullet}} J_{n_{1 \bullet}}, \; \ldots, \; \frac{1}{n_{a \bullet}} J_{n_{a \bullet}} \right) - M_B + \frac{1}{n} J_n
\end{split}
$$

with the factor B matrix $M_B$ given by

$$ \label{eq:MB}
M_B = \left[ \begin{matrix} \mathrm{diag}\left( \frac{1}{n_{\bullet 1}} J_{n_{11},n_{11}}, \; \ldots, \; \frac{1}{n_{\bullet b}} J_{n_{1b},n_{1b}} \right) & \cdots & \mathrm{diag}\left( \frac{1}{n_{\bullet 1}} J_{n_{11},n_{a1}}, \; \ldots, \; \frac{1}{n_{\bullet b}} J_{n_{1b},n_{ab}} \right) \\ \vdots & \ddots & \vdots \\ \mathrm{diag}\left( \frac{1}{n_{\bullet 1}} J_{n_{a1},n_{11}}, \; \ldots, \; \frac{1}{n_{\bullet b}} J_{n_{ab},n_{1b}} \right) & \cdots & \mathrm{diag}\left( \frac{1}{n_{\bullet 1}} J_{n_{a1},n_{a1}}, \; \ldots, \; \frac{1}{n_{\bullet b}} J_{n_{ab},n_{ab}} \right) \end{matrix} \right] \; .
$$

where $J_n$ is an $n \times n$ matrix of ones, $J_{n,m}$ is an $n \times m$ matrix of ones and $\mathrm{diag}\left( A_1, \ldots, A_n \right)$ denotes a block-diagonal matrix composed of $A_1, \ldots, A_n$. We observe that those matrices satisfy

$$ \label{eq:U-Q-B}
\sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} U_{ijk}^2 = \sum_{l=1}^{5} Q_l = \sum_{l=1}^{5} U^\mathrm{T} B^{(l)} U
$$

as well as

$$ \label{eq:B-In}
\sum_{l=1}^{5} B^{(l)} = I_n
$$

and their ranks are

$$ \label{eq:B-rk}
\begin{split}
\mathrm{rank}\left( B^{(1)} \right) &= n - a b \\
\mathrm{rank}\left( B^{(2)} \right) &= 1 \\
\mathrm{rank}\left( B^{(3)} \right) &= a - 1 \\
\mathrm{rank}\left( B^{(4)} \right) &= b - 1 \\
\mathrm{rank}\left( B^{(5)} \right) &= (a-1)(b-1) \; .
\end{split}
$$

Thus, the conditions for applying [Cochran's theorem](/P/snorm-cochran) given by \eqref{eq:cochran-p1} are fulfilled and we can use \eqref{eq:sum-Uijk-s4}, \eqref{eq:cochran-p2}, \eqref{eq:B} and \eqref{eq:B-rk} to conclude that

$$ \label{eq:anova2-cochran-s1}
\begin{split}
\frac{1}{\sigma^2} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (\bar{y}_{\bullet \bullet \bullet} - \mu)^2 &= Q_2 = U^\mathrm{T} B^{(2)} U \sim \chi^2(1) \\
\frac{1}{\sigma^2} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} ([\bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet \bullet \bullet}] - \alpha_i)^2 &= Q_3 = U^\mathrm{T} B^{(3)} U \sim \chi^2(a-1) \\
\frac{1}{\sigma^2} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} ([\bar{y}_{\bullet j \bullet} - \bar{y}_{\bullet \bullet \bullet}] - \beta_j)^2 &= Q_4 = U^\mathrm{T} B^{(4)} U \sim \chi^2(b-1) \\
\frac{1}{\sigma^2} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} ([\bar{y}_{i j \bullet} - \bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet j \bullet} + \bar{y}_{\bullet \bullet \bullet}] - \gamma_{ij})^2 &= Q_5 = U^\mathrm{T} B^{(5)} U \sim \chi^2\left( (a-1)(b-1) \right) \\
\frac{1}{\sigma^2} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (y_{ijk} - \bar{y}_{i j \bullet})^2 &= Q_1 = U^\mathrm{T} B^{(1)} U \sim \chi^2(n-ab) \; .
\end{split}
$$

Finally, we identify the terms $Q$ with [sums of squares in two-way ANOVA](/P/anova2-pss) and simplify them to reach the expressions given by \eqref{eq:anova2-cochran}:

$$ \label{eq:anova2-cochran-s2}
\begin{split}
\frac{\mathrm{SS}_M}{\sigma^2} &= \frac{1}{\sigma^2} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (\bar{y}_{\bullet \bullet \bullet} - \mu)^2 = \frac{1}{\sigma^2} n (\bar{y}_{\bullet \bullet \bullet} - \mu)^2 \\
\frac{\mathrm{SS}_A}{\sigma^2} &= \frac{1}{\sigma^2} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} ([\bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet \bullet \bullet}] - \alpha_i)^2 = \frac{1}{\sigma^2} \sum_{i=1}^{a} n_{i \bullet} ([\bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet \bullet \bullet}] - \alpha_i)^2 \\
\frac{\mathrm{SS}_B}{\sigma^2} &= \frac{1}{\sigma^2} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} ([\bar{y}_{\bullet j \bullet} - \bar{y}_{\bullet \bullet \bullet}] - \beta_j)^2 = \frac{1}{\sigma^2} \sum_{j=1}^{b} n_{\bullet j} ([\bar{y}_{\bullet j \bullet} - \bar{y}_{\bullet \bullet \bullet}] - \beta_j)^2 \\
\frac{\mathrm{SS}_{A \times B}}{\sigma^2} &= \frac{1}{\sigma^2} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} ([\bar{y}_{i j \bullet} - \bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet j \bullet} + \bar{y}_{\bullet \bullet \bullet}] - \gamma_{ij})^2 = \frac{1}{\sigma^2} \sum_{i=1}^{a} \sum_{j=1}^{b} n_{ij} ([\bar{y}_{i j \bullet} - \bar{y}_{i \bullet \bullet} - \bar{y}_{\bullet j \bullet} + \bar{y}_{\bullet \bullet \bullet}] - \gamma_{ij})^2 \\
\frac{\mathrm{SS}_\mathrm{res}}{\sigma^2} &= \frac{1}{\sigma^2} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (y_{ijk} - \bar{y}_{i j \bullet})^2 = \frac{1}{\sigma^2} \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n_{ij}} (y_{ijk} - \bar{y}_{i j \bullet})^2 \; .
\end{split}
$$