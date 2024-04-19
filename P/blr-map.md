---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2024-04-19 14:45:38

title: "Maximum-a-posteriori estimation for Bayesian linear regression"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Bayesian linear regression"
theorem: "Maximum-a-posteriori estimation"

sources:

proof_id: "P448"
shortcut: "blr-map"
username: "JoramSoch"
---


**Theorem:** Let there be a [linear regression model](/D/mlr)

$$ \label{eq:GLM}
y = X\beta + \varepsilon, \; \varepsilon \sim \mathcal{N}(0, \sigma^2 V), \; \sigma^2 V = (\tau P)^{-1}
$$

and assume a [normal-gamma prior distribution](/P/blr-prior) over the model parameters $\beta$ and $\tau = 1/\sigma^2$

$$ \label{eq:GLM-NG-prior}
p(\beta,\tau) = \mathcal{N}(\beta; \mu_0, (\tau \Lambda_0)^{-1}) \cdot \mathrm{Gam}(\tau; a_0, b_0) \; .
$$

Then, the [maximum-a-posteriori estimates](/D/map) of $\beta$ and $\tau$ are

$$ \label{eq:GLN-NG-MAP}
\begin{split}
\hat{\beta}_\mathrm{MAP} &= (X^\mathrm{T} P X + \Lambda_0)^{-1} (X^\mathrm{T} P y + \Lambda_0 \mu_0) \\
\hat{\tau}_\mathrm{MAP} &= \left( 2 a_0 + n - 2 \right) \left( 2 b_0 + (y - X \hat{\beta}_\mathrm{MAP})^\mathrm{T} P (y - X \hat{\beta}_\mathrm{MAP}) + (\hat{\beta}_\mathrm{MAP} - \mu_0)^\mathrm{T} \Lambda_0 (\hat{\beta}_\mathrm{MAP} - \mu_0) \right)^{-1}
\end{split}
$$

where $n$ is the [number of data points](/D/mlr).


**Proof:** Given the [prior distribution](/D/prior) in \eqref{eq:GLM-NG-prior}, the [posterior distribution](/D/post) for [multiple linear regression](/D/mlr) [is also a normal-gamma distribution](/P/blr-post)

$$ \label{eq:GLM-NG-post}
p(\beta,\tau|y) = \mathcal{N}(\beta; \mu_n, (\tau \Lambda_n)^{-1}) \cdot \mathrm{Gam}(\tau; a_n, b_n)
$$

where the [posterior hyperparameters](/D/post) are equal to

$$ \label{eq:GLM-NG-post-par}
\begin{split}
\mu_n &= \Lambda_n^{-1} (X^\mathrm{T} P y + \Lambda_0 \mu_0) \\
\Lambda_n &= X^\mathrm{T} P X + \Lambda_0 \\
a_n &= a_0 + \frac{n}{2} \\
b_n &= b_0 + \frac{1}{2} (y^\mathrm{T} P y + \mu_0^\mathrm{T} \Lambda_0 \mu_0 - \mu_n^\mathrm{T} \Lambda_n \mu_n) \; .
\end{split}
$$

From this, the conditional posterior distribution over $\beta$ [follows as](/D/ng)

$$ \label{eq:GLM-NG-post-beta}
p(\beta|\tau,y) = \mathcal{N}(\beta; \mu_n, (\tau \Lambda_n)^{-1})
$$

and the marginal posterior distribution over $\tau$ [follows as](/D/ng)

$$ \label{eq:GLM-NG-post-tau}
p(\tau|y) = \mathrm{Gam}(\tau; a_n, b_n) \; .
$$

The [mode of the multivariate normal distribution](/P/mvn-mode) is given by

$$ \label{eq:mvn-mode}
X \sim \mathcal{N}(\mu, \Sigma) \quad \Rightarrow \quad \mathrm{mode}(X) = \mu
$$

and the [mode of the gamma distribution](/P/gam-mode) is given by

$$ \label{eq:gam-mode}
X \sim \mathrm{Gam}(a, b) \quad \Rightarrow \quad \mathrm{mode}(X) = \frac{a-1}{b} \; .
$$

Applying \eqref{eq:mvn-mode} to \eqref{eq:GLM-NG-post-beta}, the [maximum-a-posteriori estimate](/D/map) of $\beta$ follows as

$$ \label{eq:GLN-NG-MAP-beta}
\begin{split}
\hat{\beta}_\mathrm{MAP} &= \mu_n \\
&= \Lambda_n^{-1} (X^\mathrm{T} P y + \Lambda_0 \mu_0) \\
&= (X^\mathrm{T} P X + \Lambda_0)^{-1} (X^\mathrm{T} P y + \Lambda_0 \mu_0)
\end{split}
$$

and applying \eqref{eq:gam-mode} to \eqref{eq:GLM-NG-post-tau}, the [maximum-a-posteriori estimate](/D/map) of $\tau$ follows as

$$ \label{eq:GLN-NG-MAP-tau}
\begin{split}
\hat{\tau}_\mathrm{MAP} &= \frac{a_n-1}{b_n} \\
&= \left( a_0 + \frac{n}{2} - 1 \right) \left( b_0 + \frac{1}{2} (y^\mathrm{T} P y + \mu_0^\mathrm{T} \Lambda_0 \mu_0 - \mu_n^\mathrm{T} \Lambda_n \mu_n) \right)^{-1} \\
&= \left( 2 a_0 + n - 2 \right) \left( 2 b_0 + y^\mathrm{T} P y + \mu_0^\mathrm{T} \Lambda_0 \mu_0 - \mu_n^\mathrm{T} \Lambda_n \mu_n \right)^{-1} \\
&= \left( 2 a_0 + n - 2 \right) \left( 2 b_0 + y^\mathrm{T} P y + \mu_0^\mathrm{T} \Lambda_0 \mu_0 - \hat{\beta}_\mathrm{MAP}^\mathrm{T} \left( X^\mathrm{T} P X + \Lambda_0 \right) \hat{\beta}_\mathrm{MAP} \right)^{-1} \\
&= \left( 2 a_0 + n - 2 \right) \left( 2 b_0 + y^\mathrm{T} P y + \mu_0^\mathrm{T} \Lambda_0 \mu_0 - \hat{\beta}_\mathrm{MAP}^\mathrm{T} X^\mathrm{T} P X \hat{\beta}_\mathrm{MAP} - \hat{\beta}_\mathrm{MAP}^\mathrm{T} \Lambda_0 \hat{\beta}_\mathrm{MAP} \right)^{-1} \\
&= \left( 2 a_0 + n - 2 \right) \left( 2 b_0 + (y - X \hat{\beta}_\mathrm{MAP})^\mathrm{T} P (y - X \hat{\beta}_\mathrm{MAP}) + (\hat{\beta}_\mathrm{MAP} - \mu_0)^\mathrm{T} \Lambda_0 (\hat{\beta}_\mathrm{MAP} - \mu_0) \right)^{-1} \; .
\end{split}
$$