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

dependencies:
  - theorem: "probability density function of the normal-gamma distribution"
  - theorem: "Kullback-Leibler divergence of the multivariate normal distribution"
  - theorem: "Kullback-Leibler divergence of the univariate gamma distribution"
  - theorem: "law of conditional probability"
  - theorem: "mean of the gamma distribution"

sources:
  - authors: "Soch & Allefeld"
    year: 2016
    title: "Kullback-Leibler Divergence for the Normal-Gamma Distribution"
    in: "arXiv math.ST"
    pages: "1611.01437"
    url: "https://arxiv.org/abs/1611.01437"

proof_id: "P6"
shortcut: "ng-kl"
username: "JoramSoch"
---


**Theorem:** Let $x \in \mathbb{R}^k$ be a random vector and $y > 0$ be a random variable. Assume two normal-gamma distributions $P$ and $Q$ specifying the joint distribution of $x$ and $y$ as

$$ \label{eq:NGs}
\begin{split}
P: \; (x,y) &\sim \mathrm{NG}(\mu_1, \Lambda_1^{-1}, a_1, b_1) \\
Q: \; (x,y) &\sim \mathrm{NG}(\mu_2, \Lambda_2^{-1}, a_2, b_2) \; . \\
\end{split}
$$

Then, the Kullback-Leibler divergence of $P$ from $Q$ is given by

$$ \label{eq:NG-KL}
\begin{split}
\mathrm{KL}[P\,||\,Q] &= \frac{1}{2} \frac{a_1}{b_1} \left[ (\mu_2 - \mu_1)^T \Lambda_2 (\mu_2 - \mu_1) \right] + \frac{1}{2} \, \mathrm{tr}(\Lambda_2 \Lambda_1^{-1}) - \frac{1}{2} \ln \frac{|\Lambda_2|}{|\Lambda_1|} - \frac{k}{2} \\
&+ a_2 \, \ln \frac{b_1}{b_2} - \ln \frac{\Gamma(a_1)}{\Gamma(a_2)} + (a_1 - a_2) \, \psi(a_1) - (b_1 - b_2) \, \frac{a_1}{b_1} \; .
\end{split}
$$


**Proof:** The probabibility density function of the normal-gamma (NG) distribution is

$$ \label{eq:NG-pdf}
p(x,y) = p(x|y) \cdot p(y) = \mathcal{N}(x; \mu, (y \Lambda)^{-1}) \cdot \mathrm{Gam}(y; a, b)
$$

where $\mathcal{N}(x; \mu, \Sigma)$ is a multivariate normal density with mean $\mu$ and covariance $\Sigma$ (hence, precision $\Lambda$) and $\mathrm{Gam}(y; a, b)$ is a univariate gamma density with shape $a$ and rate $b$. The Kullback-Leibler (KL) divergence of the multivariate normal distribution is

$$ \label{eq:mvn-KL}
\mathrm{KL}[P\,||\,Q] = \frac{1}{2} \left[ (\mu_2 - \mu_1)^T \Sigma_2^{-1} (\mu_2 - \mu_1) + \mathrm{tr}(\Sigma_2^{-1} \Sigma_1) - \ln \frac{|\Sigma_1|}{|\Sigma_2|} - k \right]
$$

and the Kullback-Leibler divergence of the univariate gamma distribution is

$$ \label{eq:gam-KL}
\mathrm{KL}[P\,||\,Q] = a_2 \, \ln \frac{b_1}{b_2} - \ln \frac{\Gamma(a_1)}{\Gamma(a_2)} + (a_1 - a_2) \, \psi(a_1) - (b_1 - b_2) \, \frac{a_1}{b_1}
$$

where $\Gamma(x)$ is the gamma function and $\psi(x)$ is the digamma function.

<br>
The KL divergence for a continuous random variable is given by 

$$ \label{eq:KL-cont}
\mathrm{KL}[P\,||\,Q] = \int_{\mathcal{Z}} p(z) \, \ln \frac{p(z)}{q(z)} \, \mathrm{d}z
$$

which, applied to the normal-gamma distribution over $x$ and $y$, yields

$$ \label{eq:NG-KL0}
\mathrm{KL}[P\,||\,Q] = \int_{0}^{\infty} \int_{\mathbb{R}^k} p(x,y) \, \ln \frac{p(x,y)}{q(x,y)} \, \mathrm{d}x \, \mathrm{d}y \; .
$$

Using the law of conditional probability, this can be evaluated as follows:

$$ \label{eq:NG-KL1}
\begin{split}
\mathrm{KL}[P\,||\,Q] &= \int_{0}^{\infty} \int_{\mathbb{R}^k} p(x|y) \, p(y) \, \ln \frac{p(x|y) \, p(y)}{q(x|y) \, q(y)} \, \mathrm{d}x \, \mathrm{d}y \\
&= \int_{0}^{\infty} \int_{\mathbb{R}^k} p(x|y)\, p(y) \, \ln \frac{p(x|y)}{q(x|y)} \, \mathrm{d}x \, \mathrm{d}y + \int_{0}^{\infty} \int_{\mathbb{R}^k} p(x|y)\, p(y) \, \ln \frac{p(y)}{q(y)} \, \mathrm{d}x \, \mathrm{d}y \\
&= \int_{0}^{\infty} p(y) \int_{\mathbb{R}^k} p(x|y) \, \ln \frac{p(x|y)}{q(x|y)} \, \mathrm{d}x \, \mathrm{d}y + \int_{0}^{\infty} p(y) \, \ln \frac{p(y)}{q(y)} \int_{\mathbb{R}^k} p(x|y) \, \mathrm{d}x \, \mathrm{d}y \\
&= \left\langle \mathrm{KL}[p(x|y)\,||\,q(x|y)] \right\rangle_{p(y)} + \mathrm{KL}[p(y)\,||\,q(y)] \; .
\end{split}
$$

In other words, the KL divergence between two normal-gamma distributions over $x$ and $y$ is equal to the sum of a multivariate normal KL divergence regarding $x$ conditional on $y$, expected over $y$, and a univariate gamma KL divergence regarding $y$.

<br>
From equations \eqref{eq:NG-pdf} and \eqref{eq:mvn-KL}, the first term becomes

$$ \label{eq:exp-mvn-KL-s1}
\begin{split}
&\left\langle \mathrm{KL}[p(x|y)\,||\,q(x|y)] \right\rangle_{p(y)} \\
&= \left\langle \frac{1}{2} \left[ (\mu_2 - \mu_1)^T (y \Lambda_2) (\mu_2 - \mu_1) + \mathrm{tr}\left( (y \Lambda_2) (y \Lambda_1)^{-1} \right) - \ln \frac{|(y \Lambda_1)^{-1}|}{|(y \Lambda_2)^{-1}|} - k \right] \right\rangle_{p(y)} \\
&= \left\langle \frac{y}{2} (\mu_2 - \mu_1)^T \Lambda_2 (\mu_2 - \mu_1) + \frac{1}{2} \, \mathrm{tr}(\Lambda_2 \Lambda_1^{-1}) - \frac{1}{2} \ln \frac{|\Lambda_2|}{|\Lambda_1|} - \frac{k}{2} \right\rangle_{p(y)} \\
\end{split}
$$

and using the relation $y \sim \mathrm{Gam}(a,b) \Rightarrow \left\langle y \right\rangle = a/b$, we have

$$ \label{eq:exp-mvn-KL-s2}
\begin{split}
\left\langle \mathrm{KL}[p(x|y)\,||\,q(x|y)] \right\rangle_{p(y)} = \frac{1}{2} \frac{a_1}{b_1} (\mu_2 - \mu_1)^T \Lambda_2 (\mu_2 - \mu_1) + \frac{1}{2} \, \mathrm{tr}(\Lambda_2 \Lambda_1^{-1}) - \frac{1}{2} \ln \frac{|\Lambda_2|}{|\Lambda_1|} - \frac{k}{2} \; .
\end{split}
$$

By plugging \eqref{eq:exp-mvn-KL-s2} and \eqref{eq:gam-KL} into \eqref{eq:NG-KL1}, one arrives at the KL divergence given by \eqref{eq:NG-KL}.