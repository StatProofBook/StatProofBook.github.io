---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2024-04-05 16:07:25

title: "Expression of the noise precision posterior for Bayesian linear regression using prediction and parameter errors"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Bayesian linear regression"
theorem: "Expression of posterior parameters using error terms"

sources:

proof_id: "P446"
shortcut: "blr-posterr"
username: "JoramSoch"
---


**Theorem:** Let there be a [linear regression model](/D/mlr)

$$ \label{eq:GLM}
y = X\beta + \varepsilon, \; \varepsilon \sim \mathcal{N}(0, \sigma^2 V), \; \sigma^2 V = (\tau P)^{-1} \; ,
$$

assume a [normal-gamma prior distribution](/P/blr-prior) over the model parameters $\beta$ and $\tau = 1/\sigma^2$

$$ \label{eq:GLM-NG-prior}
p(\beta,\tau) = \mathcal{N}(\beta; \mu_0, (\tau \Lambda_0)^{-1}) \cdot \mathrm{Gam}(\tau; a_0, b_0)
$$

and consider the [Bayesian posterior distribution](/P/blr-post) over these model parameters:

$$ \label{eq:GLM-NG-post}
p(\beta,\tau|y) = \mathcal{N}(\beta; \mu_n, (\tau \Lambda_n)^{-1}) \cdot \mathrm{Gam}(\tau; a_n, b_n) \; .
$$

Then, the [posterior hyperparameters](/D/post) for the [noise precision](/P/blr-prior) $\tau$ can be expressed as

$$ \label{eq:GLM-NG-post-tau}
\begin{split}
a_n &= a_0 + \frac{n}{2} \\
b_n &= b_0 + \frac{1}{2} \left( \varepsilon_y^\mathrm{T} P \varepsilon_y +  \varepsilon_\beta^\mathrm{T} \Lambda_0 \varepsilon_\beta \right)
\end{split}
$$

where $\varepsilon_y$ and $\varepsilon_\beta$ are the "prediction errors" and "parameter errors"

$$ \label{eq:GLM-NG-post-tau-err}
\begin{split}
\varepsilon_y &= y - \hat{y} \\
\varepsilon_\beta &= \mu_n - \mu_0
\end{split}
$$

where $\hat{y}$ is the [predicted signal](/D/pmat) at the [posterior mean](/P/blr-post) [regression coefficients](/D/mlr) $\mu_n$:

$$ \label{eq:GLM-NG-post-y-hat}
\hat{y} = X \mu_n \; .
$$


**Proof:** The [posterior hyperparameter for Bayesian linear regression](/P/blr-post) are:

$$ \label{eq:GLM-NG-post-par}
\begin{split}
\mu_n &= \Lambda_n^{-1} (X^\mathrm{T} P y + \Lambda_0 \mu_0) \\
\Lambda_n &= X^\mathrm{T} P X + \Lambda_0 \\
a_n &= a_0 + \frac{n}{2} \\
b_n &= b_0 + \frac{1}{2} (y^\mathrm{T} P y + \mu_0^\mathrm{T} \Lambda_0 \mu_0 - \mu_n^\mathrm{T} \Lambda_n \mu_n) \; .
\end{split}
$$

The [shape parameter](/D/gam) $a_n$ is given by this equation. The [rate parameter](/D/gam) $b_n$ of the [posterior distribution](/D/post) can be developped as follows:

$$ \label{eq:GLM-NG-post-tau-qed}
\begin{split}
b_n &\overset{\eqref{eq:GLM-NG-post-par}}{=} b_0 + \frac{1}{2} \left( y^\mathrm{T} P y + \mu_0^\mathrm{T} \Lambda_0 \mu_0 - \mu_n^\mathrm{T} \Lambda_n \mu_n \right) \\
&\overset{\eqref{eq:GLM-NG-post-par}}{=} b_0 + \frac{1}{2} \left( y^\mathrm{T} P y + \mu_0^\mathrm{T} \Lambda_0 \mu_0 - \mu_n^\mathrm{T} (X^\mathrm{T} P X + \Lambda_0) \mu_n \right) \\
&= b_0 + \frac{1}{2} \left( y^\mathrm{T} P y + \mu_0^\mathrm{T} \Lambda_0 \mu_0 - \mu_n^\mathrm{T} X^\mathrm{T} P X \mu_n - \mu_n^\mathrm{T} \Lambda_0 \mu_n \right) \\
&= b_0 + \frac{1}{2} \left( (y^\mathrm{T} P y - \mu_n^\mathrm{T} X^\mathrm{T} P X \mu_n) + (\mu_0^\mathrm{T} \Lambda_0 \mu_0 - \mu_n^\mathrm{T} \Lambda_0 \mu_n) \right) \\
&= b_0 + \frac{1}{2} \left( (y - X \mu_n)^\mathrm{T} P (y - X \mu_n) + (\mu_0 - \mu_n)^\mathrm{T} \Lambda_0 (\mu_0 - \mu_n) \right) \\
&\overset{\eqref{eq:GLM-NG-post-y-hat}}{=} b_0 + \frac{1}{2} \left( (y - \hat{y})^\mathrm{T} P (y - \hat{y}) + (\mu_n - \mu_0)^\mathrm{T} \Lambda_0 (\mu_n - \mu_0) \right) \\
&\overset{\eqref{eq:GLM-NG-post-tau-err}}{=} b_0 + \frac{1}{2} \left( \varepsilon_y^\mathrm{T} P \varepsilon_y +  \varepsilon_\beta^\mathrm{T} \Lambda_0 \varepsilon_\beta \right) \; .
\end{split}
$$

Together with equation (\ref{eq:GLM-NG-post-par}c), this completes the proof.