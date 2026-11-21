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
    pages: "Appendix B, p. 693, equations B.78–B.81"
    url: "https://www.microsoft.com/en-us/research/wp-content/uploads/2006/01/Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf"

proof_id: "P567"
shortcut: "wish-mean"
username: "leecrossley"
---


**Theorem.** Let $S$ be a $p \times p$ [Wishart random matrix](/D/wish) with positive-definite scale matrix $V$ and real degrees of freedom $\nu>p-1$. Then its [mean](/D/mean-rmat) is

$$ \label{eq:wish-mean}
\mathrm{E}[S]=\nu V.
$$

**Proof.** Fix a nonzero column vector $u\in\mathbb R^p$ and put $q=u^\mathrm{T}Vu>0$. We compute the moment-generating function of $u^\mathrm{T}Su$. The Wishart density, as a function of $S$, is proportional to

$$
|V|^{-\nu/2}|S|^{(\nu-p-1)/2}
\exp\!\left[-\tfrac12\operatorname{tr}(V^{-1}S)\right],
$$

where $|\cdot|$ denotes the determinant and the omitted constant depends only on $\nu$ and $p$. Multiplying the density by $\exp(tu^\mathrm{T}Su)$ replaces $V^{-1}$ in the exponential by $V^{-1}-2tuu^\mathrm{T}$. For $t$ sufficiently close to zero this is positive definite. Write $V_t=(V^{-1}-2tuu^\mathrm{T})^{-1}$. Since the density with scale $V_t$ integrates to one, the ratio of the two scale factors gives

$$
\mathrm{E}\big[\exp(tu^\mathrm{T}Su)\big]
=\left(\frac{|V_t|}{|V|}\right)^{\nu/2}
=(1-2tq)^{-\nu/2}.
$$

The last equality uses the matrix determinant lemma. Differentiating at $t=0$ gives $\mathrm{E}[u^\mathrm{T}Su]=\nu u^\mathrm{T}Vu$. In particular, each diagonal entry has a finite mean. Positive definiteness gives $|S_{ij}|\leq(S_{ii}+S_{jj})/2$, so the off-diagonal entries are integrable as well. The symmetric matrices $\mathrm{E}[S]$ and $\nu V$ have the same quadratic form for every $u$, proving \eqref{eq:wish-mean}.
