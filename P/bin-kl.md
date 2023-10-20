---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2023-10-20 12:49:46

title: "Kullback-Leibler divergence for the binomial distribution"
chapter: "Probability Distributions"
section: "Univariate discrete distributions"
topic: "Binomial distribution"
theorem: "Kullback-Leibler divergence"

sources:
  - authors: "PSPACEhard"
    year: 2017
    title: "Kullback-Leibler divergence for binomial distributions P and Q"
    in: "StackExchange Mathematics"
    pages: "retrieved on 2023-10-20"
    url: "https://math.stackexchange.com/a/2215384/480910"

proof_id: "P420"
shortcut: "bin-kl"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar). Assume two [binomial distributions](/D/bin) $P$ and $Q$ specifying the probability distribution of $X$ as

$$ \label{eq:bins}
\begin{split}
P: \; X &\sim \mathrm{Bin}(n, p_1) \\
Q: \; X &\sim \mathrm{Bin}(n, p_2) \; .
\end{split}
$$

Then, the [Kullback-Leibler divergence](/D/kl) of $P$ from $Q$ is given by

$$ \label{eq:bin-KL}
\mathrm{KL}[P\,||\,Q] = n p_1 \cdot \ln \frac{p_1}{p_2} + n (1-p_1) \cdot \ln \frac{1-p_1}{1-p_2} \; .
$$


**Proof:** The [KL divergence for a discrete random variable](/D/kl) is given by 

$$ \label{eq:KL-disc}
\mathrm{KL}[P\,||\,Q] = \sum_{x \in \mathcal{X}} p(x) \, \ln \frac{p(x)}{q(x)}
$$

which, applied to the [binomial distributions](/D/bin) in \eqref{eq:bins}, yields

$$ \label{eq:bin-KL-s1}
\begin{split}
\mathrm{KL}[P\,||\,Q] &= \sum_{x=0}^{n} p(x) \, \ln \frac{p(x)}{q(x)} \\
&= p(X=0) \cdot \ln \frac{p(X=0)}{q(X=0)} + \ldots + p(X=n) \cdot \ln \frac{p(X=n)}{q(X=n)} \; .
\end{split}
$$

Using the [probability mass function of the binomial distribution](/P/bin-pmf), this becomes:

$$ \label{eq:bin-KL-s2}
\begin{split}
\mathrm{KL}[P\,||\,Q] &= \sum_{x=0}^{n} {n \choose x} \, p_1^x \, (1-p_1)^{n-x} \cdot \ln \frac{ {n \choose x} \, p_1^x \, (1-p_1)^{n-x} }{ {n \choose x} \, p_2^x \, (1-p_2)^{n-x} } \\
&= \sum_{x=0}^{n} {n \choose x} \, p_1^x \, (1-p_1)^{n-x} \cdot \left[ x \cdot \ln \frac{p_1}{p_2} + (n-x) \cdot \ln \frac{1-p_1}{1-p_2} \right] \\
&= \ln \frac{p_1}{p_2} \cdot \sum_{x=0}^{n} {n \choose x} \, p_1^x \, (1-p_1)^{n-x} x + \ln \frac{1-p_1}{1-p_2} \cdot \sum_{x=0}^{n} {n \choose x} \, p_1^x \, (1-p_1)^{n-x} (n-x) \; .
\end{split}
$$

We can now see that some terms in this sum are [expected values](/D/mean) with respect to [binomial distributions](/D/bin):

$$ \label{eq:bin-means-s1}
\begin{split}
\sum_{x=0}^{n} {n \choose x} \, p_1^x \, (1-p_1)^{n-x} x &= \mathrm{E}\left[ x \right]_{\mathrm{Bin}(n,p_1)} \\
\sum_{x=0}^{n} {n \choose x} \, p_1^x \, (1-p_1)^{n-x} (n-x) &= \mathrm{E}\left[ n-x \right]_{\mathrm{Bin}(n,p_1)} \; .
\end{split}
$$

Using the [expected value of the binomial distribution](/P/bin-mean), these can be simplified to

$$ \label{eq:bin-means-s2}
\begin{split}
\mathrm{E}\left[ x \right]_{\mathrm{Bin}(n,p_1)} &= n p_1 \\
\mathrm{E}\left[ n-x \right]_{\mathrm{Bin}(n,p_1)} &= n - n p_ 1 \; ,
\end{split}
$$

such that the Kullback-Leibler divergence finally becomes:

$$ \label{eq:bin-KL-qed}
\mathrm{KL}[P\,||\,Q] = n p_1 \cdot \ln \frac{p_1}{p_2} + n (1-p_1) \cdot \ln \frac{1-p_1}{1-p_2} \; .
$$