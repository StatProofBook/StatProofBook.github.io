---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-01-03 17:53:00

title: "Posterior distribution for Bayesian linear regression"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Bayesian linear regression"
theorem: "Posterior distribution"

sources:
  - authors: "Bishop CM"
    year: 2006
    title: "Bayesian linear regression"
    in: "Pattern Recognition for Machine Learning"
    pages: "pp. 152-161, ex. 3.12, eq. 3.113"
    url: "https://www.springer.com/gp/book/9780387310732"

proof_id: "P10"
shortcut: "blr-post"
username: "JoramSoch"
---


**Theorem:** Let

$$ \label{eq:GLM}
y = X \beta + \varepsilon, \; \varepsilon \sim \mathcal{N}(0, \sigma^2 V)
$$

be a [linear regression model](/D/mlr) with measured $n \times 1$ data vector $y$, known $n \times p$ design matrix $X$, known $n \times n$ covariance structure $V$ as well as unknown $p \times 1$ regression coefficients $\beta$ and unknown noise variance $\sigma^2$. Moreover, assume a [normal-gamma prior distribution](/P/blr-prior) over the model parameters $\beta$ and $\tau = 1/\sigma^2$:

$$ \label{eq:GLM-NG-prior}
p(\beta,\tau) = \mathcal{N}(\beta; \mu_0, (\tau \Lambda_0)^{-1}) \cdot \mathrm{Gam}(\tau; a_0, b_0) \; .
$$

Then, the [posterior distribution](/D/post) is also a [normal-gamma distribution](/D/ng)

$$ \label{eq:GLM-NG-post}
p(\beta,\tau|y) = \mathcal{N}(\beta; \mu_n, (\tau \Lambda_n)^{-1}) \cdot \mathrm{Gam}(\tau; a_n, b_n)
$$

and the [posterior hyperparameters](/D/post) are given by

$$ \label{eq:GLM-NG-post-par}
\begin{split}
\mu_n &= \Lambda_n^{-1} (X^\mathrm{T} P y + \Lambda_0 \mu_0) \\
\Lambda_n &= X^\mathrm{T} P X + \Lambda_0 \\
a_n &= a_0 + \frac{n}{2} \\
b_n &= b_0 + \frac{1}{2} (y^\mathrm{T} P y + \mu_0^\mathrm{T} \Lambda_0 \mu_0 - \mu_n^\mathrm{T} \Lambda_n \mu_n) \; .
\end{split}
$$


**Proof:** According to [Bayes' theorem](/P/bayes-th), the [posterior distribution](/D/post) is given by

$$ \label{eq:GLM-NG-BT}
p(\beta,\tau|y) = \frac{p(y|\beta,\tau) \, p(\beta,\tau)}{p(y)} \; .
$$

Since $p(y)$ is just a normalization factor, the [posterior is proportional](/P/post-jl) to the numerator:

$$ \label{eq:GLM-NG-post-JL}
p(\beta,\tau|y) \propto p(y|\beta,\tau) \, p(\beta,\tau) = p(y,\beta,\tau) \; .
$$

Equation \eqref{eq:GLM} implies the following [likelihood function](/D/lf)

$$ \label{eq:GLM-LF-class}
p(y|\beta,\sigma^2) = \mathcal{N}(y; X \beta, \sigma^2 V) = \sqrt{\frac{1}{(2 \pi)^n |\sigma^2 V|}} \, \exp\left[ -\frac{1}{2 \sigma^2} (y-X\beta)^\mathrm{T} V^{-1} (y-X\beta) \right]
$$

which, for mathematical convenience, can also be parametrized as

$$ \label{eq:GLM-LF-Bayes}
p(y|\beta,\tau) = \mathcal{N}(y; X \beta, (\tau P)^{-1}) = \sqrt{\frac{|\tau P|}{(2 \pi)^n}} \, \exp\left[ -\frac{\tau}{2} (y-X\beta)^\mathrm{T} P (y-X\beta) \right]
$$

using the noise precision $\tau = 1/\sigma^2$ and the $n \times n$ [precision matrix](/D/precmat) $P = V^{-1}$.

<br>
Combining the [likelihood function](/D/lf) \eqref{eq:GLM-LF-Bayes} with the [prior distribution](/D/prior) \eqref{eq:GLM-NG-prior}, the [joint likelihood](/D/jl) of the model is given by

$$ \label{eq:GLM-NG-JL-s1}
\begin{split}
p(y,\beta,\tau) = \; & p(y|\beta,\tau) \, p(\beta,\tau) \\
= \; & \sqrt{\frac{|\tau P|}{(2 \pi)^n}} \, \exp\left[ -\frac{\tau}{2} (y-X\beta)^\mathrm{T} P (y-X\beta) \right] \cdot \\
& \sqrt{\frac{|\tau \Lambda_0|}{(2 \pi)^p}} \, \exp\left[ -\frac{\tau}{2} (\beta-\mu_0)^\mathrm{T} \Lambda_0 (\beta-\mu_0) \right] \cdot \\
& \frac{ {b_0}^{a_0}}{\Gamma(a_0)} \, \tau^{a_0-1} \exp[-b_0 \tau] \; .
\end{split}
$$

Collecting identical variables gives:

$$ \label{eq:GLM-NG-JL-s2}
\begin{split}
p(y,\beta,\tau) = \; & \sqrt{\frac{\tau^{n+p}}{(2 \pi)^{n+p}} |P| |\Lambda_0|} \, \frac{ {b_0}^{a_0}}{\Gamma(a_0)} \, \tau^{a_0-1} \exp[-b_0 \tau] \cdot \\
& \exp\left[ -\frac{\tau}{2} \left( (y-X\beta)^\mathrm{T} P (y-X\beta) + (\beta-\mu_0)^\mathrm{T} \Lambda_0 (\beta-\mu_0) \right) \right] \; .
\end{split}
$$

Expanding the products in the exponent gives:

$$ \label{eq:GLM-NG-JL-s3}
\begin{split}
p(y,\beta,\tau) = \; & \sqrt{\frac{\tau^{n+p}}{(2 \pi)^{n+p}} |P| |\Lambda_0|} \, \frac{ {b_0}^{a_0}}{\Gamma(a_0)} \, \tau^{a_0-1} \exp[-b_0 \tau] \cdot \\
& \exp\left[ -\frac{\tau}{2} \left( y^\mathrm{T} P y - y^\mathrm{T} P X \beta - \beta^\mathrm{T} X^\mathrm{T} P y + \beta^\mathrm{T} X^\mathrm{T} P X \beta + \right. \right. \\
& \hphantom{\exp \left[ -\frac{\tau}{2} \right.} \; \left. \left. \beta^\mathrm{T} \Lambda_0 \beta - \beta^\mathrm{T} \Lambda_0 \mu_0 - \mu_0^\mathrm{T} \Lambda_0 \beta + \mu_0^\mathrm{T} \Lambda_0 \mu_0 \right) \right] \; .
\end{split}
$$

Completing the square over $\beta$, we finally have

$$ \label{eq:GLM-NG-JL-s4}
\begin{split}
p(y,\beta,\tau) = \; & \sqrt{\frac{\tau^{n+p}}{(2 \pi)^{n+p}} |P| |\Lambda_0|} \, \frac{ {b_0}^{a_0}}{\Gamma(a_0)} \, \tau^{a_0-1} \exp[-b_0 \tau] \cdot \\
& \exp\left[ -\frac{\tau}{2} \left( (\beta-\mu_n)^\mathrm{T} \Lambda_n (\beta-\mu_n) + (y^\mathrm{T} P y + \mu_0^\mathrm{T} \Lambda_0 \mu_0 - \mu_n^\mathrm{T} \Lambda_n \mu_n) \right) \right]
\end{split}
$$

with the [posterior hyperparameters](/D/post)

$$ \label{eq:GLM-NG-post-beta-par}
\begin{split}
\mu_n &= \Lambda_n^{-1} (X^\mathrm{T} P y + \Lambda_0 \mu_0) \\
\Lambda_n &= X^\mathrm{T} P X + \Lambda_0 \; .
\end{split}
$$

Ergo, the joint likelihood is proportional to

$$ \label{eq:GLM-NG-JL-s5}
p(y,\beta,\tau) \propto \tau^{p/2} \cdot \exp\left[ -\frac{\tau}{2} (\beta-\mu_n)^\mathrm{T} \Lambda_n (\beta-\mu_n) \right] \cdot \tau^{a_n-1} \cdot \exp\left[ -b_n \tau \right]
$$

with the [posterior hyperparameters](/D/post)

$$ \label{eq:GLM-NG-post-tau-par}
\begin{split}
a_n &= a_0 + \frac{n}{2} \\
b_n &= b_0 + \frac{1}{2} (y^\mathrm{T} P y + \mu_0^\mathrm{T} \Lambda_0 \mu_0 - \mu_n^\mathrm{T} \Lambda_n \mu_n) \; .
\end{split}
$$

From the term in \eqref{eq:GLM-NG-JL-s5}, we can isolate the posterior distribution over $\beta$ given $\tau$:

$$ \label{eq:GLM-NG-post-beta}
p(\beta|\tau,y) = \mathcal{N}(\beta; \mu_n, (\tau \Lambda_n)^{-1}) \; .
$$

From the remaining term, we can isolate the posterior distribution over $\tau$:

$$ \label{eq:GLM-NG-post-tau}
p(\tau|y) = \mathrm{Gam}(\tau; a_n, b_n) \; .
$$

Together, \eqref{eq:GLM-NG-post-beta} and \eqref{eq:GLM-NG-post-tau} constitute the [joint](/D/prob-joint) [posterior distribution](/D/post) of $\beta$ and $\tau$.