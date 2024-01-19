---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2024-01-19 08:51:30

title: "Posterior distribution for Bayesian linear regression with known covariance"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Bayesian linear regression with known covariance"
theorem: "Posterior distribution"

sources:
  - authors: "Bishop CM"
    year: 2006
    title: "Bayesian linear regression"
    in: "Pattern Recognition for Machine Learning"
    pages: "pp. 152-161, eqs. 3.49-3.51, ex. 3.7"
    url: "https://www.springer.com/gp/book/9780387310732"
  - authors: "Penny WD"
    year: 2012
    title: "Comparing Dynamic Causal Models using AIC, BIC and Free Energy"
    in: "NeuroImage"
    pages: "vol. 59, iss. 2, pp. 319-330, eq. 27"
    url: "https://www.sciencedirect.com/science/article/pii/S1053811911008160"
    doi: "10.1016/j.neuroimage.2011.07.039"

proof_id: "P433"
shortcut: "blrkc-post"
username: "JoramSoch"
---


**Theorem:** Let

$$ \label{eq:GLM}
y = X \beta + \varepsilon, \; \varepsilon \sim \mathcal{N}(0, \Sigma)
$$

be a [linear regression model](/D/mlr) with measured $n \times 1$ data vector $y$, known $n \times p$ design matrix $X$ and known $n \times n$ covariance matrix $\Sigma$ as well as unknown $p \times 1$ regression coefficients $\beta$. Moreover, assume a [multivariate normal distribution](/P/blrkc-prior) over the model parameter $\beta$:

$$ \label{eq:GLM-N-prior}
p(\beta) = \mathcal{N}(\beta; \mu_0, \Sigma_0) \; .
$$

Then, the [posterior distribution](/D/post) is also a [multivariate normal distribution](/D/mvn)

$$ \label{eq:GLM-N-post}
p(\beta|y) = \mathcal{N}(\beta; \mu_n, \Sigma_n)
$$

and the [posterior hyperparameters](/D/post) are given by

$$ \label{eq:GLM-N-post-par}
\begin{split}
\mu_n &= \Sigma_n (X^\mathrm{T} \Sigma^{-1} y + \Sigma_0^{-1} \mu_0) \\
\Sigma_n &= \left( X^\mathrm{T} \Sigma^{-1} X + \Sigma_0^{-1} \right)^{-1} \; .
\end{split}
$$


**Proof:** According to [Bayes' theorem](/P/bayes-th), the [posterior distribution](/D/post) is given by

$$ \label{eq:GLM-N-BT}
p(\beta|y) = \frac{p(y|\beta) \, p(\beta)}{p(y)} \; .
$$

Since $p(y)$ is just a normalization factor, the [posterior is proportional](/P/post-jl) to the numerator:

$$ \label{eq:GLM-N-post-JL}
p(\beta|y) \propto p(y|\beta) \, p(\beta) = p(y,\beta) \; .
$$

Equation \eqref{eq:GLM} implies the following [likelihood function](/D/lf):

$$ \label{eq:GLM-LF}
p(y|\beta) = \mathcal{N}(y; X \beta, \Sigma) = \sqrt{\frac{1}{(2 \pi)^n |\Sigma|}} \, \exp\left[ -\frac{1}{2} (y-X\beta)^\mathrm{T} \Sigma^{-1} (y-X\beta) \right] \; .
$$

Combining the [likelihood function](/D/lf) \eqref{eq:GLM-LF} with the [prior distribution](/D/prior) \eqref{eq:GLM-N-prior} using the [probability density function of the multivariate normal distribution](/P/mvn-pdf), the [joint likelihood](/D/jl) of the model is given by

$$ \label{eq:GLM-N-JL-s1}
\begin{split}
p(y,\beta) = \; & p(y|\beta) \, p(\beta) \\
= \; & \sqrt{\frac{1}{(2 \pi)^n |\Sigma|}} \, \exp\left[ -\frac{1}{2} (y-X\beta)^\mathrm{T} \Sigma^{-1} (y-X\beta) \right] \cdot \\
\; & \sqrt{\frac{1}{(2 \pi)^p |\Sigma_0|}} \, \exp\left[ -\frac{1}{2} (\beta-\mu_0)^\mathrm{T} \Sigma_0^{-1} (\beta-\mu_0) \right] \; .
\end{split}
$$

Collecting identical variables gives:

$$ \label{eq:GLM-N-JL-s2}
\begin{split}
p(y,\beta) = \; & \sqrt{\frac{1}{(2 \pi)^{n+p} |\Sigma| |\Sigma_0|}} \cdot \\
& \exp\left[ -\frac{1}{2} \left( (y-X\beta)^\mathrm{T} \Sigma^{-1} (y-X\beta) + (\beta-\mu_0)^\mathrm{T} \Sigma_0^{-1} (\beta-\mu_0) \right) \right] \; .
\end{split}
$$

Expanding the products in the exponent gives:

$$ \label{eq:GLM-N-JL-s3}
\begin{split}
p(y,\beta) = \; & \sqrt{\frac{1}{(2 \pi)^{n+p} |\Sigma| |\Sigma_0|}} \cdot \\
& \exp\left[ -\frac{1}{2} \left( y^\mathrm{T} \Sigma^{-1} y - y^\mathrm{T} \Sigma^{-1} X \beta - \beta^\mathrm{T} X^\mathrm{T} \Sigma^{-1} y + \beta^\mathrm{T} X^\mathrm{T} \Sigma^{-1} X \beta + \right. \right. \\
& \hphantom{\exp \left[ -\frac{1}{2} \right.} \; \left. \left. \beta^\mathrm{T} \Sigma_0^{-1} \beta - \beta^\mathrm{T} \Sigma_0^{-1} \mu_0 - \mu_0^\mathrm{T} \Sigma_0^{-1} \beta + \mu_0^\mathrm{T} \Sigma_0^{-1} \mu_0 \right) \right] \; .
\end{split}
$$

Regrouping the terms in the exponent gives:

$$ \label{eq:GLM-N-JL-s4}
\begin{split}
p(y,\beta) = \; & \sqrt{\frac{1}{(2 \pi)^{n+p} |\Sigma| |\Sigma_0|}} \cdot \\
& \exp\left[ -\frac{1}{2} \left( \beta^\mathrm{T} [ X^\mathrm{T} \Sigma^{-1} X + \Sigma_0^{-1} ] \beta - 2 \beta^\mathrm{T} [X^\mathrm{T} \Sigma^{-1} y + \Sigma_0^{-1} \mu_0] + \right. \right. \\
& \hphantom{\exp \left[ -\frac{1}{2} \right.} \; \left. \left. y^\mathrm{T} \Sigma^{-1} y + \mu_0^\mathrm{T} \Sigma_0^{-1} \mu_0 \right) \right] \; .
\end{split}
$$

Completing the square over $\beta$, we finally have

$$ \label{eq:GLM-N-JL-s5}
\begin{split}
p(y,\beta) = \; & \sqrt{\frac{1}{(2 \pi)^{n+p} |\Sigma| |\Sigma_0|}} \cdot \\
& \exp\left[ -\frac{1}{2} \left( (\beta-\mu_n)^\mathrm{T} \Sigma_n^{-1} (\beta-\mu_n) + (y^\mathrm{T} \Sigma^{-1} y + \mu_0^\mathrm{T} \Sigma_0^{-1} \mu_0 - \mu_n^\mathrm{T} \Sigma_n^{-1} \mu_n) \right) \right]
\end{split}
$$

with the [posterior hyperparameters](/D/post)

$$ \label{eq:GLM-N-post-par-qed}
\begin{split}
\mu_n &= \Sigma_n (X^\mathrm{T} \Sigma^{-1} y + \Sigma_0^{-1} \mu_0) \\
\Sigma_n &= \left( X^\mathrm{T} \Sigma^{-1} X + \Sigma_0^{-1} \right)^{-1} \; .
\end{split}
$$

Ergo, the joint likelihood is proportional to

$$ \label{eq:GLM-N-JL-s6}
p(y,\beta) \propto \exp\left[ -\frac{1}{2} (\beta-\mu_n)^\mathrm{T} \Sigma_n^{-1} (\beta-\mu_n) \right] \; ,
$$

such that the posterior distribution over $\beta$ is given by

$$ \label{eq:GLM-N-post-qed}
p(\beta|y) = \mathcal{N}(\beta; \mu_n, \Sigma_n)
$$

with the posterior hyperparameters given in \eqref{eq:GLM-N-post-par-qed}.