---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2024-01-19 08:58:20

title: "Accuracy and complexity for Bayesian linear regression with known covariance"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Bayesian linear regression with known covariance"
theorem: "Accuracy and complexity"

sources:
  - authors: "Penny WD"
    year: 2012
    title: "Comparing Dynamic Causal Models using AIC, BIC and Free Energy"
    in: "NeuroImage"
    pages: "vol. 59, iss. 2, pp. 319-330, eqs. 20-21"
    url: "https://www.sciencedirect.com/science/article/pii/S1053811911008160"
    doi: "10.1016/j.neuroimage.2011.07.039"
  - authors: "Bishop CM"
    year: 2006
    title: "Bayesian Linear Regression"
    in: "Pattern Recognition for Machine Learning"
    pages: "pp. 152-161"
    url: "https://www.springer.com/gp/book/9780387310732"

proof_id: "P435"
shortcut: "blrkc-anc"
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

Then, [accuracy and complexity](/P/lme-anc) of this model are

$$ \label{eq:GLM-N-AnC}
\begin{split}
\mathrm{Acc}(m) &= - \frac{1}{2} e_y^\mathrm{T} \Sigma^{-1} e_y - \frac{1}{2} \log |\Sigma| - \frac{n}{2} \log (2 \pi) - \frac{1}{2} \mathrm{tr}(X^\mathrm{T} \Sigma^{-1} X \Sigma_n) \\
\mathrm{Com}(m) &= \hphantom{+} \frac{1}{2} e_\beta^\mathrm{T} \Sigma_0^{-1} e_\beta + \frac{1}{2} \log |\Sigma_0| - \frac{1}{2} \log |\Sigma_n| + \frac{1}{2} \mathrm{tr}(\Sigma_0^{-1} \Sigma_n) - \frac{p}{2}
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


**Proof:** Model [accuracy and complexity are defined as](/P/lme-anc)

$$ \label{eq:lme-anc}
\begin{split}
\mathrm{LME}(m) &= \mathrm{Acc}(m) - \mathrm{Com}(m) \\
\mathrm{Acc}(m) &= \left\langle \log p(y|\beta,m) \right\rangle_{p(\beta|y,m)} \\
\mathrm{Com}(m) &= \mathrm{KL} \left[ p(\beta|y,m) \, || \, p(\beta|m) \right] \; .
\end{split}
$$

<br>
1) The accuracy term is the [expectation](/D/mean) of the [log-likelihood function](/D/llf) $\log p(y|\beta)$ with respect to the [posterior distribution](/D/post) $p(\beta|y)$:

$$ \label{eq:GLM-N-Acc-s1}
\mathrm{Acc}(m) = \left\langle \log p(y|\beta) \right\rangle_{p(\beta|y)} \; .
$$

With the [likelihood function for Bayesian linear regression with known covariance](/P/blrkc-prior), we have:

$$ \label{eq:GLM-N-Acc-s2}
\begin{split}
\mathrm{Acc}(m) &= \left\langle \log \left( \sqrt{\frac{1}{(2 \pi)^n |\Sigma|}} \, \exp\left[ -\frac{1}{2} (y-X\beta)^\mathrm{T} \Sigma^{-1} (y-X\beta) \right] \right) \right\rangle_{p(\beta|y)} \\
&= \left\langle - \frac{n}{2} \log (2 \pi) - \frac{1}{2} \log |\Sigma| - \frac{1}{2} (y-X\beta)^\mathrm{T} \Sigma^{-1} (y-X\beta) \right\rangle_{p(\beta|y)} \\
&= \left\langle - \frac{n}{2} \log (2 \pi) - \frac{1}{2} \log |\Sigma| - \frac{1}{2} \left[ y^\mathrm{T} \Sigma^{-1} y - 2 y^\mathrm{T} \Sigma^{-1} X \beta + \beta^\mathrm{T} X^\mathrm{T} \Sigma^{-1} X \beta \right] \right\rangle_{p(\beta|y)} \; .
\end{split}
$$

With the [posterior distribution for Bayesian linear regression with known covariance](/P/blrkc-post), this becomes:

$$ \label{eq:GLM-N-Acc-s3}
\mathrm{Acc}(m) = \left\langle - \frac{n}{2} \log (2 \pi) - \frac{1}{2} \log |\Sigma| - \frac{1}{2} \left[ y^\mathrm{T} \Sigma^{-1} y - 2 y^\mathrm{T} \Sigma^{-1} X \beta + \beta^\mathrm{T} X^\mathrm{T} \Sigma^{-1} X \beta \right] \right\rangle_{\mathcal{N}(\beta; \mu_n, \Sigma_n)} \; .
$$

If $x \sim \mathrm{N}(\mu, \Sigma)$, then [its expected value is](/P/mvn-mean)

$$ \label{eq:mvn-mean}
\left\langle x \right\rangle = \mu
$$

and [the expectation of a quadratic form is given by](/P/mean-qf)

$$ \label{eq:mvn-meansqr}
\left\langle x^\mathrm{T} A x \right\rangle = \mu^\mathrm{T} A \mu + \mathrm{tr}(A \Sigma) \; .
$$

Thus, the model accuracy of $m$ evaluates to

$$ \label{eq:GLM-N-Acc-s4}
\begin{split}
\mathrm{Acc}(m) = - &\frac{n}{2} \log (2 \pi) - \frac{1}{2} \log |\Sigma| - \\
&\frac{1}{2} \left[ y^\mathrm{T} \Sigma^{-1} y - 2 y^\mathrm{T} \Sigma^{-1} X \mu_n + \mu_n^\mathrm{T} X^\mathrm{T} \Sigma^{-1} X \mu_n + \mathrm{tr}(X^\mathrm{T} \Sigma^{-1} X \Sigma_n) \right] \\
= - &\frac{1}{2} (y - X \mu_n)^\mathrm{T} \Sigma^{-1} (y - X \mu_n) - \frac{1}{2} \log |\Sigma| - \frac{n}{2} \log (2 \pi) - \frac{1}{2} \mathrm{tr}(X^\mathrm{T} \Sigma^{-1} X \Sigma_n) \\
\overset{\eqref{eq:GLM-N-err}}{=} - &\frac{1}{2} e_y^\mathrm{T} \Sigma^{-1} e_y - \frac{1}{2} \log |\Sigma| - \frac{n}{2} \log (2 \pi) - \frac{1}{2} \mathrm{tr}(X^\mathrm{T} \Sigma^{-1} X \Sigma_n)
\end{split}
$$

which proofs the first part of \eqref{eq:GLM-N-AnC}.

<br>
2) The complexity penalty is the [Kullback-Leibler divergence](/D/kl) of the [posterior distribution](/D/post) $p(\beta|y)$ from the [prior distribution](/D/prior) $p(\beta)$:

$$ \label{eq:GLM-N-Com-s1}
\mathrm{Com}(m) = \mathrm{KL} \left[ p(\beta|y) \, || \, p(\beta) \right] \; .
$$

With the [prior distribution](/P/blrkc-prior) given by \eqref{eq:GLM-N-prior} and the [posterior distribution for Bayesian linear regression with known covariance](/P/blrkc-post), this becomes:

$$ \label{eq:GLM-N-Com-s2}
\mathrm{Com}(m) = \mathrm{KL} \left[ \mathcal{N}(\beta; \mu_n, \Sigma_n)\,||\,\mathcal{N}(\beta; \mu_0, \Sigma_0) \right] \; .
$$

With the [Kullback-Leibler divergence for the multivariate normal distribution](/P/mvn-kl)

$$ \label{eq:mvn-kl}
\mathrm{KL}[\mathcal{N}(\mu_1, \Sigma_1)\,||\,\mathcal{N}(\mu_2, \Sigma_2)] = \frac{1}{2} \left[ (\mu_2 - \mu_1)^\mathrm{T} \Sigma_2^{-1} (\mu_2 - \mu_1) + \mathrm{tr}(\Sigma_2^{-1} \Sigma_1) - \ln \frac{|\Sigma_1|}{|\Sigma_2|} - n \right] \; ,
$$

the model complexity of $m$ evaluates to

$$ \label{eq:GLM-N-Com-s3}
\begin{split}
\mathrm{Com}(m) &= \frac{1}{2} \left[ (\mu_0 - \mu_n)^\mathrm{T} \Sigma_0^{-1} (\mu_0 - \mu_n) + \mathrm{tr}(\Sigma_0^{-1} \Sigma_n) - \log \frac{|\Sigma_n|}{|\Sigma_0|} - p \right] \\
&= \frac{1}{2} (\mu_0 - \mu_n)^\mathrm{T} \Sigma_0^{-1} (\mu_0 - \mu_n) + \frac{1}{2} \log |\Sigma_0| - \frac{1}{2} \log |\Sigma_n| + \frac{1}{2} \mathrm{tr}(\Sigma_0^{-1} \Sigma_n) - \frac{p}{2} \\
&\overset{\eqref{eq:GLM-N-err}}{=} \frac{1}{2} e_\beta^\mathrm{T} \Sigma_0^{-1} e_\beta + \frac{1}{2} \log |\Sigma_0| - \frac{1}{2} \log |\Sigma_n| + \frac{1}{2} \mathrm{tr}(\Sigma_0^{-1} \Sigma_n) - \frac{p}{2}
\end{split}
$$

which proofs the second part of \eqref{eq:GLM-N-AnC}.

<br>
3) A control calculation confirms that

$$ \label{eq:GLM-N-AnC-LME}
\mathrm{Acc}(m) - \mathrm{Com}(m) = \mathrm{LME}(m)
$$

where $\mathrm{LME}(m)$ is the [log model evidence for Bayesian linear regression with known covariance](/P/blrkc-lme):

$$ \label{eq:GLM-N-LME}
\begin{split}
\log p(y|m) = &- \frac{1}{2} e_y^\mathrm{T} \Sigma^{-1} e_y - \frac{1}{2} \log |\Sigma| - \frac{n}{2} \log (2 \pi) \\
&- \frac{1}{2} e_\beta^\mathrm{T} \Sigma_0^{-1} e_\beta - \frac{1}{2} \log |\Sigma_0| + \frac{1}{2} \log |\Sigma_n| \; .
\end{split}
$$

This requires to recognize, based on \eqref{eq:GLM-N-post-par}, that

$$ \label{eq:GLM-N-AnC-LME-a1}
\begin{split}
& \; - \frac{1}{2} \mathrm{tr}(X^\mathrm{T} \Sigma^{-1} X \Sigma_n) - \frac{1}{2} \mathrm{tr}(\Sigma_0^{-1} \Sigma_n) + \frac{p}{2} \\
= & \; - \frac{1}{2} \mathrm{tr}\left( [X^\mathrm{T} \Sigma^{-1} X + \Sigma_0^{-1}] \Sigma_n \right) + \frac{p}{2} \\
= & \; - \frac{1}{2} \mathrm{tr}\left( \Sigma_n^{-1} \Sigma_n \right) + \frac{p}{2} \\
= & \; - \frac{1}{2} \mathrm{tr}\left( I_p \right) + \frac{p}{2} \\
= & \; - \frac{p}{2} + \frac{p}{2} \\
= & \;\; 0 \; .
\end{split}
$$