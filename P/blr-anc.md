---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2024-01-12 14:24:48

title: "Accuracy and complexity for Bayesian linear regression"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Bayesian linear regression"
theorem: "Accuracy and complexity"

sources:
  - authors: "Soch J, Allefeld C, Haynes JD"
    year: 2016
    title: "How to avoid mismodelling in GLM-based fMRI data analysis: cross-validated Bayesian model selection"
    in: "NeuroImage"
    pages: "vol. 141, pp. 469-489, Appendix C"
    url: "https://www.sciencedirect.com/science/article/pii/S1053811916303615"
    doi: "10.1016/j.neuroimage.2016.07.047"
  - authors: "Soch J"
    year: 2018
    title: "cvBMS and cvBMA: filling in the gaps"
    in: "arXiv stat.ME"
    pages: "sect. 2.2, eqs. 8-24"
    url: "https://arxiv.org/abs/1807.01585"
	doi: "10.48550/arXiv.1807.01585"

proof_id: "P431"
shortcut: "blr-anc"
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

Then, [accuracy and complexity](/P/lme-anc) of this model are

$$ \label{eq:GLM-NG-AnC}
\begin{split}
\mathrm{Acc}(m) = & - \frac{1}{2} \frac{a_n}{b_n} (y-X\mu_n)^\mathrm{T} P (y-X\mu_n) - \frac{1}{2} \mathrm{tr}(X^\mathrm{T} P X \Lambda_n^{-1}) \\
& + \frac{1}{2} \log |P| - \frac{n}{2} \log (2 \pi) + \frac{n}{2} (\psi(a_n) - \log(b_n)) \\
\mathrm{Com}(m) &= \frac{1}{2} \frac{a_n}{b_n} \left[(\mu_0-\mu_n)^\mathrm{T} \Lambda_0 (\mu_0-\mu_n) - 2(b_n-b_0)\right] + \frac{1}{2} \mathrm{tr}(\Lambda_0 \Lambda_n^{-1}) - \frac{1}{2} \log \frac{|\Lambda_0|}{|\Lambda_n|} - \frac{p}{2} \\
&+ a_0 \log \frac{b_n}{b_0} - \log \frac{\Gamma(a_n)}{\Gamma(a_0)} + (a_n - a_0) \psi(a_n) \; .
\end{split}
$$

where $\mu_n$, $\Lambda_n$, $a_n$ and $b_n$ are the [posterior hyperparameters for Bayesian linear regression](/P/blr-post) and $P$ is the data [precision matrix](/D/precmat): $P = V^{-1}$.


**Proof:** Model [accuracy and complexity are defined as](/P/lme-anc)

$$ \label{eq:lme-anc}
\begin{split}
\mathrm{LME}(m) &= \mathrm{Acc}(m) - \mathrm{Com}(m) \\
\mathrm{Acc}(m) &= \left\langle \log p(y|\beta,\tau,m) \right\rangle_{p(\beta,\tau|y,m)} \\
\mathrm{Com}(m) &= \mathrm{KL} \left[ p(\beta,\tau|y,m) \, || \, p(\beta,\tau|m) \right] \; .
\end{split}
$$

<br>
1) The accuracy term is the [expectation](/D/mean) of the [log-likelihood function](/D/llf) $\log p(y|\beta,\tau)$ with respect to the [posterior distribution](/D/post) $p(\beta,\tau|y)$. This expectation can be rewritten as:

$$ \label{eq:GLM-NG-Acc-s1}
\begin{split}
\mathrm{Acc}(m) &= \iint p(\beta,\tau|y) \, \log p(y|\beta,\tau) \, \mathrm{d}\beta \, \mathrm{d}\tau \\
&= \int p(\tau|y) \int p(\beta|\tau,y) \, \log p(y|\beta,\tau) \, \mathrm{d}\beta \, \mathrm{d}\tau \\
&= \left\langle \left\langle \log p(y|\beta,\tau) \right\rangle_{p(\beta|\tau,y)} \right\rangle_{p(\tau|y)} \; .
\end{split}
$$

With the [log-likelihood function for multiple linear regression](/P/mlr-mle), we have:

$$ \label{eq:GLM-NG-Acc-s2}
\begin{split}
\mathrm{Acc}(m) &= \left\langle \left\langle \log \left( \sqrt{\frac{1}{(2\pi)^n |\sigma^2 V|}} \cdot \exp\left[ -\frac{1}{2} (y - X\beta)^\mathrm{T} (\sigma^2 V)^{-1} (y - X\beta) \right] \right) \right\rangle_{p(\beta|\tau,y)} \right\rangle_{p(\tau|y)} \\
&= \left\langle \left\langle \log \left( \sqrt{\frac{\tau^n |P|}{(2\pi)^n}} \cdot \exp\left[ -\frac{1}{2} (y - X\beta)^\mathrm{T} (\tau P) (y - X\beta) \right] \right) \right\rangle_{p(\beta|\tau,y)} \right\rangle_{p(\tau|y)} \\
&= \left\langle \left\langle \frac{1}{2} \log |P| + \frac{n}{2} \log \tau - \frac{n}{2} \log (2 \pi) - \frac{1}{2} (y-X\beta)^\mathrm{T} (\tau P) (y-X\beta) \right\rangle_{p(\beta|\tau,y)} \right\rangle_{p(\tau|y)} \\
&= \left\langle \left\langle \frac{1}{2} \log |P| + \frac{n}{2} \log \tau - \frac{n}{2} \log (2 \pi) - \frac{\tau}{2} \left[ y^\mathrm{T} P y - 2 y^\mathrm{T} P X \beta + \beta^\mathrm{T} X^\mathrm{T} P X \beta \right] \right\rangle_{p(\beta|\tau,y)} \right\rangle_{p(\tau|y)} \; .
\end{split}
$$

With the [posterior distribution for Bayesian linear regression](/P/blr-post), this becomes:

$$ \label{eq:GLM-NG-Acc-s3}
\mathrm{Acc}(m) = \left\langle \left\langle \frac{1}{2} \log |P| + \frac{n}{2} \log \tau - \frac{n}{2} \log (2 \pi) - \frac{\tau}{2} \left[ y^\mathrm{T} P y - 2 y^\mathrm{T} P X \beta + \beta^\mathrm{T} X^\mathrm{T} P X \beta \right] \right\rangle_{\mathcal{N}(\beta; \mu_n, (\tau \Lambda_n)^{-1})} \right\rangle_{\mathrm{Gam}(\tau; a_n, b_n)} \; .
$$

If $x \sim \mathrm{N}(\mu, \Sigma)$, then [its expected value is](/P/mvn-mean)

$$ \label{eq:mvn-mean}
\left\langle x \right\rangle = \mu
$$

and [the expectation of a quadratic form is given by](/P/mean-qf)

$$ \label{eq:mvn-meansqr}
\left\langle x^\mathrm{T} A x \right\rangle = \mu^\mathrm{T} A \mu + \mathrm{tr}(A \Sigma) \; .
$$

Thus, the model accuracy of $m$ evaluates to:

$$ \label{eq:GLM-NG-Acc-s4}
\begin{split}
\mathrm{Acc}(m) &= \left\langle \frac{1}{2} \log |P| + \frac{n}{2} \log \tau - \frac{n}{2} \log (2 \pi) - \right. \\
&\hphantom{= -} \left. \frac{\tau}{2} \left[ y^\mathrm{T} P y - 2 y^\mathrm{T} P X \mu_n + \mu_n^\mathrm{T} X^\mathrm{T} P X \mu_n + \frac{1}{\tau} \mathrm{tr}(X^\mathrm{T} P X \Lambda_n^{-1}) \right] \right\rangle_{\mathrm{Gam}(\tau; a_n, b_n)} \\
&= \left\langle \frac{1}{2} \log |P| + \frac{n}{2} \log \tau - \frac{n}{2} \log (2 \pi) - \frac{\tau}{2} (y-X\mu_n)^\mathrm{T} P (y-X\mu_n) - \frac{1}{2} \mathrm{tr}(X^\mathrm{T} P X \Lambda_n^{-1}) \right\rangle_{\mathrm{Gam}(\tau; a_n, b_n)} \; .
\end{split}
$$

If $x \sim \mathrm{Gam}(a, b)$, then [its expected value is](/P/gam-mean)

$$ \label{eq:gam-mean}
\left\langle x \right\rangle = \frac{a}{b}
$$

and [its logarithmic expectation is given by](/P/gam-logmean)

$$ \label{eq:gan-logmean}
\left\langle \log x \right\rangle = \psi(a) - \log(b) \; .
$$

Thus, the model accuracy of $m$ evaluates to

$$ \label{eq:GLM-NG-Acc-s5}
\begin{split}
\mathrm{Acc}(m) = & - \frac{1}{2} \frac{a_n}{b_n} (y-X\mu_n)^\mathrm{T} P (y-X\mu_n) - \frac{1}{2} \mathrm{tr}(X^\mathrm{T} P X \Lambda_n^{-1}) \\
& + \frac{1}{2} \log |P| - \frac{n}{2} \log (2 \pi) + \frac{n}{2} (\psi(a_n) - \log(b_n))
\end{split}
$$

which proofs the first part of \eqref{eq:GLM-NG-AnC}.

<br>
2) The complexity penalty is the [Kullback-Leibler divergence](/D/kl) of the [posterior distribution](/D/post) $p(\beta,\tau|y)$ from the [prior distribution](/D/prior) $p(\beta,\tau)$. This can be rewritten as follows:

$$ \label{eq:GLM-NG-Com-s1}
\begin{split}
\mathrm{Com}(m) &= \iint p(\beta,\tau|y) \, \log \frac{p(\beta,\tau|y)}{p(\beta,\tau)} \, \mathrm{d}\beta \, \mathrm{d}\tau \\
&= \iint p(\beta|\tau,y) \, p(\tau|y) \, \log \left[ \frac{p(\beta|\tau,y)}{p(\beta|\tau)} \, \frac{p(\tau|y)}{p(\tau)} \right] \, \mathrm{d}\beta \, \mathrm{d}\tau \\
&= \int p(\tau|y) \int p(\beta|\tau,y) \, \log \frac{p(\beta|\tau,y)}{p(\beta|\tau)} \, \mathrm{d}\beta \, \mathrm{d}\tau + \int p(\tau|y) \, \log \frac{p(\tau|y)}{p(\tau)} \int p(\beta|\tau,y) \, \mathrm{d}\beta \, \mathrm{d}\tau \\
&= \left\langle \mathrm{KL} \left[ p(\beta|\tau,y)\,||\,p(\beta|\tau) \right] \right\rangle_{p(\tau|y)} + \mathrm{KL} \left[ p(\tau|y)\,||\,p(\tau) \right] \; .
\end{split}
$$

With the [prior distribution](/P/blr-prior) given by \eqref{eq:GLM-NG-prior} and the [posterior distribution for Bayesian linear regression](/P/blr-post), this becomes:

$$ \label{eq:GLM-NG-Com-s2}
\begin{split}
\mathrm{Com}(m) &= \left\langle \mathrm{KL} \left[ \mathcal{N}(\beta; \mu_n, (\tau \Lambda_n)^{-1})\,||\,\mathcal{N}(\beta; \mu_0, (\tau \Lambda_0)^{-1}) \right] \right\rangle_{\mathrm{Gam}(\tau; a_n, b_n)} \\
&+ \mathrm{KL} \left[ \mathrm{Gam}(\tau; a_n, b_n)\,||\,\mathrm{Gam}(\tau; a_0, b_0) \right] \; .
\end{split}
$$

With the [Kullback-Leibler divergence for the multivariate normal distribution](/P/mvn-kl)

$$ \label{eq:mvn-kl}
\mathrm{KL}[\mathcal{N}(\mu_1, \Sigma_1)\,||\,\mathcal{N}(\mu_2, \Sigma_2)] = \frac{1}{2} \left[ (\mu_2 - \mu_1)^\mathrm{T} \Sigma_2^{-1} (\mu_2 - \mu_1) + \mathrm{tr}(\Sigma_2^{-1} \Sigma_1) - \ln \frac{|\Sigma_1|}{|\Sigma_2|} - n \right]
$$

and the [Kullback-Leibler divergence for the gamma distribution](/P/gam-kl)

$$ \label{eq:gam-kl}
\mathrm{KL}[\mathrm{Gam}(a_1, b_1)\,||\,\mathrm{Gam}(a_2, b_2)] = a_2 \, \ln \frac{b_1}{b_2} - \ln \frac{\Gamma(a_1)}{\Gamma(a_2)} + (a_1 - a_2) \, \psi(a_1) - (b_1 - b_2) \, \frac{a_1}{b_1} \; ,
$$

the model complexity of $m$ evaluates to:

$$ \label{eq:GLM-NG-Com-s3}
\begin{split}
\mathrm{Com}(m) &= \left\langle \frac{1}{2} \left[ (\mu_0 - \mu_n)^\mathrm{T} (\tau \Lambda_0) (\mu_0 - \mu_n) + \mathrm{tr}((\tau \Lambda_0) (\tau \Lambda_n)^{-1}) - \log \frac{|(\tau \Lambda_n)^{-1}|}{|(\tau \Lambda_0)^{-1}|} - p \right] \right\rangle_{p(\tau|y)} \\
&+ a_0 \, \log \frac{b_n}{b_0} - \log \frac{\Gamma(a_n)}{\Gamma(a_0)} + (a_n - a_0) \, \psi(a_n) - (b_n - b_0) \, \frac{a_n}{b_n} \; .
\end{split}
$$

Using $x \sim \mathrm{Gam}(a, b) \Rightarrow \left\langle x \right\rangle = a/b$ from \eqref{eq:gam-mean} again, it follows that

$$ \label{eq:GLM-NG-Com-s4}
\begin{split}
\mathrm{Com}(m) &= \frac{1}{2} \frac{a_n}{b_n} \left[ (\mu_0 - \mu_n)^\mathrm{T} \Lambda_0 (\mu_0 - \mu_n) \right] + \frac{1}{2} \mathrm{tr}(\Lambda_0 \Lambda_n^{-1}) - \frac{1}{2} \log \frac{|\Lambda_0|}{|\Lambda_n|} - \frac{p}{2} \\
&+ a_0 \, \log \frac{b_n}{b_0} - \log \frac{\Gamma(a_n)}{\Gamma(a_0)} + (a_n - a_0) \, \psi(a_n) - (b_n - b_0) \, \frac{a_n}{b_n} \; .
\end{split}
$$

Thus, the model complexity of $m$ evaluates to

$$ \label{eq:GLM-NG-Com-s5}
\begin{split}
\mathrm{Com}(m) &= \frac{1}{2} \frac{a_n}{b_n} \left[(\mu_0-\mu_n)^\mathrm{T} \Lambda_0 (\mu_0-\mu_n) - 2(b_n-b_0)\right] + \frac{1}{2} \mathrm{tr}(\Lambda_0 \Lambda_n^{-1}) - \frac{1}{2} \log \frac{|\Lambda_0|}{|\Lambda_n|} - \frac{p}{2} \\
&+ a_0 \log \frac{b_n}{b_0} - \log \frac{\Gamma(a_n)}{\Gamma(a_0)} + (a_n - a_0) \psi(a_n)
\end{split}
$$

which proofs the second part of \eqref{eq:GLM-NG-AnC}.

<br>
3) A control calculation confirms that

$$ \label{eq:GLM-NG-AnC-LME}
\mathrm{Acc}(m) - \mathrm{Com}(m) = \mathrm{LME}(m)
$$

where $\mathrm{LME}(m)$ is the [log model evidence for Bayesian linear regression](/P/blr-lme):

$$ \label{eq:GLM-NG-LME}
\begin{split}
\log p(y|m) = \frac{1}{2} & \log |P| - \frac{n}{2} \log (2 \pi)  + \frac{1}{2} \log |\Lambda_0| - \frac{1}{2} \log |\Lambda_n| + \\
& \log \Gamma(a_n) - \log \Gamma(a_0) + a_0 \log b_0 - a_n \log b_n
\end{split}
$$

This requires to recognize that

$$ \label{eq:GLM-NG-AnC-LME-a1}
-\frac{1}{2} \mathrm{tr}(X^\mathrm{T} P X \Lambda_n^{-1}) - \mathrm{tr}(\Lambda_0 \Lambda_n^{-1}) + \frac{p}{2} = 0
$$

and 

$$ \label{eq:GLM-NG-AnC-LME-a2}
\frac{n}{2} (\psi(a_n) - \log(b_n)) - a_0 \log \frac{b_n}{b_0} - (a_n - a_0) \psi(a_n) = a_0 \log b_0 - a_n \log b_n
$$

thanks to the nature of the [posterior hyperparameters for Bayesian linear regression](/P/blr-post).