---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-12-13 12:36:00

title: "F-test for multiple linear regression using contrast-based inference"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Multiple linear regression"
theorem: "Contrast-based F-test"

sources:
  - authors: "Stephan, Klaas Enno"
    year: 2010
    title: "Classical (frequentist) inference"
    in: "Methods and models for fMRI data analysis in neuroeconomics"
    pages: "Lecture 4, Slides 23/25"
    url: "http://www.socialbehavior.uzh.ch/teaching/methodsspring10.html"
  - authors: "Koch, Karl-Rudolf"
    year: 2007
    title: "Multivariate Distributions"
    in: "Introduction to Bayesian Statistics"
    pages: "Springer, Berlin/Heidelberg, 2007, ch. 2.5, eqs. 2.202, 2.213, 2.211"
    url: "https://www.springer.com/de/book/9783540727231"
    doi: "10.1007/978-3-540-72726-2"
  - authors: "jld"
    year: 2018
    title: "Understanding t-test for linear regression"
    in: "StackExchange CrossValidated"
    pages: "retrieved on 2022-12-13"
    url: "https://stats.stackexchange.com/a/344008"
  - authors: "Penny, William"
    year: 2006
    title: "Comparing nested GLMs"
    in: "Mathematics for Brain Imaging"
    pages: "ch. 2.3, pp. 51-52, eq. 2.9"
    url: "https://ueapsylabs.co.uk/sites/wpenny/mbi/mbi_course.pdf"

proof_id: "P392"
shortcut: "mlr-f"
username: "JoramSoch"
---


**Theorem:** Consider a [linear regression model](/D/mlr)

$$ \label{eq:mlr}
y = X\beta + \varepsilon, \; \varepsilon \sim \mathcal{N}(0, \sigma^2 V)
$$

and an [F-contrast](/D/fcon) on the model parameters

$$ \label{eq:fcon}
\gamma = C^\mathrm{T} \beta \quad \text{where} \quad C \in \mathbb{R}^{p \times q} \; .
$$

Then, the [test statistic](/D/tstat)

$$ \label{eq:mlr-f}
F = \hat{\beta}^\mathrm{T} C \left( \hat{\sigma}^2 C^\mathrm{T} (X^\mathrm{T} V^{-1} X)^{-1} C \right)^{-1} C^\mathrm{T} \hat{\beta} / q
$$

with the [parameter estimates](/P/mlr-mle)

$$ \label{eq:mlr-est}
\begin{split}
\hat{\beta} &= (X^\mathrm{T} V^{-1} X)^{-1} X^\mathrm{T} V^{-1} y \\
\hat{\sigma}^2 &= \frac{1}{n-p} (y-X\hat{\beta})^\mathrm{T} V^{-1} (y-X\hat{\beta})
\end{split}
$$

follows an [F-distribution](/D/f)

$$ \label{eq:mlr-f-dist}
F \sim \mathrm{F}(q, n-p)
$$

under the [null hypothesis](/D/h0)

$$ \label{eq:mlr-f-h0}
\begin{split}
H_0: &\; \gamma_1 = 0 \wedge \ldots \wedge \gamma_q = 0 \\
H_1: &\; \gamma_1 \neq 0 \vee \ldots \vee \gamma_q \neq 0 \; .
\end{split}
$$


**Proof:**

1) We know that [the estimated regression coefficients in linear regression follow a multivariate normal distribution](/P/mlr-wlsdist):

$$ \label{eq:b-est-dist}
\hat{\beta} \sim \mathcal{N}\left( \beta, \, \sigma^2 (X^\mathrm{T} V^{-1} X)^{-1} \right) \; .
$$

Thus, the [estimated contrast vector](/D/tcon) $\hat{\gamma} = C^\mathrm{T} \hat{\beta}$ is also [distributed according to a multivariate normal distribution](/P/mvn-ltt):

$$ \label{eq:g-est-dist-cond}
\hat{\gamma} \sim \mathcal{N}\left( C^\mathrm{T} \beta, \, \sigma^2 C^\mathrm{T} (X^\mathrm{T} V^{-1} X)^{-1} C \right) \; .
$$

Substituting the noise variance $\sigma^2$ with the noise precision $\tau = 1/\sigma^2$, we can also write this down as a [conditional distribution](/D/dist-cond):

$$ \label{eq:g-est-tau-dist-cond}
\hat{\gamma} \vert \tau \sim \mathcal{N}\left( C^\mathrm{T} \beta, (\tau Q)^{-1} \right) \quad \text{with} \quad Q = \left( C^\mathrm{T} (X^\mathrm{T} V^{-1} X)^{-1} C \right)^{-1} \; .
$$

2) We also know that the [residual sum of squares](/D/rss), divided the [true error variance](/D/mlr)

$$ \label{eq:mlr-rss}
\frac{1}{\sigma^2} \sum_{i=1}^{n} \hat{\varepsilon}_i^2 = \frac{\hat{\varepsilon}^\mathrm{T} \hat{\varepsilon}}{\sigma^2} = \frac{1}{\sigma^2} (y-X\hat{\beta})^\mathrm{T} V^{-1} (y-X\hat{\beta})
$$

[is following a chi-squared distribution](/P/mlr-rssdist):

$$ \label{eq:mlr-rss-dist}
\frac{\hat{\varepsilon}^\mathrm{T} \hat{\varepsilon}}{\sigma^2} = \tau \, \hat{\varepsilon}^\mathrm{T} \hat{\varepsilon} \sim \chi^2(n-p) \; .
$$

The [chi-squared distribution is related to the gamma distribution](/P/gam-chi2) in the following way:

$$ \label{eq:gam-chi2}
X \sim \chi^2(k) \quad \Rightarrow \quad cX \sim \mathrm{Gam}\left( \frac{k}{2}, \frac{1}{2c} \right) \; .
$$

Thus, applying \eqref{eq:gam-chi2} to \eqref{eq:mlr-rss-dist}, we obtain the [marginal distribution](/D/dist-marg) of $\tau$ as:

$$ \label{eq:tau-dist}
\frac{1}{\hat{\varepsilon}^\mathrm{T} \hat{\varepsilon}} \left( \tau \, \hat{\varepsilon}^\mathrm{T} \hat{\varepsilon} \right) = \tau \sim \mathrm{Gam}\left( \frac{n-p}{2}, \frac{\hat{\varepsilon}^\mathrm{T} \hat{\varepsilon}}{2} \right) \; .
$$

3) Note that the [joint distribution](/D/dist-joint) of $\hat{\gamma}$ and $\tau$ is, following from \eqref{eq:g-est-tau-dist-cond} and \eqref{eq:tau-dist} and [by definition, a normal-gamma distribution](/D/ng):

$$ \label{eq:g-est-tau-dist-joint}
\hat{\gamma}, \tau \sim \mathrm{NG}\left( C^\mathrm{T} \beta, Q, \frac{n-p}{2}, \frac{\hat{\varepsilon}^\mathrm{T} \hat{\varepsilon}}{2} \right) \; .
$$

The [marginal distribution of a normal-gamma distribution with respect to the normal random variable, is a multivariate t-distribution](/P/ng-marg):

$$ \label{eq:ng-mvt}
X, Y \sim \mathrm{NG}(\mu, \Lambda, a, b) \quad \Rightarrow \quad X \sim \mathrm{t}\left( \mu, \left( \frac{a}{b} \Lambda\right)^{-1}, 2a \right) \; .
$$

Thus, the [marginal distribution](/D/dist-marg) of $\hat{\gamma}$ is:

$$ \label{eq:g-est-dist-marg}
\hat{\gamma} \sim \mathrm{t}\left( C^\mathrm{T} \beta, \left( \frac{n-p}{\hat{\varepsilon}^\mathrm{T} \hat{\varepsilon}} Q \right)^{-1}, n-p \right) \; .
$$

4) Because of the following [relationship between the multivariate t-distribution and the F-distribution](/P/mvt-f)

$$ \label{eq:mvt-f}
X \sim t(\mu, \Sigma, \nu) \quad \Rightarrow \quad (X-\mu)^\mathrm{T} \, \Sigma^{-1} (X-\mu)/n \sim F(n, \nu) \; ,
$$

the following quantity [is, by definition, F-distributed](/D/f)

$$ \label{eq:mlr-f-s1}
F = \left( \hat{\gamma} -  C^\mathrm{T} \hat{\beta} \right)^\mathrm{T} \left( \frac{n-p}{\hat{\varepsilon}^\mathrm{T} \hat{\varepsilon}} Q \right) \left( \hat{\gamma} -  C^\mathrm{T} \hat{\beta} \right) / q
$$

and under the [null hypothesis](/D/h0) \eqref{eq:mlr-f-h0}, it can be evaluated as:

$$ \label{eq:mlr-t-s2}
\begin{split}
F &\overset{\eqref{eq:mlr-f-s1}}{=} \left( \hat{\gamma} -  C^\mathrm{T} \hat{\beta} \right)^\mathrm{T} \left( \frac{n-p}{\hat{\varepsilon}^\mathrm{T} \hat{\varepsilon}} Q \right) \left( \hat{\gamma} -  C^\mathrm{T} \hat{\beta} \right) / q \\
&\overset{\eqref{eq:mlr-f-h0}}{=} \hat{\gamma}^\mathrm{T} \left( \frac{n-p}{\hat{\varepsilon}^\mathrm{T} \hat{\varepsilon}} Q \right) \hat{\gamma} / q \\
&\overset{\eqref{eq:fcon}}{=} \hat{\beta}^\mathrm{T} C \left( \frac{n-p}{\hat{\varepsilon}^\mathrm{T} \hat{\varepsilon}} Q \right) C^\mathrm{T} \hat{\beta} / q \\
&\overset{\eqref{eq:g-est-tau-dist-cond}}{=} \hat{\beta}^\mathrm{T} C \left( \frac{n-p}{\hat{\varepsilon}^\mathrm{T} \hat{\varepsilon}} \left( C^\mathrm{T} (X^\mathrm{T} V^{-1} X)^{-1} C \right)^{-1} \right) C^\mathrm{T} \hat{\beta} / q \\
&\overset{\eqref{eq:mlr-rss}}{=} \hat{\beta}^\mathrm{T} C \left( \frac{n-p}{(y-X\hat{\beta})^\mathrm{T} V^{-1} (y-X\hat{\beta})} \left( C^\mathrm{T} (X^\mathrm{T} V^{-1} X)^{-1} C \right)^{-1} \right) C^\mathrm{T} \hat{\beta} / q \\
&\overset{\eqref{eq:mlr-est}}{=} \hat{\beta}^\mathrm{T} C \left( \frac{1}{\hat{\sigma}^2} \left( C^\mathrm{T} (X^\mathrm{T} V^{-1} X)^{-1} C \right)^{-1} \right) C^\mathrm{T} \hat{\beta} / q \\
&= \hat{\beta}^\mathrm{T} C \left( \hat{\sigma}^2 C^\mathrm{T} (X^\mathrm{T} V^{-1} X)^{-1} C \right)^{-1} C^\mathrm{T} \hat{\beta} / q \; .
\end{split}
$$