---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-03-24 09:05:00

title: "Log Bayes factor for the univariate Gaussian with known variance"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Univariate Gaussian with known variance"
theorem: "Log Bayes factor"

sources:

proof_id: "P215"
shortcut: "ugkv-lbf"
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

Then, the [log Bayes factor](/D/lbf) in favor of $m_1$ against $m_0$ is

$$ \label{eq:UGkv-LBF}
\mathrm{LBF}_{10} = \frac{1}{2} \log\left( \frac{\lambda_0}{\lambda_n} \right) - \frac{1}{2} \left( \lambda_0 \mu_0^2 - \lambda_n \mu_n^2 \right)
$$

where $\mu_n$ and $\lambda_n$ are the [posterior hyperparameters for the univariate Gaussian with known variance](/P/ugkv-post) which are functions of the [inverse variance or precision](/D/prec) $\tau = 1/\sigma^2$ and the [sample mean](/D/mean-samp) $\bar{y}$.


**Proof:** [The log Bayes factor is equal to the difference of two log model evidences](/P/lbf-lme):

$$ \label{eq:LBF-LME}
\mathrm{LBF}_{12} = \mathrm{LME}(m_1) - \mathrm{LME}(m_2) \; .
$$

The LME of the alternative $m_1$ is equal to the [log model evidence for the univariate Gaussian with known variance](/P/ugkv-lme):

$$ \label{eq:UGkv-LME-m1}
\mathrm{LME}(m_1) = \frac{n}{2} \log\left( \frac{\tau}{2 \pi} \right) + \frac{1}{2} \log\left( \frac{\lambda_0}{\lambda_n} \right) - \frac{1}{2} \left( \tau y^\mathrm{T} y + \lambda_0 \mu_0^2 - \lambda_n \mu_n^2 \right) \; .
$$

Because the null model $m_0$ has no free parameter, its [log model evidence](/D/lme) (logarithmized [marginal likelihood](/D/ml)) is equal to the [log-likelihood function for the univariate Gaussian with known variance](/P/ugkv-mle) at the value $\mu = 0$:

$$ \label{eq:UGkv-LME-m0}
\mathrm{LME}(m_0) = \log p(y|\mu=0) = \frac{n}{2} \log\left( \frac{\tau}{2 \pi} \right) - \frac{1}{2} \left( \tau y^\mathrm{T} y \right) \; .
$$

Subtracting the two LMEs from each other, the LBF emerges as

$$ \label{eq:UGkv-LBF-m10}
\mathrm{LBF}_{10} = \mathrm{LME}(m_1) - \mathrm{LME}(m_0) = \frac{1}{2} \log\left( \frac{\lambda_0}{\lambda_n} \right) - \frac{1}{2} \left( \lambda_0 \mu_0^2 - \lambda_n \mu_n^2 \right)
$$

where the [posterior hyperparameters](/D/post) [are given by](/P/ugkv-post)

$$ \label{eq:UGkv-post-par}
\begin{split}
\mu_n &= \frac{\lambda_0 \mu_0 + \tau n \bar{y}}{\lambda_0 + \tau n} \\
\lambda_n &= \lambda_0 + \tau n
\end{split}
$$

with the [sample mean](/D/mean-samp) $\bar{y}$ and the [inverse variance or precision](/D/prec) $\tau = 1/\sigma^2$.