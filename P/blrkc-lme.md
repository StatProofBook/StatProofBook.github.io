---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2024-01-19 08:54:19

title: "Log model evidence for Bayesian linear regression with known covariance"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Bayesian linear regression with known covariance"
theorem: "Log model evidence"

sources:
  - authors: "Penny WD"
    year: 2012
    title: "Comparing Dynamic Causal Models using AIC, BIC and Free Energy"
    in: "NeuroImage"
    pages: "vol. 59, iss. 2, pp. 319-330, eqs. 19-23"
    url: "https://www.sciencedirect.com/science/article/pii/S1053811911008160"
    doi: "10.1016/j.neuroimage.2011.07.039"
  - authors: "Bishop CM"
    year: 2006
    title: "Bayesian Linear Regression"
    in: "Pattern Recognition for Machine Learning"
    pages: "pp. 152-161"
    url: "https://www.springer.com/gp/book/9780387310732"

proof_id: "P434"
shortcut: "blrkc-lme"
username: "JoramSoch"
---


**Theorem:** Let

$$ \label{eq:GLM}
m: y = X \beta + \varepsilon, \; \varepsilon \sim \mathcal{N}(0, \Sigma)
$$

be a [linear regression model](/D/mlr) with measured $n \times 1$ data vector $y$, known $n \times p$ design matrix $X$ and known $n \times n$ covariance matrix $\Sigma$ as well as unknown $p \times 1$ regression coefficients $\beta$. Moreover, assume a [multivariate normal distribution](/P/blrkc-prior) over the model parameter $\beta$:

$$ \label{eq:GLM-N-prior}
p(\beta) = \mathcal{N}(\beta; \mu_0, \Sigma_0) \; .
$$

Then, the [log model evidence](/D/lme) for this model is

$$ \label{eq:GLM-N-LME}
\begin{split}
\log p(y|m) = &- \frac{1}{2} e_y^\mathrm{T} \Sigma^{-1} e_y - \frac{1}{2} \log |\Sigma| - \frac{n}{2} \log (2 \pi) \\
&- \frac{1}{2} e_\beta^\mathrm{T} \Sigma_0^{-1} e_\beta - \frac{1}{2} \log |\Sigma_0| + \frac{1}{2} \log |\Sigma_n| \; .
\end{split}
$$

with the "prediction error" and "parameter error" terms

$$ \label{eq:GLM-N-err}
\begin{split}
e_y &= y - X \mu_n \\
e_\beta &= \mu_0 - \mu_n
\end{split}
$$

where the [posterior hyperparameters](/D/post) are given by

$$ \label{eq:GLM-N-post-par}
\begin{split}
\mu_n &= \Sigma_n (X^\mathrm{T} \Sigma^{-1} y + \Sigma_0^{-1} \mu_0) \\
\Sigma_n &= \left( X^\mathrm{T} \Sigma^{-1} X + \Sigma_0^{-1} \right)^{-1} \; .
\end{split}
$$


**Proof:** According to the [law of marginal probability](/D/prob-marg), the [model evidence](/D/ml) for this model is:

$$ \label{eq:GLM-N-ME-s1}
p(y|m) = \int p(y|\beta) \, p(\beta) \, \mathrm{d}\beta \; .
$$

According to the [law of conditional probability](/D/prob-cond), the integrand is equivalent to the [joint likelihood](/D/jl):

$$ \label{eq:GLM-N-ME-s2}
p(y|m) = \int p(y,\beta) \, \mathrm{d}\beta \; .
$$

Equation \eqref{eq:GLM} implies the following [likelihood function](/D/lf):

$$ \label{eq:GLM-LF}
p(y|\beta) = \mathcal{N}(y; X \beta, \Sigma) = \sqrt{\frac{1}{(2 \pi)^n |\Sigma|}} \, \exp\left[ -\frac{1}{2} (y-X\beta)^\mathrm{T} \Sigma^{-1} (y-X\beta) \right] \; .
$$

When [deriving the posterior distribution](/P/blrkc-post) $p(\beta \vert y)$, the joint likelihood $p(y,\beta)$ is obtained as

$$ \label{eq:GLM-N-LME-s1}
\begin{split}
p(y,\beta) = \; & \sqrt{\frac{1}{(2 \pi)^{n+p} |\Sigma| |\Sigma_0|}} \cdot \\
& \exp\left[ -\frac{1}{2} \left( (\beta-\mu_n)^\mathrm{T} \Sigma_n^{-1} (\beta-\mu_n) + (y^\mathrm{T} \Sigma^{-1} y + \mu_0^\mathrm{T} \Sigma_0^{-1} \mu_0 - \mu_n^\mathrm{T} \Sigma_n^{-1} \mu_n) \right) \right] \; .
\end{split}
$$

Using the [probability density function of the multivariate normal distribution](/P/mvn-pdf), we can rewrite this as

$$ \label{eq:GLM-N-LME-s2}
\begin{split}
p(y,\beta) = \; & \sqrt{\frac{1}{(2 \pi)^n |\Sigma|}} \, \sqrt{\frac{1}{(2 \pi)^p |\Sigma_0|}} \, \sqrt{\frac{(2 \pi)^p |\Sigma_n|}{1}} \cdot \mathcal{N}(\beta; \mu_n, \Sigma_n) \cdot \\
& \exp\left[ -\frac{1}{2} \left( y^\mathrm{T} \Sigma^{-1} y + \mu_0^\mathrm{T} \Sigma_0^{-1} \mu_0 - \mu_n^\mathrm{T} \Sigma_n^{-1} \mu_n \right) \right] \; .
\end{split}
$$

With that, $\beta$ can be integrated out easily:

$$ \label{eq:GLM-N-LME-s3}
\int p(y,\beta) \, \mathrm{d}\beta = \sqrt{\frac{1}{(2 \pi)^n |\Sigma|}} \, \sqrt{\frac{|\Sigma_n|}{|\Sigma_0|}} \cdot \exp\left[ -\frac{1}{2} \left( y^\mathrm{T} \Sigma^{-1} y + \mu_0^\mathrm{T} \Sigma_0^{-1} \mu_0 - \mu_n^\mathrm{T} \Sigma_n^{-1} \mu_n \right) \right] \; .
$$

Now we turn to the intra-exponent term

$$ \label{eq:GLM-N-LME-s4a}
y^\mathrm{T} \Sigma^{-1} y + \mu_0^\mathrm{T} \Sigma_0^{-1} \mu_0 - \mu_n^\mathrm{T} \Sigma_n^{-1} \mu_n
$$

and plug in the posterior covariance

$$ \label{eq:GLM-N-post-par-Sigma}
\Sigma_n = \left( X^\mathrm{T} \Sigma^{-1} X + \Sigma_0^{-1} \right)^{-1} \; .
$$

This gives

$$ \label{eq:GLM-N-LME-s4b}
\begin{split}
& \; y^\mathrm{T} \Sigma^{-1} y + \mu_0^\mathrm{T} \Sigma_0^{-1} \mu_0 - \mu_n^\mathrm{T} \Sigma_n^{-1} \mu_n \\
= & \; y^\mathrm{T} \Sigma^{-1} y + \mu_0^\mathrm{T} \Sigma_0^{-1} \mu_0 - \mu_n^\mathrm{T} \left( X^\mathrm{T} \Sigma^{-1} X + \Sigma_0^{-1} \right) \mu_n \\
= & \; y^\mathrm{T} \Sigma^{-1} y + \mu_0^\mathrm{T} \Sigma_0^{-1} \mu_0 - \mu_n^\mathrm{T} X^\mathrm{T} \Sigma^{-1} X \mu_n - \mu_n^\mathrm{T} \Sigma_0^{-1} \mu_n \\
= & \; (y - X \mu_n)^\mathrm{T} \Sigma^{-1} (y - X \mu_n) + (\mu_0 - \mu_n)^\mathrm{T} \Sigma_0^{-1} (\mu_0 - \mu_n) \\
\overset{\eqref{eq:GLM-N-err}}{=} & \; e_y^\mathrm{T} \Sigma^{-1} e_y + e_\beta^\mathrm{T} \Sigma_0^{-1} e_\beta \; .
\end{split}
$$

Thus, the [marginal likelihood](/D/ml) becomes

$$ \label{eq:GLM-N-LME-s5}
p(y|m) = \int p(y,\beta) \, \mathrm{d}\beta \overset{\eqref{eq:GLM-N-LME-s3}}{=} \sqrt{\frac{1}{(2 \pi)^n |\Sigma|}} \, \sqrt{\frac{|\Sigma_n|}{|\Sigma_0|}} \cdot \exp\left[ -\frac{1}{2} \left( e_y^\mathrm{T} \Sigma^{-1} e_y + e_\beta^\mathrm{T} \Sigma_0^{-1} e_\beta \right) \right]
$$

and the [log model evidence](/D/lme) of this model is given by

$$ \label{eq:GLM-N-LME-s6}
\begin{split}
\log p(y|m) = &- \frac{1}{2} e_y^\mathrm{T} \Sigma^{-1} e_y - \frac{1}{2} \log |\Sigma| - \frac{n}{2} \log (2 \pi) \\
&- \frac{1}{2} e_\beta^\mathrm{T} \Sigma_0^{-1} e_\beta - \frac{1}{2} \log |\Sigma_0| + \frac{1}{2} \log |\Sigma_n| \; .
\end{split}
$$