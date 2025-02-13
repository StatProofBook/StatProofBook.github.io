---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2025-02-06 10:12:43

title: "Marginal distributions of the multinomial distribution"
chapter: "Probability Distributions"
section: "Multivariate discrete distributions"
topic: "Multinomial distribution"
theorem: "Marginal distributions"

sources:

proof_id: "P485"
shortcut: "mult-marg"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random vector](/D/rvec) following a [multinomial distribution](/D/mult):

$$ \label{eq:mult}
X \sim \mathrm{Mult}(n,\left[p_1, \ldots, p_k \right]) \; .
$$

Then, the [marginal distribution](/D/dist-marg) of any entry $X_i$ is a [binomial distribution](/D/bin):

$$ \label{eq:mult-marg}
X_i \sim \mathrm{Bin}(n, p_i)
\quad \text{for all} \quad
i = 1, \ldots, k \; .
$$


**Proof:** The entries of a [multinomial](/D/mult) random vector $X$ are the numbers of observations belonging to $k$ distinct categories in $n$ [independent](/D/ind) trials where $p_1, \ldots, p_k$ are the [category probabilities](/D/mult) identical across trials.

Let us define for each category $i = 1, \ldots, k$ and each trial $j = 1, \ldots, n$:

$$ \label{eq:Y-ij}
Y_{ij} = \left\{
\begin{array}{rl}
0 \; , & \text{if} \; X_i = 0 \; \text{in trial} \; j \\
1 \; , & \text{if} \; X_i = 1 \; \text{in trial} \; j \; .
\end{array}
\right.
$$

Since $\mathrm{Pr}(Y_{ij} = 1) = p_i$ and $\mathrm{Pr}(Y_{ij} = 0) = 1-p_i$, $Y_{ij}$ is a [Bernoulli](/D/bern) random variable with [success probability](/D/bern) $p_i$:

$$ \label{eq:Y-ij-dist}
Y_{ij} \sim \mathrm{Bern}(p_i) \; .
$$

Moreover, each $X_i$ is the sum of the corresponding $Y_{ij}$ over all trials

$$ \label{eq:X-i-sum}
X_i = \sum_{j=1}^n Y_{ij} \; ,
$$

i.e. $X_i$ is a sum of independent Bernoulli random variables which, [by definition, follows a binomial distribution](/D/bin):

$$ \label{eq:X-i-dist}
X_i \sim \mathrm{Bin}(n, p_i) \; .
$$