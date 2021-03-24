---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-03-12 09:34:00

title: "Paired t-test for dependent observations"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Univariate Gaussian"
theorem: "Paired t-test"

sources:
  - authors: "Wikipedia"
    year: 2021
    title: "Student's t-test"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-03-12"
    url: "https://en.wikipedia.org/wiki/Student%27s_t-test#Dependent_t-test_for_paired_samples"

proof_id: "P206"
shortcut: "ug-ttestp"
username: "JoramSoch"
---


**Theorem:** Let $y_{i1}$ and $y_{i2}$ with $i = 1, \ldots, n$ be paired observations, such that

$$ \label{eq:ug}
y_{i1} \sim \mathcal{N}(y_{i2} + \mu, \sigma^2), \quad i = 1, \ldots, n
$$

is a [univariate Gaussian data set](/D/ug) with unknown shift $\mu$ and unknown variance $\sigma^2$. Then, the [test statistic](/D/tstat)

$$ \label{eq:t}
t = \frac{\bar{d}-\mu_0}{s_d / \sqrt{n}} \quad \text{where} \quad d_i = y_{i1} - y_{i2}
$$

with [sample mean](/D/mean-samp) $\bar{d}$ and [sample variance](/D/var-samp) $s^2_d$ follows a [Student's t-distribution](/D/t) with $n-1$ [degrees of freedom](/D/dof)

$$ \label{eq:t-dist}
t \sim \mathrm{t}(n-1)
$$

under the [null hypothesis](/D/h0)

$$ \label{eq:ttestp-h0}
H_0: \; \mu = \mu_0 \; .
$$


**Proof:** Define the pair-wise difference $d_i = y_{i1} - y_{i2}$ which is, according to the [linearity of the expected value](/P/mean-lin) and the [invariance of the variance under addition](/P/var-inv), distributed as

$$ \label{eq:d-dist}
d_i = y_{i1} - y_{i2} \sim \mathcal{N}(\mu, \sigma^2), \quad i = 1, \ldots, n \; .
$$

Therefore, $d_1, \ldots, d_n$ satisfy the conditions of the [one-sample t-test](/P/ug-ttest1) which results in the test statistic given by \eqref{eq:t}.