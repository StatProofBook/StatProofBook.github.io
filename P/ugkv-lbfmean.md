---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-03-24 10:03:00

title: "Expectation of the log Bayes factor for the univariate Gaussian with known variance"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Univariate Gaussian with known variance"
theorem: "Expectation of log Bayes factor"

sources:

proof_id: "P216"
shortcut: "ugkv-lbfmean"
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

Then, under the [null hypothesis](/D/h0) that $m_0$ generated the data, the [expectation](/D/mean) of the [log Bayes factor](/D/lbf) in favor of $m_1$ with $\mu_0 = 0$ against $m_0$ is

$$ \label{eq:UGkv-LBF}
\left\langle \mathrm{LBF}_{10} \right\rangle = \frac{1}{2} \log\left( \frac{\lambda_0}{\lambda_n} \right) + \frac{1}{2} \left( \frac{\lambda_n - \lambda_0}{\lambda_n} \right)
$$

where $\lambda_n$ is the [posterior precision for the univariate Gaussian with known variance](/P/ugkv-post).


**Proof:** The [log Bayes factor for the univariate Gaussian with known variance](/P/ugkv-lbf) is

$$ \label{eq:UGkv-LBF-m10-s1}
\mathrm{LBF}_{10} = \frac{1}{2} \log\left( \frac{\lambda_0}{\lambda_n} \right) - \frac{1}{2} \left( \lambda_0 \mu_0^2 - \lambda_n \mu_n^2 \right)
$$

where the [posterior hyperparameters](/D/post) [are given by](/P/ugkv-post)

$$ \label{eq:UGkv-post-par}
\begin{split}
\mu_n &= \frac{\lambda_0 \mu_0 + \tau n \bar{y}}{\lambda_0 + \tau n} \\
\lambda_n &= \lambda_0 + \tau n
\end{split}
$$

with the [sample mean](/D/mean-samp) $\bar{y}$ and the [inverse variance or precision](/D/prec) $\tau = 1/\sigma^2$. Plugging $\mu_n$ from \eqref{eq:UGkv-post-par} into \eqref{eq:UGkv-LBF-m10-s1}, we obtain:

$$ \label{eq:UGkv-LBF-m10-s2}
\begin{split}
\mathrm{LBF}_{10} &= \frac{1}{2} \log\left( \frac{\lambda_0}{\lambda_n} \right) - \frac{1}{2} \left( \lambda_0 \mu_0^2 - \lambda_n \, \frac{(\lambda_0 \mu_0 + \tau n \bar{y})^2}{\lambda_n^2} \right) \\
&= \frac{1}{2} \log\left( \frac{\lambda_0}{\lambda_n} \right) - \frac{1}{2} \left( \lambda_0 \mu_0^2 - \frac{1}{\lambda_n} (\lambda_0^2 \mu_0^2 - 2 \tau n \lambda_0 \mu_0 \bar{y} + \tau^2 (n \bar{y})^2) \right)
\end{split}
$$

Because $m_1$ uses a zero-mean [prior distribution](/D/prior) with prior [mean](/D/mean) $\mu_0 = 0$ per construction, the log Bayes factor simplifies to:

$$ \label{eq:UGkv-LBF-m10-s3}
\mathrm{LBF}_{10} = \frac{1}{2} \log\left( \frac{\lambda_0}{\lambda_n} \right) + \frac{1}{2} \left( \frac{\tau^2 (n \bar{y})^2}{\lambda_n} \right) \; .
$$

From \eqref{eq:ugkv}, we know that the data are distributed as $y_i \sim \mathcal{N}(\mu, \sigma^2)$, such that we can derive the [expectation](/D/mean) of $(n \bar{y})^2$ as follows:

$$ \label{eq:UGkv-E(ny2)}
\begin{split}
\left\langle (n \bar{y})^2 \right\rangle = \left\langle \sum_{i=1}^n \sum_{j=1}^n y_i y_j \right\rangle &= \left\langle n y_i^2 + (n^2-n) [y_i y_j]_{i \neq j} \right\rangle \\
&= n (\mu^2 + \sigma^2) + (n^2 - n) \mu^2 \\
&= n^2 \mu^2 + n \sigma^2 \; .
\end{split}
$$

Applying this [expected value](/D/mean) to \eqref{eq:UGkv-LBF-m10-s3}, the expected LBF emerges as:

$$ \label{eq:UGkv-LBF-m10-s4}
\begin{split}
\left\langle \mathrm{LBF}_{10} \right\rangle &= \frac{1}{2} \log\left( \frac{\lambda_0}{\lambda_n} \right) + \frac{1}{2} \left( \frac{\tau^2 (n^2 \mu^2 + n \sigma^2)}{\lambda_n} \right) \\
&= \frac{1}{2} \log\left( \frac{\lambda_0}{\lambda_n} \right) + \frac{1}{2} \left( \frac{(\tau n \mu)^2 + \tau n}{\lambda_n} \right)
\end{split}
$$

Under the [null hypothesis](/D/h0) that $m_0$ generated the data, the unknown mean is $\mu = 0$, such that the log Bayes factor further simplifies to:

$$ \label{eq:UGkv-LBF-m10-s5}
\left\langle \mathrm{LBF}_{10} \right\rangle = \frac{1}{2} \log\left( \frac{\lambda_0}{\lambda_n} \right) + \frac{1}{2} \left( \frac{\tau n}{\lambda_n} \right) \; .
$$

Finally, plugging $\lambda_n$ from \eqref{eq:UGkv-post-par} into \eqref{eq:UGkv-LBF-m10-s5}, we obtain:

$$ \label{eq:UGkv-LBF-m10-s6}
\left\langle \mathrm{LBF}_{10} \right\rangle = \frac{1}{2} \log\left( \frac{\lambda_0}{\lambda_n} \right) + \frac{1}{2} \left( \frac{\lambda_n - \lambda_0}{\lambda_n} \right) \; .
$$