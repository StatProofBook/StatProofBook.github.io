---
layout: proof
mathjax: true

author: "Alex Kipnis"
affiliation: "The Book of Statistical Proofs"
e_mail: "StatProofBook@gmail.com"
date: 2022-05-11 16:40:00

title: "Covariance matrix of the multinomial distribution"
chapter: "Probability Distributions"
section: "Multivariate discrete distributions"
topic: "Multinomial
distribution"
theorem: "Covariance Matrix"

sources:
- authors: "Tutz"
    year: 2012
    title: "Regression for Categorical Data"
    pages: "209ff."
proof_id:
shortcut: "mult-cov"
username: "adkipnis"
---


**Theorem:** Let $X$ be a [random vector](/D/rvec) following a [multinomial distribution](/D/mult):

$$ \label{eq:mult}
\left[X_1, \ldots, X_k \right] = X \sim \mathrm{Mult}(n, p), \; n \in \mathbb{N}, \; p = \left[p_1, \ldots, p_k \right],
$$

then the [covariance matrix](/D/covmat) of $X$ is

$$ \label{eq:bin-cov}
\mathbb{V}(X) = n \left(\mathrm{diag}(p_i)_{i = 1, \ldots, k} - pp^\top \right) \; .
$$

**Proof:** We first observe that the [sample space](/D/samp-spc) of each coordinate $X_i$ is $\left\{0, 1, \ldots, n \right\}$ and $X_i$ is the sum of independent draws of category $i$, which is drawn with probability $p_i$. Thus each coordinate follows a [binomial distribution](/P/bin):

$$ \label{eq:Marginal}
X_i \stackrel{iid}{\sim} \mathrm{Bin}(n, p_i),\; i = 1,\ldots, k,
$$

which has the [variance](/P/bin-var) $\mathbb{V}(X_i) = n p_i(1-p_i) = n (p_i - p_i^2)$, constituting the elements of the main diagonal in $\mathbb{V}(X)$ in \eqref{eq:bin-cov}. To prove $\mathbb{C}\mathrm{ov}(X_i, X_j)=-np_i p_j$ for $i\ne j$ (which constitutes the off-diagonal elements of the covariance matrix), we first recognize that

$$ \label{eq:bin-sum}
X_i = \sum_{k=1}^n \mathbb{I}_i(k), \; \text{with} \;\; \mathbb{I}_i(k) := \begin{cases}
    1 & \text{if $k$-th draw was of category $i$}, \\
    0 & \text{otherwise},
  \end{cases}
$$
the indicator function $\mathbb{I}_i$ being a [Bernoulli-distributed](/P/bern) random variable with the [expected value](/P/bern-mean) $p_i$. Then we have 

$$ \label{eq:bin-cov}
\begin{split}
  \mathbb{C}\mathrm{ov}(X_i, X_j)
  &= \mathbb{C}\mathrm{ov}\left(\sum_{k=1}^n \mathbb{I}_i(k), \sum_{l=1}^n \mathbb{I}_j(l)\right)\\
  &= \sum_{k=1}^n\sum_{l=1}^n \mathbb{C}\mathrm{ov}\left(\mathbb{I}_i(k), \mathbb{I}_j(l)\right)\\
  &= \sum_{k=1}^n \mathbb{C}\mathrm{ov}\left(\mathbb{I}_i(k), \mathbb{I}_j(k)\right) + \sum_{k\ne l}^n \underbrace{\mathbb{C}\mathrm{ov}\left(\mathbb{I}_i(k), \mathbb{I}_j(l)\right)}_\text{0}\\
  & \stackrel{\mathclap{(i \ne j)}}{=} \;\; \sum_{k=1}^n \left(\mathbb{E}\Big( \underbrace{\mathbb{I}_i(k) \,\mathbb{I}_j(k)}_\text{0} \Big) - \mathbb{E}\big(\mathbb{I}_i(k)\big) \mathbb{E}\big(\mathbb{I}_j(k)\big) \right)\\
  &= - \sum_{k=1}^n \mathbb{E}\big(\mathbb{I}_i(k)\big) \mathbb{E}\big(\mathbb{I}_j(k)\big) \\
  &= -n p_i p_j,
\end{split}
$$
as desired.