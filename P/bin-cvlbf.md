---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2026-03-26 18:08:00

title: "Cross-validated log Bayes factor for binomial observations"
chapter: "Statistical Models"
section: "Count data"
topic: "Binomial observations"
theorem: "Cross-validated log Bayes factor"

sources:

proof_id: "P531"
shortcut: "bin-cvlbf"
username: "JoramSoch"
---


**Theorem:** Let $y$ be the number of successes resulting from $n$ independent trials with unknown success probability $p$, such that $y$ follows a binomial distribution:

$$ \label{eq:Bin}
y \sim \mathrm{Bin}(n,p) \; .
$$

Moreover, assume two [statistical models](/D/fpm), one assuming that $p$ is 0.5 ([null model](/D/h0)), the other imposing a [beta distribution](/P/bin-prior) as the [prior distribution](/D/prior) on the model parameter $p$ ([alternative](/D/h1)):

$$ \label{eq:Bin-m01}
\begin{split}
m_0 &: \; y \sim \mathrm{Bin}(n,p), \; p = 0.5 \\
m_1 &: \; y \sim \mathrm{Bin}(n,p), \; p \sim \mathrm{Bet}(\alpha_0, \beta_0) \; .
\end{split}
$$

Then, the [cross-validated](/D/cvlme) [log Bayes factor](/D/lbf) in favor of $m_1$ against $m_0$ is

$$ \label{eq:Bin-cvLBF}
\mathrm{cvLBF}_{10} = S \cdot \log B(y, n-y) - \sum_{i=1}^S \log B \left( y_1^{(i)}, n_1 - y_1^{(i)} \right) + n \log(2)
$$

where $y_1^{(i)}$ are the training data with $n_1$ data points in the $i$-th cross-validation fold, $S$ is the [number of data subsets](/D/cvlme) and $B(x,y)$ is the beta function.


**Proof:** The [relationship between log Bayes factor and log model evidences](/P/lbf-lme) also holds for [cross-validated log bayes factor](/D/lbf) (cvLBF) and [cross-validated log model evidences](/D/cvlme) (cvLME):

$$ \label{eq:cvLBF-cvLME}
\mathrm{cvLBF}_{12} = \mathrm{cvLME}(m_1) - \mathrm{cvLME}(m_2) \; .
$$

The [cross-validated log model evidences](/D/cvlme) of $m_0$ and $m_1$ [are given by](/P/bin-cvlme)

$$ \label{eq:Bin-cvLME-m01}
\begin{split}
\mathrm{cvLME}(m_0) &= -n \log(2) + \sum_{i=1}^S \left[ \log {n_2 \choose y_2^{(i)}} \right] \\
\mathrm{cvLME}(m_1) &= S \cdot \log B(y, n-y) + \sum_{i=1}^S \left[ \log {n_2 \choose y_2^{(i)}} - \log B \left( y_1^{(i)}, n_1 - y_1^{(i)} \right) \right]
\end{split}
$$

Subtracting the two cvLMEs from each other, the cvLBF emerges as

$$ \label{eq:Bin-cvLBF-qed}
\begin{split}
\mathrm{cvLBF}_{10} &= \mathrm{cvLME}(m_1) - \mathrm{LME}(m_0) \\
&= \left( S \cdot \log B(y, n-y) + \sum_{i=1}^S \left[ \log {n_2 \choose y_2^{(i)}} - \log B \left( y_1^{(i)}, n_1 - y_1^{(i)} \right) \right] \right) \\
&- \left( -n \log(2) + \sum_{i=1}^S \left[ \log {n_2 \choose y_2^{(i)}} \right] \right) \\
&= S \cdot \log B(y, n-y) - \sum_{i=1}^S \log B \left( y_1^{(i)}, n_1 - y_1^{(i)} \right) + n \log(2) \; .
\end{split}
$$