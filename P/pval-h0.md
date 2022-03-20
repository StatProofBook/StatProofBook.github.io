---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-03-18 22:37:00

title: "The p-value follows a uniform distribution under the null hypothesis"
chapter: "General Theorems"
section: "Frequentist statistics"
topic: "Hypothesis testing"
theorem: "Distribution of p-value under null hypothesis"

sources:
  - authors: "jll"
    year: 2018
    title: "Why are p-values uniformly distributed under the null hypothesis?"
    in: "StackExchange CrossValidated"
    pages: "retrieved on 2022-03-18"
    url: "https://stats.stackexchange.com/a/11288"

proof_id: "P318"
shortcut: "pval-h0"
username: "JoramSoch"
---


**Theorem:** Under the [null hypothesis](/D/h0), the [p-value](/D/pval) in a [statistical test](/D/test) follows a [continuous uniform distribution](/D/cuni):

$$ \label{eq:pval-h0}
p \sim \mathcal{U}(0,1) \; .
$$


**Proof:** Without loss of generality, consider a [left-sided one-tailed hypothesis test](/D/hyp-tail). Then, [the p-value is equal to](/D/pval)

$$ \label{eq:pval}
p = F_T(t_\mathrm{obs})
$$

where $t_\mathrm{obs}$ is the [observed test statistic](/D/tstat) and $F_T(t)$ is the [cumulative distribution function](/D/cdf) of the [test statistic](/D/tstat) under the [null hypothesis](/D/h0).

Then, we can obtain the [cumulative distribution function](/D/cdf) of the [p-value](/D/pval) as

$$ \label{eq:pval-cdf-s1}
\begin{split}
F_P(p) &= \mathrm{Pr}(P < p) \\
&= \mathrm{Pr}(F_T^{-1}(P) < F_T^{-1}(p)) \\
&\overset{\eqref{eq:pval}}{=} \mathrm{Pr}(T < t_\mathrm{obs})
\end{split}
$$

Because the [p-value is the probability of obtaining a test statistic more extreme than the observed test statistic](/D/pval), we get

$$ \label{eq:pval-cdf-s2}
F_P(p) = \mathrm{Pr}(T < t_\mathrm{obs}) = p
$$

which is the [cumulative distribution function of a continuous uniform distribution](/P/cuni-cdf) over the interval $[0,1]$:

$$ \label{eq:cuni-cdf}
F_X(x) = \int_{-\infty}^{x} \mathcal{U}(z; 0, 1) \, \mathrm{d}z = x \quad \text{where} \quad 0 \leq x \leq 1 \; .
$$