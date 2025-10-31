---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2025-03-07 01:14:00

title: "Cross-validated log Bayes factor for the univariate Gaussian"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Univariate Gaussian"
theorem: "Cross-validated log Bayes factor"

sources:

proof_id: "P491"
shortcut: "ug-cvlbf"
username: "JoramSoch"
---


**Theorem:** Let

$$ \label{eq:UG}
y = \left\lbrace y_1, \ldots, y_n \right\rbrace, \quad y_i \sim \mathcal{N}(\mu, \sigma^2), \quad i = 1, \ldots, n
$$

be a [univariate Gaussian data set](/D/ug) with unknown mean $\mu$ and unknown variance $\sigma^2$. Moreover, assume two [statistical models](/D/fpm), one assuming that $\mu$ is zero ([null model](/D/h0)), the other imposing a [normal distribution](/P/ug-prior) as the [prior distribution](/D/prior) on the [mean parameter](/D/mean) $\mu$ ([alternative](/D/h1)) and both imposing a [gamma distribtion](/P/ug-prior) on the [precision parameter](/D/prec) $\tau = 1/\sigma^2$:

$$ \label{eq:UG-m01}
\begin{split}
m_0 &: \; y_i \sim \mathcal{N}(\mu, \tau^{-1}), \; \mu = 0, \; \tau \sim \mathrm{Gam}(a_0, b_0) \\
m_1 &: \; y_i \sim \mathcal{N}(\mu, \tau^{-1}), \; \mu|\tau \sim \mathcal{N}(\mu_0, (\tau \lambda_0)^{-1}), \; \tau \sim \mathrm{Gam}(a_0, b_0)
\end{split}
$$

Then, the [cross-validated](/D/cvlme) [log Bayes factor](/D/lbf) in favor of $m_1$ against $m_0$ is

$$ \label{eq:UG-cvLBF}
\mathrm{cvLBF}_{10} = \frac{S}{2} \log \left( \frac{S-1}{S} \right) - \frac{S \cdot n}{2} \left[ \log \left( 1 - \frac{n {\bar{y}}^2}{y^\mathrm{T} y} \right) \right] + \frac{n_1}{2} \sum_{i=1}^S \left[ \log \left( 1 - \frac{ n_1 \bar{y}_1^{(i)} }{ {y_1^{(i)}}^\mathrm{T} y_1^{(i)} } \right) \right]
$$

where $\bar{y}$ is the [sample mean](/D/mean-samp), $y_1^{(i)}$ are the training data in the $i$-th cross-validation fold with $n_1$ data points and $S$ is the [number of data subsets](/D/cvlme).


**Proof:** The [relationship between log Bayes factor and log model evidences](/P/lbf-lme) also holds for [cross-validated log bayes factor](/D/lbf) (cvLBF) and [cross-validated log model evidences](/D/cvlme) (cvLME):

$$ \label{eq:cvLBF-cvLME}
\mathrm{cvLBF}_{12} = \mathrm{cvLME}(m_1) - \mathrm{cvLME}(m_2) \; .
$$

The [cross-validated log model evidences](/D/cvlme) of $m_0$ and $m_1$ [are given by](/P/ug-cvlme)

$$ \label{eq:UG-cvLME-m01}
\begin{split}
  \mathrm{cvLME}(m_0)
= & - \frac{n}{2} \log (2 \pi) + S \cdot \log \Gamma \left( \frac{n}{2} \right) - S \cdot \log \Gamma \left( \frac{1}{2} \frac{S-1}{S} n \right) \\
  &- \frac{S \cdot n}{2} \log \left[ \frac{1}{2} \left( y^\mathrm{T} y \right) \right] + \frac{n_1}{2} \sum_{i=1}^S \log \left[ \frac{1}{2} \left( {y_1^{(i)}}^\mathrm{T} y_1^{(i)} \right) \right] \\
  \mathrm{cvLME}(m_1)
= & - \frac{n}{2} \log (2 \pi) + \frac{S}{2} \log \left( \frac{S-1}{S} \right) + S \cdot \log \Gamma \left( \frac{n}{2} \right) - S \cdot \log \Gamma \left( \frac{1}{2} \frac{S-1}{S} n \right) \\
  &- \frac{S \cdot n}{2} \log \left[ \frac{1}{2} \left( y^\mathrm{T} y - n {\bar{y}}^2 \right) \right] + \frac{n_1}{2} \sum_{i=1}^S \log \left[ \frac{1}{2} \left( {y_1^{(i)}}^\mathrm{T} y_1^{(i)} - n_1 \bar{y}_1^{(i)} \right) \right] \; .
\end{split}
$$

Subtracting the two cvLMEs from each other, the cvLBF emerges as

$$ \label{eq:UG-cvLBF-qed}
\begin{split}
  \mathrm{cvLBF}_{10}
= &\; \mathrm{cvLME}(m_1) - \mathrm{LME}(m_0) \\
= &+  \frac{S}{2} \log \left( \frac{S-1}{S} \right) - \frac{S \cdot n}{2} \left[ \log \left( \frac{1}{2} \left( y^\mathrm{T} y - n {\bar{y}}^2 \right) \right) - \log \left( \frac{1}{2} \left( y^\mathrm{T} y \right) \right) \right] \\
  &+  \frac{n_1}{2} \sum_{i=1}^S \left[ \log \left( \frac{1}{2} \left( {y_1^{(i)}}^\mathrm{T} y_1^{(i)} - n_1 \bar{y}_1^{(i)} \right) \right) - \log \left( \frac{1}{2} \left( {y_1^{(i)}}^\mathrm{T} y_1^{(i)} \right) \right) \right] \\
= &\; \frac{S}{2} \log \left( \frac{S-1}{S} \right) - \frac{S \cdot n}{2} \left[ \log \left( \frac{y^\mathrm{T} y - n {\bar{y}}^2}{y^\mathrm{T} y} \right) \right] + \frac{n_1}{2} \sum_{i=1}^S \left[ \log \left( \frac{ {y_1^{(i)}}^\mathrm{T} y_1^{(i)} - n_1 \bar{y}_1^{(i)} }{ {y_1^{(i)}}^\mathrm{T} y_1^{(i)} } \right) \right] \\
= &\; \frac{S}{2} \log \left( \frac{S-1}{S} \right) - \frac{S \cdot n}{2} \left[ \log \left( 1 - \frac{n {\bar{y}}^2}{y^\mathrm{T} y} \right) \right] + \frac{n_1}{2} \sum_{i=1}^S \left[ \log \left( 1 - \frac{ n_1 \bar{y}_1^{(i)} }{ {y_1^{(i)}}^\mathrm{T} y_1^{(i)} } \right) \right] \; .
\end{split}
$$