---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-01-27 09:03:00

title: "Range of the variance of the Bernoulli distribution"
chapter: "Probability Distributions"
section: "Univariate discrete distributions"
topic: "Bernoulli distribution"
theorem: "Range of Variance"

sources:
  - authors: "Wikipedia"
    year: 2022
    title: "Bernoulli distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2022-01-27"
    url: "https://en.wikipedia.org/wiki/Bernoulli_distribution#Variance"

proof_id: "P303"
shortcut: "bern-varrange"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [Bernoulli distribution](/D/bern):

$$ \label{eq:bern}
X \sim \mathrm{Bern}(p) \; .
$$

Then, the [variance](/D/var) of $X$ is necessarily between 0 and 1/4:

$$ \label{eq:bern-var-range}
0 \leq \mathrm{Var}(X) \leq \frac{1}{4} \; .
$$


**Proof:** The [variance of a Bernoulli random variable](/P/bern-var) is

$$ \label{eq:bern-var}
X \sim \mathrm{Bern}(p) \quad \Rightarrow \quad \mathrm{Var}(X) = p \, (1-p)
$$

which can also be understood as a function of the [success probability](/D/bern) $p$:

$$ \label{eq:bern-var-p}
\mathrm{Var}(X) = \mathrm{Var}(p) = -p^2 + p \; .
$$

The first derivative of this function is

$$ \label{eq:dVar-dp}
\frac{\mathrm{d}\mathrm{Var}(p)}{\mathrm{d}p} = -2 \, p + 1
$$

and setting this deriative to zero

$$ \label{eq:dVar-dp-0}
\begin{split}
\frac{\mathrm{d}\mathrm{Var}(p_M)}{\mathrm{d}p} &= 0 \\
0 &= -2 \, p_M + 1 \\
p_M &= \frac{1}{2} \; ,
\end{split}
$$

we obtain the maximum possible variance

$$ \label{eq:bern-var-max}
\mathrm{max}\left[\mathrm{Var}(X)\right] = \mathrm{Var}(p_M) = -\left( \frac{1}{2} \right)^2 + \frac{1}{2} = \frac{1}{4} \; .
$$

The function $\mathrm{Var}(p)$ is monotonically increasing for $0 < p < p_M$ as $\mathrm{d}\mathrm{Var}(p)/\mathrm{d}p > 0$ in this interval and it is monotonically decreasing for $p_M < p < 1$ as $\mathrm{d}\mathrm{Var}(p)/\mathrm{d}p < 0$ in this interval. Moreover, as [variance is always non-negative](/P/var-nonneg), the minimum variance is

$$ \label{eq:bern-var-min}
\mathrm{min}\left[\mathrm{Var}(X)\right] = \mathrm{Var}(0) = \mathrm{Var}(1) = 0 \; .
$$

Thus, we have:

$$ \label{eq:bern-var-int}
\mathrm{Var}(p) \in \left[ 0, \; \frac{1}{4} \right] \; .
$$