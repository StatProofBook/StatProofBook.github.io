---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-10-11 09:25:00

title: "Probability-generating function of the binomial distribution"
chapter: "Probability Distributions"
section: "Univariate discrete distributions"
topic: "Binomial distribution"
theorem: "Probability-generating function"

sources:
  - authors: "ProofWiki"
    year: 2022
    title: "Probability Generating Function of Binomial Distribution"
    in: "ProofWiki"
    pages: "retrieved on 2022-10-11"
    url: "https://proofwiki.org/wiki/Probability_Generating_Function_of_Binomial_Distribution"

proof_id: "P363"
shortcut: "bin-pgf"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [binomial distribution](/D/bin):

$$ \label{eq:bin}
X \sim \mathrm{Bin}(n,p) \; .
$$

Then, the [probability-generating function](/D/pgf) of $X$ is

$$ \label{eq:bin-pgf}
G_X(z) = (q + pz)^n
$$

where $q = 1-p$.


**Proof:** The [probability-generating function](/D/pgf) of $X$ is defined as

$$ \label{eq:pgf}
G_X(z) = \sum_{x=0}^{\infty} f_X(x) \, z^x
$$

With the [probability mass function of the binomial distribution](/P/bin-pmf)

$$ \label{eq:bin-pmf}
f_X(x) = {n \choose x} \, p^x \, (1-p)^{n-x} \; ,
$$

we obtain:

$$ \label{eq:pgf-zero-s1}
\begin{split}
G_X(z) &= \sum_{x=0}^{n} {n \choose x} \, p^x \, (1-p)^{n-x} \, z^x \\
&= \sum_{x=0}^{n} {n \choose x} \, (pz)^x \, (1-p)^{n-x} \; .
\end{split}
$$

According to the binomial theorem

$$ \label{eq:bin-th}
(x+y)^n = \sum_{k=0}^{n} {n \choose k} \, x^{n-k} \, y^k \; ,
$$

the sum in equation \eqref{eq:pgf-zero-s1} equals

$$ \label{eq:pgf-zero-s2}
G_X(z) = \left( (1-p) + (pz) \right)^n
$$

which is equivalent to the result in \eqref{eq:bin-pgf}.