---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-08-19 06:09:00

title: "Mean of the Poisson distribution"
chapter: "Probability Distributions"
section: "Univariate discrete distributions"
topic: "Poisson distribution"
theorem: "Mean"

sources:
  - authors: "ProofWiki"
    year: 2020
    title: "Expectation of Poisson Distribution"
    in: "ProofWiki"
    pages: "retrieved on 2020-08-19"
    url: "https://proofwiki.org/wiki/Expectation_of_Poisson_Distribution"

proof_id: "P151"
shortcut: "poiss-mean"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [Poisson distribution](/D/poiss):

$$ \label{eq:poiss}
X \sim \mathrm{Poiss}(\lambda) \; .
$$

Then, the [mean or expected value](/D/mean) of $X$ is

$$ \label{eq:poiss-mean}
\mathrm{E}(X) = \lambda \; .
$$


**Proof:** The [expected value of a discrete random variable](/D/mean) is defined as

$$ \label{eq:mean}
\mathrm{E}(X) = \sum_{x \in \mathcal{X}} x \cdot f_X(x) \; ,
$$

such that, with the [probability mass function of the Poisson distribution](/P/poiss-pmf), we have:

$$ \label{eq:poiss-mean-s1}
\begin{split}
\mathrm{E}(X) &= \sum_{x=0}^\infty x \cdot \frac{\lambda^x \, e^{-\lambda}}{x!} \\
&= \sum_{x=1}^\infty x \cdot \frac{\lambda^x \, e^{-\lambda}}{x!} \\
&= e^{-\lambda} \cdot \sum_{x=1}^\infty \frac{x}{x!} \lambda^x \\
&= \lambda e^{-\lambda} \cdot \sum_{x=1}^\infty \frac{\lambda^{x-1}}{(x-1)!} \; .
\end{split}
$$

Substituting $z = x-1$, such that $x = z+1$, we get:

$$ \label{eq:poiss-mean-s2}
\mathrm{E}(X) = \lambda e^{-\lambda} \cdot \sum_{z=0}^\infty \frac{\lambda^z}{z!} \; .
$$

Using the power series expansion of the exponential function

$$ \label{eq:exp-ps}
e^x = \sum_{n=0}^\infty \frac{x^n}{n!} \; ,
$$

the expected value of $X$ finally becomes

$$ \label{eq:poiss-mean-s3}
\begin{split}
\mathrm{E}(X) &= \lambda e^{-\lambda} \cdot e^{\lambda} \\
&= \lambda \; .
\end{split}
$$