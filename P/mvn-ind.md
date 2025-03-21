---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-06-02 09:22:00

title: "Necessary and sufficient condition for independence of multivariate normal random variables"
chapter: "Probability Distributions"
section: "Multivariate continuous distributions"
topic: "Multivariate normal distribution"
theorem: "Conditions for independence"

sources:

proof_id: "P236"
shortcut: "mvn-ind"
username: "JoramSoch"
---


**Theorem:** Let $x$ be an $n \times 1$ [random vector](/D/rvec) following a [multivariate normal distribution](/D/mvn):

$$ \label{eq:mvn}
x \sim \mathcal{N}(\mu, \Sigma) \; .
$$

Then, the components of $x$ are [statistically independent](/D/ind), if and only if the [covariance matrix](/D/covmat) is a diagonal matrix:

$$ \label{eq:mvn-ind}
p(x) = p(x_1) \cdot \ldots \cdot p(x_n) \quad \Leftrightarrow \quad \Sigma = \mathrm{diag}\left( \left[ \sigma^2_1, \ldots, \sigma^2_n \right] \right) \; .
$$


**Proof:** The [marginal distribution of one entry from a multivariate normal random vector is a univariate normal distribution](/P/mvn-marg) where [mean](/D/mean) and [variance](/D/var) are equal to the corresponding entries of the mean vector and covariance matrix:

$$ \label{eq:mvn-marg}
x \sim \mathcal{N}(\mu, \Sigma) \quad \Rightarrow \quad x_i \sim \mathcal{N}(\mu_i, \sigma^2_{ii}) \; .
$$

The [probability density function of the multivariate normal distribution](/P/mvn-pdf) is

$$ \label{eq:mvn-pdf}
p(x) = \frac{1}{\sqrt{(2 \pi)^n |\Sigma|}} \cdot \exp \left[ -\frac{1}{2} (x-\mu)^\mathrm{T} \Sigma^{-1} (x-\mu) \right]
$$

and the [probability density function of the univariate normal distribution](/P/norm-pdf) is

$$ \label{eq:norm-pdf}
p(x_i) = \frac{1}{\sqrt{2 \pi \sigma^2_i}} \cdot \exp \left[ -\frac{1}{2} \left( \frac{x_i-\mu_i}{\sigma_i} \right)^2 \right] \; .
$$

<br>
1) Let

$$ \label{eq:x-ind}
p(x) = p(x_1) \cdot \ldots \cdot p(x_n) \; .
$$

Then, because the [covariance is zero under independence](/P/cov-ind), the [entries of the covariance matrix are the pair-wise covariances](/D/covmat) and the [covariance matrix of the multivariate normal distribution](/P/mvn-cov) is equal to $\Sigma$, we have

$$ \label{eq:Sigma-diag-s1}
\Sigma = \mathrm{diag}\left( \left[ \mathrm{Cov}(x_1,x_1), \ldots, \mathrm{Cov}(x_n,x_n) \right] \right) \; .
$$

Moreover, because the [diagonal entries of the covariance matrix are the element-wise variances](/P/cov-var) and the [variance of the univariate normal distribution](/P/norm-var) is equal to $\sigma^2$ and equating $\sigma^2\_i = \sigma^2\_{ii}$ from \eqref{eq:mvn-marg}, we get

$$ \label{eq:Sigma-diag-s2}
\Sigma = \mathrm{diag}\left( \left[ \sigma^2_1, \ldots, \sigma^2_n \right] \right) \; .
$$


<br>
2) Let

$$ \label{eq:Sigma-diag}
\Sigma = \mathrm{diag}\left( \left[ \sigma^2_1, \ldots, \sigma^2_n \right] \right) \; .
$$

Then, we have

$$ \label{eq:Sigma-diag-dev}
\begin{split}
p(x) &\overset{\eqref{eq:mvn-pdf}}{=} \frac{1}{\sqrt{(2 \pi)^n |\mathrm{diag}\left( \left[ \sigma^2_1, \ldots, \sigma^2_n \right] \right)|}} \cdot \exp \left[ -\frac{1}{2} (x-\mu)^\mathrm{T} \mathrm{diag}\left( \left[ \sigma^2_1, \ldots, \sigma^2_n \right] \right)^{-1} (x-\mu) \right] \\
&= \frac{1}{\sqrt{(2 \pi)^n \prod_{i=1}^{n} \sigma^2_i}} \cdot \exp \left[ -\frac{1}{2} (x-\mu)^\mathrm{T} \mathrm{diag}\left( \left[ 1/\sigma^2_1, \ldots, 1/\sigma^2_n \right] \right) (x-\mu) \right] \\
&= \frac{1}{\sqrt{(2 \pi)^n \prod_{i=1}^{n} \sigma^2_i}} \cdot \exp \left[ -\frac{1}{2} \sum_{i=1}^{n} \frac{(x_i-\mu_i)^2}{\sigma^2_i} \right] \\
&= \prod_{i=1}^n \frac{1}{\sqrt{2 \pi \sigma^2_i}} \cdot \exp \left[ -\frac{1}{2} \left( \frac{x_i-\mu_i}{\sigma_i} \right)^2 \right]
\end{split}
$$

which implies that

$$ \label{eq:x-ind-qed}
p(x) = p(x_1) \cdot \ldots \cdot p(x_n) \; .
$$