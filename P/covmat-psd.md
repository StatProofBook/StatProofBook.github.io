---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-09-26 11:26:00

title: "Positive semi-definiteness of the covariance matrix"
chapter: "General Theorems"
section: "Probability theory"
topic: "Covariance"
theorem: "Positive semi-definiteness"

sources:
  - authors: "hkBattousai"
    year: 2013
    title: "What is the proof that covariance matrices are always semi-definite?"
    in: "StackExchange Mathematics"
    pages: "retrieved on 2022-09-26"
    url: "https://math.stackexchange.com/a/327872"
  - authors: "Wikipedia"
    year: 2022
    title: "Covariance matrix"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2022-09-26"
    url: "https://en.wikipedia.org/wiki/Covariance_matrix#Basic_properties"

proof_id: "P351"
shortcut: "covmat-psd"
username: "JoramSoch"
---


**Theorem:** Each [covariance matrix](/D/covmat) is positive semi-definite:

$$ \label{eq:covmat-symm}
a^\mathrm{T} \Sigma_{XX} a \geq 0 \quad \text{for all} \quad a \in \mathbb{R}^n \; .
$$


**Proof:** The [covariance matrix](/D/covmat) of $X$ [can be expressed](/P/covmat-mean) in terms of [expected values](/D/mean) as follows

$$ \label{eq:covmat}
\Sigma_{XX} = \Sigma(X) = \mathrm{E}\left[ (X-\mathrm{E}[X]) (X-\mathrm{E}[X])^\mathrm{T} \right]
$$

A positive semi-definite matrix is a matrix whose eigenvalues are all non-negative or, equivalently,

$$ \label{eq:psd}
M \; \text{pos. semi-def.} \quad \Leftrightarrow \quad x^\mathrm{T} M x \geq 0 \quad \text{for all} \quad x \in \mathbb{R}^n \; .
$$

Here, for an arbitrary real column vector $a \in \mathbb{R}^n$, we have:

$$ \label{eq:covmat-symm-s1}
a^\mathrm{T} \Sigma_{XX} a \overset{\eqref{eq:covmat}}{=} a^\mathrm{T} \mathrm{E}\left[ (X-\mathrm{E}[X]) (X-\mathrm{E}[X])^\mathrm{T} \right] a \; .
$$

Because the [expected value is a linear operator](/P/mean-lin), we can write:

$$ \label{eq:covmat-symm-s2}
a^\mathrm{T} \Sigma_{XX} a = \mathrm{E}\left[ a^\mathrm{T} (X-\mathrm{E}[X]) (X-\mathrm{E}[X])^\mathrm{T} a \right] \; .
$$

Now define the [scalar random variable](/D/rvar)

$$ \label{eq:Y-X}
Y = a^\mathrm{T} (X-\mu_X) \; .
$$

where $\mu_X = \mathrm{E}[X]$ and note that

$$ \label{eq:YT-Y}
a^\mathrm{T} (X-\mu_X) = (X-\mu_X)^\mathrm{T} a \; .
$$

Thus, combing \eqref{eq:covmat-symm-s2} with \eqref{eq:Y-X}, we have:

$$ \label{eq:covmat-symm-s3}
a^\mathrm{T} \Sigma_{XX} a = \mathrm{E}\left[ Y^2 \right] \; .
$$

Because $Y^2$ is a random variable that cannot become negative and the [expected value of a strictly non-negative random variable is also non-negative](/P/mean-nonneg), we finally have

$$ \label{eq:covmat-symm-s4}
a^\mathrm{T} \Sigma_{XX} a \geq 0
$$

for any $a \in \mathbb{R}^n$.