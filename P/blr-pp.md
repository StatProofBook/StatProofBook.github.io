---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-07-17 17:03:00

title: "Posterior probability of the alternative hypothesis for Bayesian linear regression"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Bayesian linear regression"
theorem: "Posterior probability of alternative hypothesis"

sources:
  - authors: "Koch, Karl-Rudolf"
    year: 2007
    title: "Multivariate t-distribution"
    in: "Introduction to Bayesian Statistics"
    pages: "Springer, Berlin/Heidelberg, 2007, eqs. 2.235, 2.236, 2.213, 2.210, 2.188"
    url: "https://www.springer.com/de/book/9783540727231"
    doi: "10.1007/978-3-540-72726-2"

proof_id: "P133"
shortcut: "blr-pp"
username: "JoramSoch"
---


**Theorem:** Let there be a [linear regression model](/D/mlr) with [normally distributed](/D/mvn) errors:

$$ \label{eq:GLM}
y = X \beta + \varepsilon, \; \varepsilon \sim \mathcal{N}(0, \sigma^2 V)
$$

and assume a [normal-gamma](/D/ng) [prior distribution](/D/prior) over the model parameters $\beta$ and $\tau = 1/\sigma^2$:

$$ \label{eq:GLM-NG-prior}
p(\beta,\tau) = \mathcal{N}(\beta; \mu_0, (\tau \Lambda_0)^{-1}) \cdot \mathrm{Gam}(\tau; a_0, b_0) \; .
$$

Then, the [posterior](/D/post) [probability](/D/prob) of the [alternative hypothesis](/D/h1)

$$ \label{eq:GLM-H1}
\mathrm{H}_1: \, c^\mathrm{T} \beta > 0
$$

is given by

$$ \label{eq:GLM-NG-PP}
\mathrm{Pr}\left( \mathrm{H}_1 | y \right) = 1 - \mathrm{T}\left( -\frac{c^\mathrm{T} \mu}{\sqrt{c^\mathrm{T} \Sigma c}}; \nu \right)
$$

where $c$ is a $p \times 1$ [contrast vector](/D/con), $\mathrm{T}(x; \nu)$ is the [cumulative distribution function](/D/cdf) of the [t-distribution](/D/t) with $\nu$ [degrees of freedom](/D/dof) and $\mu$, $\Sigma$ and $\nu$ can be obtained from the [posterior hyperparameters](/D/post) of Bayesian linear regression.


**Proof:** The [posterior distribution for Bayesian linear regression](/P/blr-post) is given by a [normal-gamma distribution](/D/ng) over $\beta$ and $\tau = 1/\sigma^2$

$$ \label{eq:GLM-NG-post}
p(\beta,\tau|y) = \mathcal{N}(\beta; \mu_n, (\tau \Lambda_n)^{-1}) \cdot \mathrm{Gam}(\tau; a_n, b_n)
$$

with the [posterior hyperparameters](/D/post)

$$ \label{eq:GLM-NG-post-par}
\begin{split}
\mu_n &= \Lambda_n^{-1} (X^\mathrm{T} P y + \Lambda_0 \mu_0) \\
\Lambda_n &= X^\mathrm{T} P X + \Lambda_0 \\
a_n &= a_0 + \frac{n}{2} \\
b_n &= b_0 + \frac{1}{2} (y^\mathrm{T} P y + \mu_0^\mathrm{T} \Lambda_0 \mu_0 - \mu_n^\mathrm{T} \Lambda_n \mu_n) \; .
\end{split}
$$

The [marginal distribution of a normal-gamma distribution is a multivariate t-distribution](/P/ng-marg), such that the [marginal](/D/dist-marg) [posterior](/D/post) distribution of $\beta$ is

$$ \label{eq:GLM-NG-post-beta}
p(\beta|y) = t(\beta; \mu, \Sigma, \nu)
$$

with the [posterior hyperparameters](/D/post)

$$ \label{eq:GLM-NG-post-par-beta}
\begin{split}
\mu &= \mu_n \\
\Sigma &= \left( \frac{a_n}{b_n} \Lambda_n \right)^{-1} \\
\nu &= 2 \, a_n \; .
\end{split}
$$

Define the quantity $\gamma = c^\mathrm{T} \beta$. According to the [linear transformation theorem for the multivariate t-distribution](/P/mvt-ltt), $\gamma$ also follows a [multivariate t-distribution](/D/mvt):

$$ \label{eq:GLM-NG-post-gamma}
p(\gamma|y) = t(\gamma; c^\mathrm{T} \mu, c^\mathrm{T} \Sigma \, c, \nu) \; .
$$

Because $c^\mathrm{T}$ is a $1 \times p$ vector, $\gamma$ is a scalar and actually has a [non-standardized t-distribution](/D/nst). Therefore, the posterior probability of $H_1$ can be calculated using a one-dimensional integral:

$$ \label{eq:GLM-NG-post-prob-H0-s1}
\begin{split}
\mathrm{Pr}\left( \mathrm{H}_1 | y \right) &= p(\gamma > 0|y) \\
&= \int_{0}^{+\infty} p(\gamma|y) \, \mathrm{d}\gamma \\
&= 1 - \int_{-\infty}^{0} p(\gamma|y) \, \mathrm{d}\gamma \\
&= 1 - \mathrm{T}_\mathrm{nst}(0; c^\mathrm{T} \mu, c^\mathrm{T} \Sigma \, c, \nu) \; .
\end{split}
$$

Using [the relation between non-standardized t-distribution and standard t-distribution](/P/nst-t), we can finally write:

$$ \label{eq:GLM-NG-post-prob-H0-s2}
\begin{split}
\mathrm{Pr}\left( \mathrm{H}_1 | y \right) &= 1 - \mathrm{T}\left( \frac{(0 - c^\mathrm{T} \mu)}{\sqrt{c^\mathrm{T} \Sigma c}}; \nu \right) \\
&= 1 - \mathrm{T}\left( -\frac{c^\mathrm{T} \mu}{\sqrt{c^\mathrm{T} \Sigma c}}; \nu \right) \; .
\end{split}
$$