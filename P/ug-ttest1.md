---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-03-12 08:43:00

title: "One-sample t-test for independent observations"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Univariate Gaussian"
theorem: "One-sample t-test"

sources:
  - authors: "Wikipedia"
    year: 2021
    title: "Student's t-distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-03-12"
    url: "https://en.wikipedia.org/wiki/Student%27s_t-distribution#Derivation"

proof_id: "P204"
shortcut: "ug-ttest1"
username: "JoramSoch"
---


**Theorem:** Let

$$ \label{eq:ug}
y_i \sim \mathcal{N}(\mu, \sigma^2), \quad i = 1, \ldots, n
$$

be a [univariate Gaussian data set](/D/ug) with unknown mean $\mu$ and unknown variance $\sigma^2$. Then, the [test statistic](/D/tstat)

$$ \label{eq:t}
t = \frac{\bar{y}-\mu_0}{s / \sqrt{n}}
$$

with [sample mean](/D/mean-samp) $\bar{y}$ and [sample variance](/D/var-samp) $s^2$ follows a [Student's t-distribution](/D/t) with $n-1$ [degrees of freedom](/D/dof)

$$ \label{eq:t-dist}
t \sim \mathrm{t}(n-1)
$$

under the [null hypothesis](/D/h0)

$$ \label{eq:ttest1-h0}
H_0: \; \mu = \mu_0 \; .
$$


**Proof:** The [sample mean](/D/mean-samp) is given by

$$ \label{eq:mean-samp}
\bar{y} = \frac{1}{n} \sum_{i=1}^{n} y_i
$$

and the [sample variance](/D/var-samp) is given by

$$ \label{eq:var-samp}
s^2 = \frac{1}{n-1} \sum_{i=1}^{n} (y_i - \bar{y})^2 \; .
$$

Using the [linearity of the expected value](/P/mean-lin), the [additivity of the variance under independence](/P/var-add) and [scaling of the variance upon multiplication](/P/var-scal), the sample mean follows a [normal distribution](/D/norm)

$$ \label{eq:mean-samp-dist}
\bar{y} = \frac{1}{n} \sum_{i=1}^{n} y_i \sim \mathcal{N}\left( \frac{1}{n} n \mu, \left(\frac{1}{n}\right)^2 n \sigma^2 \right) = \mathcal{N}\left( \mu, \sigma^2/n \right)
$$

and additionally using the [invariance of the variance under addition](/P/var-inv) and applying the null hypothesis from \eqref{eq:ttest1-h0}, the distribution of $Z = \sqrt{n}(\bar{y}-\mu_0)/\sigma$ becomes [standard normal](/D/snorm)

$$ \label{eq:Z-dist}
Z = \frac{\sqrt{n}(\bar{y}-\mu_0)}{\sigma} \sim \mathcal{N}\left( \frac{\sqrt{n}}{\sigma} (\mu - \mu_0), \left(\frac{\sqrt{n}}{\sigma}\right)^2 \frac{\sigma^2}{n} \right) \overset{H_0}{=} \mathcal{N}\left( 0, 1 \right) \; .
$$

Because [sample variances calculated from independent normal random variables follow a chi-squared distribution](/P/norm-chi2), the distribution of $V = (n-1)\,s^2/\sigma^2$ is

$$ \label{eq:V-dist}
V = \frac{(n-1)\,s^2}{\sigma^2} \sim \chi^2\left(n-1\right) \; .
$$

Finally, since [the ratio of a standard normal random variable and the square root of a chi-squared random variable follows a t-distribution](/D/t), the distribution of the [test statistic](/D/tstat) is given by

$$ \label{eq:t-dist-qed}
t = \frac{\bar{y}-\mu_0}{s / \sqrt{n}} = \frac{Z}{\sqrt{V / (n-1)}} \sim \mathrm{t}(n-1) \; .
$$

This means that the [null hypothesis](/D/h0) can be rejected when $t$ is as extreme or more extreme than the [critical value](/D/cval) obtained from the [Student's t-distribution](/D/t) with $n-1$ [degrees of freedom](/D/dof) using a [significance level](/D/alpha) $\alpha$.