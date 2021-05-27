---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-03-12 09:20:00

title: "Two-sample t-test for independent observations"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Univariate Gaussian"
theorem: "Two-sample t-test"

sources:
  - authors: "Wikipedia"
    year: 2021
    title: "Student's t-distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-03-12"
    url: "https://en.wikipedia.org/wiki/Student%27s_t-distribution#Derivation"
  - authors: "Wikipedia"
    year: 2021
    title: "Student's t-test"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-03-12"
    url: "https://en.wikipedia.org/wiki/Student%27s_t-test#Equal_or_unequal_sample_sizes,_similar_variances_(1/2_%3C_sX1/sX2_%3C_2)"

proof_id: "P205"
shortcut: "ug-ttest2"
username: "JoramSoch"
---


**Theorem:** Let

$$ \label{eq:ug}
\begin{split}
y_{1i} &\sim \mathcal{N}(\mu_1, \sigma^2), \quad i = 1, \ldots, n_1 \\
y_{2i} &\sim \mathcal{N}(\mu_2, \sigma^2), \quad i = 1, \ldots, n_2
\end{split}
$$

be a [univariate Gaussian data set](/D/ug) representing two groups of unequal size $n_1$ and $n_2$ with unknown means $\mu_1$ and $\mu_2$ and equal unknown variance $\sigma^2$. Then, the [test statistic](/D/tstat)

$$ \label{eq:t}
t = \frac{(\bar{y}_1-\bar{y}_2)-\mu_\Delta}{s_p \cdot \sqrt{\frac{1}{n_1}+\frac{1}{n_2}}}
$$

with [sample means](/D/mean-samp) $\bar{y}_1$ and $\bar{y}_2$ and [pooled standard deviation](/D/std-pool) $s_p$ follows a [Student's t-distribution](/D/t) with $n_1+n_2-1$ [degrees of freedom](/D/dof)

$$ \label{eq:t-dist}
t \sim \mathrm{t}(n_1+n_2-1)
$$

under the [null hypothesis](/D/h0)

$$ \label{eq:ttest2-h0}
H_0: \; \mu_1-\mu_2 = \mu_\Delta \; .
$$


**Proof:** The [sample means](/D/mean-samp) are given by

$$ \label{eq:mean-samp}
\begin{split}
\bar{y}_1 &= \frac{1}{n_1} \sum_{i=1}^{n_1} y_{1i} \\
\bar{y}_2 &= \frac{1}{n_2} \sum_{i=1}^{n_2} y_{2i}
\end{split}
$$

and the [pooled standard deviation](/D/std-pool) is given by

$$ \label{eq:std-pool}
s_p = \sqrt{ \frac{(n_1-1) s^2_1 + (n_2-1) s^2_2}{n_1+n_2-2} }
$$

with the [sample variances](/D/var-samp)

$$ \label{eq:var-samp}
\begin{split}
s^2_1 &= \frac{1}{n_1-1} \sum_{i=1}^{n_1} (y_{1i} - \bar{y}_1)^2 \\
s^2_2 &= \frac{1}{n_2-1} \sum_{i=1}^{n_2} (y_{2i} - \bar{y}_2)^2 \; .
\end{split}
$$

Using the [linearity of the expected value](/P/mean-lin), the [additivity of the variance under independence](/P/var-add) and [scaling of the variance upon multiplication](/P/var-scal), the sample means follow a [normal distribution](/D/norm)

$$ \label{eq:mean-samp-dist}
\begin{split}
\bar{y}_1 &= \frac{1}{n_1} \sum_{i=1}^{n_1} y_{1i} \sim \mathcal{N}\left( \frac{1}{n_1} n_1 \mu_1, \left(\frac{1}{n_1}\right)^2 n_1 \sigma^2 \right) = \mathcal{N}\left( \mu_1, \sigma^2/n_1 \right) \\
\bar{y}_2 &= \frac{1}{n_2} \sum_{i=1}^{n_2} y_{2i} \sim \mathcal{N}\left( \frac{1}{n_2} n_2 \mu_2, \left(\frac{1}{n_2}\right)^2 n_2 \sigma^2 \right) = \mathcal{N}\left( \mu_2, \sigma^2/n_2 \right)
\end{split}
$$

and additionally using the [invariance of the variance under addition](/P/var-inv) and applying the null hypothesis from \eqref{eq:ttest2-h0}, the distribution of $Z = ( ( \bar{y}_1 - \bar{y}_2 ) - \mu_{\Delta} ) / ( \sigma \sqrt{1/n_1+1/n_2} )$ becomes [standard normal](/D/snorm)

$$ \label{eq:Z-dist}
Z = \frac{(\bar{y}_1-\bar{y}_2)-\mu_\Delta}{\sigma \cdot \sqrt{\frac{1}{n_1}+\frac{1}{n_2}}} \sim \mathcal{N}\left( \frac{(\mu_1-\mu_2)-\mu_\Delta}{\sigma \cdot \sqrt{\frac{1}{n_1}+\frac{1}{n_2}}}, \left(\frac{1}{\sigma \cdot \sqrt{\frac{1}{n_1}+\frac{1}{n_2}}}\right)^2 \left( \frac{\sigma^2}{n_1} + \frac{\sigma^2}{n_2} \right) \right) \overset{H_0}{=} \mathcal{N}\left( 0, 1 \right) \; .
$$

Because [sample variances calculated from independent normal random variables follow a chi-squared distribution](/P/norm-chi2), the distribution of $V = (n_1+n_2-2)\,s_p^2/\sigma^2$ is

$$ \label{eq:V-dist}
V = \frac{(n_1+n_2-1)\,s_p^2}{\sigma^2} \sim \chi^2\left(n_1+n_2-2\right) \; .
$$

Finally, since [the ratio of a standard normal random variable and the square root of a chi-squared random variable follows a t-distribution](/D/t), the distribution of the [test statistic](/D/tstat) is given by

$$ \label{eq:t-dist-qed}
t = \frac{(\bar{y}_1-\bar{y}_2)-\mu_\Delta}{s_p \cdot \sqrt{\frac{1}{n_1}+\frac{1}{n_2}}} = \frac{Z}{\sqrt{V / (n_1+n_2-2)}} \sim \mathrm{t}(n_1+n_2-2) \; .
$$

This means that the [null hypothesis](/D/h0) can be rejected when $t$ is as extreme or more extreme than the [critical value](/D/cval) obtained from the [Student's t-distribution](/D/t) with $n_1+n_2-2$ [degrees of freedom](/D/dof) using a [significance level](/D/alpha) $\alpha$.