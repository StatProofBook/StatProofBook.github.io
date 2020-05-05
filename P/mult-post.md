---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-03-11 14:40:00

title: "Posterior distribution for multinomial observations"
chapter: "Statistical Models"
section: "Categorical data"
topic: "Multinomial observations"
theorem: "Posterior distribution"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Dirichlet distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-03-11"
    url: "https://en.wikipedia.org/wiki/Dirichlet_distribution#Conjugate_to_categorical/multinomial"

proof_id: "P80"
shortcut: "mult-post"
username: "JoramSoch"
---


**Theorem:** Let $y = [y_1, \ldots, y_k]$ be the number of observations in $k$ categories resulting from $n$ independent trials with unknown category probabilities $p = [p_1, \ldots, p_k]$, such that $y$ follows a [multinomial distribution](/D/mult):

$$ \label{eq:Mult}
y \sim \mathrm{Mult}(n,p) \; .
$$

Moreover, assume a [Dirichlet prior distribution](/P/mult-prior) over the model parameter $p$:

$$ \label{eq:Mult-prior}
\mathrm{p}(p) = \mathrm{Dir}(p; \alpha_0) \; .
$$

Then, the [posterior distribution](/D/post) is also a [Dirichlet distribution](/D/dir)

$$ \label{eq:Mult-post}
\mathrm{p}(p|y) = \mathrm{Dir}(p; \alpha_n) \; .
$$

and the [posterior hyperparameters](/D/post) are given by

$$ \label{eq:Mult-post-par}
\alpha_{nj} = \alpha_{0j} + y_j, \; j = 1,\ldots,k \; .
$$


**Proof:** With the [probability mass function of the multinomial distribution](/P/mult-pmf), the [likelihood function](/D/lf) implied by \eqref{eq:Mult} is given by

$$ \label{eq:Mult-LF}
\mathrm{p}(y|p) = {n \choose {y_1, \ldots, y_k}} \prod_{j=1}^{k} {p_j}^{y_j} \; .
$$

Combining the likelihood function \eqref{eq:Mult-LF} with the prior distribution \eqref{eq:Mult-prior}, the [joint likelihood](/D/jl) of the model is given by

$$ \label{eq:Mult-JL}
\begin{split}
\mathrm{p}(y,p) &= \mathrm{p}(y|p) \, \mathrm{p}(p) \\
&= {n \choose {y_1, \ldots, y_k}} \prod_{j=1}^{k} {p_j}^{y_j} \cdot \frac{\Gamma \left( \sum_{j=1}^{k} \alpha_{0j} \right)}{\prod_{j=1}^k \Gamma(\alpha_{0j})} \prod_{j=1}^{k} {p_j}^{\alpha_{0j}-1} \\
&= \frac{\Gamma \left( \sum_{j=1}^{k} \alpha_{0j} \right)}{\prod_{j=1}^k \Gamma(\alpha_{0j})} {n \choose {y_1, \ldots, y_k}} \prod_{j=1}^{k} {p_j}^{\alpha_{0j}+y_j-1} \; .
\end{split}
$$

Note that the [posterior distribution is proportional to the joint likelihood](/P/post-jl):

$$ \label{eq:Mult-post-s1}
\mathrm{p}(p|y) \propto \mathrm{p}(y,p) \; .
$$

Setting $\alpha_{nj} = \alpha_{0j} + y_j$, the posterior distribution is therefore proportional to

$$ \label{eq:Mult-post-s2}
\mathrm{p}(p|y) \propto \prod_{j=1}^{k} {p_j}^{\alpha_{nj}-1}
$$

which, when normalized to one, results in the [probability density function of the Dirichlet distribution](/P/dir-pdf):

$$ \label{eq:Mult-post-qed}
\mathrm{p}(p|y) = \frac{\Gamma \left( \sum_{j=1}^{k} \alpha_{nj} \right)}{\prod_{j=1}^k \Gamma(\alpha_{nj})} \prod_{j=1}^{k} {p_j}^{\alpha_{nj}-1} = \mathrm{Dir}(p; \alpha_n) \; .
$$