---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-01-24 00:44:00

title: "Log model evidence for binomial observations"
chapter: "Statistical Models"
section: "Categorical data"
topic: "Binomial observations"
theorem: "Log model evidence"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Beta-binomial distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-01-24"
    url: "https://en.wikipedia.org/wiki/Beta-binomial_distribution#Motivation_and_derivation"

proof_id: "P31"
shortcut: "bin-lme"
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

Then, the [log model evidence](/D/lme) for this model is

$$ \label{eq:Bin-LME}
\begin{split}
\log \mathrm{p}(y|m) = \log \Gamma(n+1) &- \log \Gamma(k+1) - \log \Gamma(n-k+1) \\
&+ \log B(\alpha_n,\beta_n) - \log B(\alpha_0,\beta_0) \; .
\end{split}
$$

where the [posterior hyperparameters](/D/post) are given by

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

$$ \label{eq:Bin-JL-s1}
\begin{split}
\mathrm{p}(y,p) &= \mathrm{p}(y|p) \, \mathrm{p}(p) \\
&= {n \choose y} \, p^y \, (1-p)^{n-y} \cdot frac{1}{B(\alpha_0,\beta_0)} \, p^{\alpha_0-1} \, (1-p)^{\beta_0-1} \\
&= {n \choose y} \, \frac{1}{B(\alpha_0,\beta_0)} \, p^{\alpha_0+y-1} \, (1-p)^{\beta_0+(n-y)-1} \; .
\end{split}
$$

Note that the [model evidence is the marginal density of the joint likelihood](/D/ml):

$$ \label{eq:Bin-ME-s1}
\mathrm{p}(y) = \int \mathrm{p}(y,p) \, \mathrm{d}p \; .
$$

Setting $\alpha_n = \alpha_0 + y$ and $\beta_n = \beta_0 + (n-y)$, the joint likelihood can also be written as

$$ \label{eq:Bin-JL-s2}
\mathrm{p}(y,p) = {n \choose y} \, \frac{1}{B(\alpha_0,\beta_0)} \, \frac{B(\alpha_n,\beta_n)}{1} \, \frac{1}{B(\alpha_n,\beta_n)} \, p^{\alpha_n-1} \, (1-p)^{\beta_n-1} \; .
$$

Using the [probability density function of the beta distribution](/P/beta-pdf), $p$ can now be integrated out easily

$$ \label{eq:Bin-ME-s2}
\begin{split}
\mathrm{p}(y) &= \int {n \choose y} \, \frac{1}{B(\alpha_0,\beta_0)} \, \frac{B(\alpha_n,\beta_n)}{1} \, \frac{1}{B(\alpha_n,\beta_n)} \, p^{\alpha_n-1} \, (1-p)^{\beta_n-1} \, \mathrm{d}p \\
&= {n \choose y} \, \frac{B(\alpha_n,\beta_n)}{B(\alpha_0,\beta_0)} \int \mathrm{Bet}(p; \alpha_n, \beta_n) \, \mathrm{d}p \\
&= {n \choose y} \, \frac{B(\alpha_n,\beta_n)}{B(\alpha_0,\beta_0)} \; ,
\end{split}
$$

such that the [log model evidence](/D/lme) (LME) is shown to be

$$ \label{eq:Bin-LME-s1}
\log \mathrm{p}(y|m) = \log {n \choose y} + \log B(\alpha_n,\beta_n) - \log B(\alpha_0,\beta_0) \; .
$$

With the definition of the binomial coefficient

$$ \label{eq:bin-coeff}
{n \choose k} = \frac{n!}{k! \, (n-k)!}
$$

and the definition of the gamma function

$$ \label{eq:gam-fct}
\Gamma(n) = (n-1)! \; ,
$$

the LME finally becomes

$$ \label{eq:Bin-LME-s2}
\begin{split}
\log \mathrm{p}(y|m) = \log \Gamma(n+1) &- \log \Gamma(k+1) - \log \Gamma(n-k+1) \\
&+ \log B(\alpha_n,\beta_n) - \log B(\alpha_0,\beta_0) \; .
\end{split}
$$