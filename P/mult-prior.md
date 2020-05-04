---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-03-11 14:15:00

title: "Conjugate prior distribution for multinomial observations"
chapter: "Statistical Models"
section: "Categorical data"
topic: "Multinomial observations"
theorem: "Conjugate prior distribution"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Dirichlet distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-03-11"
    url: "https://en.wikipedia.org/wiki/Dirichlet_distribution#Conjugate_to_categorical/multinomial"

proof_id: "P79"
shortcut: "mult-prior"
username: "JoramSoch"
---


**Theorem:** Let $y = [y_1, \ldots, y_k]$ be the number of observations in $k$ categories resulting from $n$ independent trials with unknown category probabilities $p = [p_1, \ldots, p_k]$, such that $y$ follows a [multinomial distribution](/D/mult):

$$ \label{eq:Mult}
y \sim \mathrm{Mult}(n,p) \; .
$$

Then, the [conjugate prior](/D/prior-conj) for the model parameter $p$ is a [Dirichlet distribution](/D/dir):

$$ \label{eq:Dir}
\mathrm{p}(p) = \mathrm{Dir}(p; \alpha_0) \; .
$$


**Proof:** With the [probability mass function of the multinomial distribution](/P/mult-pmf), the [likelihood function](/D/lf) implied by \eqref{eq:Mult} is given by

$$ \label{eq:Mult-LF}
\mathrm{p}(y|p) = {n \choose {y_1, \ldots, y_k}} \prod_{j=1}^{k} {p_j}^{y_j} \; .
$$

In other words, the likelihood function is proportional to a product of powers of the entries of the vector $p$:

$$ \label{eq:Mult-LF-prop}
\mathrm{p}(y|p) \propto \prod_{j=1}^{k} {p_j}^{y_j} \; .
$$

The same is true for a Dirichlet distribution over $p$

$$ \label{eq:Mult-prior-s1}
\mathrm{p}(p) = \mathrm{Dir}(p; \alpha_0)
$$

the [probability density function of which](/P/dir-pdf)

$$ \label{eq:Mult-prior-s2}
\mathrm{p}(p) = \frac{\Gamma \left( \sum_{j=1}^{k} \alpha_{0j} \right)}{\prod_{j=1}^k \Gamma(\alpha_{0j})} \prod_{j=1}^{k} {p_j}^{\alpha_{0j}-1}
$$

exhibits the same proportionality

$$ \label{eq:Mult-prior-s3}
\mathrm{p}(p) \propto \prod_{j=1}^{k} {p_j}^{\alpha_{0j}-1}
$$

and is therefore conjugate relative to the likelihood.