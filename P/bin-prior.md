---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-01-23 23:38:00

title: "Conjugate prior distribution for binomial observations"
chapter: "Statistical Models"
section: "Categorical data"
topic: "Binomial observations"
theorem: "Conjugate prior distribution"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Binomial distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-01-23"
    url: "https://en.wikipedia.org/wiki/Binomial_distribution#Estimation_of_parameters"

proof_id: "P29"
shortcut: "bin-prior"
username: "JoramSoch"
---


**Theorem:** Let $y$ be the number of successes resulting from $n$ independent trials with unknown success probability $p$, such that $y$ follows a [binomial distribution](/D/bin):

$$ \label{eq:Bin}
y \sim \mathrm{Bin}(n,p) \; .
$$

Then, the [conjugate prior](/D/prior-conj) for the model parameter $p$ is a [beta distribution](/D/beta):

$$ \label{eq:Beta}
\mathrm{p}(p) = \mathrm{Bet}(p; \alpha_0, \beta_0) \; .
$$


**Proof:** With the [probability mass function of the binomial distribution](/P/bin-pmf), the [likelihood function](/D/lf) implied by \eqref{eq:Bin} is given by

$$ \label{eq:Bin-LF}
\mathrm{p}(y|p) = {n \choose y} \, p^y \, (1-p)^{n-y} \; .
$$

In other words, the likelihood function is proportional to a power of $p$ times a power of $(1-p)$:

$$ \label{eq:Bin-LF-prop}
\mathrm{p}(y|p) \propto p^y \, (1-p)^{n-y} \; .
$$

The same is true for a beta distribution over $p$

$$ \label{eq:Bin-prior-s1}
\mathrm{p}(p) = \mathrm{Bet}(p; \alpha_0, \beta_0)
$$

the [probability density function of which](/P/beta-pdf)

$$ \label{eq:Bin-prior-s2}
\mathrm{p}(p) = \frac{1}{B(\alpha_0,\beta_0)} \, p^{\alpha_0-1} \, (1-p)^{\beta_0-1}
$$

exhibits the same proportionality

$$ \label{eq:Bin-prior-s3}
\mathrm{p}(p) \propto p^{\alpha_0-1} \, (1-p)^{\beta_0-1}
$$

and is therefore conjugate relative to the likelihood.