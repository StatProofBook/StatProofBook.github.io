---
layout: proof
mathjax: true

author: "Lee Crossley"
affiliation: ""
e_mail: ""
date: 2026-11-21 22:12:00

title: "Mean of the Wishart distribution"
chapter: "Probability Distributions"
section: "Matrix-variate continuous distributions"
topic: "Wishart distribution"
theorem: "Mean"

sources:
  - authors: "Bishop, Christopher M."
    year: 2006
    title: "Pattern Recognition and Machine Learning"
    in: "Springer"
    pages: "Appendix B, p. 693, eqs. B.78–B.81"
    url: "https://www.microsoft.com/en-us/research/wp-content/uploads/2006/01/Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf"

proof_id: "P567"
shortcut: "wish-mean"
username: "leecrossley"
---


**Theorem:** Let $S$ be a $p \times p$ [Wishart random matrix](/D/wish) with positive-definite scale matrix $V \in \mathbb{R}^{p \times p}$ and real [degrees of freedom](/D/dof) $\nu>p-1$. Then, its [mean](/D/mean-rmat) is

$$ \label{eq:wish-mean}
\mathrm{E}[S] = \nu V \; .
$$


**Proof:** Fix a non-zero column vector $u \in \mathbb R^p$ and let $q = u^\mathrm{T} V u > 0$. We compute the moment-generating function of $u^\mathrm{T}Su$. The [Wishart density](/P/wish-pdf), as a function of $S$, is proportional to

$$ \label{eq:wish-mean-s1}
|V|^{-\nu/2} \, |S|^{(\nu-p-1)/2} \, \exp\!\left[ -\frac{1}{2} \operatorname{tr}(V^{-1} S) \right]
$$

where $\lvert \cdot \rvert$ denotes the determinant and the omitted constant depends only on $\nu$ and $p$. Multiplying the density by $\exp(t u^\mathrm{T} S u)$ replaces $V^{-1}$ in the exponential by $V^{-1} - 2 t u u^\mathrm{T}$. For $t$ sufficiently close to zero, this is positive-definite. Write $V_t = (V^{-1} - 2 t u u^\mathrm{T})^{-1}$. Since the density with scale $V_t$ integrates to one, the ratio of the two scale factors gives

$$ \label{eq:wish-mean-s2}
  \mathrm{E}\left[ \exp(t u^\mathrm{T} S u) \right]
= \left( \frac{|V_t|}{|V|} \right)^{\nu/2}
= (1 - 2 t q)^{-\nu/2}.
$$

The last equality uses the matrix determinant lemma. Differentiating at $t=0$ gives $\mathrm{E}[u^\mathrm{T} S u] = \nu u^\mathrm{T} V u$. In particular, each diagonal entry has a [finite mean](/D/mean). Positive-definiteness gives $\lvert S_{ij} \rvert \leq (S_{ii} + S_{jj})/2$, so the off-diagonal entries are integrable as well. Thus, the symmetric matrices $\mathrm{E}[S]$ and $\nu V$ have the same quadratic form for every $u$, proving \eqref{eq:wish-mean}.