---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-03-24 04:23:00

title: "One-sample z-test for independent observations"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Univariate Gaussian with known variance"
theorem: "One-sample z-test"

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
    url: "https://de.wikipedia.org/wiki/Gau%C3%9F-Test#Einstichproben-Gau%C3%9F-Test"

proof_id: "P208"
shortcut: "ugkv-ztest1"
username: "JoramSoch"
---


**Theorem:** Let

$$ \label{eq:ugkv}
y_i \sim \mathcal{N}(\mu, \sigma^2), \quad i = 1, \ldots, n
$$

be a [univariate Gaussian data set](/D/ugkv) with unknown mean $\mu$ and known variance $\sigma^2$. Then, the [test statistic](/D/tstat)

$$ \label{eq:z}
z = \sqrt{n} \, \frac{\bar{y}-\mu_0}{\sigma}
$$

with [sample mean](/D/mean-samp) $\bar{y}$ follows a [standard normal distribution](/D/snorm)

$$ \label{eq:z-dist}
z \sim \mathcal{N}(0, 1)
$$

under the [null hypothesis](/D/h0)

$$ \label{eq:ztest1-h0}
H_0: \; \mu = \mu_0 \; .
$$


**Proof:** The [sample mean](/D/mean-samp) is given by

$$ \label{eq:mean-samp}
\bar{y} = \frac{1}{n} \sum_{i=1}^{n} y_i \; .
$$

Using the [linearity of the expected value](/P/mean-lin), the [additivity of the variance under independence](/P/var-add) and [scaling of the variance upon multiplication](/P/var-scal), the sample mean follows a [normal distribution](/D/norm)

$$ \label{eq:mean-samp-dist}
\bar{y} = \frac{1}{n} \sum_{i=1}^{n} y_i \sim \mathcal{N}\left( \frac{1}{n} n \mu, \left(\frac{1}{n}\right)^2 n \sigma^2 \right) = \mathcal{N}\left( \mu, \sigma^2/n \right)
$$

and additionally using the [invariance of the variance under addition](/P/var-inv), the distribution of $z = \sqrt{n/\sigma^2} (\bar{y}-\mu_0)$ becomes

$$ \label{eq:z-dist-s1}
z = \sqrt{\frac{n}{\sigma^2}} (\bar{y} - \mu_0) \sim \mathcal{N}\left( \sqrt{\frac{n}{\sigma^2}} (\mu - \mu_0), \left(\sqrt{\frac{n}{\sigma^2}}\right)^2 \frac{\sigma^2}{n} \right) = \mathcal{N}\left( \sqrt{n} \, \frac{\mu-\mu_0}{\sigma}, 1 \right) \; ,
$$

such that, under the null hypothesis in \eqref{eq:ztest1-h0}, we have:

$$ \label{eq:z-dist-s2}
z \sim \mathcal{N}(0, 1), \quad \text{if } \mu = \mu_0 \; .
$$

This means that the [null hypothesis](/D/h0) can be rejected when $z$ is as extreme or more extreme than the [critical value](/D/cval) obtained from the [standard normal distribution](/D/snorm) using a [significance level](/D/alpha) $\alpha$.