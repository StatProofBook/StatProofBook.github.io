---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-01-29 15:12:00

title: "Marginal distributions of the multivariate normal distribution"
chapter: "Probability Distributions"
section: "Multivariate continuous distributions"
topic: "Multivariate normal distribution"
theorem: "Marginal distributions"

sources:

proof_id: "P35"
shortcut: "mvn-marg"
username: "JoramSoch"
---


**Theorem:** Let $x$ follow a [multivariate normal distribution](/D/mvn):

$$ \label{eq:mvn}
x \sim \mathcal{N}(\mu, \Sigma) \; .
$$

Then, the [marginal distribution](/D/dist-marg) of any subset vector $x_s$ is also a multivariate normal distribution

$$ \label{eq:mvn-marg}
x_s \sim \mathcal{N}(\mu_s, \Sigma_s)
$$

where $\mu_s$ drops the irrelevant variables (the ones not in the subset, i.e. marginalized out) from the mean vector $\mu$ and $\Sigma_s$ drops the corresponding rows and columns from the covariance matrix $\Sigma$.


**Proof:** Define an $m \times n$ subset matrix $S$ such that $s_{ij} = 1$, if the $j$-th element in $x_s$ corresponds to the $i$-th element in $x$, and $s_{ij} = 0$ otherwise. Then,

$$ \label{eq:xs}
x_s = S x
$$

and we can apply the [linear transformation theorem](/P/mvn-ltt) to give

$$ \label{eq:mvn-marg-qed}
x_s \sim \mathcal{N}(S \mu, S \Sigma S^\mathrm{T}) \; .
$$

Finally, we see that $S \mu = \mu_s$ and $S \Sigma S^\mathrm{T} = \Sigma_s$.