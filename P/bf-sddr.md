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

def_id: "P156"
shortcut: "bf-sddr"
username: "tomfaulkenberry"
---


**Theorem:** Consider two competing [models](/D/gm) on data $y$ containing parameters $\delta$ and $\varphi$, namely $\mathcal{M}_0:\delta=\delta_0,\varphi$ and $\mathcal{M}_1:\delta,\varphi$. In this context, we say that $\delta$ is a parameter of interest, $\varphi$ is a nuisance parameter (i.e., common to both models), and $\mathcal{M}_0$ is a sharp point hypothesis nested within $\mathcal{M}_1$. Suppose further that the prior for the nuisance parameter $\varphi$ in $\mathcal{M}_0$ is equal to the prior for $\varphi$ in $\mathcal{M}_1$ after conditioning on the restriction -- that is, $p(\varphi\mid \mathcal{M}_0) = p(\varphi\mid \delta=\delta_0,\mathcal{M}_1)$. Then the [Bayes factor](/D/bf) for $\mathcal{M}_0$ over $\mathcal{M}_1$ can be computed as:

$$ \label{eq:sd}
\text{BF}_{01} = \frac{p(\delta=\delta_0\mid y,\mathcal{M}_1)}{p(\delta=\delta_0\mid \mathcal{M}_1)}.
$$

**Proof:**

By [definition](/D/bf), the Bayes factor $\text{BF}_{01}$ is the ratio of marginal likelihoods of data $y$ over $\mathcal{M}_0$ and $\mathcal{M}_1$, respectively. That is,

$$ \label{eq:bf}
\text{BF}_{01}=\frac{p(y \mid \mathcal{M}_0)}{p(y \mid \mathcal{M}_1)}.
$$

The key idea in the proof is that we can use a "change of variables" technique to express $\text{BF}_{01}$ entirely in terms of the "encompassing" model $\mathcal{M}_1$. This proceeds by first unpacking the [marginal likelihood](/D/ml) for $\mathcal{M}_0$ over the nuisance parameter $\varphi$ and then using the fact that $\mathcal{M}_0$ is a sharp hypothesis nested within $\mathcal{M}_1$ to rewrite everything in terms of $\mathcal{H}_1$. Specifically,

$$
\begin{aligned}
 p(y \mid \mathcal{M}_0) &= \int p(y \mid \varphi,\mathcal{M}_0)p(\varphi\mid \mathcal{M}_0)d\varphi\\
  &= \int p(y \mid \varphi,\delta=\delta_0,\mathcal{M}_1)p(\varphi\mid \delta=\delta_0,\mathcal{M}_1)d\varphi\\
  &= p(y \mid \delta=\delta_0,\mathcal{M}_1).\\
\end{aligned}
$$

By [Bayes Theorem](/P/bayes-th), we can rewrite this last line as

$$
p(y \mid \delta=\delta_0,\mathcal{M}_1) = \frac{p(\delta=\delta_0\mid y,\mathcal{M}_1)p(y \mid \mathcal{M}_1)}{p(\delta=\delta_0\mid \mathcal{M}_1)}.
$$

Thus we have

$$ 
\begin{aligned}
  \text{BF}_{01} &= \frac{p(y \mid \mathcal{M}_0)}{p(y \mid \mathcal{M}_1)}\\
  &= p(y \mid \mathcal{M}_0) \cdot \frac{1}{p(y \mid \mathcal{M}_1)}\\
  &= p(y \mid \delta=\delta_0,\mathcal{M}_1) \cdot \frac{1}{p(y \mid \mathcal{M}_1)}\\
  &= \frac{p(\delta=\delta_0\mid y,\mathcal{M}_1)p(y \mid \mathcal{M}_1)}{p(\delta=\delta_0\mid \mathcal{M}_1)} \cdot \frac{1}{p(y \mid \mathcal{M}_1)}\\
  &=\frac{p(\delta=\delta_0 \mid y,\mathcal{M}_1)}{p(\delta=\delta_0\mid \mathcal{M}_1)},
\end{aligned}
$$

which completes the proof of \eqref{eq:sd}.