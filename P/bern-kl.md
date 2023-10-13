---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2023-10-13 15:20:57

title: "Kullback-Leibler divergence for the Bernoulli distribution"
chapter: "Probability Distributions"
section: "Univariate discrete distributions"
topic: "Bernoulli distribution"
theorem: "Kullback-Leibler divergence"

sources:

proof_id: "P419"
shortcut: "bern-kl"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar). Assume two [Bernoulli distributions](/D/bern) $P$ and $Q$ specifying the probability distribution of $X$ as

$$ \label{eq:berns}
\begin{split}
P: \; X &\sim \mathrm{Bern}(p_1) \\
Q: \; X &\sim \mathrm{Bern}(p_2) \; .
\end{split}
$$

Then, the [Kullback-Leibler divergence](/D/kl) of $P$ from $Q$ is given by

$$ \label{eq:bern-KL}
\mathrm{KL}[P\,||\,Q] = \ln \frac{1-p_1}{1-p_2} + p_1 \cdot \ln \frac{p_1 \, (1-p_2)}{p_2 \, (1-p_1)} \; .
$$


**Proof:** The [KL divergence for a discrete random variable](/D/kl) is given by 

$$ \label{eq:KL-disc}
\mathrm{KL}[P\,||\,Q] = \sum_{x \in \mathcal{X}} p(x) \, \ln \frac{p(x)}{q(x)}
$$

which, applied to the [Bernoulli distributions](/D/bern) in \eqref{eq:berns}, yields

$$ \label{eq:bern-KL-s1}
\begin{split}
\mathrm{KL}[P\,||\,Q] &= \sum_{x \in \left\lbrace 0,1 \right\rbrace} p(x) \, \ln \frac{p(x)}{q(x)} \\
&= p(X=0) \cdot \ln \frac{p(X=0)}{q(X=0)} + p(X=0) \cdot \ln \frac{p(X=0)}{q(X=0)} \; .
\end{split}
$$

Using the [probability mass function of the Bernoulli distribution](/P/bern-pmf), this becomes:

$$ \label{eq:bern-KL-s2}
\begin{split}
\mathrm{KL}[P\,||\,Q] &= (1-p_1) \cdot \ln \frac{1-p_1}{1-p_2} + p_1 \cdot \ln \frac{p_1}{p_2} \\
&= \ln \frac{1-p_1}{1-p_2} + p_1 \cdot \ln \frac{p_1}{p_2} - p_1 \cdot \ln \frac{1-p_1}{1-p_2} \\
&= \ln \frac{1-p_1}{1-p_2} + p_1 \cdot \left( \ln \frac{p_1}{p_2} + \ln \frac{1-p_2}{1-p_1} \right) \\
&= \ln \frac{1-p_1}{1-p_2} + p_1 \cdot \ln \frac{p_1 \, (1-p_2)}{p_2 \, (1-p_1)}
\end{split}
$$