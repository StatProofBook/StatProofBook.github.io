---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2024-07-05 10:42:16

title: "F-test for equality of variances in two independent samples"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Univariate Gaussian"
theorem: "F-test for equality of variances"

sources:
  - authors: "Wikipedia"
    year: 2024
    title: "F-test of equality of variances"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2024-07-05"
    url: "https://en.wikipedia.org/wiki/F-test_of_equality_of_variances#The_test"

proof_id: "P460"
shortcut: "ug-fev"
username: "JoramSoch"
---


**Theorem:** Let

$$ \label{eq:ug}
\begin{split}
y_{1i} &\sim \mathcal{N}(\mu_1, \sigma_1^2), \quad i = 1, \ldots, n_1 \\
y_{2i} &\sim \mathcal{N}(\mu_2, \sigma_2^2), \quad i = 1, \ldots, n_2
\end{split}
$$

be two [univariate Gaussian data sets](/D/ug) representing two groups of unequal size $n_1$ and $n_2$ with unknown means $\mu_1$ and $\mu_2$ and unknown variances $\sigma_1^2$ and $\sigma_2^2$. Then, the [test statistic](/D/tstat)

$$ \label{eq:F}
F
= \frac{s_1^2}{s_1^2}
= \frac{\frac{1}{n_1-1} \sum_{i=1}^{n_1} (y_{1i}-\bar{y}_1)^2}{\frac{1}{n_2-1} \sum_{i=1}^{n_2} (y_{2i}-\bar{y}_2)^2}
$$

with [sample means](/D/mean-samp) $\bar{y}_1$ and $\bar{y}_2$ and [samle variances](/D/var-samp) $s_1^2$ and $s_2^2$ follows an [F-distribution](/D/f) with numerator degrees of freedom $n_1-1$ and denominator degrees of freedom $n_2-1$

$$ \label{eq:F-dist}
F \sim \mathrm{F}(n_1-1, n_2-1)
$$

under the [null hypothesis](/D/h0) that the [two variances](/D/norm) are equal:

$$ \label{eq:fev-h0}
H_0: \; \sigma_1^2 = \sigma_2^2 \; .
$$


**Proof:** We know that, [for a sample of normal random variables, the sample variance is following a chi-squared distribution](/P/norm-chi2):

$$ \label{eq:norm-chi2}
X_i \sim \mathcal{N}(\mu, \sigma^2), \; i = 1, \ldots, n
\quad \Rightarrow \quad
V = (n-1) \frac{s^2}{\sigma^2} \sim \chi^2(n-1) \; .
$$

Thus, we have:

$$ \label{eq:V-dist}
\begin{split}
V_1 &= (n_1-1) \frac{s_1^2}{\sigma_1^2} \sim \chi^2(n_1-1) \quad \text{and} \\
V_2 &= (n_2-1) \frac{s_2^2}{\sigma_2^2} \sim \chi^2(n_2-1) \; .
\end{split}
$$

Moreover, by definition, [the ratio of two chi-squared random variables, divided by their degrees of freedom, is following an F-distribution](/D/f):

$$ \label{eq:chi2-f}
X_1 \sim \chi^2(d_1), \; X_2 \sim \chi^2(d_2)
\quad \Rightarrow \quad
Y = \frac{X_1/d_1}{X_2/d_2} \sim F(d_1, d_2) \; .
$$

Thus, we have:

$$ \label{eq:F-dist-qed}
\begin{split}
F
&= \frac{V_1/(n_1-1)}{V_2/(n_2-1)} \\
&= \frac{\left. (n_1-1) \frac{s_1^2}{\sigma_1^2} \middle/ (n_1-1) \right.}{\left. (n_2-1) \frac{s_2^2}{\sigma_2^2} \middle/ (n_2-1) \right.} \\
&= \frac{s_1^2 / \sigma_1^2}{s_2^2 / \sigma_2^2} \\
&\overset{\eqref{eq:fev-h0}}{=} \frac{s_1^2}{s_2^2} \; .
\end{split}
$$

This means that the [null hypothesis](/D/h0) of equal variances can be rejected when $F$ is as extreme or more extreme than the [critical value](/D/cval) obtained from the [F-distribution](/D/F) with [degrees of freedom](/D/dof) $n_1-1$ and $n_2-1$ using a [significance level](/D/alpha) $\alpha$.