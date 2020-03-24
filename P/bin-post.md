---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-01-24 00:20:00

title: "Posterior distribution for binomial observations"
chapter: "Statistical Models"
section: "Categorical data"
topic: "Binomial observations"
theorem: "Posterior distribution"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Binomial distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-01-23"
    url: "https://en.wikipedia.org/wiki/Binomial_distribution#Estimation_of_parameters"

proof_id: "P30"
shortcut: "bin-post"
username: "JoramSoch"
---


**Theorem:** Let $y$ be the number of successes resulting from $n$ independent trials with unknown success probability $p$, such that $y$ follows a [binomial distribution](/D/bin):

$$ \label{eq:Bin}
y \sim \mathrm{Bin}(n,p) \; .
$$

Moreover, assume a [beta prior distribution](/P/bin-prior) over the model parameter $p$:

$$ \label{eq:Bin-prior}
\mathrm{p}(p) = \mathrm{Bet}(p; \alpha_0, \beta_0) \; .
$$

Then, the [posterior distribution](/D/post) is also a [beta distribution](/D/beta)

$$ \label{eq:Bin-post}
\mathrm{p}(p|y) = \mathrm{Bet}(p; \alpha_n, \beta_n) \; .
$$

and the [posterior hyperparameters](/D/post) are given by

$$ \label{eq:Bin-post-par}
\begin{split}
\alpha_n &= \alpha_0 + y \\
\beta_n &= \beta_0 + (n-y) \; .
\end{split}
$$


**Proof:** With the [probability mass function of the binomial distribution](/P/bin-pmf), the [likelihood function](/D/lf) implied by \eqref{eq:Bin} is given by

$$ \label{eq:Bin-LF}
\mathrm{p}(y|p) = {n \choose y} \, p^y \, (1-p)^{n-y} \; .
$$

Combining the likelihood function \eqref{eq:Bin-LF} with the prior distribution \eqref{eq:Bin-prior}, the [joint likelihood](/D/jl) of the model is given by

$$ \label{eq:Bin-JL}
\begin{split}
\mathrm{p}(y,p) &= \mathrm{p}(y|p) \, \mathrm{p}(p) \\
&= {n \choose y} \, p^y \, (1-p)^{n-y} \cdot frac{1}{B(\alpha_0,\beta_0)} \, p^{\alpha_0-1} \, (1-p)^{\beta_0-1} \\
&= \frac{1}{B(\alpha_0,\beta_0)} {n \choose y} \, p^{\alpha_0+y-1} \, (1-p)^{\beta_0+(n-y)-1} \; .
\end{split}
$$

Note that the [posterior distribution is proportional to the joint likelihood](/P/post-jl):

$$ \label{eq:Bin-post-s1}
\mathrm{p}(p|y) \propto \mathrm{p}(y,p) \; .
$$

Setting $\alpha_n = \alpha_0 + y$ and $\beta_n = \beta_0 + (n-y)$, the posterior distribution is therefore proportional to

$$ \label{eq:Bin-post-s2}
\mathrm{p}(p|y) \propto p^{\alpha_n-1} \, (1-p)^{\beta_n-1}
$$

which, when normalized to one, results in the [probability density function of the beta distribution](/P/beta-pdf):

$$ \label{eq:Bin-post-qed}
\mathrm{p}(p|y) = \frac{1}{B(\alpha_n,\beta_n)} \, p^{\alpha_n-1} \, (1-p)^{\beta_n-1} = \mathrm{Bet}(p; \alpha_n, \beta_n) \; .
$$