---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2025-09-25 10:57:55

title: "Decompositions of the variational free energy"
chapter: "General Theorems"
section: "Bayesian statistics"
topic: "Bayesian inference"
theorem: "Decomposition of the free energy"

sources:
  - authors: "Zeidman et al."
    year: 2023
    title: "A primer on Variational Laplace (VL)"
    in: "NeuroImage"
    pages: "vol. 279, art. 120310, p. 5, eqs. 12-14"
    url: "https://www.sciencedirect.com/science/article/pii/S1053811923004615"
    doi: "10.1016/j.neuroimage.2023.120310"

proof_id: "P516"
shortcut: "fren-dec"
username: "JoramSoch"
---


**Theorem:** Let $m$ be a [generative model](/D/gm) with [likelihood function](/D/lf) $p(y \vert \theta,m) = p(y \vert \theta)$, [prior distribution](/D/prior) $p(\theta \vert m) = p(\theta)$, [joint likelihood](/D/jl) $p(y,\theta \vert m) = p(y,\theta)$, true [posterior distribution](/D/post) $p(\theta \vert y,m) = p(\theta \vert y)$ and [approximate posterior](/D/vb) distribution $q(\theta \vert m) = q(\theta) \approx p(\theta \vert y)$. Then, the [variational free energy](/D/vblme) can be decomposed as

1) the difference between log model evidence and KL divergence of approximate from true posterior

$$ \label{eq:vb-fe1}
\mathrm{F}[q(\theta)] = \log p(y) - \mathrm{KL}[q(\theta) || p(\theta \vert y)] \; ,
$$

2) the difference of expected log-likelihood and KL divergence of approximate posterior from prior

$$ \label{eq:vb-fe2}
\mathrm{F}[q(\theta)] = \left\langle \log p(y \vert \theta) \right\rangle_{q(\theta)} - \mathrm{KL}[q(\theta) || p(\theta)]
$$

3) the sum of expected joint log-likelihood and approximate posterior differential entropy

$$ \label{eq:vb-fe3}
\mathrm{F}[q(\theta)] = \left\langle \log p(y,\theta) \right\rangle_{q(\theta)} - \mathrm{h}[q(\theta)]
$$

where $p(y \vert m) = p(y)$ is the [marginal likelihood](/D/ml), $\left\langle \cdot \right\rangle_{p(x)}$ denotes an [expectation](/D/mean) with respect to the [density](/D/pdf) $p(x)$, $\mathrm{KL}[\cdot \vert\vert \cdot]$ denotes the [Kullback-Leibler divergence](/D/kl) and $\mathrm{h}[\cdot]$ denotes the [differential entropy](/D/dent).


**Proof:** The [log model evidence](/D/lme) is defined as

$$ \label{eq:lme}
\log p(y) = \log \int_{\Theta} p(y,\theta) \, \mathrm{d}\theta
$$

and using the approximate posterior density $q(\theta)$, this can be rewritten as

$$ \label{eq:lme-eq}
\begin{split}
   \log p(y)
&= \log \int_{\Theta} \frac{q(\theta)}{q(\theta)}  \, \mathrm{d}\theta \\
&= \log \left\langle \frac{p(y,\theta)}{q(\theta)} \right\rangle_{q(\theta)} \; .
\end{split}
$$

By [Jensen's inequality](/P/jens-ineq) and [because the logarithm is a concave function](/P/kl-nonneg3), we have:

$$ \label{eq:lme-ineq}
     \log \left\langle \frac{p(y,\theta)}{q(\theta)} \right\rangle_{q(\theta)}
\geq \left\langle \log \frac{p(y,\theta)}{q(\theta)} \right\rangle_{q(\theta)} \; .
$$

The right-hand side of this equation is referred to as the [free energy](/D/vblme):

$$ \label{eq:fe}
\mathrm{F}[q(\theta)] = \left\langle \log \frac{p(y,\theta)}{q(\theta)} \right\rangle_{q(\theta)} \; .
$$

With that, we can show the above identites:

1) the difference between log model evidence and KL divergence of approximate from true posterior

$$ \label{eq:vb-fe1-qed}
\begin{split}
   \mathrm{F}[q(\theta)]
&= \left\langle \log \frac{p(y,\theta)}{q(\theta)} \right\rangle_{q(\theta)} \\
&= \left\langle \log \frac{p(\theta \vert y) p(y)}{q(\theta)} \right\rangle_{q(\theta)} \\
&= \left\langle \log p(y) - \log \frac{q(\theta)}{p(\theta \vert y)} \right\rangle_{q(\theta)} \\
&= \left\langle \log p(y) \right\rangle_{q(\theta)} - \int_{\Theta} q(\theta) \log \frac{q(\theta)}{p(\theta \vert y)} \, \mathrm{d}\theta \\
&= \log p(y) - \mathrm{KL}[q(\theta) || p(\theta \vert y)]
\end{split}
$$

where the first term is the [log model evidence](/D/lme) (= log marginal likelihood) and the second term can be seen as an approximation error (= divergence of approximate from true posterior distribution);

2) the difference of expected log-likelihood and KL divergence of approximate posterior from prior

$$ \label{eq:vb-fe2-qed}
\begin{split}
   \mathrm{F}[q(\theta)]
&= \left\langle \log \frac{p(y,\theta)}{q(\theta)} \right\rangle_{q(\theta)} \\
&= \left\langle \log \frac{p(y \vert \theta) p(\theta)}{q(\theta)} \right\rangle_{q(\theta)} \\
&= \left\langle \log p(y \vert \theta) - \log \frac{q(\theta)}{p(\theta)} \right\rangle_{q(\theta)} \\
&= \int_{\Theta} q(\theta) \log p(y \vert \theta) \, \mathrm{d}\theta - \int_{\Theta} q(\theta) \log \frac{q(\theta)}{p(\theta)} \, \mathrm{d}\theta \\
&= \left\langle \log p(y \vert \theta) \right\rangle_{q(\theta)} - \mathrm{KL}[q(\theta) || p(\theta)]
\end{split}
$$

where the first term can be seen as an [accuracy term](/P/lme-anc) (= posterior expected log-likelihood) and the second term can be seen as a [complexity penalty](/P/lme-anc) (= divergence of posterior from prior distribution);

3) the sum of expected joint log-likelihood and approximate posterior entropy

$$ \label{eq:vb-fe3-qed}
\begin{split}
\mathrm{F}[q(\theta)]
&= \left\langle \log \frac{p(y,\theta)}{q(\theta)} \right\rangle_{q(\theta)} \\
&= \left\langle \log p(y,\theta) - \log q(\theta) \right\rangle_{q(\theta)} \\
&= \int_{\Theta} q(\theta) \log p(y,\theta) \, \mathrm{d}\theta - \int_{\Theta} q(\theta) \log q(\theta) \, \mathrm{d}\theta  \\
&= \left\langle \log p(y,\theta) \right\rangle_{q(\theta)} + \mathrm{h}[q(\theta)]
\end{split}
$$

where the first term represents the negative energy (= posterior expected joint log-likelihood) and the second term presents the [posterior entropy](/D/dent) (= differential entropy of the approximate posterior distribution).