---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-11-15 16:22:00

title: "Reparametrization for one-way analysis of variance"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Analysis of variance"
theorem: "Reparametrization of one-way ANOVA"

sources:
  - authors: "Wikipedia"
    year: 2022
    title: "Analysis of variance"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2022-11-15"
    url: "https://en.wikipedia.org/wiki/Analysis_of_variance#For_a_single_factor"

proof_id: "P375"
shortcut: "anova1-repara"
username: "JoramSoch"
---


**Theorem:** The [one-way analysis of variance](/D/anova1) model

$$ \label{eq:anova1}
y_{ij} = \mu_i + \varepsilon_{ij}, \; \varepsilon_{ij} \overset{\mathrm{i.i.d.}}{\sim} \mathcal{N}(0, \sigma^2)
$$

can be rewritten using paraneters $\mu$ and $\delta_i$ instead of $\mu_i$

$$ \label{eq:anova1-repara}
y_{ij} = \mu + \delta_i + \varepsilon_{ij}, \; \varepsilon_{ij} \overset{\mathrm{i.i.d.}}{\sim} \mathcal{N}(0, \sigma^2)
$$

with the constraint

$$ \label{eq:anova1-constr}
\sum_{i=1}^{k} \frac{n_i}{n} \delta_i = 0 \; ,
$$

in which case

1) the model parameters are related to each other as

$$ \label{eq:anova1-repara-c1}
\delta_i = \mu_i - \mu, \; i = 1, \ldots, k \; ;
$$

2) the [ordinary least squares estimates](/P/anova1-ols) are given by

$$ \label{eq:anova1-repara-c2}
\hat{\delta}_i = \bar{y}_i - \bar{y} = \frac{1}{n_i} \sum_{j=1}^{n_i} y_{ij} - \frac{1}{n} \sum_{i=1}^{k} \sum_{j=1}^{n_i} y_{ij} \; ;
$$

3) the following [sum of squares](/P/anova1-pss) is [chi-square distributed](/D/chi2)

$$ \label{eq:anova1-repara-c3}
\frac{1}{\sigma^2} \sum_{i=1}^{k} \sum_{j=1}^{n_i} \left( \hat{\delta}_i - \delta_i \right)^2 \sim \chi^2(k-1) \; ;
$$

4) and the following [test statistic](/D/tstat) is [F-distributed](/D/f)

$$ \label{eq:anova1-repara-c4}
F = \frac{\frac{1}{k-1} \sum_{i=1}^{k} n_i \hat{\delta}_i^2}{\frac{1}{n-k} \sum_{i=1}^{k} \sum_{j=1}^{n_i} (y_{ij} - \bar{y}_i)^2} \sim \mathrm{F}(k-1, n-k)
$$

under the [null hypothesis for the main effect](/P/anova1-f)

$$ \label{eq:anova1-repara-c4-h0}
H_0: \; \delta_1 = \ldots = \delta_k = 0 \; .
$$


**Proof:**

1) Equating \eqref{eq:anova1} with \eqref{eq:anova1-repara}, we get:

$$ \label{eq:anova1-repara-c1-qed}
\begin{split}
y_{ij} = \mu + \delta_i + \varepsilon_{ij} &= \mu_i + \varepsilon_{ij} = y_{ij} \\
\mu + \delta_i &= \mu_i \\
\delta_i &= \mu_i - \mu \; .
\end{split}
$$

2) Equation \eqref{eq:anova1-repara} is a special case of the [two-way analysis of variance](/D/anova2) with (i) just one factor $A$ and (ii) no interaction term. Thus, OLS estimates are identical to [that of two-way ANOVA](/P/anova2-ols), i.e. given by

$$ \label{eq:anova1-repara-c2-qed}
\begin{split}
\hat{\mu} &= \bar{y}_{\bullet \bullet} = \frac{1}{n} \sum_{i=1}^{k} \sum_{j=1}^{n_i} y_{ij} \\
\hat{\delta}_i &= \bar{y}_{i \bullet} - \bar{y}_{\bullet \bullet} = \frac{1}{n_i} \sum_{j=1}^{n_i} y_{ij} - \frac{1}{n} \sum_{i=1}^{k} \sum_{j=1}^{n_i} y_{ij} \; .
\end{split}
$$

3) Let $U_{ij} = (y_{ij} - \mu - \delta_i)/\sigma$, [such that](/P/norm-snorm) $U_{ij} \sim \mathcal{N}(0, 1)$ and consider the sum of all squared [random variables](/D/rvar) $U_{ij}$:

$$ \label{eq:anova1-repara-c3-s1}
\begin{split}
\sum_{i=1}^{k} \sum_{j=1}^{n_i} U_{ij}^2 &= \sum_{i=1}^{k} \sum_{j=1}^{n_i} \left( \frac{y_{ij} - \mu - \delta_i}{\sigma} \right)^2 \\
&= \frac{1}{\sigma^2} \sum_{i=1}^{k} \sum_{j=1}^{n_i} \left[ (y_{ij} - \bar{y}_i) + ([\bar{y}_i - \bar{y}] - \delta_i) + (\bar{y} - \mu) \right]^2 \; .
\end{split}
$$

This square of sums, [using a number of intermediate steps, can be developed](/P/anova1-f) into a sum of squares:

$$ \label{eq:anova1-repara-c3-s2}
\begin{split}
\sum_{i=1}^{k} \sum_{j=1}^{n_i} U_{ij}^2 &= \frac{1}{\sigma^2} \sum_{i=1}^{k} \sum_{j=1}^{n_i} \left[ (y_{ij} - \bar{y}_i)^2 + ([\bar{y}_i - \bar{y}] - \delta_i)^2 + (\bar{y} - \mu)^2 \right] \\
&= \frac{1}{\sigma^2} \left[ \sum_{i=1}^{k} \sum_{j=1}^{n_i} (y_{ij} - \bar{y}_i)^2 + \sum_{i=1}^{k} \sum_{j=1}^{n_i} ([\bar{y}_i - \bar{y}] - \delta_i)^2 + \sum_{i=1}^{k} \sum_{j=1}^{n_i} (\bar{y} - \mu)^2 \right] \; .
\end{split}
$$

To this sum, [Cochran's theorem for one-way analysis of variance can be applied](/P/anova1-f), yielding the distributions:

$$ \label{eq:anova1-repara-c3-qed}
\begin{split}
\frac{1}{\sigma^2} \sum_{i=1}^{k} \sum_{j=1}^{n_i} (y_{ij} - \bar{y}_i)^2 &\sim \chi^2(n-k) \\
\frac{1}{\sigma^2} \sum_{i=1}^{k} \sum_{j=1}^{n_i} ([\bar{y}_i - \bar{y}] - \delta_i)^2 \overset{\eqref{eq:anova1-repara-c2-qed}}{=} \frac{1}{\sigma^2} \sum_{i=1}^{k} \sum_{j=1}^{n_i} (\hat{\delta}_i - \delta_i)^2 &\sim \chi^2(k-1) \; .
\end{split}
$$

4) The ratio of two [chi-square distributed](/D/chi2) [random variables](/D/rvar), divided by their [degrees of freedom](/D/dof), is [defined to be F-distributed](/D/f), so that

$$ \label{eq:anova1-repara-c4-s1}
\begin{split}
F &= \frac{\left( \frac{1}{\sigma^2} \sum_{i=1}^{k} \sum_{j=1}^{n_i} (\hat{\delta}_i - \delta_i)^2 \right)/(k-1)}{\left( \frac{1}{\sigma^2} \sum_{i=1}^{k} \sum_{j=1}^{n_i} (y_{ij} - \bar{y}_i)^2 \right)/(n-k)} \\
&= \frac{\frac{1}{k-1} \sum_{i=1}^{k} \sum_{j=1}^{n_i} (\hat{\delta}_i - \delta_i)^2}{\frac{1}{n-k} \sum_{i=1}^{k} \sum_{j=1}^{n_i} (y_{ij} - \bar{y}_i)^2} \\
&= \frac{\frac{1}{k-1} \sum_{i=1}^{k} n_i (\hat{\delta}_i - \delta_i)^2}{\frac{1}{n-k} \sum_{i=1}^{k} \sum_{j=1}^{n_i} (y_{ij} - \bar{y}_i)^2} \\
&\overset{\eqref{eq:anova1-repara-c4-h0}}{=} \frac{\frac{1}{k-1} \sum_{i=1}^{k} n_i \hat{\delta}_i^2}{\frac{1}{n-k} \sum_{i=1}^{k} \sum_{j=1}^{n_i} (y_{ij} - \bar{y}_i)^2}
\end{split}
$$

follows the F-distribution

$$ \label{eq:anova1-repara-c4-qed}
F \sim \mathrm{F}(k-1, n-k)
$$

under the null hypothesis.