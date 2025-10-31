---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2025-04-04 14:40:01

title: "Binomial distribution is a special case of multinomial distribution"
chapter: "Probability Distributions"
section: "Univariate discrete distributions"
topic: "Binomial distribution"
theorem: "Special case of multinomial distribution"

sources:

proof_id: "P495"
shortcut: "bin-mult"
username: "JoramSoch"
---


**Theorem:** The [binomial distribution](/D/bin) with sample size $n$ and success probability $p$ is a special case of the [multinomial distribution](/D/mult) with sample size $n$ category probabilities $p_1 = p$ and $p_2 = 1-p$:

$$ \label{eq:bin-mult}
X \sim \mathrm{Mult}(n, \left[ p, 1-p \right])
\quad \Rightarrow \quad
X \sim \mathrm{Bin}(p) \; .
$$


**Proof:** The [probability mass function of the multinomial distribution](/P/mult-pmf), where $x$ is a $1 \times k$ vector with $x_i \in \left\lbrace 0, 1, \ldots, n \right\rbrace$, is as follows:

$$ \label{eq:mult-pmf}
\mathrm{Mult}(x; n, \left[ p_1, \ldots, p_k \right]) = {n \choose {x_1, \ldots, x_k}} \, \prod_{i=1}^k {p_i}^{x_i} \; .
$$

If we let $k = 2$, $p_1 = p$ and $p_2 = 1-p$, we obtain

$$ \label{eq:mult-pmf-bin-s1}
\mathrm{Mult}(x; n, \left[ p, 1-p \right]) = {n \choose {x_1, x_2}} \, p^{x_1} \, (1-p)^{n-x_1} \; .
$$

Recognizing that $\sum_{i=1}^{k} x_i = n$, such that $x_2 = n - x_1$, we get

$$ \label{eq:mult-pmf-bin-s2}
\begin{split}
\mathrm{Mult}(x; n, \left[ p, 1-p \right])
&= {n \choose {x_1, n-x_1}} \, p^{x_1} \, (1-p)^{n-x_1} \\
&= {n \choose x_1} \, p^{x_1} \, (1-p)^{n-x_1}
\end{split}
$$

which is equivalent to the [probability mass function of the binomial distribution](/P/bin-pmf).