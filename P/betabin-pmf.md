---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-10-20 08:56:00

title: "Probability mass function of the beta-binomial distribution"
chapter: "Probability Distributions"
section: "Univariate discrete distributions"
topic: "Beta-binomial distribution"
theorem: "Probability mass function"

sources:
  - authors: "Wikipedia"
    year: 2022
    title: "Beta-binomial distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2022-10-20"
    url: "https://en.wikipedia.org/wiki/Beta-binomial_distribution#As_a_compound_distribution"

proof_id: "P364"
shortcut: "betabin-pmf"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [beta-binomial distribution](/D/betabin):

$$ \label{eq:betabin}
X \sim \mathrm{BetBin}(n,\alpha,\beta) \; .
$$

Then, the [probability mass function](/D/pmf) of $X$ is

$$ \label{eq:betabin-pmf}
f_X(x) = {n \choose x} \cdot \frac{\mathrm{B}(\alpha+x,\beta+n-x)}{\mathrm{B}(\alpha,\beta)}
$$

where $\mathrm{B}(x,y)$ is the beta function.


**Proof:** A [beta-binomial random variable](/D/betabin) is defined as a [binomial variate](/D/bin) for which the success probability is following a [beta distribution](/D/beta):

$$ \label{eq:betabin-bin-beta}
\begin{split}
X \mid p &\sim \mathrm{Bin}(n, p) \\
p &\sim \mathrm{Bet}(\alpha, \beta) \; .
\end{split}
$$

Thus, we can combine the [law of marginal probability](/D/prob-marg) and the [law of conditional probability](/D/prob-cond) to derive the [probability](/D/prob) of $X$ as

$$ \label{eq:betabin-pmf-s1}
\begin{split}
p(x) &= \int_\mathcal{P} \mathrm{p}(x,p) \, \mathrm{d}p \\
&= \int_\mathcal{P} \mathrm{p}(x \vert p) \, \mathrm{p}(p) \, \mathrm{d}p
\end{split}
$$

where $\mathcal{P} = [0,1]$ is the set of possible values of $p$. Now, we can plug in the [probability mass function of the binomial distribution](/P/bin-pmf) and the [probability density function of the beta distribution](/P/beta-pdf) to get

$$ \label{eq:betabin-pmf-s2}
\begin{split}
p(x) &= \int_0^1 {n \choose x} \, p^x \, (1-p)^{n-x} \cdot \frac{1}{\mathrm{B}(\alpha, \beta)} \, p^{\alpha-1} \, (1-p)^{\beta-1} \, \mathrm{d}p \\
&= {n \choose x} \cdot \frac{1}{\mathrm{B}(\alpha, \beta)} \, \int_0^1 p^{\alpha+x-1} \, (1-p)^{\beta+n-x-1} \, \mathrm{d}p \\
&= {n \choose x} \cdot \frac{\mathrm{B}(\alpha+x,\beta+n-x)}{\mathrm{B}(\alpha, \beta)} \, \int_0^1 \frac{1}{\mathrm{B}(\alpha+x,\beta+n-x)} \, p^{\alpha+x-1} \, (1-p)^{\beta+n-x-1} \, \mathrm{d}p \; .
\end{split}
$$

Finally, we recognize that the integrand is equal to the [probability density function of a beta distribution](/P/beta-pdf) and [because probability density integrates to one](/D/pdf), we have

$$ \label{eq:betabin-pmf-qed}
p(x) = {n \choose x} \cdot \frac{\mathrm{B}(\alpha+x,\beta+n-x)}{\mathrm{B}(\alpha,\beta)} = f_X(x) \; .
$$

This completes the proof.