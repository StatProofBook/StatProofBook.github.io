---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-03-24 05:10:00

title: "Paired z-test for dependent observations"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Univariate Gaussian with known variance"
theorem: "Paired z-test"

sources:
  - authors: "Wikipedia"
    year: 2021
    title: "Z-test"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-03-24"
    url: "https://en.wikipedia.org/wiki/Z-test#Use_in_location_testing"
  - authors: "Wikipedia"
    year: 2021
    title: "Gauß-Test"
    in: "Wikipedia – Die freie Enzyklopädie"
    pages: "retrieved on 2021-03-24"
    url: "https://de.wikipedia.org/wiki/Gau%C3%9F-Test#Zweistichproben-Gau%C3%9F-Test_f%C3%BCr_abh%C3%A4ngige_(verbundene)_Stichproben"

proof_id: "P210"
shortcut: "ugkv-ztestp"
username: "JoramSoch"
---


**Theorem:** Let $y_{i1}$ and $y_{i2}$ with $i = 1, \ldots, n$ be paired observations, such that

$$ \label{eq:ugkv}
y_{i1} \sim \mathcal{N}(y_{i2} + \mu, \sigma^2), \quad i = 1, \ldots, n
$$

is a [univariate Gaussian data set](/D/ugkv) with unknown shift $\mu$ and known variance $\sigma^2$. Then, the [test statistic](/D/tstat)

$$ \label{eq:z}
z = \sqrt{n} \, \frac{\bar{d}-\mu_0}{\sigma} \quad \text{where} \quad d_i = y_{i1} - y_{i2}
$$

with [sample mean](/D/mean-samp) $\bar{d}$ follows a [standard normal distribution](/D/snorm)

$$ \label{eq:z-dist}
z \sim \mathcal{N}(0, 1)
$$

under the [null hypothesis](/D/h0)

$$ \label{eq:ztestp-h0}
H_0: \; \mu = \mu_0 \; .
$$


**Proof:** Define the pair-wise difference $d_i = y_{i1} - y_{i2}$ which is, according to the [linearity of the expected value](/P/mean-lin) and the [invariance of the variance under addition](/P/var-inv), distributed as

$$ \label{eq:d-dist}
d_i = y_{i1} - y_{i2} \sim \mathcal{N}(\mu, \sigma^2), \quad i = 1, \ldots, n \; .
$$

Therefore, $d_1, \ldots, d_n$ satisfy the conditions of the [one-sample z-test](/P/ugkv-ztest1) which results in the test statistic given by \eqref{eq:z}.