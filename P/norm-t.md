---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-05-27 08:10:00

title: "Relationship between normal distribution and t-distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Normal distribution"
theorem: "Relationship to t-distribution"

sources:
  - authors: "Wikipedia"
    year: 2021
    title: "Student's t-distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-05-27"
    url: "https://en.wikipedia.org/wiki/Student%27s_t-distribution#Characterization"
  - authors: "Wikipedia"
    year: 2021
    title: "Normal distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-05-27"
    url: "https://en.wikipedia.org/wiki/Normal_distribution#Operations_on_multiple_independent_normal_variables"

proof_id: "P234"
shortcut: "norm-t"
username: "JoramSoch"
---


**Theorem:** Let $X_1, \ldots, X_n$ be [independent](/D/ind) [random variables](/D/rvar) where each of them is following a [normal distribution](/D/norm) with mean $\mu$ and variance $\sigma^2$:

$$ \label{eq:norm}
X_i \sim \mathcal{N}(\mu, \sigma^2) \quad \text{for} \quad i = 1, \ldots, n \; .
$$

Define the [sample mean](/D/mean-samp)

$$ \label{eq:mean-samp}
\bar{X} = \frac{1}{n} \sum_{i=1}^{n} X_i
$$

and the [unbiased sample variance](/D/var-samp)

$$ \label{eq:var-samp}
s^2 = \frac{1}{n-1} \sum_{i=1}^{n} \left( X_i - \bar{X} \right)^2 \; .
$$

Then, subtracting $\mu$ from the sample [mean](/D/mean), dividing by the sample [standard deviation](/D/std) and multiplying with $\sqrt{n}$ results in a qunatity that follows a [t-distribution](/D/t) with $n-1$ degrees of freedom:

$$ \label{eq:norm-t}
t = \sqrt{n} \, \frac{\bar{X}-\mu}{s} \sim \mathrm{t}(n-1) \; .
$$


**Proof:** Note that $\bar{X}$ is a linear combination of $X_1, \ldots, X_n$:

$$ \label{eq:X-bar-lincomb}
\bar{X} = \frac{1}{n} X_1, + \ldots + \frac{1}{n} X_n \; .
$$

Because the [linear combination of independent normal random variables is also normally distributed](/P/norm-lincomb), we have:

$$ \label{eq:X-bar-dist}
\bar{X} \sim \mathcal{N}\left( \frac{1}{n} \, n \mu, \left(\frac{1}{n}\right)^2 n \sigma^2 \right) = \mathcal{N}\left( \mu, \sigma^2/n \right) \; .
$$

Let $Z = \sqrt{n} \, (\bar{X}-\mu)/\sigma$. Because $Z$ is [a linear transformation](/P/mvn-ltt) of $\bar{X}$, it also follows a normal distribution:

$$ \label{eq:Z-dist}
Z = \sqrt{n} \frac{\bar{X}-\mu}{\sigma} \sim \mathcal{N}\left( \frac{\sqrt{n}}{\sigma} (\mu - \mu), \left(\frac{\sqrt{n}}{\sigma}\right)^2 \sigma^2/n \right) = \mathcal{N}\left( 0, 1 \right) \; .
$$

Let $V = (n-1) \, s^2/\sigma^2$. We know that [this function of the sample variance follows a chi-squared distribution](/P/norm-chi2) with $n-1$ degrees of freedom:

$$ \label{eq:V-dist}
V = (n-1) \frac{s^2}{\sigma^2} \sim \chi^2(n-1) \; .
$$

Observe that $t$ is the ratio of a [standard normal random variable](/D/snorm) and the square root of a [chi-squared random variable](/D/chi2), divided by its degrees of freedom:

$$ \label{eq:t-Z-V}
t = \sqrt{n} \, \frac{\bar{X}-\mu}{s} = \frac{\sqrt{n} \frac{\bar{X}-\mu}{\sigma}}{\sqrt{(n-1) \frac{s^2}{\sigma^2}/(n-1)}} =  \frac{Z}{\sqrt{V/(n-1)}} \; .
$$

Thus, by [definition of the t-distribution](/D/t), this ratio follows a t-distribution with $n-1$ degrees of freedom:

$$ \label{eq:norm-t-qed}
t \sim \mathrm{t}(n-1) \; .
$$