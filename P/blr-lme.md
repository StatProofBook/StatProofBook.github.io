---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-01-03 22:05:00

title: "Log model evidence for Bayesian linear regression"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Bayesian linear regression"
theorem: "Log model evidence"

sources:
  - authors: "Bishop CM"
    year: 2006
    title: "Bayesian linear regression"
    in: "Pattern Recognition for Machine Learning"
    pages: "pp. 152-161, ex. 3.23, eq. 3.118"
    url: "https://www.springer.com/gp/book/9780387310732"

proof_id: "P11"
shortcut: "blr-lme"
username: "JoramSoch"
---


**Theorem:** Let

$$ \label{eq:GLM}
m: \; y = X \beta + \varepsilon, \; \varepsilon \sim \mathcal{N}(0, \sigma^2 V)
$$

be a [linear regression model](/D/mlr) with measured $n \times 1$ data vector $y$, known $n \times p$ design matrix $X$, known $n \times n$ covariance structure $V$ as well as unknown $p \times 1$ regression coefficients $\beta$ and unknown noise variance $\sigma^2$. Moreover, assume a [normal-gamma prior distribution](/P/blr-prior) over the model parameters $\beta$ and $\tau = 1/\sigma^2$:

$$ \label{eq:GLM-NG-prior}
p(\beta,\tau) = \mathcal{N}(\beta; \mu_0, (\tau \Lambda_0)^{-1}) \cdot \mathrm{Gam}(\tau; a_0, b_0) \; .
$$

Then, the [log model evidence](/D/lme) for this model is

$$ \label{eq:GLM-NG-LME}
\begin{split}
\log p(y|m) = \frac{1}{2} & \log |P| - \frac{n}{2} \log (2 \pi)  + \frac{1}{2} \log |\Lambda_0| - \frac{1}{2} \log |\Lambda_n| + \\
& \log \Gamma(a_n) - \log \Gamma(a_0) + a_0 \log b_0 - a_n \log b_n
\end{split}
$$

where the [posterior hyperparameters](/D/post) are given by

$$ \label{eq:GLM-NG-post-par}
\begin{split}
\mu_n &= \Lambda_n^{-1} (X^\mathrm{T} P y + \Lambda_0 \mu_0) \\
\Lambda_n &= X^\mathrm{T} P X + \Lambda_0 \\
a_n &= a_0 + \frac{n}{2} \\
b_n &= b_0 + \frac{1}{2} (y^\mathrm{T} P y + \mu_0^\mathrm{T} \Lambda_0 \mu_0 - \mu_n^\mathrm{T} \Lambda_n \mu_n) \; .
\end{split}
$$


**Proof:** According to the [law of marginal probability](/D/prob-marg), the [model evidence](/D/ml) for this model is:

$$ \label{eq:GLM-NG-ME-s1}
p(y|m) = \iint p(y|\beta,\tau) \, p(\beta,\tau) \, \mathrm{d}\beta \, \mathrm{d}\tau \; .
$$

According to the [law of conditional probability](/D/prob-cond), the integrand is equivalent to the [joint likelihood](/D/jl):

$$ \label{eq:GLM-NG-ME-s2}
p(y|m) = \iint p(y,\beta,\tau) \, \mathrm{d}\beta \, \mathrm{d}\tau \; .
$$

Equation \eqref{eq:GLM} implies the following [likelihood function](/D/lf)

$$ \label{eq:GLM-LF-class}
p(y|\beta,\sigma^2) = \mathcal{N}(y; X \beta, \sigma^2 V) = \sqrt{\frac{1}{(2 \pi)^n |\sigma^2 V|}} \, \exp\left[ -\frac{1}{2 \sigma^2} (y-X\beta)^\mathrm{T} V^{-1} (y-X\beta) \right]
$$

which, for mathematical convenience, can also be parametrized as

$$ \label{eq:GLM-LF-Bayes}
p(y|\beta,\tau) = \mathcal{N}(y; X \beta, (\tau P)^{-1}) = \sqrt{\frac{|\tau P|}{(2 \pi)^n}} \, \exp\left[ -\frac{\tau}{2} (y-X\beta)^\mathrm{T} P (y-X\beta) \right]
$$

using the noise precision $\tau = 1/\sigma^2$ and the $n \times n$ precision matrix $P = V^{-1}$.

<br>
When [deriving the posterior distribution](/P/blr-post) $p(\beta,\tau|y)$, the joint likelihood $p(y,\beta,\tau)$ is obtained as

$$ \label{eq:GLM-NG-LME-s1}
\begin{split}
p(y,\beta,\tau) = \; & \sqrt{\frac{\tau^n |P|}{(2 \pi)^n}} \, \sqrt{\frac{\tau^p |\Lambda_0|}{(2 \pi)^p}} \, \frac{ {b_0}^{a_0}}{\Gamma(a_0)} \, \tau^{a_0-1} \exp[-b_0 \tau] \cdot \\
& \exp\left[ -\frac{\tau}{2} \left( (\beta-\mu_n)^T \Lambda_n (\beta-\mu_n) + (y^T P y + \mu_0^T \Lambda_0 \mu_0 - \mu_n^T \Lambda_n \mu_n) \right) \right] \; .
\end{split}
$$

Using the [probability density function of the multivariate normal distribution](/P/mvn-pdf), we can rewrite this as

$$ \label{eq:GLM-NG-LME-s2}
\begin{split}
p(y,\beta,\tau) = \; & \sqrt{\frac{\tau^n |P|}{(2 \pi)^n}} \, \sqrt{\frac{\tau^p |\Lambda_0|}{(2 \pi)^p}} \, \sqrt{\frac{(2 \pi)^p}{\tau^p |\Lambda_n|}} \, \frac{ {b_0}^{a_0}}{\Gamma(a_0)} \, \tau^{a_0-1} \exp[-b_0 \tau] \cdot \\
& \mathcal{N}(\beta; \mu_n, (\tau \Lambda_n)^{-1}) \, \exp\left[ -\frac{\tau}{2} (y^T P y + \mu_0^T \Lambda_0 \mu_0 - \mu_n^T \Lambda_n \mu_n) \right] \; .
\end{split}
$$

Now, $\beta$ can be integrated out easily:

$$ \label{eq:GLM-NG-LME-s3}
\begin{split}
\int p(y,\beta,\tau) \, \mathrm{d}\beta = \; & \sqrt{\frac{\tau^n |P|}{(2 \pi)^n}} \, \sqrt{\frac{|\Lambda_0|}{|\Lambda_n|}} \, \frac{ {b_0}^{a_0}}{\Gamma(a_0)} \, \tau^{a_0-1} \exp[-b_0 \tau] \cdot \\
& \exp\left[ -\frac{\tau}{2} (y^T P y + \mu_0^T \Lambda_0 \mu_0 - \mu_n^T \Lambda_n \mu_n) \right] \; .
\end{split}
$$

Using the [probability density function of the gamma distribution](/P/gam-pdf), we can rewrite this as

$$ \label{eq:GLM-NG-LME-s4}
\int p(y,\beta,\tau) \, \mathrm{d}\beta = \sqrt{\frac{|P|}{(2 \pi)^n}} \, \sqrt{\frac{|\Lambda_0|}{|\Lambda_n|}} \, \frac{ {b_0}^{a_0}}{\Gamma(a_0)} \, \frac{\Gamma(a_n)}{ {b_n}^{a_n}} \, \mathrm{Gam}(\tau; a_n, b_n) \; .
$$

Finally, $\tau$ can also be integrated out:

$$ \label{eq:GLM-NG-LME-s5}
\iint p(y,\beta,\tau) \, \mathrm{d}\beta \, \mathrm{d}\tau = \sqrt{\frac{|P|}{(2 \pi)^n}} \, \sqrt{\frac{|\Lambda_0|}{|\Lambda_n|}} \, \frac{\Gamma(a_n)}{\Gamma(a_0)} \, \frac{ {b_0}^{a_0}}{ {b_n}^{a_n}} = p(y|m) \; .
$$

Thus, the [log model evidence](/D/lme) of this model is given by

$$ \label{eq:GLM-NG-LME-s6}
\begin{split}
\log p(y|m) = \frac{1}{2} & \log |P| - \frac{n}{2} \log (2 \pi)  + \frac{1}{2} \log |\Lambda_0| - \frac{1}{2} \log |\Lambda_n| + \\
& \log \Gamma(a_n) - \log \Gamma(a_0) + a_0 \log b_0 - a_n \log b_n \; .
\end{split}
$$