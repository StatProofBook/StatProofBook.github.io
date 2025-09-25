---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2025-09-25 09:46:53

title: "Non-negativity of the Kullback-Leibler divergence"
chapter: "General Theorems"
section: "Information theory"
topic: "Kullback-Leibler divergence"
theorem: "Non-negativity"

sources:
  - authors: "Ostwald et al."
    year: 2014
    title: "A tutorial on variational Bayes for latent linear stochastic time-series models"
    in: "Journal of Mathematical Psychology"
    pages: "vol. 60, pp. 1-19, App. A"
    url: "https://www.sciencedirect.com/science/article/pii/S0022249614000352"
    doi: "10.1016/j.jmp.2014.04.0"

proof_id: "P515"
shortcut: "kl-nonneg3"
username: "JoramSoch"
---


**Theorem:** The [Kullback-Leibler divergence](/D/kl) is always non-negative

$$ \label{eq:KL-nonneg}
\mathrm{KL}[P||Q] \geq 0
$$

with $\mathrm{KL}[P \vert \vert Q] = 0$, if and only if $P = Q$.


**Proof:** The continuous [Kullback-Leibler divergence](/D/kl) is defined as

$$ \label{eq:KL-cont}
\mathrm{KL}[P||Q] = \int_{\mathcal{X}} p(x) \cdot \log \frac{p(x)}{q(x)} \, \mathrm{d}x \; .
$$

For a [continuous random variable](/D/rvar-disc) $X$ with possible values $x \in \mathcal{X}$, [Jensen's inequality](/P/jens-ineq) implies that

$$ \label{eq:jens-ineq-cont}
\int_{\mathcal{X}} q(x) g(x) \, \mathrm{d}x \geq g\left( \int_{\mathcal{X}} q(x) x \, \mathrm{d}x \right)
$$

where $g(x)$ is a convex function and $q(x)$ is the [probability density function](/D/pdf) of $X$. The negative KL divergence is equal to

$$ \label{eq:KL-nonneg-s1}
\begin{split}
   -\mathrm{KL}[P||Q]
&= -\int_{\mathcal{X}} p(x) \cdot \log \frac{p(x)}{q(x)} \, \mathrm{d}x \\
&= \int_{\mathcal{X}} p(x) \cdot \log \frac{q(x)}{p(x)} \, \mathrm{d}x \; .
\end{split}
$$

Applying \eqref{eq:jens-ineq-cont} to \eqref{eq:KL-nonneg-s1}, we have

$$ \label{eq:KL-nonneg-s2}
\begin{split}
      -\mathrm{KL}[P||Q]
&\leq \log \int_{\mathcal{X}} p(x) \cdot \frac{q(x)}{p(x)} \, \mathrm{d}x \\
&=    \log \int_{\mathcal{X}} q(x) \, \mathrm{d}x \\
&=    \log 1 = 0
\end{split}
$$

where the inequality sign has been reversed, because $\log(x)$ is a concave function, and we have used the fact that a PDF [integrates to one](/D/pdf). From \eqref{eq:KL-nonneg-s2}, we get

$$ \label{eq:KL-nonneg-s3}
\begin{split}
-\mathrm{KL}[P||Q] &\leq 0 \\
 \mathrm{KL}[P||Q] &\geq 0 \; .
\end{split}
$$