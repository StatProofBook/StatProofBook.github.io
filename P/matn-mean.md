---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-09-15 12:05:00

title: "Mean of the matrix-normal distribution"
chapter: "Probability Distributions"
section: "Matrix-variate continuous distributions"
topic: "Matrix-normal distribution"
theorem: "Mean"

sources:
  - authors: "Wikipedia"
    year: 2022
    title: "Matrix normal distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2022-09-15"
    url: "https://en.wikipedia.org/wiki/Matrix_normal_distribution#Expected_values"

proof_id: "P341"
shortcut: "matn-mean"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random matrix](/D/rmat) following a [matrix-normal distribution](/D/matn):

$$ \label{eq:matn}
X \sim \mathcal{MN}(M, U, V) \; .
$$

Then, the [mean or expected value](/D/mean) of $X$ is

$$ \label{eq:matn-mean}
\mathrm{E}(X) = M \; .
$$


**Proof:** When $X$ follows a [matrix-normal distribution](/D/matn), [its vectorized version follows a multivariate normal distribution](/P/matn-mvn)

$$ \label{eq:matn-mvn}
\mathrm{vec}(X) \sim \mathcal{N}(\mathrm{vec}(M), V \otimes U)
$$

and [the expected value of this multivariate normal distribution is](/P/mvn-mean)

$$ \label{eq:mvn-mean}
\mathrm{E}[\mathrm{vec}(X)] = \mathrm{vec}(M) \; .
$$

Since [the expected value of a random matrix is calculated element-wise](/D/mean-rmat), we can invert the vectorization operator to get:

$$ \label{eq:matn-mean-qed}
\mathrm{E}[X] = M \; .
$$