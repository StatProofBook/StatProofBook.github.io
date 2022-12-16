---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-12-13 16:44:00

title: "Independence of products of multivariate normal random vector"
chapter: "Probability Distributions"
section: "Multivariate continuous distributions"
topic: "Multivariate normal distribution"
theorem: "Independence of products"

sources:
  - authors: "jld"
    year: 2018
    title: "Understanding t-test for linear regression"
    in: "StackExchange CrossValidated"
    pages: "retrieved on 2022-12-13"
    url: "https://stats.stackexchange.com/a/344008"

proof_id: "P394"
shortcut: "mvn-indprod"
username: "JoramSoch"
---


**Theorem:** Let $X$ be an $n \times 1$ [random vector](/D/rvec) following a [multivariate normal distribution](/D/mvn):

$$ \label{eq:mvn}
X \sim \mathcal{N}(\mu, \Sigma)
$$

and consider two matrices $A \in \mathbb{R}^{k \times n}$ and $B \in \mathbb{R}^{l \times n}$. Then, $AX$ and $BX$ are [independent](/D/ind), if and only if the cross-matrix product, weighted with the [covariance matrix](/P/mvn-cov) is equal to the zero matrix:

$$ \label{eq:mvn-indprod}
AX \quad \text{and} \quad BX \quad \text{ind.} \quad \Leftrightarrow \quad A \Sigma B^\mathrm{T} = 0_{kl} \; .
$$


**Proof:** Define a new [random vector](/D/rvec) $C$ as

$$ \label{eq:C}
C = \left[ \begin{array}{c} A \\ B \end{array} \right] \in \mathbb{R}^{(k+l) \times n} \; .
$$

Then, due to the [linear transformation theorem](/P/mvn-ltt), we have

$$ \label{eq:CX}
CX = \left[ \begin{array}{c} AX \\ BX \end{array} \right] \sim \mathcal{N}\left( \left[ \begin{array}{c} A\mu \\ B\mu \end{array} \right], C \Sigma C^\mathrm{T} \right)
$$

with the combined [covariance matrix](/D/covmat)

$$ \label{eq:CSC}
C \Sigma C^\mathrm{T} = \left[ \begin{array}{cc} A \Sigma A^\mathrm{T} & A \Sigma B^\mathrm{T} \\ B \Sigma A^\mathrm{T} & B \Sigma B^\mathrm{T} \end{array} \right] \; .
$$

We know that [the necessary and sufficient condition for two components of a multivariate normal random vector to be independent is that their entries in the covariance matrix are zero](/P/mvn-ind). Thus, $AX$ and $BX$ are [independent](/D/ind), if and only if

$$ \label{eq:mvn-indprod-qed}
A \Sigma B^\mathrm{T} = (B \Sigma A^\mathrm{T})^\mathrm{T} = 0_{kl}
$$

where $0_{kl}$ is the $k \times l$ zero matrix. This proves the result in \eqref{eq:mvn-indprod}.