---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-03-01 12:10:00

title: "Deviance information criterion for multiple linear regression"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Bayesian linear regression"
theorem: "Deviance information criterion"

sources:

proof_id: "P313"
shortcut: "blr-dic"
username: "JoramSoch"
---


**Theorem:** Consider a [linear regression model](/D/mlr) $m$

$$ \label{eq:mlr}
m: \; y = X\beta + \varepsilon, \; \varepsilon \sim \mathcal{N}(0, \sigma^2 V), \; \sigma^2 V = (\tau P)^{-1}
$$

with a [normal-gamma prior distribution](/P/blr-prior)

$$ \label{eq:blr-prior}
p(\beta,\tau) = \mathcal{N}(\beta; \mu_0, (\tau \Lambda_0)^{-1}) \cdot \mathrm{Gam}(\tau; a_0, b_0) \; .
$$

Then, the [deviance information criterion](/D/dic) for this model is

$$ \label{eq:mlr-dic}
\begin{split}
\mathrm{DIC}(m) &= n \cdot \log(2\pi) - n \left[ 2 \psi(a_n) - \log(a_n) - \log(b_n) \right] - \log|P| \\
&+ \frac{a_n}{b_n} (y - X\mu_n)^\mathrm{T} P (y - X\mu_n) + \mathrm{tr}\left( X^\mathrm{T} P X \Lambda_n^{-1} \right)
\end{split}
$$

where $\mu_n$ and $\Lambda_n$ as well as $a_n$ and $b_n$ are [posterior parameters](/D/post) describing the [posterior distribution in Bayesian linear regression](/P/blr-post).


**Proof:** The [deviance for multiple linear regression](/P/mlr-dev) is

$$ \label{eq:mlr-dev-s1}
D(\beta,\sigma^2) = n \cdot \log(2\pi) + n \cdot \log(\sigma^2) + \log|V| + \frac{1}{\sigma^2} (y - X\beta)^\mathrm{T} V^{-1} (y - X\beta)
$$

which, applying the equalities $\tau = 1/\sigma^2$ and $P = V^{-1}$, becomes

$$ \label{eq:mlr-dev-s2}
D(\beta,\tau) = n \cdot \log(2\pi) - n \cdot \log(\tau) - \log|P| + \tau \cdot (y - X\beta)^\mathrm{T} P (y - X\beta) \; .
$$

The [deviance information criterion](/D/dic) (DIC) is defined as

$$ \label{eq:dic}
\mathrm{DIC}(m) = -2 \log p(y|\left\langle \beta \right\rangle, \left\langle \tau \right\rangle, m) + 2 \, p_D
$$

where $\log p(y \vert \left\langle \beta \right\rangle, \left\langle \tau \right\rangle, m)$ is the [log-likelihood function](/P/mlr-mll) at the posterior [expectations](/D/mean) and the "effective number of parameters" $p_D$ is the [difference between the expectation of the deviance and the deviance at the expectation](/D/dic):

$$ \label{eq:dic-pD}
p_D = \left\langle D(\beta,\tau) \right\rangle - D(\left\langle \beta \right\rangle, \left\langle \tau \right\rangle) \; .
$$

With that, the DIC for multiple linear regression becomes:

$$ \label{eq:mlr-dic-s1}
\begin{split}
\mathrm{DIC}(m) &= -2 \log p(y|\left\langle \beta \right\rangle, \left\langle \tau \right\rangle, m) + 2 \, p_D \\
&= D(\left\langle \beta \right\rangle, \left\langle \tau \right\rangle) + 2 \left[ \left\langle D(\beta,\tau) \right\rangle - D(\left\langle \beta \right\rangle, \left\langle \tau \right\rangle) \right] \\
&= 2 \left\langle D(\beta,\tau) \right\rangle - D(\left\langle \beta \right\rangle, \left\langle \tau \right\rangle) \; .
\end{split}
$$

The [posterior distribution for multiple linear regression](/P/blr-post) is

$$ \label{eq:blr-post}
p(\beta,\tau|y) = \mathcal{N}(\beta; \mu_n, (\tau \Lambda_n)^{-1}) \cdot \mathrm{Gam}(\tau; a_n, b_n)
$$

where the [posterior hyperparameters](/D/post) are given by

$$ \label{eq:blr-post-par}
\begin{split}
\mu_n &= \Lambda_n^{-1} (X^\mathrm{T} P y + \Lambda_0 \mu_0) \\
\Lambda_n &= X^\mathrm{T} P X + \Lambda_0 \\
a_n &= a_0 + \frac{n}{2} \\
b_n &= b_0 + \frac{1}{2} (y^\mathrm{T} P y + \mu_0^\mathrm{T} \Lambda_0 \mu_0 - \mu_n^\mathrm{T} \Lambda_n \mu_n) \; .
\end{split}
$$

Thus, we have the following posterior expectations:

$$ \label{eq:blr-post-beta}
\left\langle \beta \right\rangle_{\beta,\tau|y} = \mu_n
$$

$$ \label{eq:blr-post-tau}
\left\langle \tau \right\rangle_{\beta,\tau|y} = \frac{a_n}{b_n}
$$

$$ \label{eq:blr-post-log-tau}
\left\langle \log \tau \right\rangle_{\beta,\tau|y} = \psi(a_n) - \log(b_n)
$$

$$ \label{eq:blr-post-beta-qf}
\begin{split}
\left\langle \beta^\mathrm{T} A \beta \right\rangle_{\beta|\tau,y} &= \mu_n^\mathrm{T} A \mu_n + \mathrm{tr}\left( A (\tau \Lambda_n)^{-1} \right) \\
&= \mu_n^\mathrm{T} A \mu_n + \frac{1}{\tau} \mathrm{tr}\left( A \Lambda_n^{-1} \right) \; .
\end{split}
$$

In these identities, we have used the [mean of the multivariate normal distribution](/P/mvn-mean), the [mean of the gamma distribution](/P/gam-mean), the [logarithmic expectation of the gamma distribution](/P/gam-logmean), the [expectation of a quadratic form](/P/mean-qf) and the [covariance of the multivariate normal distribution](/P/mvn-cov).

With that, the deviance at the expectation is:

$$ \label{eq:mlr-dev-exp}
\begin{split}
D(\left\langle \beta \right\rangle, \left\langle \tau \right\rangle) &\overset{\eqref{eq:mlr-dev-s2}}{=} n \cdot \log(2\pi) - n \cdot \log(\left\langle \tau \right\rangle) - \log|P| + \tau \cdot (y - X\left\langle \beta \right\rangle)^\mathrm{T} P (y - X\left\langle \beta \right\rangle) \\
&\overset{\eqref{eq:blr-post-beta}}{=} n \cdot \log(2\pi) - n \cdot \log(\left\langle \tau \right\rangle) - \log|P| + \tau \cdot (y - X\mu_n)^\mathrm{T} P (y - X\mu_n) \\
&\overset{\eqref{eq:blr-post-tau}}{=} n \cdot \log(2\pi) - n \cdot \log\left(\frac{a_n}{b_n}\right) - \log|P| + \frac{a_n}{b_n} \cdot (y - X\mu_n)^\mathrm{T} P (y - X\mu_n) \; .
\end{split}
$$

Moreover, the expectation of the deviance is:

$$ \label{eq:mlr-exp-dev}
\begin{split}
\left\langle D(\beta,\tau) \right\rangle &\overset{\eqref{eq:mlr-dev-s2}}{=} \left\langle n \cdot \log(2\pi) - n \cdot \log(\tau) - \log|P| + \tau \cdot (y - X\beta)^\mathrm{T} P (y - X\beta) \right\rangle \\
&= n \cdot \log(2\pi) - n \cdot \left\langle \log(\tau) \right\rangle - \log|P| + \left\langle \tau \cdot (y - X\beta)^\mathrm{T} P (y - X\beta) \right\rangle \\
&\overset{\eqref{eq:blr-post-log-tau}}{=} n \cdot \log(2\pi) - n \cdot \left[ \psi(a_n) - \log(b_n) \right] - \log|P| \\
&+ \left\langle \tau \cdot \left\langle (y - X\beta)^\mathrm{T} P (y - X\beta) \right\rangle_{\beta|\tau,y} \right\rangle_{\tau|y} \\
&= n \cdot \log(2\pi) - n \cdot \left[ \psi(a_n) - \log(b_n) \right] - \log|P| \\
&+ \left\langle \tau \cdot \left\langle y^\mathrm{T} P y - y^\mathrm{T} P X\beta - \beta^\mathrm{T} X^\mathrm{T} P y + \beta^\mathrm{T} X^\mathrm{T} P X \beta \right\rangle_{\beta|\tau,y} \right\rangle_{\tau|y} \\
&\overset{\eqref{eq:blr-post-beta-qf}}{=} n \cdot \log(2\pi) - n \cdot \left[ \psi(a_n) - \log(b_n) \right] - \log|P| \\
&+ \left\langle \tau \cdot \left[ y^\mathrm{T} P y - y^\mathrm{T} P X\mu_n - \mu_n^\mathrm{T} X^\mathrm{T} P y + \mu_n^\mathrm{T} X^\mathrm{T} P X \mu_n  + \frac{1}{\tau} \mathrm{tr}\left( X^\mathrm{T} P X \Lambda_n^{-1} \right) \right] \right\rangle_{\tau|y} \\
&= n \cdot \log(2\pi) - n \cdot \left[ \psi(a_n) - \log(b_n) \right] - \log|P| \\
&+ \left\langle \tau \cdot (y - X\mu_n)^\mathrm{T} P (y - X\mu_n) \right\rangle_{\tau|y} + \mathrm{tr}\left( X^\mathrm{T} P X \Lambda_n^{-1} \right) \\
&\overset{\eqref{eq:blr-post-tau}}{=} n \cdot \log(2\pi) - n \cdot \left[ \psi(a_n) - \log(b_n) \right] - \log|P| \\
&+ \frac{a_n}{b_n} \cdot (y - X\mu_n)^\mathrm{T} P (y - X\mu_n) + \mathrm{tr}\left( X^\mathrm{T} P X \Lambda_n^{-1} \right) \; .
\end{split}
$$

Finally, combining the two terms, we have:

$$ \label{eq:mlr-dic-s2}
\begin{split}
\mathrm{DIC}(m) &\overset{\eqref{eq:mlr-dic-s1}}{=} 2 \left\langle D(\beta,\tau) \right\rangle - D(\left\langle \beta \right\rangle, \left\langle \tau \right\rangle) \\
&\overset{\eqref{eq:mlr-exp-dev}}{=} 2 \left[ n \cdot \log(2\pi) - n \cdot \left[ \psi(a_n) - \log(b_n) \right] - \log|P| \right. \\
&+ \left. \frac{a_n}{b_n} \cdot (y - X\mu_n)^\mathrm{T} P (y - X\mu_n) + \mathrm{tr}\left( X^\mathrm{T} P X \Lambda_n^{-1} \right) \right] \\
&\overset{\eqref{eq:mlr-dev-exp}}{-} \left[ n \cdot \log(2\pi) - n \cdot \log\left(\frac{a_n}{b_n}\right) - \log|P| + \frac{a_n}{b_n} \cdot (y - X\mu_n)^\mathrm{T} P (y - X\mu_n) \right] \\
&= n \cdot \log(2\pi) - 2 n \psi(a_n) + 2 n \log(b_n) + n \log(a_n) - \log(b_n) - \log|P| \\
&+ \frac{a_n}{b_n} (y - X\mu_n)^\mathrm{T} P (y - X\mu_n) + \mathrm{tr}\left( X^\mathrm{T} P X \Lambda_n^{-1} \right) \\
&= n \cdot \log(2\pi) - n \left[ 2 \psi(a_n) - \log(a_n) - \log(b_n) \right] - \log|P| \\
&+ \frac{a_n}{b_n} (y - X\mu_n)^\mathrm{T} P (y - X\mu_n) + \mathrm{tr}\left( X^\mathrm{T} P X \Lambda_n^{-1} \right) \; .
\end{split}
$$

This conforms to equation \eqref{eq:mlr-dic}.