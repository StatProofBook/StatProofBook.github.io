---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-03-24 04:38:00

title: "Two-sample z-test for independent observations"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Univariate Gaussian with known variance"
theorem: "Two-sample z-test"

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
    url: "https://de.wikipedia.org/wiki/Gau%C3%9F-Test#Zweistichproben-Gau%C3%9F-Test_f%C3%BCr_unabh%C3%A4ngige_Stichproben"

proof_id: "P209"
shortcut: "ugkv-ztest2"
username: "JoramSoch"
---


**Theorem:** Let

$$ \label{eq:ugkv}
\begin{split}
y_{1i} &\sim \mathcal{N}(\mu_1, \sigma_1^2), \quad i = 1, \ldots, n_1 \\
y_{2i} &\sim \mathcal{N}(\mu_2, \sigma_2^2), \quad i = 1, \ldots, n_2
\end{split}
$$

be a [univariate Gaussian data set](/D/ug) representing two groups of unequal size $n_1$ and $n_2$ with unknown means $\mu_1$ and $\mu_2$ and unknown variances $\sigma_1^2$ and $\sigma_2^2$. Then, the [test statistic](/D/tstat)

$$ \label{eq:z}
z = \frac{(\bar{y}_1-\bar{y}_2)-\mu_\Delta}{\sqrt{\frac{\sigma_1^2}{n_1}+\frac{\sigma_2^2}{n_2}}}
$$

with [sample means](/D/mean-samp) $\bar{y}_1$ and $\bar{y}_2$ follows a [standard normal distribution](/D/snorm)

$$ \label{eq:z-dist}
z \sim \mathcal{N}(0, 1)
$$

under the [null hypothesis](/D/h0)

$$ \label{eq:ztest2-h0}
H_0: \; \mu_1-\mu_2 = \mu_\Delta \; .
$$


**Proof:** The [sample means](/D/mean-samp) are given by

$$ \label{eq:mean-samp}
\begin{split}
\bar{y}_1 &= \frac{1}{n_1} \sum_{i=1}^{n_1} y_{1i} \\
\bar{y}_2 &= \frac{1}{n_2} \sum_{i=1}^{n_2} y_{2i} \; .
\end{split}
$$

Using the [linearity of the expected value](/P/mean-lin), the [additivity of the variance under independence](/P/var-add) and [scaling of the variance upon multiplication](/P/var-scal), the sample means follow a [normal distribution](/D/norm)

$$ \label{eq:mean-samp-dist}
\begin{split}
\bar{y}_1 &= \frac{1}{n_1} \sum_{i=1}^{n_1} y_{1i} \sim \mathcal{N}\left( \frac{1}{n_1} n_1 \mu_1, \left(\frac{1}{n_1}\right)^2 n_1 \sigma^2 \right) = \mathcal{N}\left( \mu_1, \sigma_1^2/n_1 \right) \\
\bar{y}_2 &= \frac{1}{n_2} \sum_{i=1}^{n_2} y_{2i} \sim \mathcal{N}\left( \frac{1}{n_2} n_2 \mu_2, \left(\frac{1}{n_2}\right)^2 n_2 \sigma^2 \right) = \mathcal{N}\left( \mu_2, \sigma_2^2/n_2 \right)
\end{split}
$$

and additionally using the [invariance of the variance under addition](/P/var-inv), the distribution of $z = [(\bar{y}_1-\bar{y}_2)-\mu_\Delta]/\sigma_\Delta$ becomes

$$ \label{eq:z-dist-s1}
z = \frac{(\bar{y}_1-\bar{y}_2)-\mu_\Delta}{\sigma_\Delta} \sim \mathcal{N}\left( \frac{(\mu_1-\mu_2)-\mu_\Delta}{\sigma_\Delta}, \left(\frac{1}{\sigma_\Delta}\right)^2 \sigma_\Delta^2 \right) = \mathcal{N}\left( \frac{(\mu_1-\mu_2)-\mu_\Delta}{\sigma_\Delta}, 1 \right)
$$

where $\sigma_\Delta$ is the [pooled standard deviation](/D/std-pool)

$$ \label{eq:std-pool}
\sigma_\Delta = \sqrt{\frac{\sigma_1^2}{n_1}+\frac{\sigma_2^2}{n_2}} \; ,
$$

such that, under the null hypothesis in \eqref{eq:ztest2-h0}, we have:

$$ \label{eq:z-dist-s2}
z \sim \mathcal{N}(0, 1), \quad \text{if } \mu_\Delta = \mu_1-\mu_2 \; .
$$

This means that the [null hypothesis](/D/h0) can be rejected when $z$ is as extreme or more extreme than the [critical value](/D/cval) obtained from the [standard normal distribution](/D/snorm) using a [significance level](/D/alpha) $\alpha$.