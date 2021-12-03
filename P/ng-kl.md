---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2019-12-06 09:35:00

title: "Kullback-Leibler divergence for the normal-gamma distribution"
chapter: "Probability Distributions"
section: "Multivariate continuous distributions"
topic: "Normal-gamma distribution"
theorem: "Kullback-Leibler divergence"

sources:
  - authors: "Soch J, Allefeld A"
    year: 2016
    title: "Kullback-Leibler Divergence for the Normal-Gamma Distribution"
    in: "arXiv math.ST"
    pages: "1611.01437"
    url: "https://arxiv.org/abs/1611.01437"

proof_id: "P6"
shortcut: "ng-kl"
username: "JoramSoch"
---


**Theorem:** Let $x$ be an $n \times 1$ [random vector](/D/rvec) and let $y$ be a positive [random variable](/D/rvar). Assume two [normal-gamma distributions](/D/ng) $P$ and $Q$ specifying the joint distribution of $x$ and $y$ as

$$ \label{eq:NGs}
\begin{split}
P: \; (x,y) &\sim \mathrm{NG}(\mu_1, \Lambda_1^{-1}, a_1, b_1) \\
Q: \; (x,y) &\sim \mathrm{NG}(\mu_2, \Lambda_2^{-1}, a_2, b_2) \; .
\end{split}
$$

Then, the [Kullback-Leibler divergence](/D/kl) of $P$ from $Q$ is given by

$$ \label{eq:NG-KL}
\begin{split}
\mathrm{KL}[P\,||\,Q] &= \frac{1}{2} \frac{a_1}{b_1} \left[ (\mu_2 - \mu_1)^\mathrm{T} \Lambda_2 (\mu_2 - \mu_1) \right] + \frac{1}{2} \, \mathrm{tr}(\Lambda_2 \Lambda_1^{-1}) - \frac{1}{2} \ln \frac{|\Lambda_2|}{|\Lambda_1|} - \frac{n}{2} \\
&+ a_2 \, \ln \frac{b_1}{b_2} - \ln \frac{\Gamma(a_1)}{\Gamma(a_2)} + (a_1 - a_2) \, \psi(a_1) - (b_1 - b_2) \, \frac{a_1}{b_1} \; .
\end{split}
$$


**Proof:** The [probabibility density function of the normal-gamma distribution](/P/ng-pdf) is

$$ \label{eq:NG-pdf}
p(x,y) = p(x|y) \cdot p(y) = \mathcal{N}(x; \mu, (y \Lambda)^{-1}) \cdot \mathrm{Gam}(y; a, b) \; .
$$

The [Kullback-Leibler divergence of the multivariate normal distribution](/P/mvn-kl) is

$$ \label{eq:mvn-KL}
\mathrm{KL}[P\,||\,Q] = \frac{1}{2} \left[ (\mu_2 - \mu_1)^\mathrm{T} \Sigma_2^{-1} (\mu_2 - \mu_1) + \mathrm{tr}(\Sigma_2^{-1} \Sigma_1) - \ln \frac{|\Sigma_1|}{|\Sigma_2|} - n \right]
$$

and the [Kullback-Leibler divergence of the univariate gamma distribution](/P/gam-kl) is

$$ \label{eq:gam-KL}
\mathrm{KL}[P\,||\,Q] = a_2 \, \ln \frac{b_1}{b_2} - \ln \frac{\Gamma(a_1)}{\Gamma(a_2)} + (a_1 - a_2) \, \psi(a_1) - (b_1 - b_2) \, \frac{a_1}{b_1}
$$

where $\Gamma(x)$ is the gamma function and $\psi(x)$ is the digamma function.

<br>
The [KL divergence for a continuous random variable](/D/kl) is given by 

$$ \label{eq:KL-cont}
\mathrm{KL}[P\,||\,Q] = \int_{\mathcal{Z}} p(z) \, \ln \frac{p(z)}{q(z)} \, \mathrm{d}z
$$

which, applied to the [normal-gamma distribution](/D/ng) over $x$ and $y$, yields

$$ \label{eq:NG-KL0}
\mathrm{KL}[P\,||\,Q] = \int_{0}^{\infty} \int_{\mathbb{R}^n} p(x,y) \, \ln \frac{p(x,y)}{q(x,y)} \, \mathrm{d}x \, \mathrm{d}y \; .
$$

Using the [law of conditional probability](/D/prob-cond), this can be evaluated as follows:

$$ \label{eq:NG-KL1}
\begin{split}
\mathrm{KL}[P\,||\,Q] &= \int_{0}^{\infty} \int_{\mathbb{R}^n} p(x|y) \, p(y) \, \ln \frac{p(x|y) \, p(y)}{q(x|y) \, q(y)} \, \mathrm{d}x \, \mathrm{d}y \\
&= \int_{0}^{\infty} \int_{\mathbb{R}^n} p(x|y)\, p(y) \, \ln \frac{p(x|y)}{q(x|y)} \, \mathrm{d}x \, \mathrm{d}y + \int_{0}^{\infty} \int_{\mathbb{R}^n} p(x|y)\, p(y) \, \ln \frac{p(y)}{q(y)} \, \mathrm{d}x \, \mathrm{d}y \\
&= \int_{0}^{\infty} p(y) \int_{\mathbb{R}^n} p(x|y) \, \ln \frac{p(x|y)}{q(x|y)} \, \mathrm{d}x \, \mathrm{d}y + \int_{0}^{\infty} p(y) \, \ln \frac{p(y)}{q(y)} \int_{\mathbb{R}^n} p(x|y) \, \mathrm{d}x \, \mathrm{d}y \\
&= \left\langle \mathrm{KL}[p(x|y)\,||\,q(x|y)] \right\rangle_{p(y)} + \mathrm{KL}[p(y)\,||\,q(y)] \; .
\end{split}
$$

In other words, the KL divergence between two normal-gamma distributions over $x$ and $y$ is equal to the sum of a multivariate normal KL divergence regarding $x$ conditional on $y$, expected over $y$, and a univariate gamma KL divergence regarding $y$.

<br>
From equations \eqref{eq:NG-pdf} and \eqref{eq:mvn-KL}, the first term becomes

$$ \label{eq:exp-mvn-KL-s1}
\begin{split}
&\left\langle \mathrm{KL}[p(x|y)\,||\,q(x|y)] \right\rangle_{p(y)} \\
&= \left\langle \frac{1}{2} \left[ (\mu_2 - \mu_1)^\mathrm{T} (y \Lambda_2) (\mu_2 - \mu_1) + \mathrm{tr}\left( (y \Lambda_2) (y \Lambda_1)^{-1} \right) - \ln \frac{|(y \Lambda_1)^{-1}|}{|(y \Lambda_2)^{-1}|} - n \right] \right\rangle_{p(y)} \\
&= \left\langle \frac{y}{2} (\mu_2 - \mu_1)^\mathrm{T} \Lambda_2 (\mu_2 - \mu_1) + \frac{1}{2} \, \mathrm{tr}(\Lambda_2 \Lambda_1^{-1}) - \frac{1}{2} \ln \frac{|\Lambda_2|}{|\Lambda_1|} - \frac{n}{2} \right\rangle_{p(y)} \\
\end{split}
$$

and using [the relation](/P/gam-mean) $y \sim \mathrm{Gam}(a,b) \Rightarrow \left\langle y \right\rangle = a/b$, we have

$$ \label{eq:exp-mvn-KL-s2}
\begin{split}
\left\langle \mathrm{KL}[p(x|y)\,||\,q(x|y)] \right\rangle_{p(y)} = \frac{1}{2} \frac{a_1}{b_1} (\mu_2 - \mu_1)^\mathrm{T} \Lambda_2 (\mu_2 - \mu_1) + \frac{1}{2} \, \mathrm{tr}(\Lambda_2 \Lambda_1^{-1}) - \frac{1}{2} \ln \frac{|\Lambda_2|}{|\Lambda_1|} - \frac{n}{2} \; .
\end{split}
$$

By plugging \eqref{eq:exp-mvn-KL-s2} and \eqref{eq:gam-KL} into \eqref{eq:NG-KL1}, one arrives at the KL divergence given by \eqref{eq:NG-KL}.