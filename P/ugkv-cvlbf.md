---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-03-24 11:13:00

title: "Cross-validated log Bayes factor for the univariate Gaussian with known variance"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Univariate Gaussian with known variance"
theorem: "Cross-validated log Bayes factor"

sources:

proof_id: "P218"
shortcut: "ugkv-cvlbf"
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

Then, the [cross-validated](/D/cvlme) [log Bayes factor](/D/lbf) in favor of $m_1$ against $m_0$ is

$$ \label{eq:UGkv-cvLBF}
\mathrm{cvLBF}_{10} = \frac{S}{2} \log \left( \frac{S-1}{S} \right) - \frac{\tau}{2} \sum_{i=1}^S \left( \frac{\left(n_1 \bar{y}_1^{(i)}\right)^2}{n_1} - \frac{(n \bar{y})^2}{n} \right)
$$

where $\bar{y}$ is the [sample mean](/D/mean-samp), $\tau = 1/\sigma^2$ is the [inverse variance or precision](/D/prec), $y_1^{(i)}$ are the training data in the $i$-th cross-validation fold and $S$ is the [number of data subsets](/D/cvlme).


**Proof:** The [relationship between log Bayes factor and log model evidences](/P/lbf-lme) also holds for [cross-validated log bayes factor](/D/lbf) (cvLBF) and [cross-validated log model evidences](/D/cvlme) (cvLME):

$$ \label{eq:cvLBF-cvLME}
\mathrm{cvLBF}_{12} = \mathrm{cvLME}(m_1) - \mathrm{cvLME}(m_2) \; .
$$

The [cross-validated log model evidences](/D/cvlme) of $m_0$ and $m_1$ [are given by](/P/ugkv-cvlme)

$$ \label{eq:UGkv-cvLME-m01}
\begin{split}
\mathrm{cvLME}(m_0) &= \frac{n}{2} \log\left( \frac{\tau}{2 \pi} \right) - \frac{1}{2} \left( \tau y^\mathrm{T} y \right) \\
\mathrm{cvLME}(m_1) &= \frac{n}{2} \log \left( \frac{\tau}{2 \pi} \right) + \frac{S}{2} \log \left( \frac{S-1}{S} \right) - \frac{\tau}{2} \left[ y^\mathrm{T} y + \sum_{i=1}^S \left( \frac{\left(n_1 \bar{y}_1^{(i)}\right)^2}{n_1} - \frac{(n \bar{y})^2}{n} \right) \right] \; .
\end{split}
$$

Subtracting the two cvLMEs from each other, the cvLBF emerges as

$$ \label{eq:UGkv-cvLBF-qed}
\begin{split}
\mathrm{cvLBF}_{10} &= \mathrm{cvLME}(m_1) - \mathrm{LME}(m_0) \\
&= \left( \frac{n}{2} \log \left( \frac{\tau}{2 \pi} \right) + \frac{S}{2} \log \left( \frac{S-1}{S} \right) - \frac{\tau}{2} \left[ y^\mathrm{T} y + \sum_{i=1}^S \left( \frac{\left(n_1 \bar{y}_1^{(i)}\right)^2}{n_1} - \frac{(n \bar{y})^2}{n} \right) \right] \right) \\
&- \left( \frac{n}{2} \log \left( \frac{\tau}{2 \pi} \right) - \frac{1}{2} \left( \tau y^\mathrm{T} y \right) \right) \\
&= \frac{S}{2} \log \left( \frac{S-1}{S} \right) - \frac{\tau}{2} \sum_{i=1}^S \left( \frac{\left(n_1 \bar{y}_1^{(i)}\right)^2}{n_1} - \frac{(n \bar{y})^2}{n} \right) \; .
\end{split}
$$