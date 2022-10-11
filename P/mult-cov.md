---
layout: proof
mathjax: true

author: "Alex Kipnis"
affiliation: "Max Planck Institute for Biological Kybernetics"
e_mail: "alexander.kipnis@tuebingen.mpg.de"
date: 2022-05-11 16:40:00

title: "Covariance matrix of the multinomial distribution"
chapter: "Probability Distributions"
section: "Multivariate discrete distributions"
topic: "Multinomial distribution"
theorem: "Covariance"

sources:
  - authors: "Tutz"
    year: 2012
    title: "Regression for Categorical Data"
    pages: "pp. 209ff."

proof_id: P322
shortcut: "mult-cov"
username: "adkipnis"
---


**Theorem:** Let $X$ be a [random vector](/D/rvec) following a [multinomial distribution](/D/mult):

$$ \label{eq:mult}
\left[X_1, \ldots, X_k \right] = X \sim \mathrm{Mult}(n, p), \; n \in \mathbb{N}, \; p = \left[p_1, \ldots, p_k \right]^\mathrm{T} \; .
$$

Then, the [covariance matrix](/D/covmat) of $X$ is

$$ \label{eq:mult-cov}
\mathrm{Cov}(X) = n \left(\mathrm{diag}(p) - pp^\mathrm{T} \right) \; .
$$

**Proof:** We first observe that the [sample space](/D/samp-spc) of each coordinate $X_i$ is $\left\lbrace 0, 1, \ldots, n \right\rbrace$ and $X_i$ is the sum of independent draws of category $i$, which is drawn with probability $p_i$. Thus each coordinate follows a [binomial distribution](/D/bin):

$$ \label{eq:Marginal}
X_i \stackrel{\mathrm{i.i.d.}}{\sim} \mathrm{Bin}(n, p_i), \; i = 1,\ldots, k \; ,
$$

which [has the variance](/P/bin-var) $\mathrm{Var}(X_i) = n p_i(1-p_i) = n (p_i - p_i^2)$, constituting the elements of the main diagonal in $\mathrm{Cov}(X)$ in \eqref{eq:mult-cov}. To prove $\mathrm{Cov}(X_i, X_j) = -n p_i p_j$ for $i \ne j$ (which constitutes the off-diagonal elements of the covariance matrix), we first recognize that

$$ \label{eq:bin-sum}
X_i = \sum_{k=1}^n \mathbb{I}_i(k), \quad \text{with} \quad \mathbb{I}_i(k) = \begin{cases}
    1 & \text{if $k$-th draw was of category $i$}, \\
    0 & \text{otherwise} \; ,
\end{cases}
$$

where the indicator function $\mathbb{I}_i$ is a [Bernoulli-distributed](/D/bern) random variable with the [expected value](/P/bern-mean) $p_i$. Then, we have 

$$ \label{eq:mult-cov-qed}
\begin{split}
\mathrm{Cov}(X_i, X_j) &= \mathrm{Cov}\left(\sum_{k=1}^n \mathbb{I}_i(k), \sum_{l=1}^n \mathbb{I}_j(l)\right) \\
&= \sum_{k=1}^n\sum_{l=1}^n \mathrm{Cov}\left(\mathbb{I}_i(k), \mathbb{I}_j(l)\right) \\
&= \sum_{k=1}^n \left[ \mathrm{Cov}\left(\mathbb{I}_i(k), \mathbb{I}_j(k)\right) + \sum_{\substack{l=1 \\ l \ne k}}^n \underbrace{\mathrm{Cov}\left(\mathbb{I}_i(k), \mathbb{I}_j(l)\right)}_{=0} \right] \\
& \stackrel{i \ne j}{=} \;\; \sum_{k=1}^n \left(\mathrm{E}\Big( \underbrace{\mathbb{I}_i(k) \,\mathbb{I}_j(k)}_{=0} \Big) - \mathrm{E}\big(\mathbb{I}_i(k)\big) \mathrm{E}\big(\mathbb{I}_j(k)\big) \right) \\
&= -\sum_{k=1}^n \mathrm{E}\big(\mathbb{I}_i(k)\big) \mathrm{E}\big(\mathbb{I}_j(k)\big) \\
&= -n p_i p_j \; ,
\end{split}
$$

as desired.
