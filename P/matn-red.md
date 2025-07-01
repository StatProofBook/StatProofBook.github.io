---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2025-06-24 11:55:00

title: "Redundancy of parameters describing the matrix-normal distribution"
chapter: "Probability Distributions"
section: "Matrix-variate continuous distributions"
topic: "Matrix-normal distribution"
theorem: "Redundancy of parameters"

sources:
  - authors: "Glanz, Hunter; Carvalho, Luis"
    year: 2013
    title: "An Expectation-Maximization Algorithm for the Matrix Normal Distribution"
    in: "arXiv stat.ME"
    pages: "sect. 2.1, p. 3"
    url: "https://arxiv.org/abs/1309.6609"
    doi: "10.48550/arXiv.1309.6609"

proof_id: "P505"
shortcut: "matn-red"
username: "JoramSoch"
---


**Theorem:** The [covariance parameters of the matrix-normal distribution](/D/matn) are redundant up to a scalar factor, i.e. the two [probability distributions](/D/dist)

$$ \label{eq:matn-red}
\begin{split}
X &\sim \mathcal{MN}(M, U, V) \\
X &\sim \mathcal{MN}\left( M, a \cdot U, \frac{1}{a} \cdot V \right)
\end{split}
$$

are equivalent for any $a \in \mathbb{R}$ with $a > 0$ where $X \in \mathbb{R}^{n \times p}$ is a [random matrix](/D/rmat) and $U \in \mathbb{R}^{n \times n}$ and $V \in \mathbb{R}^{p \times p}$ are positive-definite matrices.


**Proof:** Since $U$ and $V$ [must be positive-definite in the matrix-normal distribution](/D/matn), the scalar $a$ must be larger than zero. A [random matrix follows a matrix-normal distribution, if and only if its vectorization is multivariate normally distributed](/P/matn-mvn)

$$ \label{eq:matn-mvn}
X \sim \mathcal{MN}(M, U, V)
\quad \Leftrightarrow \quad
\mathrm{vec}(X) \sim \mathcal{N}(\mathrm{vec}(M), V \otimes U)
$$

where $\mathrm{vec}(X)$ is the vectorization operator and $\otimes$ is the Kronecker product. Thus, the second distribution in \eqref{eq:matn-red} is equivalent to

$$ \label{eq:matn-red-qed}
\begin{split}
X \sim \mathcal{MN}\left( M, a \cdot U, \frac{1}{a} \cdot V \right)
\quad \Leftrightarrow \quad
\mathrm{vec}(X) &\sim \mathcal{N}\left( \mathrm{vec}(M), \frac{1}{a} V \otimes a U \right) \\
                &\sim \mathcal{N}\left( \mathrm{vec}(M), \frac{1}{a} \left( V \otimes a U \right) \right) \\
                &\sim \mathcal{N}\left( \mathrm{vec}(M), \frac{a}{a} \left( V \otimes U \right) \right) \\
                &\sim \mathcal{N}\left( \mathrm{vec}(M), V \otimes U \right)
\end{split}
$$

which proves the equivalence of the two distributions in \eqref{eq:matn-red}.