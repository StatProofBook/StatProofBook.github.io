---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-03-24 12:27:00

title: "Expectation of the cross-validated log Bayes factor for the univariate Gaussian with known variance"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Univariate Gaussian with known variance"
theorem: "Expectation of cross-validated log Bayes factor"

sources:

proof_id: "P219"
shortcut: "ugkv-cvlbfmean"
username: "JoramSoch"
---


**Theorem:** Let

$$ \label{eq:ugkv}
y = \left\lbrace y_1, \ldots, y_n \right\rbrace, \quad y_i \sim \mathcal{N}(\mu, \sigma^2), \quad i = 1, \ldots, n
$$

be a [univariate Gaussian data set](/D/ugkv) with unknown mean $\mu$ and known variance $\sigma^2$. Moreover, assume two [statistical models](/D/fpm), one assuming that $\mu$ is zero ([null model](/D/h0)), the other imposing a [normal distribution](/P/ugkv-prior) as the [prior distribution](/D/prior) on the model parameter $\mu$ ([alternative](/D/h1)):

$$ \label{eq:UGkv-m01}
\begin{split}
m_0&: \; y_i \sim \mathcal{N}(\mu, \sigma^2), \; \mu = 0 \\
m_1&: \; y_i \sim \mathcal{N}(\mu, \sigma^2), \; \mu \sim \mathcal{N}(\mu_0, \lambda_0^{-1}) \; .
\end{split}
$$

Then, the [expectation](/D/mean) of the [cross-validated](/D/cvlme) [log Bayes factor](/D/lbf) (cvLBF) in favor of $m_1$ against $m_0$ is

$$ \label{eq:UGkv-cvLBF}
\left\langle \mathrm{cvLBF}_{10} \right\rangle = \frac{S}{2} \log \left( \frac{S-1}{S} \right) + \frac{1}{2} \left[ \tau n \mu^2 \right]
$$

where $\tau = 1/\sigma^2$ is the [inverse variance or precision](/D/prec) and $S$ is the number of [data subsets](/D/cvlme).


**Proof:** The [cross-validated log Bayes factor for the univariate Gaussian with known variance](/P/ugkv-cvlbf) is

$$ \label{eq:UGkv-cvLBF-m10-s1}
\mathrm{cvLBF}_{10} = \frac{S}{2} \log \left( \frac{S-1}{S} \right) - \frac{\tau}{2} \sum_{i=1}^S \left( \frac{\left(n_1 \bar{y}_1^{(i)}\right)^2}{n_1} - \frac{(n \bar{y})^2}{n} \right)
$$

From \eqref{eq:ugkv}, we know that the data are distributed as $y_i \sim \mathcal{N}(\mu, \sigma^2)$, such that we can derive the [expectation](/D/mean) of $(n \bar{y})^2$ and $\left(n_1 \bar{y}_1^{(i)}\right)^2$ as follows:

$$ \label{eq:UGkv-E(ny2)}
\begin{split}
\left\langle (n \bar{y})^2 \right\rangle = \left\langle \sum_{i=1}^n \sum_{j=1}^n y_i y_j \right\rangle &= \left\langle n y_i^2 + (n^2-n) [y_i y_j]_{i \neq j} \right\rangle \\
&= n (\mu^2 + \sigma^2) + (n^2 - n) \mu^2 \\
&= n^2 \mu^2 + n \sigma^2 \; .
\end{split}
$$

Applying this [expected value](/D/mean) to \eqref{eq:UGkv-cvLBF-m10-s1}, the expected cvLBF emerges as:

$$ \label{eq:UGkv-cvLBF-m10-s2}
\begin{split}
\left\langle \mathrm{cvLBF}_{10} \right\rangle &= \left\langle \frac{S}{2} \log \left( \frac{S-1}{S} \right) - \frac{\tau}{2} \sum_{i=1}^S \left( \frac{\left(n_1 \bar{y}_1^{(i)}\right)^2}{n_1} - \frac{(n \bar{y})^2}{n} \right) \right\rangle \\
&= \frac{S}{2} \log \left( \frac{S-1}{S} \right) - \frac{\tau}{2} \sum_{i=1}^S \left( \frac{\left\langle \left(n_1 \bar{y}_1^{(i)}\right)^2 \right\rangle}{n_1} - \frac{\left\langle (n \bar{y})^2 \right\rangle}{n} \right) \\
&\overset{\eqref{eq:UGkv-E(ny2)}}{=} \frac{S}{2} \log \left( \frac{S-1}{S} \right) - \frac{\tau}{2} \sum_{i=1}^S \left( \frac{n_1^2 \mu^2 + n_1 \sigma^2}{n_1} - \frac{n^2 \mu^2 + n \sigma^2}{n} \right) \\
&= \frac{S}{2} \log \left( \frac{S-1}{S} \right) - \frac{\tau}{2} \sum_{i=1}^S \left( [n_1 \mu^2 + \sigma^2] - [n \mu^2 + \sigma^2] \right) \\
&= \frac{S}{2} \log \left( \frac{S-1}{S} \right) - \frac{\tau}{2} \sum_{i=1}^S (n_1 - n) \mu^2
\end{split}
$$

Because [it holds that](/P/ugkv-cvlme) $n_1 + n_2 = n$ and $n_2 = n/S$, we finally have:

$$ \label{eq:UGkv-cvLBF-m10-s3}
\begin{split}
\left\langle \mathrm{cvLBF}_{10} \right\rangle &= \frac{S}{2} \log \left( \frac{S-1}{S} \right) - \frac{\tau}{2} \sum_{i=1}^S (-n_2) \mu^2 \\
&= \frac{S}{2} \log \left( \frac{S-1}{S} \right) + \frac{1}{2} \left[ \tau n \mu^2 \right] \; .
\end{split}
$$