---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2026-03-26 18:38:00

title: "Cross-validated log Bayes factor for multinomial observations"
chapter: "Statistical Models"
section: "Count data"
topic: "Multinomial observations"
theorem: "Cross-validated log Bayes factor"

sources:

proof_id: "P532"
shortcut: "mult-cvlbf"
username: "JoramSoch"
---


**Theorem:** Let $y = [y_1, \ldots, y_k] \in \mathbb{N}_0^{1 \times k}$ be the number of observations in $k$ categories resulting from $n$ independent trials with unknown category probabilities $p = [p_1, \ldots, p_k]$, such that $y$ follows a [multinomial distribution](/D/mult):

$$ \label{eq:Mult}
y \sim \mathrm{Mult}(n,p) \; .
$$

Moreover, assume two [statistical models](/D/fpm), one assuming that each $p_j$ is $1/k$ ([null model](/D/h0)), the other imposing a [Dirichlet distribution](/P/mult-prior) as the [prior distribution](/D/prior) on the model parameters $p_1, \ldots, p_k$ ([alternative](/D/h1)):

$$ \label{eq:Mult-m01}
\begin{split}
m_0 &: \; y \sim \mathrm{Mult}(n,p), \; p = [1/k, \ldots, 1/k] \\
m_1 &: \; y \sim \mathrm{Mult}(n,p), \; p \sim \mathrm{Dir}(\alpha_0) \; .
\end{split}
$$

Then, the [cross-validated](/D/cvlme) [log Bayes factor](/D/cvlbf) in favor of $m_1$ against $m_0$ is

$$ \label{eq:Mult-cvLBF}
\mathrm{cvLBF}_{10} = S \cdot \log \frac{\Gamma(n_1)}{\Gamma(y)} - \sum_{i=1}^S \sum_{j=1}^k \log \left( \frac{y_{1j}^{(i)}}{y_j} \right) + n \log(k)
$$

where $y_1^{(i)}$ are the training data with $n_1$ data points in the $i$-th cross-validation fold, $S$ is the [number of data subsets](/D/cvlme) and $\Gamma(x)$ is the gamma function.


**Proof:** The [relationship between log Bayes factor and log model evidences](/P/lbf-lme) also holds for [cross-validated log bayes factor](/D/lbf) (cvLBF) and [cross-validated log model evidences](/D/cvlme) (cvLME):

$$ \label{eq:cvLBF-cvLME}
\mathrm{cvLBF}_{12} = \mathrm{cvLME}(m_1) - \mathrm{cvLME}(m_2) \; .
$$

The [cross-validated log model evidences](/D/cvlme) of $m_0$ and $m_1$ [are given by](/P/mult-cvlme)

$$ \label{eq:Mult-cvLME-m01}
\begin{split}
\mathrm{cvLME}(m_0) &= -n \log(k) + \sum_{i=1}^S \left[ \log {n_2 \choose {y_{21}^{(i)}, \ldots, y_{2k}^{(i)}}} \right] \\
\mathrm{cvLME}(m_1) &= S \cdot \log \frac{\Gamma(n_1)}{\Gamma(y)} + \sum_{i=1}^S \left[ \log {n_2 \choose {y_{21}^{(i)}, \ldots, y_{2k}^{(i)}}} - \sum_{j=1}^k \log \left( \frac{y_{1j}^{(i)}}{y_j} \right) \right] \; .
\end{split}
$$

Subtracting the two cvLMEs from each other, the cvLBF emerges as

$$ \label{eq:Mult-cvLBF-qed}
\begin{split}
\mathrm{cvLBF}_{10} &= \mathrm{cvLME}(m_1) - \mathrm{LME}(m_0) \\
&= \left( S \cdot \log \frac{\Gamma(n_1)}{\Gamma(y)} + \sum_{i=1}^S \left[ \log {n_2 \choose {y_{21}^{(i)}, \ldots, y_{2k}^{(i)}}} - \sum_{j=1}^k \log \left( \frac{y_{1j}^{(i)}}{y_j} \right) \right] \right) \\
&- \left( -n \log(k) + \sum_{i=1}^S \left[ \log {n_2 \choose {y_{21}^{(i)}, \ldots, y_{2k}^{(i)}}} \right] \right) \\
&= S \cdot \log \frac{\Gamma(n_1)}{\Gamma(y)} - \sum_{i=1}^S \sum_{j=1}^k \log \left( \frac{y_{1j}^{(i)}}{y_j} \right) + n \log(k) \; .
\end{split}
$$