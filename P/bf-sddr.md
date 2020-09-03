---
layout: proof
mathjax: true

author: "Thomas J. Faulkenberry"
affiliation: "Tarleton State University"
e_mail: "faulkenberry@tarleton.edu"
date: 2020-08-26 12:00:00

title: "Savage-Dickey Density Ratio for computing Bayes Factors"
chapter: "Model Selection"
section: "Bayesian model selection"
topic: "Bayes factor"
theorem: "Computation using Savage-Dickey Density Ratio"

sources:
  - authors: "Faulkenberry, Thomas J."
    year: 2019
    title: "A tutorial on generalizing the default Bayesian t-test via posterior sampling and encompassing priors"
    in: "Communications for Statistical Applications and Methods"
    pages: "vol. 26, no. 2, pp. 217-238"
    url: "https://dx.doi.org/10.29220/CSAM.2019.26.2.217"
    doi: "10.29220/CSAM.2019.26.2.217"
  - authors: "Penny, W.D. and Ridgway, G.R."
    year: 2013
    title: "Efficient Posterior Probability Mapping Using Savage-Dickey Ratios"
    in: "PLoS ONE"
    pages: "vol. 8, iss. 3, art. e59655, eq. 16"
    url: "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0059655"
    doi: "10.1371/journal.pone.0059655"

proof_id: "P156"
shortcut: "bf-sddr"
username: "tomfaulkenberry"
---


**Theorem:** Consider two competing [models](/D/gm) on data $y$ containing parameters $\delta$ and $\varphi$, namely $m_0:\delta=\delta_0,\varphi$ and $m_1:\delta,\varphi$. In this context, we say that $\delta$ is a parameter of interest, $\varphi$ is a nuisance parameter (i.e., common to both models), and $m_0$ is a sharp point hypothesis nested within $m_1$. Suppose further that the prior for the nuisance parameter $\varphi$ in $m_0$ is equal to the prior for $\varphi$ in $m_1$ after conditioning on the restriction -- that is, $p(\varphi\mid m_0) = p(\varphi\mid \delta=\delta_0,m_1)$. Then the [Bayes factor](/D/bf) for $m_0$ over $m_1$ can be computed as:

$$ \label{eq:sd}
\text{BF}_{01} = \frac{p(\delta=\delta_0\mid y,m_1)}{p(\delta=\delta_0\mid m_1)}.
$$

**Proof:** By [definition](/D/bf), the Bayes factor $\text{BF}_{01}$ is the ratio of marginal likelihoods of data $y$ over $m_0$ and $m_1$, respectively. That is,

$$ \label{eq:bf}
\text{BF}_{01}=\frac{p(y \mid m_0)}{p(y \mid m_1)}.
$$

The key idea in the proof is that we can use a "change of variables" technique to express $\text{BF}_{01}$ entirely in terms of the "encompassing" model $m_1$. This proceeds by first unpacking the [marginal likelihood](/D/ml) for $m_0$ over the nuisance parameter $\varphi$ and then using the fact that $m_0$ is a sharp hypothesis nested within $m_1$ to rewrite everything in terms of $m_1$. Specifically,

$$ \label{eq:ml-m0}
\begin{split}
 p(y \mid m_0) &= \int p(y \mid \varphi,m_0) \, p(\varphi\mid m_0) \, \mathrm{d} \varphi \\
  &= \int p(y \mid \varphi,\delta=\delta_0,m_1) \, p(\varphi\mid \delta=\delta_0,m_1) \, \mathrm{d} \varphi \\
  &= p(y \mid \delta=\delta_0,m_1).\\
\end{split}
$$

By [Bayes' theorem](/P/bayes-th), we can rewrite this last line as

$$ \label{eq:ml-m0-bt}
p(y \mid \delta=\delta_0,m_1) = \frac{p(\delta=\delta_0\mid y,m_1) \, p(y \mid m_1)}{p(\delta=\delta_0\mid m_1)}.
$$

Thus we have

$$ 
\begin{split}
  \text{BF}_{01} &\overset{\eqref{eq:bf}}{=} \frac{p(y \mid m_0)}{p(y \mid m_1)}\\
  &= p(y \mid m_0) \cdot \frac{1}{p(y \mid m_1)}\\
  &\overset{\eqref{eq:ml-m0}}{=} p(y \mid \delta=\delta_0,m_1) \cdot \frac{1}{p(y \mid m_1)}\\
  &\overset{\eqref{eq:ml-m0-bt}}{=} \frac{p(\delta=\delta_0\mid y,m_1) \, p(y \mid m_1)}{p(\delta=\delta_0\mid m_1)} \cdot \frac{1}{p(y \mid m_1)}\\
  &= \frac{p(\delta=\delta_0 \mid y,m_1)}{p(\delta=\delta_0\mid m_1)},
\end{split}
$$

which completes the proof of \eqref{eq:sd}.