---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-09-09 16:57:00

title: "Covariance matrix of the categorical distribution"
chapter: "Probability Distributions"
section: "Multivariate discrete distributions"
topic: "Categorical distribution"
theorem: "Covariance"

sources:

proof_id: "P338"
shortcut: "cat-cov"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random vector](/D/rvec) following a [categorical distribution](/D/cat):

$$ \label{eq:cat}
X \sim \mathrm{Cat}(n,p) \; .
$$

Then, the [covariance matrix](/D/covmat) of $X$ is

$$ \label{eq:cat-cov}
\mathrm{Cov}(X) = \mathrm{diag}(p) - pp^\mathrm{T} \; .
$$


**Proof:** The [categorical distribution](/D/cat) is a special case of the [multinomial distribution](/D/mult) in which $n = 1$:

$$ \label{eq:cat-mult}
X \sim \mathrm{Mult}(n,p) \quad \text{and} \quad n = 1 \quad \Rightarrow \quad X \sim \mathrm{Cat}(p) \; .
$$

The [covariance matrix of the multinomial distribution](/P/mult-cov) is

$$ \label{eq:mult-cov}
\mathrm{Cov}(X) = n \left(\mathrm{diag}(p) - pp^\mathrm{T} \right) \; ,
$$

thus the covariance matrix of the categorical distribution is

$$ \label{eq:cat-cov-qed}
\mathrm{Cov}(X) = \mathrm{diag}(p) - pp^\mathrm{T} \; .
$$