---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-11-25 14:40:00

title: "Log model evidence for binomial observations"
chapter: "Statistical Models"
section: "Count data"
topic: "Binomial observations"
theorem: "Log Bayes factor"

sources:

proof_id: "P383"
shortcut: "bin-lbf"
username: "JoramSoch"
---


**Theorem:** Let $y$ be the number of successes resulting from $n$ independent trials with unknown success probability $p$, such that $y$ follows a [binomial distribution](/D/bin):

$$ \label{eq:Bin}
y \sim \mathrm{Bin}(n,p) \; .
$$

Moreover, assume two [statistical models](/D/fpm), one assuming that $p$ is 0.5 ([null model](/D/h0)), the other imposing a [beta distribution](/P/bin-prior) as the [prior distribution](/D/prior) on the model parameter $p$ ([alternative](/D/h1)):

$$ \label{eq:Bin-m01}
\begin{split}
m_0&: \; y \sim \mathrm{Bin}(n,p), \; p = 0.5 \\
m_1&: \; y \sim \mathrm{Bin}(n,p), \; p \sim \mathrm{Bet}(\alpha_0, \beta_0) \; .
\end{split}
$$

Then, the [log Bayes factor](/D/lbf) in favor of $m_1$ against $m_0$ is

$$ \label{eq:Bin-LBF}
\mathrm{LBF}_{10} = \log B(\alpha_n,\beta_n) - \log B(\alpha_0,\beta_0) - n \log \left( \frac{1}{2} \right)
$$

where $B(x,y)$ is the beta function and $\alpha_n$ and $\beta_n$ are the [posterior hyperparameters for binomial observations](/P/bin-post) which are functions of the [number of trials](/D/bin) $n$ and the [number of successes](/D/bin) $y$.


**Proof:** [The log Bayes factor is equal to the difference of two log model evidences](/P/lbf-lme):

$$ \label{eq:LBF-LME}
\mathrm{LBF}_{12} = \mathrm{LME}(m_1) - \mathrm{LME}(m_2) \; .
$$

The LME of the alternative $m_1$ is equal to the [log model evidence for binomial observations](/P/bin-lme):

$$ \label{eq:Bin-LME-m1}
\mathrm{LME}(m_1) = \log p(y|m_1) = \log {n \choose y} + \log B(\alpha_n,\beta_n) - \log B(\alpha_0,\beta_0) \; .
$$

Because the null model $m_0$ has no free parameter, its [log model evidence](/D/lme) (logarithmized [marginal likelihood](/D/ml)) is equal to the [log-likelihood function for binomial observations](/P/bin-mle) at the value $p = 0.5$:

$$ \label{eq:Bin-LME-m0}
\begin{split}
\mathrm{LME}(m_0) = \log p(y|p=0.5) &= \log {n \choose y} + y \log(0.5) + (n-y) \log (1-0.5)  \\
&= \log {n \choose y} + n \log \left( \frac{1}{2} \right) \; .
\end{split}
$$

Subtracting the two LMEs from each other, the LBF emerges as

$$ \label{eq:Bin-LBF-m10}
\mathrm{LBF}_{10} = \log B(\alpha_n,\beta_n) - \log B(\alpha_0,\beta_0) - n \log \left( \frac{1}{2} \right)
$$

where the [posterior hyperparameters](/D/post) [are given by](/P/bin-post)

$$ \label{eq:Bin-post-par}
\begin{split}
\alpha_n &= \alpha_0 + y \\
\beta_n &= \beta_0 + (n-y)
\end{split}
$$

with the [number of trials](/D/bin) $n$ and the [number of successes](/D/bin) $y$.