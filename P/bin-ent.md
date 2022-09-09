---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-09-02 13:52:00

title: "Entropy of the binomial distribution"
chapter: "Probability Distributions"
section: "Univariate discrete distributions"
topic: "Binomial distribution"
theorem: "Shannon entropy"

sources:

proof_id: "P335"
shortcut: "bin-ent"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [binomial distribution](/D/bin):

$$ \label{eq:bin}
X \sim \mathrm{Bin}(n,p) \; .
$$

Then, the [(Shannon) entropy](/D/ent) of $X$ in bits is

$$ \label{eq:bin-ent}
\mathrm{H}(X) = n \cdot \mathrm{H}_\mathrm{bern}(p) - \mathrm{E}_\mathrm{lbc}(n,p)
$$

where $\mathrm{H}_\mathrm{bern}(p)$ is the binary entropy function, i.e. the [(Shannon) entropy of the Bernoulli distribution](/P/bern-ent) with success probability $p$

$$ \label{eq:H-bern}
\mathrm{H}_\mathrm{bern}(p) = - p \cdot \log_2 p - (1-p) \log_2 (1-p)
$$

and $\mathrm{E}_\mathrm{lbc}(n,p)$ is the [expected value](/D/mean) of the logarithmized [binomial coefficient](/P/bin-pmf) with superset size $n$

$$ \label{eq:E-lbf}
\mathrm{E}_\mathrm{lbc}(n,p) = \mathrm{E}\left[ \log_2 {n \choose X} \right] \quad \text{where} \quad X \sim \mathrm{Bin}(n,p) \; .
$$


**Proof:** The [entropy](/D/ent) is defined as the probability-weighted average of the logarithmized probabilities for all possible values:

$$ \label{eq:ent}
\mathrm{H}(X) = - \sum_{x \in \mathcal{X}} p(x) \cdot \log_b p(x) \; .
$$

Entropy is measured in bits by setting $b = 2$. Then, with the [probability mass function of the binomial distribution](/P/bin-pmf), we have:

$$ \label{eq:bin-ent-s1}
\begin{split}
\mathrm{H}(X) &= - \sum_{x \in \mathcal{X}} f_X(x) \cdot \log_2 f_X(x) \\
&= - \sum_{x=0}^{n} {n \choose x} \, p^x \, (1-p)^{n-x} \cdot \log_2 \left[ {n \choose x} \, p^x \, (1-p)^{n-x} \right] \\
&= - \sum_{x=0}^{n} {n \choose x} \, p^x \, (1-p)^{n-x} \cdot \left[ \log_2 {n \choose x} + x \cdot \log_2 p + (n-x) \cdot \log_2 (1-p) \right] \\
&= - \sum_{x=0}^{n} {n \choose x} \, p^x \, (1-p)^{n-x} \cdot \left[ \log_2 {n \choose x} + x \cdot \log_2 p + n \cdot \log_2 (1-p) - x \cdot \log_2 (1-p) \right] \; .
\end{split}
$$

Since the first factor in the sum corresponds to the [probability mass](/D/pmf) of $X=x$, we can rewrite this as the sum of the [expected values](/D/mean) [of the functions](/P/mean-lotus) of the [discrete random variable](/D/rvar-disc) $x$ in the square bracket:

$$ \label{eq:bin-ent-s2}
\begin{split}
\mathrm{H}(X) &= - \left\langle \log_2 {n \choose x} \right\rangle_{p(x)} - \left\langle x \cdot \log_2 p \right\rangle_{p(x)} - \left\langle n \cdot \log_2 (1-p) \right\rangle_{p(x)} + \left\langle x \cdot \log_2 (1-p) \right\rangle_{p(x)} \\
&= - \left\langle \log_2 {n \choose x} \right\rangle_{p(x)} - \log_2 p \cdot \left\langle x \right\rangle_{p(x)} - n \cdot \log_2 (1-p) +  \log_2 (1-p) \cdot \left\langle x \right\rangle_{p(x)} \; .
\end{split}
$$

Using the [expected value of the binomial distribution](/P/bin-mean), i.e. $X \sim \mathrm{Bin}(n,p) \Rightarrow \left\langle x \right\rangle = n p$, this gives:

$$ \label{eq:bin-ent-s3}
\begin{split}
\mathrm{H}(X) &= - \left\langle \log_2 {n \choose x} \right\rangle_{p(x)} - n p \cdot \log_2 p - n \cdot \log_2 (1-p) +  n p \cdot \log_2 (1-p) \\
&= - \left\langle \log_2 {n \choose x} \right\rangle_{p(x)} + n \left[ - p \cdot \log_2 p - (1-p) \log_2 (1-p) \right] \; .
\end{split}
$$

Finally, we note that the first term is the negative [expected value](/D/mean) of the logarithm of a [binomial coefficient](/P/bin-pmf) and that the term in square brackets is the [entropy of the Bernoulli distribution](/P/bin-ent), such that we finally get:

$$ \label{eq:bin-ent-s4}
\mathrm{H}(X) = n \cdot \mathrm{H}_\mathrm{bern}(p) - \mathrm{E}_\mathrm{lbc}(n,p) \; .
$$

Note that, because $0 \leq \mathrm{H}_\mathrm{bern}(p) \leq 1$, we have $0 \leq n \cdot \mathrm{H}_\mathrm{bern}(p) \leq n$, and because the [entropy is non-negative](/P/ent-nonneg), it must hold that $n \geq \mathrm{E}_\mathrm{lbc}(n,p) \geq 0$.